import pandas
import os
from datetime import datetime
import threading
import math

OPERATION_MAXIMUM = {
    "addList": 200,
    "updateList": 100,
    "upsertList": 200,
}
CONCURRENCY_LIMIT = 25

class hub:
    record_chunk_stack = []

# Function to be executed by each thread
def soap_uploader_thread(
        thread_number,
        api,
        api_method="addList",
):
    thread_response_logger = response_logger(thread_number)
    keep_track.new_thread(thread_number)

    # Iterate through the dataframe 100 rows at a time
    while hub.record_chunk_stack != []:
        record_chunk = hub.record_chunk_stack.pop()

        if api_method == "addList":
            response = api.service_proxy.addList(
                record = record_chunk,
                _soapheaders=api.build_soap_headers(),
            )
        elif api_method == "updateList":
            response = api.service_proxy.updateList(
                record = record_chunk,
                _soapheaders=api.build_soap_headers(),
            )
        elif api_method == "upsertList":
            response = api.service_proxy.upsertList(
                record = record_chunk,
                _soapheaders=api.build_soap_headers(),
            )

        df = thread_response_logger.process_response(record_chunk, response, api_method)
        keep_track.just_uploaded(thread_number, df)

    keep_track.thread_complete(thread_number)

def upload_all_these_records(netsuite_record_list, api, api_method="addList"):
    keep_track.uploads_done = 0
    threads = []
    rows_per_thread = math.ceil(len(netsuite_record_list) / CONCURRENCY_LIMIT)
    max_records_per_block = OPERATION_MAXIMUM[api_method]

    # can't deal with records larger than max upload size
    record_chunk_size = min([max_records_per_block, rows_per_thread])

    hub.record_chunk_stack = [
        netsuite_record_list[i:i + record_chunk_size]
        for i in range(0, len(netsuite_record_list), record_chunk_size)
    ]

    assert sum([len(l) for l in hub.record_chunk_stack]) == len(netsuite_record_list), "missing some"
    rids = set([row.externalId for row in netsuite_record_list])
    for l in hub.record_chunk_stack:
        print(f"> [{len(l)}] records in this chunk")
        for row in l:
            assert row.externalId in rids, "missing some specific"

    print()

    threads_needed = min([CONCURRENCY_LIMIT, len(hub.record_chunk_stack)])
    print(f"THREADS NEEDED: {len(hub.record_chunk_stack)} ")

    print()

    keep_track.start()
    for n in range(threads_needed):
        print(f"thread ({n}) spawned")
        thread = threading.Thread(
            target=soap_uploader_thread,
            args=(n, api, api_method)
        )
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

def zeep_df(records):
    record_list = list(records)
    attributes = dir(record_list[0])
    return pandas.DataFrame(
        [
            {
                attr: getattr(r, attr)
                for attr in attributes
            }
            for r in record_list]
    )

class response_logger:
    def __init__(self, thread_number):
        self.thread_file_name = os.path.join(os.getcwd(), "thread_logs", f"thread_{thread_number}.csv")

        if os.path.exists(self.thread_file_name):
            self.thread_file = pandas.read_csv(self.thread_file_name)
        else:
            self.thread_file = pandas.DataFrame()

    def process_response(self, uploaded_records, response, api_method):
        uploaded_records_df = zeep_df(uploaded_records)
        uploaded_records_df["api_method"] = api_method

        def gen_row(status_detail, success):
            row = status_detail[0]
            row.success = success
            row.num_status_details = len(status_detail)
            return row

        response_df = zeep_df([
            gen_row(row.status.statusDetail, row.status.isSuccess)
            for row in response.body.writeResponseList.writeResponse
        ])

        df = pandas.merge(response_df, uploaded_records_df, left_on = uploaded_records_df.index, right_on = uploaded_records_df.index)

        self.thread_file = pandas.concat([self.thread_file, df], ignore_index=True)
        self.thread_file.to_csv(self.thread_file_name, index=False)

        return df




class keep_track:
    uploads_done = 0
    started_time = None

    @staticmethod
    def start():
        keep_track.started_time = datetime.now()

    @staticmethod
    def how_long_has_it_been():
        print(datetime.now() - keep_track.started_time)

    @staticmethod
    def just_uploaded(thread_number, response_df):
        keep_track.uploads_done += len(response_df)

        success = len(response_df[response_df.success == True])
        failure = len(response_df[response_df.success == False])

        print(f"# thread ({thread_number}) total [{keep_track.uploads_done}] records [{len(response_df)}]  success [{success}] failure [{failure}]")
        keep_track.how_long_has_it_been()

    @staticmethod
    def new_thread(n):
        print(f"+++++++++ new thread ({n}) +++++++++")

    @staticmethod
    def thread_complete(n):
        print(f"+++++++++ thread completed ({n}) +++++++++")
        print("==========================================")
import pandas
import os
from datetime import datetime
import threading
import math

OPERATION_MAXIMUM = {
    "addList": 200,
    "updateList": 200,
    "upsertList": 200,
}
CONCURRENCY_LIMIT = 28

# Function to be executed by each thread
def soap_uploader_thread(
        netsuite_record_list,
        thread_number,
        api,
        api_method="addList",
):
    max_records_per_block = OPERATION_MAXIMUM[api_method]

    thread_response_logger = response_logger(thread_number)
    keep_track.new_thread(netsuite_record_list, thread_number)
    num_record_blocks = len(netsuite_record_list) // max_records_per_block + 1

    # Iterate through the dataframe 100 rows at a time
    for i in range(num_record_blocks):
        start_row = max_records_per_block * i
        end_row = max_records_per_block * (i + 1)

        if api_method == "addList":
            response = api.service_proxy.addList(
                record = netsuite_record_list[start_row:end_row],
                _soapheaders=api.build_soap_headers(),
            )
        elif api_method == "updateList":
            response = api.service_proxy.updateList(
                record = netsuite_record_list[start_row:end_row],
                _soapheaders=api.build_soap_headers(),
            )
        elif api_method == "upsertList":
            response = api.service_proxy.upsertList(
                record = netsuite_record_list[start_row:end_row],
                _soapheaders=api.build_soap_headers(),
            )

        keep_track.just_uploaded(len(netsuite_record_list))
        thread_response_logger.process_response(netsuite_record_list, response, api_method)

    keep_track.thread_complete(thread_number)

def upload_all_these_records(netsuite_record_list, api, api_method="addList"):
    threads = []
    rows_per_thread = math.ceil(len(netsuite_record_list) / CONCURRENCY_LIMIT)

    keep_track.start()
    for n in range(CONCURRENCY_LIMIT):
        start_row = rows_per_thread * n
        end_row = rows_per_thread * (n + 1)

        print(f"thread ({n}) start_row: {start_row}, end_row: {end_row}")
        thread = threading.Thread(
            target=soap_uploader_thread,
            args=(netsuite_record_list[start_row: end_row], n, api, api_method)
        )
        threads.append(thread)

        if end_row >= len(netsuite_record_list):
            break

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
    def just_uploaded(how_many_rows):
        keep_track.uploads_done += how_many_rows

        print(f"> maybe uploaded [{keep_track.uploads_done}] records")
        keep_track.how_long_has_it_been()

    @staticmethod
    def new_thread(records, n):
        print(f"+++++++++ new thread ({n}) +++++++++")
        #print([(type(r), r.externalId) for r in records])

    @staticmethod
    def thread_complete(n):
        print(f"+++++++++ thread completed ({n}) +++++++++")
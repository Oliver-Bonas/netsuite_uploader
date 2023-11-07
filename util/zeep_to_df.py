from oliverbonas_source_dags.apis.api_netsuite import zeep_object_to_dict
import pandas
def complete_zeep_df(records):
    record_list = zeep_object_to_dict(list(records))
    return pandas.DataFrame(record_list)
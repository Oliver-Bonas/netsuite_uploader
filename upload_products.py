import sys
import os
import pandas

AIRFLOW_REPO = "airflow_pipelines"

sys.path.append(os.path.join(
    os.path.dirname(__file__),
    "..",
    AIRFLOW_REPO,
    "dags"
))

from config.environment import ENVIRONMENT

ENVIRONMENT.set_development()

from oliverbonas_source_dags.apis.api_netsuite import APIConfig_netsuite

api = APIConfig_netsuite()


from util.get_ns_number import get_ns_number

print(get_ns_number(api, "InventoryItem"))

df = pandas.read_gbq("""
select *
from `bq-central-dev`.data_migration_products.dbt_products__everything_all
limit 10
""")



# python library zeep
InventoryItem = api.client.get_type("ns17:InventoryItem")
CostCategory = api.client.get_type("ns17:CostCategory")
CostCategorySearch = api.client.get_type("ns17:CostCategorySearch")
CostCategorySearchBasic = api.client.get_type("ns5:CostCategorySearchBasic")
RecordRef = api.client.get_type("ns0:RecordRef")


#response = api.service_proxy.search(
#    searchRecord = CostCategorySearch(),
#    _soapheaders = api.build_soap_headers(),
#)



response = api.service_proxy.addList(
    record = [
        InventoryItem(
            assetAccount = {
                "internalId": 1786
            },
            cogsAccount = {
                "internalId": 1785
            },
            #internalId = ,
            itemId = f"mystery",
            externalId = "i am the sku!",
            taxSchedule = RecordRef(
                internalId = 4,
                #name= "Cake"
            ),
            costCategory = RecordRef(
                internalId = 2,
                # this needs to be costCategory, with a lower case c at the start
                type="costCategory",
                #name = "Default Cost Category",
            ),
            #customForm = RecordRef(
            #    internalId = 195,
            #    name = "Oliver Bonas – Inventory (WIP JULIAN)",
            #    type="inventoryItem"
            #)
        )
    ],
    _soapheaders = api.build_soap_headers(),
)
"""{
    'code': 'USER_ERROR',
    'message': 'You must specify asset and COGS accounts for this inventory item.',
    'afterSubmitFailed': None,
    'type': 'ERROR'
}
{
    'code': 'USER_ERROR',
    'message': 'You may not use duplicate accounts on an item.',
    'afterSubmitFailed': None,
    'type': 'ERROR'
}
{
    'code': 'USER_ERROR',
    'message': 'Please enter value(s) for: Item Name/Number, Tax Schedule, Cost Category',
    'afterSubmitFailed': None,
    'type': 'ERROR'
}
{
    'code': 'INVALID_KEY_OR_REF',
    'message': 'Invalid costcategory reference key 1.',
    'afterSubmitFailed': None,
    'type': 'ERROR'
}
{
    'code': 'USER_ERROR',
    'message': 'Please enter value(s) for: Tax Schedule, Cost Category',
    'afterSubmitFailed': None,
    'type': 'ERROR'
}
{
    'code': 'DUP_ITEM',
    'message': 'Uniqueness error - there is already an item with that name or name/parent combination.',
    'afterSubmitFailed': None,
    'type': 'ERROR'
}

zeep.exceptions.Fault: org.xml.sax.SAXException: Expected {urn:core_2021_2.platform.webservices.netsuite.com}name, found {urn:accounting_2021_2.lists.webservices.netsuite.com}name
"""

line = response.body.writeResponseList.writeResponse
print(line)
print("stop")

"""
[{
    'nullFieldList': None,
    'name': 'Test',
    'account': {
        'name': '6000 Expenses',
        'internalId': '58',
        'externalId': None,
        'type': None
    },
    'itemCostType': '_landed',
    'isInactive': False,
    'internalId': '1',
    'externalId': None
}, {
    'nullFieldList': None,
    'name': 'Default Cost Category',
    'account': None,
    'itemCostType': '_material',
    'isInactive': False,
    'internalId': '2',
    'externalId': None
}, {
    'nullFieldList': None,
    'name': 'Freight',
    'account': {
        'name': '6000 Expenses',
        'internalId': '58',
        'externalId': None,
        'type': None
    },
    'itemCostType': '_landed',
    'isInactive': False,
    'internalId': '3',
    'externalId': None
}, {
    'nullFieldList': None,
    'name': 'Test test',
    'account': None,
    'itemCostType': '_material',
    'isInactive': False,
    'internalId': '4',
    'externalId': None
}, {
    'nullFieldList': None,
    'name': 'UK Labour Run STD Test',
    'account': None,
    'itemCostType': '_material',
    'isInactive': False,
    'internalId': '6',
    'externalId': None
}, {
    'nullFieldList': None,
    'name': 'Test Landed Cost Category',
    'account': {
        'name': '22030 Current Assets : Stock & Work In Progress : Stock - Duty',
        'internalId': '1889',
        'externalId': None,
        'type': None
    },
    'itemCostType': '_landed',
    'isInactive': False,
    'internalId': '7',
    'externalId': None
}]
"""





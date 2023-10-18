import sys

print(sys.executable)
import os

import pandas

AIRFLOW_REPO = "airflow_pipelines"

sys.path.append(os.path.join(
    os.getcwd(),
    "..",
    AIRFLOW_REPO,
    "dags"
))

from config.environment import ENVIRONMENT

ENVIRONMENT.set_development()

from oliverbonas_source_dags.apis.api_netsuite import (BINDING_NAME,
                                                       DATACENTER_URL,
                                                       WSDL_URL,
                                                       APIConfig_netsuite)

api = APIConfig_netsuite()


from util.get_ns_number import get_ns_number

print(get_ns_number(api, "CustomRecordRef"))

df = pandas.read_gbq("""
select *
from `bq-central-dev`.data_migration_products.dbt_products__everything_all
limit 10
""")



class product_mapping:
    list_info = {}
    list_values = {}


# python library zeep
InventoryItem = api.client.get_type("ns17:InventoryItem")
CostCategory = api.client.get_type("ns17:CostCategory")
CostCategorySearch = api.client.get_type("ns17:CostCategorySearch")
CostCategorySearchBasic = api.client.get_type("ns5:CostCategorySearchBasic")
RecordRef = api.client.get_type("ns0:RecordRef")
StringCustomFieldRef = api.client.get_type(f"ns0:StringCustomFieldRef")
CustomRecordSearchBasic = api.client.get_type("ns5:CustomRecordSearchBasic")
CustomRecordSearch = api.client.get_type("ns32:CustomRecordSearch")
CustomListSearch = api.client.get_type("ns32:CustomListSearch")
CustomListSearchBasic = api.client.get_type("ns5:CustomListSearchBasic")
CustomRecordRef = api.client.get_type("ns0:CustomRecordRef")


def __call__(self, *args, **kwargs):
    """Call the operation with the given args and kwargs.

    :rtype: zeep.xsd.CompoundValue

    """
    soap_headers = self._merge_soap_headers(kwargs.get("_soapheaders"))
    if soap_headers:
        kwargs["_soapheaders"] = soap_headers

    return self._proxy._binding.send(
        self._proxy._client,
        self._proxy._binding_options,
        self._op_name,
        args,
        kwargs,
    )

def send(self, client, options, operation, args, kwargs):
    """Called from the service

    :param client: The client with which the operation was called
    :type client: zeep.client.Client
    :param options: The binding options
    :type options: dict
    :param operation: The operation object from which this is a reply
    :type operation: zeep.wsdl.definitions.Operation
    :param args: The args to pass to the operation
    :type args: tuple
    :param kwargs: The kwargs to pass to the operation
    :type kwargs: dict

    """
    envelope, http_headers = self._create(
        operation, args, kwargs, client=client, options=options
    )

    response = client.transport.post_xml(options["address"], envelope, http_headers)

    operation_obj = self.get(operation)

    # If the client wants to return the raw data then let's do that.
    if client.settings.raw_response:
        return response

    return self.process_reply(client, operation_obj, response)



def stolen_zeep_code_send(self, client, options, operation, args, kwargs):
    envelope, http_headers = self._create(
        operation, args, kwargs, client=client, options=options
    )

    response = client.transport.post_xml(options["address"], envelope, http_headers)

    operation_obj = self.get(operation)

    # If the client wants to return the raw data then let's do that.
    if client.settings.raw_response:
        return response

    return response

def stolen_zeep_code__call__(api, *args, **kwargs):
    # look at the service proxy class to understand this madness
    self = api.service_proxy._operations["get"]
    print(type(self))

    soap_headers = self._merge_soap_headers(kwargs.get("_soapheaders"))
    if soap_headers:
        kwargs["_soapheaders"] = soap_headers

    return stolen_zeep_code_send(
        self._proxy._binding,
        self._proxy._client,
        self._proxy._binding_options,
        self._op_name,
        args,
        kwargs,
    )

import json

raw_response = stolen_zeep_code__call__(
    api,
        RecordRef(
            internalId = 2721,
            type="itemCustomField"
        ),
        _soapheaders=api.build_soap_headers(),
    )

import xml.etree.ElementTree as ET

root = ET.fromstring(raw_response.content.decode("utf-8"))

select_record_type = root.find(".//{*}selectRecordType")

internalId = select_record_type.get("internalId")

print(raw_response.content.decode("utf-8"))
1/0

response = api.service_proxy.getCustomizationId(
    customizationType="customList",#"itemCustomField",
    includeInactives=False,
    _soapheaders = api.build_soap_headers(),
)
customlists = response.body.getCustomizationIdResult.customizationRefList.customizationRef

response = api.service_proxy.getList(
        baseRef=[RecordRef(
            internalId = cl.internalId,
            type="customList",
        )
        for cl in customlists
        ],
        _soapheaders=api.build_soap_headers(),
    )
['refnr', 'pgr_no', 'sgr_no', 'type_no', 'group_no', 'item_name_standard', 'item_name_with_variant', 'department', 'sub_department', 'config',
 'new_pgr', 'new_sgr', 'new_type', 'new_type_detail', 'unit_text', 'variant_text', 'item_hierarchy', 'add_check', 'analytics_children_no',
 'alphabet_matrix', 'alphabet_id', 'bedroom_textiles_matrix', 'bedroom_textiles_id', 'clothing_matrix', 'clothing_id', 'colour_matrix',
 'colour_id', 'flavour_matrix', 'flavour_id', 'footwear_matrix', 'footwear_id', 'frames_matrix', 'frames_id', 'paper_matrix', 'paper_id',
 'ring_size_matrix', 'ring_size_id', 'scent_matrix', 'scent_id', 'stone_matrix', 'stone_id', 'uat_matrix', 'uat_id', 'xs_xxl_matrix',
 'xs_xxl_id', 'xs_s_xl_xxl_matrix', 'xs_s_xl_xxl_id', 'department_magento', 'nightwear_length', 'lined', 'nightwear_lining',
 'accessories_fastening', 'clothing_fastening', 'fastening_', 'Hit', 'shower_resistant', 'lining_material', 'care_instructions', 'pattern',
 'pattern_', 'finish', 'fashion_finish', 'detail', 'fashion_detail', 'matching_items', 'fashion_matching_items', 'Cuffs', 'heel_type', 'sunglasses_frame',
 'filter_category', 'lense_colour', 'touch_screen_gloves', 'set_hg', 'set_fashion', 'elasticated', 'one_size', 'card_slots', 'compartment_details',
 'hardware', 'inner_slip_pockets', 'lining', 'main_compartments', 'outer_pockets', 'strap_type', 'number_of_straps', 'length_extendable', 'necklace_length',
 'chain_type', 'hair_closure', 'inside_compartment', 'shape', 'opening', 'home_variations', 'wall_hanging_fixtures', 'carry_handles', 'bottle_capacity', 'nesting',
 'Power_source', 'Conversion_ring_included', 'bulb_included', 'cord_colour', 'switch_type', 'shade_included', 'lighting_tint', 'maximum_wattage', 'lighting_hours',
 'voltage', 'kelvin', 'dimmable', 'bulb_fitting', 'compatible_bulb', 'frame_aperture', 'frame_opening', 'stand_included', 'drainage_hole', 'plant_included', 'faux_bedding',
 'pot_type', 'cushion_inner', 'cushion_inner_included', 'cushion_cover_included', 'print_size', 'recessed_frame', 'frame_finish', 'frame_colour', 'mount_colour',
 'removable_print', 'design', 'ribbon_colour', 'string_colour', 'illustrated', 'envelope_colour', 'number_of_players', 'perishable_product', 'suitable_for', 'wheels',
 'foot_adjusters', 'number_of_seats', 'back_type', 'movement_type', 'cushion_firmness', 'size_actual_size', 'outdoor_use', 'Lumens', 'Frame_orientation', 'Wall_art_design',
 'Wall_art_designer', 'Cover_type', 'Skin_type_suitability', 'Parabens_and_sls_free', 'Size_filter', 'Brand_filter', 'inner_zipped_pockets', 'jewellery_care_instruction',
 'gift_boxed', 'Display_in_catalog_if_OOS', 'Display_in_Search_if_OOS', 'pre_order_delivery_time', 'price_label', 'product_page_template', 'size_guide', 'staff_only_product',
 'allow_giftbox', 'Visibility', 'hazmat', 'hanging_string', 'letter', 'category_listing_label', 'delivery_flag', 'colorcustom', 'jewellery_giftbox_enabled', 'staff_discount_level',
 'scent', 'Dimensions_clothing', 'length_56', 'length_fewer_skus', 'height', 'height_', 'home_height', 'width', 'width_', 'home_width', 'weight_', 'weight_kg', 'material_composition',
 'mi_detail', 'clothing_lining', 'Sole_Material', 'heel_height', 'bridge', 'strap_drop', 'strap_length', 'Jewellery_Material', 'shortest_length_fashion', 'shortest_length_home',
 'longest_length_fashion', 'longest_length_home', 'stone_length', 'stone_width', 'drop', 'stone', 'depth', 'depth_', 'home_depth', 'boxed_height', 'boxed_width', 'boxed_depth',
 'boxed_weight', 'drawers', 'doors', 'compartments', 'shelves', 'home_material_breakdown', 'scent_notes', 'burn_time', 'fill_weight_g', 'fill_weight_ml', 'hanging_length',
 'cord_length', 'author', 'publisher', 'quantity_per_pack', 'Message_inside', 'No_of_pieces', 'servings', 'leg_height', 'floor_to_table_height', 'seat_height', 'seat_depth',
 'backrest_height', 'product_features', 'wash_info_1', 'wash_info_2', 'wash_info_3', 'care_info_1', 'care_info_2', 'care_info_3', 'fragrance_name', 'Fluid_capacity_ml',
 'Pot_internal_Diameter_cm', 'Page_count', 'Supplier_description', 'Bag_Strap_Width', 'extra_features', 'listing_page_name', 'allow_gift_message', 'allow_gift_wrapping',
 'use_and_care_information', 'ean', 'safety_info', 'shipping_group', 'stat_period', 'display_name', 'gift_box_product_id', 'discontinued', 'arm_length', 'Ingredients',
 'Ingredients_New', 'Allergens', 'Directions_of_use', 'Style', 'Sleeve_length', 'Neckline', 'Occasion', 'Closure', 'Number_of_chains', 'Book_subject', 'Card_occasion',
 'sunglasses_flag', 'product_collection', 'home_flag', 'fragrance_family', 'colour_filter', 'material', 'product_type', 'dimensions_content', 'bag_fits', 'earring_backs',
 'description', 'fit_and_features_content', 'directions_content', 'flags', 'material_care_instructions', 'model_spec_flags', 'sustainability_cta', 'sustainability_flag',
 'brand_blurb', 'price', 'special_price', 'cost', 'tier_prices', 'extra_features_content', 'jewellery_giftbox_size', 'jewellery_material_flag', 'assembly_required',
 'config_futura', 'CountryOfOrigin', 'supplier', 'Supplier_No', 'supplier_item_no', 'pivot_rcode', 'USWEBSITE', 'IrelandWebsite', 'WEB', 'HAZMATCODE', 'SeasonalityCoding',
 'COLLECTION', 'OWNBRANDBRANDED', 'PGR', 'SGR', 'ATV_Type', 'GrpNo', 'CLOTHINGFIT', 'TrouserWaist', 'TrouserStyle', 'TrimComposition', 'DetachableStrap', 'NUMBEROFPLAYERS',
 'ASSEMBLYREQUIRED', 'ATV_REF_NUMBER', 'NOOFHANGINGBARS', 'NOOFEARRINGBARS', 'NOOFCOMPARTMENTS', 'NOOFHOOKS', 'LEDBULB', 'TILT', 'PLANTPOTHEIGHTCM', 'PLANTPOTDEPTHCM',
 'PLANTPOTWIDTHCM', 'STANDWIDTHCM', 'STANDDEPTHCM', 'STANDHEIGHTCM', 'RECOMMENDEDAGE', 'ADJUSTABLE', 'DETACHABLEFEET', 'UPHOLSTERED', 'REMOVABLECUSHIONCOVERS', 'HANGINGRAILS',
 'SUITABLEFOR', 'width_home_and_gift', 'width_fashion', 'fashion_length', 'clothing_shape', 'diary_type', 'kelvin_futura', 'lumens_futura', 'no_of_drawers_futura',
 'no_of_pieces_futura', 'plant_included_futura', 'recommended_age', 'removable_cushion_covers', 'current_gbp_price', 'original_gbp_price', 'current_eur_price',
 'original_eur_price', 'current_usd_price', 'original_usd_price', 'asset_account_constant', 'income_account_constant', 'cogs_account_constant', 'cost_price_constant',
 'cost_category_constant', 'cost_estimate_type_constant', 'subsidiary_constant', 'include_children_constant', 'tax_schedule_req_constant', 'matrix_type_constant',
 'track_landed_cost_constant', 'season_launch_constant', 'item__hierarchy_versions_1_hierarchy_version_constant', 'item__hierarchy_versions_1_included_in_version_constant',
 'pricing_1_currency_constant', 'pricing_1_pricing_level_constant', 'pricing_1_quantity_constant', 'pricing_2_currency_constant', 'pricing_2_pricing_level_constant',
 'pricing_2_quantity_constant', 'pricing_3_currency_constant', 'pricing_3_pricing_level_constant', 'pricing_3_quantity_constant']

for row in response.body.readResponseList.readResponse:
    print("#######################################")
    if row.record.customValueList is not None:
        product_mapping.list_values[row.record.internalId] = row.record.customValueList.customValue

for customlist in customlists:
    product_mapping.list_info[customlist.internalId] = customlist

    for value in valuelist:
        product_mapping.list_values[value.valueId] = value.value
    print(customlist.name)

print(response.body)
1/0
response = api.service_proxy.get(
    baseRef =RecordRef(
                #internalId = 1872,
                type="customList",
            ),
_soapheaders = api.build_soap_headers(),
)
print(response.body)
print(StringCustomFieldRef.signature())


print(RecordRef.signature())



response = api.service_proxy.addList(
    record = [
        InventoryItem(
            #agent = "Go Sourcing",
            assetAccount = {
                "internalId": 1786
            },
            cogsAccount = {
                "internalId": 1785
            },
            #internalId = ,
            itemId = f"what55",
            externalId = "whatwhat55",
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
            customForm = RecordRef(
                internalId = 195,
                #name = "Oliver Bonas – Inventory (WIP JULIAN)",
                #
                #type="custform_175_1026328_sb1_847"
            ),
            #Agent		custitem_ob_agent	4863
            #brand="hello"
            customFieldList= [{"customField":StringCustomFieldRef(internalId= "4863",value=3)}],
                             # {"customField":StringCustomFieldRef(internalId= "agsdfasdfasdfent",value="Nunomsdfasdfoura")}],
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

{
    'code': 'USER_ERROR',
    'message': 'Nonexistent externalId 22010 for assetAccount',
    'afterSubmitFailed': None,
    'type': 'ERROR'
}
this is because it was none before

{
                'code': 'INSUFFICIENT_PERMISSION',
                'message': 'You do not have permissions to set a value for element matrixtype due to one of the following reasons: 1) The field is read-only; 2) An associated feature is disabled; 3) The field is available either when a record is created or updated, but not in both cases.',
                'afterSubmitFailed': None,
                'type': 'ERROR'
            }

            
{
    'code': 'USER_ERROR',
    'message': 'Nonexistent externalId 22010 for assetAccount',
    'afterSubmitFailed': None,
    'type': 'ERROR'
}

{
    'code': 'RCRD_DSNT_EXIST',
    'message': 'That record does not exist.',
    'afterSubmitFailed': None,
    'type': 'ERROR'
}
{
    'code': 'INVALID_CSTM_RCRD_QUERY',
    'message': 'Invalid custom record object in query.',
    'afterSubmitFailed': None,
    'type': 'ERROR'
}
 {
    'code': 'USER_ERROR',
    'message': 'All lines of sublist hierarchyVersionsList have to be specified when replace All is requested.',
    'afterSubmitFailed': None,
    'type': 'ERROR'
}
{
    'code': 'USER_ERROR',
    'message': 'All lines of sublist hierarchyVersionsList have to be specified when replace All is requested.',
    'afterSubmitFailed': None,
    'type': 'ERROR'
}
 {
    'code': 'INVALID_NUMBER',
    'message': 'You entered "1&#xfff9;2" into a field where a numeric value was expected. Please go back and change this value to a number.',
    'afterSubmitFailed': None,
    'type': 'ERROR'
}
 {
    'code': 'INVALID_NUMBER',
    'message': 'You entered "1&#xfff9;2&#xfff9;3&#xfff9;4&#xfff9;5" into a field where a numeric value was expected. Please go back and change this value to a number.',
    'afterSubmitFailed': None,
    'type': 'ERROR'
}
     {
                'code': 'INSUFFICIENT_PERMISSION',
                'message': 'You do not have permissions to set a value for element custitem_ob_bm_status due to one of the following reasons: 1) The field is read-only; 2) An associated feature is disabled; 3) The field is available either when a record is created or updated, but not in both cases.',
                'afterSubmitFailed': None,
                'type': 'ERROR'
            }
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
}
{
    'code': 'INVALID_CSTM_RCRD_TYP_KEY',
    'message': 'Invalid custom record type key in query.',
    'afterSubmitFailed': None,
    'type': 'ERROR'
}

]
"""





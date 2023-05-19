from app.constant import DB_Name, TwitterDataType, MastodonDataType

def get_state_number(area_code):
    return str(area_code)[0]

def get_doc_name_and_view_from_type(db_name, type):
    result = {
        DB_Name.TWITTER: {
            TwitterDataType.RELATED_TWEETS: [ "state", "state_view" ],
            TwitterDataType.UNRELATED_TWEETS: [ "state", "new-state" ]
        },
        DB_Name.MASTODON: {
            MastodonDataType.RELATED_TOOTS: [ "count", "relatetoot" ],
            MastodonDataType.RELATED_USERS: [ "count", "relateusr" ]
        }
    }
    
    return result[db_name][type]

def map_to_key_value(list):
    aggregated_list = []
    for (key, value) in list.items():
        aggregated_list.append({ "key": key, "value": value})

def aggregate_home_and_community_data(data):
    list = {}

    for item in data:
        state = get_state_number(item["area_code"])
        if state not in list:
            list[state] = item
        else:
            list[state]["hcc_cco_1_no_7_12_6_13"] += item["hcc_cco_1_no_7_12_6_13"] 
            list[state]["hcc_dom_1_no_7_12_6_13"] += item["hcc_dom_1_no_7_12_6_13"] 
            list[state]["area_code"] += item["area_code"] 
            list[state]["area_name"] += item["area_name"] 
            list[state]["hcc_day_1_no_7_12_6_13"] += item["hcc_day_1_no_7_12_6_13"] 
            list[state]["hcc_toti_1_no_7_12_6_13"] += item["hcc_toti_1_no_7_12_6_13"] 
            list[state]["hcc_mls_1_no_7_12_6_13"] += item["hcc_mls_1_no_7_12_6_13"] 
            list[state]["hcc_cns_1_no_7_12_6_13"] += item["hcc_cns_1_no_7_12_6_13"] 

    return map_to_key_value(list)

def aggregate_volunteer_work_data(data):
    list = {}

    for item in data:
        state = get_state_number(item["SA2_MAIN11"])
        if state not in list:
            list[state] = item
        else:
            list[state]["P_Tot_Volunteer"] += item["P_Tot_Volunteer"] 
            list[state]["P_Tot_N_a_volunteer"] += item["P_Tot_N_a_volunteer"] 
            list[state]["P_Tot_Voluntary_work_ns"] += item["P_Tot_Voluntary_work_ns"] 
            list[state]["P_85ov_Volunteer"] += item["P_85ov_Volunteer"]

    return map_to_key_value(list)
from enum import Enum

URL = "http://172.26.134.182:8296/data"

default_state_value = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}

class DATA(Enum):
    HOME_AND_COMMNUNITY_CARE = "/sudo/home_and_community_care"
    VOLUNTARY_WORK = "/sudo/voluntary_work"
    UNPAID_ASSISTANCE = "/sudo/unpaid_assistance"
    TWITTER_RELATED = "/twitter/related"
    TWITTER_UNRELATED = "/twitter/unrelated"
    MASTODON_TOOTS = "/mastodon/toots"
    MASTODON_USERS = "/mastodon/users"

state_name = {
    1 : "New South Wales",
    2 : "Victoria",
    3 : "Queensland",
    4 : "Western Australia",
    5 : "South Australia",
    6 : "Tasmania",
    7 : "Northern Territory",
    8 : "Australian Capital Territory",
    9 : "Other",
}

def get_url(data):
    return URL + data.value

def get_state_number(area_code):
    return str(area_code)[0]

def map_to_key_value(list):
    aggregated_list = []
    for (key, value) in list.items():
        aggregated_list.append({ "key": key, "value": value})
    return aggregated_list

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


def aggregate_unpaid_assistance_data(data):
    list = {}

    for item in data:
        state = get_state_number(item["lga_code_2016"])
        if state not in list:
            list[state] = item
        else:
            list[state]["f_tot_no_upaid_assist_pvded"] += item["f_tot_no_upaid_assist_pvded"] 

    return map_to_key_value(list)






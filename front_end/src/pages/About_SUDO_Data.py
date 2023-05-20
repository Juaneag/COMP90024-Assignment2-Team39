import streamlit as st

st.set_page_config(page_title="Twitter Related", page_icon="📈")
st.markdown('''
## SD Home and Community Care Program 2012-2013
#### db name: sudo
The Home and Community Care (HACC) Program is a joint Commonwealth, State and Territory initiative. It funds services which support people who are frail, aged and younger people with a disability (and their carers), who live at home and whose capacity for independent living is at risk or who are at risk of premature or inappropriate admission to long-term residential care. The broad aim is to offer maintenance and support services to help frail older people and younger people with disabilities to continue living in their communities. HACC services may be offered in the home or local community by an HACC agency, community health centre or local council. Services include centre-based and other respite, social support and counselling, personal care, home modification and maintenance, transport, meals and other food services, information, advocacy and assessment, support for carers, allied health services, domestic assistance and community nursing. Data are presented by SD for 2012 and 2013.

#### Fields
- hcc_cco_1_no_7_12_6_13 - HACC Client Care Coordination Instances - Count
- hcc_dom_1_no_7_12_6_13 - HACC Domestic Assistance Instances - Count
- area_code - Statistical Division code
- area_name - Statistical Division name
- hcc_day_1_no_7_12_6_13 - HACC Centre Based Day Care Instances - Count
- hcc_toti_1_no_7_12_6_13 - HACC Total Instances of Assistance - Count
- hcc_mls_1_no_7_12_6_13 - HACC Meals at Centre Plus Meals at Home Instances - Count
- hcc_cns_1_no_7_12_6_13 - HACC Care Counselling Instances - Count

#### Example
```
{
    "hcc_cco_1_no_7_12_6_13": 2216.3005,
    "hcc_dom_1_no_7_12_6_13": 5617.5726,
    "area_code": 309,
    "area_name": "Sunshine Coast",
    "hcc_day_1_no_7_12_6_13": 1890.2813,
    "hcc_toti_1_no_7_12_6_13": 43564.4939,
    "hcc_mls_1_no_7_12_6_13": 2560.7165,
    "hcc_cns_1_no_7_12_6_13": 2207.025
}
```

## LGA-I09 Unpaid Assistance to a Person with a Disability by Age by Sex for Aboriginal & Torres Strait Islander Persons-Census 2016
#### db name: unpaid
LGA based data for Unpaid Assistance to a Person with a Disability by Age by Sex for Aboriginal and/or Torres Strait Islander persons, in Aboriginal and Torres Strait Islander People Profile (ATSIP), 2016 Census. Count of Aboriginal and/or Torres Strait Islander persons aged 15 years and over who in the two weeks prior to Census night spent time providing unpaid care, help or assistance to family members or others because of a disability, a long-term health condition or problems related to old age. This includes people who are in receipt of a Carer Allowance or Carer Payment. It does not include work done through a voluntary organisation or group. The data is by LGA 2016 boundaries. Periodicity: 5-Yearly.
Note: There are small random adjustments made to all cell values to protect the confidentiality of data. These adjustments may cause the sum of rows or columns to differ by small amounts from table totals.

#### Fields
- f_tot_no_upaid_assist_pvded - Females Total No unpaid assistance providedFemales Total No unpaid assistance provided
- lga_code_2016 - LGA Code 2016.

#### Example
```
{
    "f_tot_no_upaid_assist_pvded": 240,
    "lga_code_2016": "56620"
}
```

## SA2-based B19 Voluntary Work for an Organisation or Group by Age by Sex as at 2011-08-11
#### db name: sa2
SA2 based data for Voluntary Work For An Organisation Or Group Age by Sex, for 2011 Census. Count of all persons on Census night based on place of usual residence. Data sourced from: http://www.abs.gov.au/census. For further information about these and related statistics, contact the National Information and Referral Services on 1300 135 070. Periodicity: 5-Yearly.

#### Fields
- P_Tot_Volunteer - Persons Total Volunteer
- P_Tot_N_a_volunteer - Persons Total Not a volunteer
- P_Tot_Voluntary_work_ns - Persons Total Voluntary work not stated.
- P_85ov_Volunteer - Persons 85 years and over Volunteer.
- SA2_MAIN11 - Statistical Area Level 2 (SA2) Code.

#### Example
```
{
    "P_Tot_Volunteer": 891,
    "P_Tot_N_a_volunteer": 3587,
    "P_Tot_Voluntary_work_ns": 489,
    "P_85ov_Volunteer": 0,
    "SA2_MAIN11": "306011143"
}
```
''')

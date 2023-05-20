_Show how data from each endpoint being visualized_

_SUDO data explation are available in sudo_data_explanation.md_

# Twitter Data
1. TWITTER_RELATED = "/twitter/related"
    - tweets with related=1 grouped by each state
    - Visualization
        - Map_1, show different by value for each state
            - position of data is centered of each state
            - tooltip shows state name and count related tweets for each state
        - StackBar_0, a stacked bar of TWITTER_RELATED vs TWITTER_UNRELATED by state
2. TWITTER_UNRELATED = "/twitter/unrelated"
    - tweets with related=0 grouped by each state
    - Visualization
        - StackBar_0, a stacked bar of TWITTER_RELATED vs TWITTER_UNRELATED by state
# Mastodon Data
1. MASTODON_TOOTS = "/mastodon/toots"
    - get related and unrelated count for toots
    -  Visualization
        - PieChart_1, a pie chart of key=0 (unrelated) vs key=1 (related)
2. MASTODON_USERS = "/mastodon/users"
    - get related and unrelated count for user
    - no visualization as only unrelated data returned

# SUDO Data
1. HOME_AND_COMMNUNITY_CARE = "/sudo/home_and_community_care"
    - home and commnunity care data, grouped by state in frontend
    - field use
        - hcc_toti_1_no_7_12_6_13 - HACC Total Instances of Assistance - Count
    - Visualization
        - Bar_1, home and comnunity total assistance count(hcc_toti_1_no_7_12_6_13) for each state
2. VOLUNTARY_WORK = "/sudo/voluntary_work"
    - voluntary work data, grouped by state in frontend
    - field use
        - P_Tot_Volunteer - Persons Total Volunteer
        - P_Tot_N_a_volunteer - Persons Total Not a volunteer
        - P_Tot_Voluntary_work_ns - Persons Total Voluntary work not stated.
    - Visualization
        - StackBar_1, volunteer(P_Tot_Volunteer) vs not a volunteer (P_Tot_N_a_volunteer)
3. UNPAID_ASSISTANCE = "/sudo/unpaid_assistance"
    - unpaid assistance data, grouped by state in frontend
    - field use
        - f_tot_no_upaid_assist_pvded - Females Total No unpaid assistance providedFemales Total No unpaid
    - Visualization
        - Bar_2, unpaid assistance(f_tot_no_upaid_assist_pvded) for each state

# Summary
1. [DONE] Map_1, Twitter data of related tweets with charity in each state
2. **StackBar_0, Twitter data of related vs unrelated tweets with charity in each state
3. PieChart_1, Mastodon related vs unrelated
4. [DONE] StackBar_1, [sa2] volunteer work vs not a volunteer for each state
5. [DONE] Bar_1, [sudo] home and comnunity total assistance count for each state
6. Bar_2, [unpaid] unpaid assistance for each state

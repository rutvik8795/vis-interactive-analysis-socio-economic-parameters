import pandas as pd
import configparser
from sklearn.preprocessing import MinMaxScaler, StandardScaler




def get_rent_mean_per_state(data):
    state_list = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","D.C.","Delaware",
                  "Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana",
                  "Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
                  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina",
                  "North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","South Carolina","South Dakota","Tennessee",
                  "Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

    state_df = pd.DataFrame(state_list, columns=['state'])

    result_list = []

    for index, row in data.iterrows():
        state_obj = {
                        'state' : row['state'],
                        'rent_mean'  : str(row['rent_mean']),
                        'ALand' : str(row['ALand']),
                        'AWater': str(row['AWater']),
                        'pop': str(row['pop']),
                        'family_mean': str(row['family_mean']),
                        'hs_degree': str(row['hs_degree']),
                        'debt': str(row['debt']),
                        'hc_mortgage': str(row['hc_mortgage_mean']),
                        'hc_mean': str(row['hc_mean']),
                        'home_equity': str(row['home_equity']),
                        'second_mortgage': str(row['second_mortgage'])

                    }
        result_list.append(state_obj)
    return result_list


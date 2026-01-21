import streamlit as st
import pandas as pd
import constants as c

def load_data(file_path):
    try:
        data=pd.read_csv("players_data-2024_2025.csv")
        data_clear=data.drop_duplicates()
        data_clear = data_clear.iloc[:, 1:]
        return data_clear
    except FileNotFoundError:
        return None
    
def parse_positions(pos_str):
    return set(p.strip() for p in pos_str.split(','))

def get_params_and_ranges(pos_list):
    if any(p in ['FW', 'FW,MF', 'FW,DF'] for p in pos_list):
        return c.params_FW, c.max_range_FW
    elif any(p in ['MF', 'MF,FW', 'MF,DF'] for p in pos_list):
        return c.params_MF, c.max_range_MF
    elif any(p in ['DF', 'DF,MF', 'DF,FW'] for p in pos_list):
        return c.params_DF, c.max_range_DF
    else:
        return c.params_GK, c.max_range_GK
    
def get_player_data(df, player_name, params):
    row = df[df['Player'] == player_name].loc[:, params].iloc[0]
    return pd.to_numeric(row, errors='coerce').fillna(0).tolist()

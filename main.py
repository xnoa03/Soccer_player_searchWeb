import streamlit as st
import pandas as pd
from mplsoccer import Radar, FontManager
import matplotlib.pyplot as plt

data=pd.read_csv("players_data-2024_2025.csv")
data_clear=data.drop_duplicates()
Players=data_clear['Player']

st.title('유럽 5대리그 스카우팅 차트 웹')
S_Player = st.selectbox("선수 선택", Players)
st.write("Selected Player: ",S_Player)


print(data_clear[data_clear['Player']=='Florian Wirtz'])

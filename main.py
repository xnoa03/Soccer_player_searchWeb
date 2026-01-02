import streamlit as st
import pandas as pd
from mplsoccer import Radar, FontManager
import matplotlib.pyplot as plt

def main():
    data=pd.read_csv("players_data-2024_2025.csv")
    data_clear=data.drop_duplicates()
    data_clear = data_clear.iloc[:, 1:]
    Leagues=sorted(data_clear['Comp'].unique())

    st.title('유럽 5대리그 스카우팅 차트 웹')
    S_League = st.selectbox("리그 선택", Leagues)
    if(S_League!=None):
        League_data=data_clear[data_clear['Comp']==S_League]
        Players=League_data['Player']
        S_Player = st.selectbox("선수 선택", Players)
        st.write("Selected Player: ",S_Player)
        player_data=data_clear[data_clear['Player']==S_Player]
        st.write(player_data)

if __name__ == "__main__":
    main()
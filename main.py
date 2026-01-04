import streamlit as st
import pandas as pd
from mplsoccer import Radar, FontManager
import matplotlib.pyplot as plt

def main():
    data=pd.read_csv("players_data-2024_2025.csv")
    data_clear=data.drop_duplicates()
    data_clear = data_clear.iloc[:, 1:]
    Leagues=sorted(data_clear['Comp'].unique())
    params=['Gls','Ast','G+A','G-PK','PK','PKatt','CrdY','CrdR','xG','npxG','xAG','npxG+xAG']
    rader=Radar(params=params,min_range=[0,0,0,0,0,0,0,0,0,0,0,0],max_range=[100,100,100,100,100,100,100,100,100,100,100,100])
    fig,ax=rader.setup_axis()


    st.title('유럽 5대리그 스카우팅 차트 웹')
    S_League = st.selectbox("리그 선택", Leagues)
    if(S_League!=None):
        League_data=data_clear[data_clear['Comp']==S_League]
        Players=League_data['Player']
        S_Player = st.selectbox("선수 선택", Players)
        st.write("Selected Player: ",S_Player)
        player_data=data_clear[data_clear['Player']==S_Player]
        st.write(player_data)
        values_data=player_data.loc[:,'Gls':'npxG+xAG']
        values_data=values_data.iloc[0].tolist()
        rader.draw_radar_solid(values_data,ax=ax,kwargs={'facecolor': 'blue', 'alpha': 0.6})
        st.pyplot(fig)
        print(values_data)
        
        

if __name__ == "__main__":
    main()
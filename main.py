import streamlit as st
import pandas as pd
from mplsoccer import Radar, FontManager
import matplotlib.pyplot as plt
URL1 = ('https://raw.githubusercontent.com/googlefonts/SourceSerifProGFVersion/main/fonts/'
        'SourceSerifPro-Regular.ttf')
serif_regular = FontManager(URL1)
URL2 = ('https://raw.githubusercontent.com/googlefonts/SourceSerifProGFVersion/main/fonts/'
        'SourceSerifPro-ExtraLight.ttf')
serif_extra_light = FontManager(URL2)
URL3 = ('https://raw.githubusercontent.com/google/fonts/main/ofl/rubikmonoone/'
        'RubikMonoOne-Regular.ttf')
rubik_regular = FontManager(URL3)
URL4 = 'https://raw.githubusercontent.com/googlefonts/roboto/main/src/hinted/Roboto-Thin.ttf'
robotto_thin = FontManager(URL4)
URL5 = ('https://raw.githubusercontent.com/google/fonts/main/apache/robotoslab/'
        'RobotoSlab%5Bwght%5D.ttf')
robotto_bold = FontManager(URL5)

#포지션별 파라미터
params_FW = [ 
    # 득점 기본
    'Gls', 'Ast', 'G+A', 'G-PK', 'PK', 'PKatt',

    # 기대 득점
    'xG', 'npxG', 'xAG', 'npxG+xAG', 'xG+xAG',
    'G-xG', 'np:G-xG',

    # 슈팅
    'Sh', 'SoT', 'SoT%', 'Sh/90', 'SoT/90',
    'G/Sh', 'G/SoT', 'Dist',

    # 공격 관여
    'Touches', 'Att Pen',
    'PrgC', 'PrgP', 'PrgR',

    # 찬스 창출
    'KP', 'SCA', 'SCA90', 'GCA', 'GCA90']#29
params_MF = [
    # 득점 관여 (공통)
    'Gls', 'Ast',

    # 패싱 & 창의성
    'xAG', 'xA', 'KP',
    'Cmp', 'Att', 'Cmp%',
    'TotDist', 'PrgDist', 'PrgP',
    'PPA', 

    # 볼 운반
    'Carries', 'PrgC', '1/3', 'CPA',
    'Succ', 'Succ%', 'Tkld%',

    # 공격 기여
    'SCA', 'SCA90', 'GCA', 'GCA90',

    # 수비 기여
    'Tkl', 'TklW', 'Int', 'Tkl+Int',
    'Def 3rd', 'Mid 3rd']#30
params_DF = [
    # 득점 관여 (공통)
    'Gls', 'Ast',

    # 수비 핵심
    'Tkl', 'TklW', 'Tkl%', 'Int', 'Tkl+Int',
    'Blocks', 'Clr', 'Err',
    'Def 3rd', 'Mid 3rd', 'Att 3rd',

    # 경합
    'Won', 'Lost', 'Won%',

    # 빌드업
    'Cmp', 'Cmp%', 'TotDist', 'PrgDist', 'PrgP',

    # 팀 기여도
    '+/-', '+/-90', 'On-Off',
    'xG+/-', 'xG+/-90']#26
params_GK = [

    # 기본 수비
    'GA', 'GA90',
    'SoTA', 'Saves', 'Save%',
    'CS', 'CS%',

    # 경기 결과
    'W', 'D', 'L',

    # 기대 실점
    'PSxG', 'PSxG/SoT',
    'PSxG+/-', 'PSxG+/-90',

    # PK 대응
    'PKatt', 'PKA', 'PKsv', 'PKm',

    # 스위퍼 / 발밑
    '#OPA', '#OPA/90', 'AvgDist']#21

# max param of positions
max_range_FW = [
    35, 20, 50, 25, 10, 10,       # Gls, Ast, G+A, G-PK, PK, PKatt
    30, 25, 15, 35, 5.5,          # xG, npxG, xAG, npxG+xAG, xG+xAG
    10, 10,                       # G-xG, np:G-xG
    160, 80, 100, 10, 5,          # Sh, SoT, SoT%, Sh/90, SoT/90 (90분당은 10정도로 제한 추천)
    0.5, 0.5, 45,                 # G/Sh, G/SoT, Dist (골결정력은 1.0이 최대지만 0.5 정도가 적당)
    3900, 360,                    # Touches, Att Pen
    220, 370, 500,                # PrgC, PrgP, PrgR
    100, 210, 15, 30, 15          # KP, SCA, SCA90, GCA, GCA90
]

max_range_MF = [
    35, 20,                       # Gls, Ast
    15, 15, 100,                  # xAG, xA, KP
    3300, 3700, 100,              # Cmp, Att, Cmp%
    60000, 26000, 370,            # TotDist, PrgDist, PrgP
    120, 440,                     # PPA, 1/3 (패스 관련)
    2400, 220, 130,               # Carries, PrgC, CPA
    170, 100, 100,                # Succ, Succ%, Tkld%
    210, 15, 30, 15,              # SCA, SCA90, GCA, GCA90
    140, 80, 80, 190,             # Tkl, TklW, Int, Tkl+Int
    90, 60                        # Def 3rd, Mid 3rd
]

max_range_DF = [
    15, 15,                       # Gls, Ast (수비수는 낮게 설정 추천)
    140, 80, 100, 80, 190,        # Tkl, TklW, Tkl%, Int, Tkl+Int
    80, 250, 10,                  # Blocks, Clr, Err
    90, 60, 30,                   # Def 3rd, Mid 3rd, Att 3rd
    170, 70, 100,                 # Won, Lost, Won%
    3300, 100, 60000, 26000, 370, # Cmp, Cmp%, TotDist, PrgDist, PrgP
    65, 3, 3,                     # +/-, +/-90, On-Off (90분당 데이터는 3~5 내외 추천)
    55, 3                         # xG+/-, xG+/-90
]

max_range_GK = [
    80, 5.0,                      # GA, GA90
    210, 150, 100,                # SoTA, Saves, Save%
    16, 100,                      # CS, CS%
    25, 20, 25,                   # W, D, L
    75, 0.6, 15, 1.5,             # PSxG, PSxG/SoT, PSxG+/-, /90
    10, 15, 5, 5,                 # PKatt, PKA, PKsv, PKm
    90, 10, 30                    # #OPA, #OPA/90, AvgDist
]

def parse_positions(pos_str):
    return set(p.strip() for p in pos_str.split(','))


def main():
    data=pd.read_csv("players_data-2024_2025.csv")
    data_clear=data.drop_duplicates()
    data_clear = data_clear.iloc[:, 1:]
    Leagues=sorted(data_clear['Comp'].unique())
    st.title('유럽 5대리그 스카우팅 차트 웹')
    on =st.toggle("비교 모드")
    if on:
        st.write("비교 모드 on")
    else:
        st.write("비교 모드 off")
    S_League_1 = st.selectbox("리그 선택", Leagues,key="league_1")
    if on:#플레이어 비교 모드
        if(S_League_1!=None):
            League_data_1=data_clear[data_clear['Comp']==S_League_1]
            Players_1=League_data_1['Player']
            S_Player_1 = st.selectbox("선수 선택1", Players_1)
            st.write("Selected Player: ",S_Player_1)
            player_data_1=data_clear[data_clear['Player']==S_Player_1]
            st.write(player_data_1)
            pos=player_data_1.iloc[0]['Pos']
            st.write(S_Player_1,"\'s main stats")
            if pos in ['FW', 'FW,MF', 'FW,DF']:
                st.write(player_data_1.loc[:,params_FW])
            elif pos in ['MF', 'MF,FW', 'MF,DF']:
                st.write(player_data_1.loc[:,params_MF])
            elif pos in ['DF', 'DF,MF', 'DF,FW']:
                st.write(player_data_1.loc[:,params_DF])
            else:
                st.write(player_data_1.loc[:,params_GK])
        
        
        
            if pos in ['FW', 'FW,MF', 'FW,DF']:
                num_params = len(params_FW)
                rader=Radar(params=params_FW,min_range=[0]*num_params,max_range=max_range_FW)
                
                values_data_1=player_data_1.loc[:,params_FW]
            elif pos in ['MF', 'MF,FW', 'MF,DF']:
                num_params = len(params_MF)
                rader=Radar(params=params_MF,min_range=[0]*num_params,max_range=max_range_MF)
                
                values_data_1=player_data_1.loc[:,params_MF]
            elif pos in ['DF', 'DF,MF', 'DF,FW']:
                num_params = len(params_DF)
                rader=Radar(params=params_DF,min_range=[0]*num_params,max_range=max_range_DF)
                
                values_data_1=player_data_1.loc[:,params_DF]
            else:
                num_params = len(params_GK)
                rader=Radar(params=params_GK,min_range=[0]*num_params,max_range=max_range_GK)
                
                values_data_1=player_data_1.loc[:,params_GK]
            values_data_1=values_data_1.iloc[0]
            values_data_1 = pd.to_numeric(values_data_1, errors='coerce').fillna(0).tolist()

            S_League_2 = st.selectbox("리그 선택", Leagues,key="league_2")
            League_data_2=data_clear[data_clear['Comp']==S_League_2]
            Players_2=League_data_2['Player']
            S_Player_2 = st.selectbox("선수 선택2", Players_2)
            st.write("Selected Player: ",S_Player_2)
            player_data_2=data_clear[data_clear['Player']==S_Player_2]
            st.write(player_data_2)
            pos=player_data_2.iloc[0]['Pos']
            st.write(S_Player_2,"\'s main stats")
            if pos in ['FW', 'FW,MF', 'FW,DF']:
                st.write(player_data_2.loc[:,params_FW])
            elif pos in ['MF', 'MF,FW', 'MF,DF']:
                st.write(player_data_2.loc[:,params_MF])
            elif pos in ['DF', 'DF,MF', 'DF,FW']:
                st.write(player_data_2.loc[:,params_DF])
            else:
                st.write(player_data_2.loc[:,params_GK])
        
        
        
            if pos in ['FW', 'FW,MF', 'FW,DF']:
                num_params = len(params_FW)
                rader=Radar(params=params_FW,min_range=[0]*num_params,max_range=max_range_FW)
                fig,ax=rader.setup_axis()
                values_data_2=player_data_2.loc[:,params_FW]
            elif pos in ['MF', 'MF,FW', 'MF,DF']:
                num_params = len(params_MF)
                rader=Radar(params=params_MF,min_range=[0]*num_params,max_range=max_range_MF)
                fig,ax=rader.setup_axis()
                values_data_2=player_data_2.loc[:,params_MF]
            elif pos in ['DF', 'DF,MF', 'DF,FW']:
                num_params = len(params_DF)
                rader=Radar(params=params_DF,min_range=[0]*num_params,max_range=max_range_DF)
                fig,ax=rader.setup_axis()
                values_data_2=player_data_2.loc[:,params_DF]
            else:
                num_params = len(params_GK)
                rader=Radar(params=params_GK,min_range=[0]*num_params,max_range=max_range_GK)
                fig,ax=rader.setup_axis()
                values_data_2=player_data_2.loc[:,params_GK]
            values_data_2=values_data_2.iloc[0]
            values_data_2 = pd.to_numeric(values_data_2, errors='coerce').fillna(0).tolist()
            pos1_set=parse_positions(player_data_1.iloc[0]['Pos'])
            pos2_set=parse_positions(player_data_2.iloc[0]['Pos'])
            pos_set=pos1_set&pos2_set
            if not pos_set:
                st.warning("동포지션의 선수만 비교가 가능합니다.")
                return
            else:
                rings_inner = rader.draw_circles(ax=ax, facecolor='#ffb2b2', edgecolor='#fc5f5f')
                radar_output = rader.draw_radar_compare(values_data_1, values_data_2, ax=ax,
                                        kwargs_radar={'facecolor': '#00f2c1', 'alpha': 0.6},
                                        kwargs_compare={'facecolor': '#d80499', 'alpha': 0.6})
                radar_poly, radar_poly2, vertices1, vertices2 = radar_output
                range_labels = rader.draw_range_labels(ax=ax, fontsize=15,
                                       fontproperties=robotto_thin.prop)
                param_labels = rader.draw_param_labels(ax=ax, fontsize=15,
                                       fontproperties=robotto_thin.prop)
            st.pyplot(fig)
    else:#플레이어 비교 모드 off
        if(S_League_1!=None):
            League_data=data_clear[data_clear['Comp']==S_League_1]
            Players=League_data['Player']
            S_Player = st.selectbox("선수 선택", Players)
            st.write("Selected Player: ",S_Player)
            player_data=data_clear[data_clear['Player']==S_Player]
            st.write(player_data)
            pos=player_data.iloc[0]['Pos']
            st.write(S_Player,"\'s main stats")
            if pos in ['FW', 'FW,MF', 'FW,DF']:
                st.write(player_data.loc[:,params_FW])
            elif pos in ['MF', 'MF,FW', 'MF,DF']:
                st.write(player_data.loc[:,params_MF])
            elif pos in ['DF', 'DF,MF', 'DF,FW']:
                st.write(player_data.loc[:,params_DF])
            else:
                st.write(player_data.loc[:,params_GK])
        
        
        
            if pos in ['FW', 'FW,MF', 'FW,DF']:
                num_params = len(params_FW)
                rader=Radar(params=params_FW,min_range=[0]*num_params,max_range=max_range_FW)
                fig,ax=rader.setup_axis()
                values_data=player_data.loc[:,params_FW]
            elif pos in ['MF', 'MF,FW', 'MF,DF']:
                num_params = len(params_MF)
                rader=Radar(params=params_MF,min_range=[0]*num_params,max_range=max_range_MF)
                fig,ax=rader.setup_axis()
                values_data=player_data.loc[:,params_MF]
            elif pos in ['DF', 'DF,MF', 'DF,FW']:
                num_params = len(params_DF)
                rader=Radar(params=params_DF,min_range=[0]*num_params,max_range=max_range_DF)
                fig,ax=rader.setup_axis()
                values_data=player_data.loc[:,params_DF]
            else:
                num_params = len(params_GK)
                rader=Radar(params=params_GK,min_range=[0]*num_params,max_range=max_range_GK)
                fig,ax=rader.setup_axis()
                values_data=player_data.loc[:,params_GK]
            values_data=values_data.iloc[0]
            values_data = pd.to_numeric(values_data, errors='coerce').fillna(0).tolist()
            rings_inner = rader.draw_circles(ax=ax, facecolor="#FF8E8E8F", edgecolor="#000000")  # draw circles
            radar_output = rader.draw_radar(values_data, ax=ax,
                                kwargs_radar={'facecolor': "#c5a5f8b9"})
            radar_poly, rings_outer, vertices = radar_output
            range_labels = rader.draw_range_labels(ax=ax, fontsize=10,
                                       fontproperties=robotto_thin.prop)
            param_labels = rader.draw_param_labels(ax=ax, fontsize=15,
                                       fontproperties=robotto_bold.prop)
            lines = rader.spoke(ax=ax, color='#a6a4a1', linestyle='--', zorder=2)
            st.pyplot(fig)

        
        

if __name__ == "__main__":
    main()
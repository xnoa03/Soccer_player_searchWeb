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
    'PPA', '01-03',

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

    #포지션별 파라미터 인덱스
params_FW_IDX = [
    11, 12, 13, 14, 15, 16,          # Gls, Ast, G+A, G-PK, PK, PKatt
    19, 20, 21, 22, 27,              # xG, npxG, xAG, npxG+xAG, xG+xAG
    44, 45,                          # G-xG, np:G-xG
    35, 36, 37, 38, 39,              # Sh, SoT, SoT%, Sh/90, SoT/90
    40, 41, 42,                      # G/Sh, G/SoT, Dist
    123, 128,                        # Touches, Att Pen
    23, 24, 25,                      # PrgC, PrgP, PrgR
    66, 90, 91, 98, 99               # KP, SCA, SCA90, GCA, GCA90
    ]
params_MF_IDX = [
    11, 12,                          # Gls, Ast
    21, 64, 66,                      # xAG, xA, KP
    54, 55, 56,                      # Cmp, Att, Cmp%
    57, 58, 24,                      # TotDist, PrgDist, PrgP
    68, 67,                          # PPA, 01-03
    131, 23, 135, 136,               # Carries, PrgC, 1/3, CPA
    133, 134, 138,                   # Succ, Succ%, Tkld%
    90, 91, 98, 99,                  # SCA, SCA90, GCA, GCA90
    103, 104, 110, 111,              # Tkl, TklW, Int, Tkl+Int
    105, 106                         # Def 3rd, Mid 3rd
    ]
params_DF_IDX = [
    11, 12,                          # Gls, Ast
    103, 104, 108,                   # Tkl, TklW, Tkl%
    110, 111,                        # Int, Tkl+Int
    109, 112, 113,                   # Blocks, Clr, Err
    105, 106, 107,                   # Def 3rd, Mid 3rd, Att 3rd
    171, 172, 173,                   # Won, Lost, Won%
    54, 56, 57, 58, 24,              # Cmp, Cmp%, TotDist, PrgDist, PrgP
    160, 161, 162,                   # +/-, +/-90, On-Off
    165, 166                         # xG+/-, xG+/-90
    ]
params_GK_IDX = [
    11, 12,                          # Gls, Ast
    186, 187,                        # GA, GA90
    188, 189, 190,                   # SoTA, Saves, Save%
    194, 195,                        # CS, CS%
    191, 192, 193,                   # W, D, L
    206, 207,                        # PSxG, PSxG/SoT
    208, 209,                        # PSxG+/-, PSxG+/-90
    196, 197, 198, 199,              # PKatt, PKA, PKsv, PKm
    219, 220, 221                    # #OPA, #OPA/90, AvgDist
    ]

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
        pos=player_data.iloc[0]['Pos']
        st.write(S_Player,"\'s main stats")
        if pos in ['FW', 'FW,MF', 'FW,DF']:
            st.write(player_data.iloc[:,params_FW_IDX])
        elif pos in ['MF', 'MF,FW', 'MF,DF']:
            st.write(player_data.iloc[:,params_MF_IDX])
        elif pos in ['DF', 'DF,MF', 'DF,FW']:
            st.write(player_data.iloc[:,params_DF_IDX])
        else:
            st.write(player_data.iloc[:,params_GK_IDX])
        
        
        
        if pos in ['FW', 'FW,MF', 'FW,DF']:
            num_params = len(params_FW)
            rader=Radar(params=params_FW,min_range=[0]*num_params,max_range=[40]*num_params)
            fig,ax=rader.setup_axis()
            values_data=player_data.iloc[:,params_FW_IDX]
        elif pos in ['MF', 'MF,FW', 'MF,DF']:
            num_params = len(params_MF)
            rader=Radar(params=params_MF,min_range=[0]*num_params,max_range=[40]*num_params)
            fig,ax=rader.setup_axis()
            values_data=player_data.iloc[:,params_MF_IDX]
        elif pos in ['DF', 'DF,MF', 'DF,FW']:
            num_params = len(params_DF)
            rader=Radar(params=params_DF,min_range=[0]*num_params,max_range=[40]*num_params)
            fig,ax=rader.setup_axis()
            values_data=player_data.iloc[:,params_DF_IDX]
        else:
            num_params = len(params_GK)
            rader=Radar(params=params_GK,min_range=[0]*num_params,max_range=[40]*num_params)
            fig,ax=rader.setup_axis()
            values_data=player_data.iloc[:,params_GK_IDX]
        values_data=values_data.iloc[0]
        values_data = pd.to_numeric(values_data, errors='coerce').fillna(0).tolist()
        rings_inner = rader.draw_circles(ax=ax, facecolor="#FFFFFF63", edgecolor="#000000")  # draw circles
        radar_output = rader.draw_radar(values_data, ax=ax,
                                kwargs_radar={'facecolor': "#dbc4ff"})  # draw the radar
        radar_poly, rings_outer, vertices = radar_output
        range_labels = rader.draw_range_labels(ax=ax, fontsize=10,
                                       fontproperties=robotto_thin.prop)  # draw the range labels
        param_labels = rader.draw_param_labels(ax=ax, fontsize=15,
                                       fontproperties=robotto_bold.prop)  # draw the param labels
        st.pyplot(fig)
        
        

if __name__ == "__main__":
    main()
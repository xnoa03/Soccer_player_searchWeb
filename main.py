# main.py
import streamlit as st
import pandas as pd
import utils as u
import draw_radar as v

def main():
    data_clear = u.load_data("players_data-2024_2025.csv")
    if data_clear is None:
        st.error("데이터 파일을 찾을 수 없습니다.")
        return

    Leagues = sorted(data_clear['Comp'].unique())

    st.title('⚽ 유럽 5대리그 스카우팅 차트 웹')
    
    on = st.toggle("비교 모드")
    if on:
        st.write(" **비교 모드 ON**")
    else:
        st.write(" **싱글 모드**")

    S_League_1 = st.selectbox("리그 선택", Leagues, key="league_1")

    if on:
        if S_League_1:
            League_data_1 = data_clear[data_clear['Comp'] == S_League_1]
            Players_1 = sorted(League_data_1['Player'].unique())
            S_Player_1 = st.selectbox("선수 선택 1", Players_1)
            

            S_League_2 = st.selectbox("리그 선택 (비교 대상)", Leagues, key="league_2")
            if S_League_2:
                League_data_2 = data_clear[data_clear['Comp'] == S_League_2]
                Players_2 = sorted(League_data_2['Player'].unique())
                S_Player_2 = st.selectbox("선수 선택 2", Players_2)

                if S_Player_1 and S_Player_2:

                    p1_data = data_clear[data_clear['Player'] == S_Player_1].iloc[0]
                    p2_data = data_clear[data_clear['Player'] == S_Player_2].iloc[0]
                    
                    st.write(f"**{S_Player_1}** ({p1_data['Pos']}) vs **{S_Player_2}** ({p2_data['Pos']})")


                    pos1_set = u.parse_positions(p1_data['Pos'])
                    pos2_set = u.parse_positions(p2_data['Pos'])
                    pos_set = pos1_set & pos2_set

                    if not pos_set:
                        st.warning(" 두 선수의 포지션이 겹치지 않아 비교할 수 없습니다.")
                    else:

                        params, max_range = u.get_params_and_ranges(list(pos_set))
                        

                        v1 = u.get_player_data(data_clear, S_Player_1, params)
                        v2 = u.get_player_data(data_clear, S_Player_2, params)


                        fig = v.create_comparison_chart(params, max_range, v1, v2, S_Player_1, S_Player_2)
                        st.pyplot(fig)
                        

                        st.dataframe(pd.DataFrame({S_Player_1: v1, S_Player_2: v2}, index=params).T)

    else:
        if S_League_1:
            League_data = data_clear[data_clear['Comp'] == S_League_1]
            Players = sorted(League_data['Player'].unique())
            S_Player = st.selectbox("선수 선택", Players)
            
            if S_Player:
                player_data = data_clear[data_clear['Player'] == S_Player].iloc[0]
                pos_str = player_data['Pos']
                st.write(f"Selected Player: **{S_Player}** ({pos_str})")
                
                pos_list = [p.strip() for p in pos_str.split(',')]
                params, max_range = u.get_params_and_ranges(pos_list)
                
                values = u.get_player_data(data_clear, S_Player, params)
                
                fig = v.create_radar_chart(params, max_range, values)
                st.pyplot(fig)
                
                st.dataframe(pd.DataFrame(values, index=params, columns=[S_Player]).T)

if __name__ == "__main__":
    main()
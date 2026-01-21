from mplsoccer import Radar, FontManager

URL1 = 'https://raw.githubusercontent.com/googlefonts/SourceSerifProGFVersion/main/fonts/SourceSerifPro-Regular.ttf'
URL2 = 'https://raw.githubusercontent.com/googlefonts/SourceSerifProGFVersion/main/fonts/SourceSerifPro-ExtraLight.ttf'
URL3 = 'https://raw.githubusercontent.com/google/fonts/main/ofl/rubikmonoone/RubikMonoOne-Regular.ttf'
URL4 = 'https://raw.githubusercontent.com/googlefonts/roboto/main/src/hinted/Roboto-Thin.ttf'
URL5 = 'https://raw.githubusercontent.com/google/fonts/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf'

fonts = {
    "serif_regular": FontManager(URL1),
    "serif_extra_light": FontManager(URL2),
    "rubik_regular": FontManager(URL3),
    "robotto_thin": FontManager(URL4),
    "robotto_bold": FontManager(URL5),
}

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
    'Carries', 'PrgC', 'CPA',
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
    120,                          # PPA
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
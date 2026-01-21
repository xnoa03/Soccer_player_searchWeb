# visualization.py
from mplsoccer import Radar
import constants as c

def create_radar_chart(params, max_range, values, color='#c5a5f8b9'):
    num_params = len(params)
    radar = Radar(params=params, min_range=[0]*num_params, max_range=max_range)
    fig, ax = radar.setup_axis()
    
    radar.draw_circles(ax=ax, facecolor="#FF8E8E8F", edgecolor="#000000")
    radar.draw_radar(values, ax=ax, kwargs_radar={'facecolor': color})
    
    radar.draw_range_labels(ax=ax, fontsize=10, fontproperties=c.fonts["robotto_thin"].prop)
    radar.draw_param_labels(ax=ax, fontsize=15, fontproperties=c.fonts["robotto_bold"].prop)
    radar.spoke(ax=ax, color='#a6a4a1', linestyle='--', zorder=2)
    
    return fig

def create_comparison_chart(params, max_range, v1, v2, player1_name, player2_name):
    num_params = len(params)
    radar = Radar(params=params, min_range=[0]*num_params, max_range=max_range)
    fig, ax = radar.setup_axis()
    
    radar.draw_circles(ax=ax, facecolor='#ffb2b2', edgecolor='#fc5f5f')
    
    radar.draw_radar_compare(
        v1, v2, ax=ax,
        kwargs_radar={'facecolor': '#00f2c1', 'alpha': 0.6},
        kwargs_compare={'facecolor': '#d80499', 'alpha': 0.6}
    )
    
    radar.draw_range_labels(ax=ax, fontsize=10, fontproperties=c.fonts["robotto_thin"].prop)
    radar.draw_param_labels(ax=ax, fontsize=15, fontproperties=c.fonts["robotto_bold"].prop)
    

    ax.legend([player1_name, player2_name], loc='upper center', bbox_to_anchor=(0.5, 1.1))
    
    return fig
import matplotlib.pyplot as plt              # 引入 matplotlib 的绘图库
import seaborn as sns                        # seaborn 用于美化图表（虽然你这里没调样式）
import matplotlib.ticker as ticker           # 控制坐标轴刻度格式
import numpy as np                           # 数值运算库
from matplotlib.ticker import MaxNLocator    # 控制 X 轴刻度数量（虽然这里没用）
import pandas as pd                          # 数据处理库，确保能处理 datetime 类型


def plot_accumulated_exports(dataframe_list, highlight_years):
    """
    根据 dataframe_list 绘制累计出口图。
    参数：
        dataframe_list: 一个按年份排序的 DataFrame 列表，每个代表一个 crop year 的数据。
        highlight_years: 需要高亮的年份（int）列表。
    """

    # 初始化画布
    fig, ax = plt.subplots()

    # 禁用科学计数法显示 Y 轴数字（例如避免 2e7 这种写法）
    ax.get_yaxis().get_major_formatter().set_scientific(False)

    # 加网格线（alpha 是透明度）
    plt.grid(alpha=0.3)

    # 设置 X 轴刻度位置（每 2 个月一个 tick，4.28 周 ≈ 1 月）
    tick_val_x = [0, 4.28*2, 4.28*4, 4.28*6, 4.28*8, 4.28*10, 4.28*12]
    tick_lab_x = ['Sep 01', 'Nov 01', 'Jan 01', 'Mar 01', 'May 01', 'Jul 01', 'Sep 01']
    ax.xaxis.set_ticks(tick_val_x)
    plt.xticks(tick_val_x, tick_lab_x)

    # 去掉上右左三条轴线（美化图表）
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # 设置 Y 轴从 0 开始
    ax.set_ylim(ymin=0)

    # 高亮年份随机色（或循环使用标准颜色）
    color_palette = plt.cm.tab10.colors + plt.cm.Set2.colors + plt.cm.Dark2.colors
    highlight_color_map = {year: color_palette[i % len(color_palette)] for i, year in enumerate(highlight_years)}

    # 遍历 dataframe_list 中每一个年份的数据
    for df in dataframe_list:
        df['weekEndingDate'] = pd.to_datetime(df['weekEndingDate'])
        df['index1'] = df.index
        year_label = df.iloc[0, -2].year + 1

        if year_label in highlight_years:
            ax.plot(
                df['index1'],
                df['accumulatedExports'],
                color=highlight_color_map[year_label],
                marker='o',
                linewidth=2,
                label=str(year_label)
            )
        else:
            ax.plot(
                df['index1'],
                df['accumulatedExports'],
                linewidth=1,
                label=str(year_label)
            )

    # 设置坐标轴标签和图标题
    ax.set_xlabel("Ending week date", labelpad=8)
    ax.set_ylabel("Accumulated Exports (tons)", labelpad=8)

    # 图标题根据年份范围动态生成
    first_year = dataframe_list[0].iloc[0, -2].year + 1
    last_year = dataframe_list[-1].iloc[0, -2].year + 1
    ax.set_title(f"Weekly Soybean Accumulated Exports by Crop Year: {first_year} to {last_year}", pad=30)

    # 图例放到右侧外面，字体大小 9，加标题，去掉边框
    ax.legend(
        bbox_to_anchor=(1.01, 1.025),
        prop={'size': 9},
        title="Crop Year",
        frameon=False
    )

    # 自定义 Y 轴刻度值和显示文字（单位：百万吨）
    tick_val = list(range(0, 35000001, 5000000))
    tick_lab = ['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M']
    plt.yticks(tick_val, tick_lab)

    # 显示图形
    plt.show()
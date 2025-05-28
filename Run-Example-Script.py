#在运行之前，请在usda_export_fetcher中输入API key
import sys
sys.path.append("src")

from soybean_report import YearList, fetch_usda_data_for_years, plot_accumulated_exports, print_welcome

# 打印欢迎界面
print_welcome()

# 获取用户输入的年份和高亮年份
yl = YearList()
yl.prompt_user_input()
years = yl.get_years()
highlight_years = yl.get_highlight_years()

# 抓取数据
dataframe_list = fetch_usda_data_for_years(years)

# 显示图表
plot_accumulated_exports(dataframe_list, highlight_years)
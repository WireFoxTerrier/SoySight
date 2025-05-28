class YearList:
    def __init__(self):
        # 初始化时创建一个空列表，用来存储用户输入的年份列表
        self.years = []
        self.highlight_years = []  # 新增：用于存储需要高亮显示的年份

    def prompt_user_input(self):
        # 向用户展示输入格式说明
        print("📅 Please input years in one of the following formats:")
        print("  - Range format: 2001-2009")
        print("  - List format: 2001,2003,2007")
        print("👉 Just type the years directly below (no need for quotation marks)\n")

        # 读取用户输入
        user_input = input("Enter years (e.g., 2001-2009 or 2001,2002,2003): ")
        self.years = self.parse_input(user_input)  # 解析并保存

        # 新增功能：提示是否高亮某些年份
        highlight_input = input("Do you want to highlight any year(s)? (Enter like: 2015,2022 or leave blank to skip): ")
        if highlight_input.strip():
            self.highlight_years = self.parse_input(highlight_input)  # 重用相同的解析逻辑
        else:
            self.highlight_years = []

    def parse_input(self, user_input: str):
        # 清除前后空格
        user_input = user_input.strip()

        # 如果是用“-”连接的区间格式（例如 2001-2009）
        if '-' in user_input:
            start_str, end_str = user_input.split('-')

            # 校验是否为数字
            if not (start_str.isdigit() and end_str.isdigit()):
                raise ValueError("Invalid range format. Example: 2001-2009")

            start, end = int(start_str), int(end_str)

            if start > end or start < 1900:
                raise ValueError("Year range is invalid or too old.")

            return list(range(start, end + 1))

        else:
            # 逗号分隔格式（例如 2001,2002,2015）
            year_strs = user_input.split(',')
            years = []

            for y in year_strs:
                y = y.strip()
                if not y.isdigit() or len(y) != 4:
                    raise ValueError(f"Invalid year: {y}")

                years.append(int(y))

            return sorted(set(years))  # 去重并排序

    def get_years(self):
        return self.years

    def get_highlight_years(self):
        return self.highlight_years
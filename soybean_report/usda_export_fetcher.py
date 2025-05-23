import requests
import pandas as pd

# 固定的 API Key 和 URL 头部
API_KEY = "a25d46d9-0186-4ee5-b60a-dcd1045d5be9"
URL_HEAD = "https://apps.fas.usda.gov/OpenData/api/esr/exports/commodityCode/801/countryCode/5700/marketYear/"

def fetch_usda_data_for_year(year):
    """
    向 USDA API 请求指定年份的大豆出口数据，返回一个 DataFrame。
    如果请求失败，将抛出异常。
    """
    url = URL_HEAD + str(year)
    response = requests.get(url, headers={"API_KEY": API_KEY})
    response.raise_for_status()  # ❗ 如果状态码非 200，立刻抛异常，不默默失败
    json_data = response.json()
    return pd.DataFrame(json_data)

def fetch_usda_data_for_years(year_list):
    """
    对多个年份调用 fetch_usda_data_for_year，返回一个包含多个 DataFrame 的列表。
    每个 DataFrame 表示一个 crop year。
    """
    df_list = []
    for year in year_list:
        print(f"📡 Fetching data for {year}...")
        df = fetch_usda_data_for_year(year)
        df_list.append(df)

    return df_list 
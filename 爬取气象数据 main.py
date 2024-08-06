from request import get_city_id, read_now, get_image, read_past, read_forecast,create_rgb_image,get_city_name
from datetime import datetime

# # 示例调用
# print(read_now('南京')["Temperature"])
# # print((read_past(33.22, 120.1, 2024052500, 2024052624)))
# print(read_forecast('北京'))
# get_image(202405280630)
# path = r"F:\TC\气象虚拟实习_kxy\气象卫星资料处理实践与应用\FY4A-_AGRI--_N_DISK_1047E_L1-_FDI-_MULT_NOM_20180517040000_20180517041459_4000M_V0001.HDF"
# create_rgb_image(path)
# print(type(read_forecast('北京')['日期']))
# print(read_forecast('北京')['最低温度'])
# print(read_forecast('北京')['最高温度'])
# print(read_forecast('北京')['日期'])
import pandas as pd

# 调用 read_past 获取数据
data = read_past(30, 120.1, 2021090110, 2021100910)[0]

# 将数据转换为 DataFrame
df = pd.DataFrame(data)

# 保存 DataFrame 到 Excel 文件
df.to_excel('past_data.xlsx', index=False)



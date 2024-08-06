import json
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import os
import pandas as pd
from datetime import datetime, timedelta
from PIL import Image

def generate_radar(folder_path, excel_path, output_gif_path='outputradar.gif'):
    # 获取文件夹下所有文件
    file_list = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.txt')]

    # 创建图像列表
    images = []

    # 循环处理每个文件
    for file_path in file_list:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()

        # 使用json模块解析数据
        data_dict = json.loads(data)

        # 提取数值部分
        values = data_dict["values"]

        # 检查数据长度
        x_points = 861
        y_points = 571
        expected_length = x_points * y_points
        if len(values) != expected_length:
            raise ValueError(f"数据长度不匹配: 期望 {expected_length}, 但得到 {len(values)}")

        # 将一维数据转换为二维数据
        values_2d = np.array(values).reshape((y_points, x_points))

        # 获取时间
        file_name = os.path.basename(file_path)
        file_name = file_name.replace('DBZ_', '').replace('.txt', '')
        time_start = datetime.strptime(file_name, '%Y%m%d%H%M')
        # 计算结束时间（比起始时间多6分钟）
        time_end = time_start + timedelta(minutes=6)

        # 读取Excel文件
        df = pd.read_excel(excel_path, usecols=['time', 'latitude', 'longitude', 'density'])

        # 转换time列为datetime对象
        df['time'] = pd.to_datetime(df['time'], format='%d/%m/%Y %H:%M:%S.%f')

        # 筛选在start_time和end_time之间的数据
        lightning_data = df[(df['time'] >= time_start) & (df['time'] <= time_end)]

        # 处理回波值，小于等于0的值设为np.nan
        values_2d[values_2d <= 0] = np.nan

        # 经纬度范围
        lat_start, lat_end = 19.99, 25.7
        lon_start, lon_end = 109.4, 118.01

        # 创建经纬度网格
        lats = np.linspace(lat_end, lat_start, y_points)  # 反转纬度方向
        lons = np.linspace(lon_start, lon_end, x_points)
        lon_grid, lat_grid = np.meshgrid(lons, lats)

        # 绘制雷达回波图
        fig = plt.figure(figsize=(10, 8))
        ax = plt.axes(projection=ccrs.PlateCarree())

        # 添加自然地理特征
        ax.add_feature(cfeature.LAND)
        ax.add_feature(cfeature.OCEAN)
        ax.add_feature(cfeature.COASTLINE)
        ax.add_feature(cfeature.BORDERS, linestyle=':')
        ax.add_feature(cfeature.LAKES, alpha=0.5)
        ax.add_feature(cfeature.RIVERS)

        # 设置地图范围
        ax.set_extent([113, 113.5, 22, 22.5])

        # 绘制回波图
        mesh = ax.pcolormesh(lon_grid, lat_grid, values_2d, shading='auto', cmap='jet')

        # 绘制闪电位置
        sc = ax.scatter(lightning_data['longitude'], lightning_data['latitude'],
                        edgecolor='red', marker='+', color='black', s=2, transform=ccrs.PlateCarree())

        # 添加自定义图例说明
        plt.text(0.95, 0.05, '+: Lightning', ha='right', va='bottom', transform=ax.transAxes, fontsize=10,
                 bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

        # 添加颜色条，设置小一点
        plt.colorbar(mesh, ax=ax, orientation='vertical', label='Radar Echo DBZ', shrink=0.7)

        # 设置标签和标题
        ax.set_xlabel('Longitude(E)')
        ax.set_ylabel('Latitude(N)')

        # 添加经纬度网格和标签
        ax.set_xticks(np.arange(112.5, 114.6, 0.2))
        ax.set_yticks(np.arange(21.8, 23.8, 0.2))

        # 设置标题，使用'\n'换行符
        ax.set_title(r'Echo_GuangDong_Zongshang_Beijing Time: {}  Max:{} DBZ'.format(file_name, np.nanmax(values_2d)),
                     fontsize=14)

        # 保存图像
        img_path = f"{file_name}.png"
        plt.savefig(img_path, dpi=360, bbox_inches='tight')
        images.append(Image.open(img_path))
        plt.close()

    # 保存GIF
    images[0].save(output_gif_path, save_all=True, append_images=images[1:], optimize=False, duration=1200, loop=0)

# 使用示例
# generate_radar(r"F:\TC\Lighting\20220816", r"F:\TC\Lighting\zs0816.xlsx", 'output.gif')

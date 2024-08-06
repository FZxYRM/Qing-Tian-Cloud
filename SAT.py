import os
import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import geopandas as gpd
from datetime import datetime, timedelta
import pandas as pd
import imageio  # 导入 imageio 库

def generate_sat(folder_path, excel_path, output_path='outputsat.gif'):
    # 存储图片的列表
    images = []

    # 读取shp文件
    file_path_gd = r"F:\Arcgis\2021年5月区县\区县数据-21-05.shp"
    guangdong = gpd.read_file(file_path_gd)
    guangdong = guangdong[guangdong['province'] == '广东省']

    # 循环读取文件夹中的NC文件
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.NC'):
            file_path = os.path.join(folder_path, file_name)
            # 读取 nc 文件
            dataset = nc.Dataset(file_path)
            # 提取变量
            ctt = dataset['CTT'][:]
            x_nc = dataset['x'][:]
            y_nc = dataset['y'][:]
            # 定义经纬度范围
            lat_min, lat_max = -80.883, 80.883
            lon_min, lon_max = 61.820, 134.730
            # 转换x和y为经纬度
            x_deg = np.linspace(lon_min, lon_max, len(x_nc))
            y_deg = np.linspace(lat_min, lat_max, len(y_nc))
            # 转置CTT以匹配x和y的形状
            ctt = ctt.T
            # 创建网格
            x_grid, y_grid = np.meshgrid(x_deg, y_deg)

            # 提取时间信息
            start_time_str = dataset.time_coverage_start
            end_time_str = dataset.time_coverage_end
            # 将字符串转换为datetime对象
            start_time = datetime.strptime(start_time_str, "%Y-%m-%dT%H:%M:%S.%fZ")
            end_time = datetime.strptime(end_time_str, "%Y-%m-%dT%H:%M:%S.%fZ")
            # 加上8小时
            start_time += timedelta(hours=8)
            end_time += timedelta(hours=8)
            # 格式化时间为字符串
            title_time = f"Beijing Time: {start_time} to {end_time}"

            # 读取Excel文件
            df = pd.read_excel(excel_path, usecols=['time', 'latitude', 'longitude', 'density'])

            # 转换time列为datetime对象
            df['time'] = pd.to_datetime(df['time'], format='%d/%m/%Y %H:%M:%S.%f')

            # 筛选在start_time和end_time之间的数据
            lightning_data = df[(df['time'] >= start_time) & (df['time'] <= end_time)]

            # 绘制图像
            fig = plt.figure(figsize=(10, 8))
            ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

            # 添加底图（广东省区县地图）
            guangdong.plot(ax=ax, facecolor='lightgray', edgecolor='black')

            # 绘制CTT图像
            contour = ax.contourf(x_grid, y_grid, ctt, cmap='coolwarm', transform=ccrs.PlateCarree())
            cbar = plt.colorbar(contour, label='CTT', orientation='vertical', shrink=0.7)
            cbar.set_label('Cloud Top Temperature (K)', rotation=90, labelpad=15)

            # 设置显示范围
            ax.set_extent([113, 113.5, 22, 22.5])  # zs
            ax.set_xticks(np.arange(112.5, 114.5, 0.2))
            ax.set_yticks(np.arange(21.8, 23.8, 0.2))

            # 设置标题
            ax.set_title(f'Zhong Shang Cloud Top Temperature\n{title_time}')

            # 绘制闪电位置
            sc = ax.scatter(lightning_data['longitude'], lightning_data['latitude'],
                            edgecolor='red', marker='x', color='black', s=2, transform=ccrs.PlateCarree())

            # 添加自定义图例说明
            plt.text(0.95, 0.05, '+: Lightning', ha='right', va='bottom', transform=ax.transAxes, fontsize=10,
                     bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

            # 将图像保存到列表中
            plt.savefig(f"output_{file_name[:-3]}.png", bbox_inches='tight', dpi=360)
            images.append(imageio.imread(f"output_{file_name[:-3]}.png"))
            plt.close()

    # 生成 GIF
    imageio.mimsave(output_path, images, duration=1200)

# 使用示例
generate_sat(r"F:\TC\Lighting\CTT ZS", r"F:\TC\Lighting\zs0816.xlsx", 'output.gif')

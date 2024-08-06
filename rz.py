import h5py
import matplotlib.pyplot as plt
import os
import numpy as np

# 文件路径
path = r"F:\TC\气象虚拟实习_kxy\气象卫星资料处理实践与应用\FY4A-_AGRI--_N_DISK_1047E_L1-_FDI-_MULT_NOM_20180517040000_20180517041459_4000M_V0001.HDF"

# 打开 HDF 文件
data = h5py.File(path, "r")

# 打印 HDF 文件的键（即数据集的名称）
keys = list(data.keys())
print(keys)

# 关键词
keyword = "NOMChannel"

# 遍历数据集的名称，并寻找包含关键词的名称
for key in keys:
    if keyword in str(key):
        channel_data = data[key][:]+1
        # channel_data[channel_data > 3000] = 0  # 将超过3000的值标定为0
        plt.imshow(channel_data, cmap='gray')
        plt.title(key)
        plt.colorbar(label='Intensity')
        plt.xlabel('X Axis')
        plt.ylabel('Y Axis')
        plt.axis('off')
        plt.savefig(os.path.join(os.path.dirname(__file__), f"{key}.png"), dpi=1080, facecolor='white', bbox_inches='tight')
        plt.show()
        print("通道 " + key + " 绘制完成并保存")

# 黑白增强通道1
channel_data = data['NOMChannel01'][:]
channel_data[channel_data > 3000] = 0  # 将超过3000的值标定为0

# 黑白增强处理
enhanced_data = (channel_data - np.min(channel_data)) / (np.max(channel_data) - np.min(channel_data))

# # 绘制图像
# plt.imshow(enhanced_data, cmap='gray')
# plt.title('NOMChannel01 0.47um strengthen')
# plt.colorbar(label='Intensity')
# plt.xlabel('X Axis')
# plt.ylabel('Y Axis')
# plt.axis('off')
# # 保存图像
# plt.savefig(os.path.join(os.path.dirname(__file__), f"NOMChannel01 增强.png"), dpi=1080, facecolor='white', bbox_inches='tight')
# plt.show()




# # 加载通道数据并加上 1
# red_channel = data['NOMChannel01'][:] 
# green_channel = data['NOMChannel02'][:] 
# blue_channel = data['NOMChannel03'][:] 
# # 标定超过3000的值为0
# red_channel[red_channel > 3000] = 0
# green_channel[green_channel > 3000] = 0
# blue_channel[blue_channel > 3000] = 0
# 创建一个RGB图像数组
# rgb_image = np.stack([red_channel, green_channel, blue_channel], axis=-1)

# # 归一化到0-1范围
# rgb_image = (rgb_image - rgb_image.min()) / (rgb_image.max() - rgb_image.min())

# # 绘制RGB彩色增强图像
# fig, ax = plt.subplots()
# cax = ax.imshow(rgb_image)
# ax.set_title('True Color Composite Image (0.47um, 0.65um, 0.83um)')
# ax.set_xlabel('X Axis')
# ax.set_ylabel('Y Axis')
# ax.axis('off')  # 关闭坐标轴显示

# # 增加 color bar 在图片下面
# cbar = fig.colorbar(cax, ax=ax, orientation='horizontal', pad=0.05)
# cbar.set_label('Intensity')

# # 保存图像到与脚本同目录下，文件名为 TrueColor_composite.png
# plt.savefig(os.path.join(os.path.dirname(__file__), "TrueColor_composite.png"), dpi=1080, facecolor='white', bbox_inches='tight')
# plt.show()
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QTableWidgetItem,
)
from PySide6 import QtCharts, QtWidgets, QtGui
from PySide6.QtCore import QTimer, QDateTime, QEvent, Qt, QObject
from PySide6.QtGui import QFont
from 天气预报_UI_real import Ui_Form
from Fig_rc import *
import pandas as pd
from request import (
    get_city_id, read_now, read_past, read_forecast, get_image,
    readfigtempture, create_rgb_image, get_city_name,create_BW_image,create_TD_image
)
import os
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
# from SAT import generate_sat
# from radar import generate_radar
# 设置中文字体
font = FontProperties(fname=r'C:\Windows\Fonts\simhei.ttf', size=12)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置全局中文字体为黑体或其他支持的字体
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


        self.ui.textEditNowTime1.setReadOnly(True)
        self.ui.textEditNowTime2.setReadOnly(True)
        self.ui.textEditNowTime3.setReadOnly(True)
        self.ui.textEditNowTime4.setReadOnly(True)
        self.ui.textEditNowTime5.setReadOnly(True)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(60000)  # 60000 milliseconds = 1 minute
        self.update_time()
        self.ui.Filedirectorycity1.returnPressed.connect(self.NOW)
        self.ui.Filedirectorycity2.returnPressed.connect(self.Forecast)
        self.ui.Filedirectorycity3.returnPressed.connect(self.PlotAndDisplayWeatherData)
        self.ui.Filedirectorysattime.returnPressed.connect(self.FY)
        self.ui.Filedirectorysatfile.returnPressed.connect(self.FY4A)
        self.ui.Filedirectorysatfiletongdao.returnPressed.connect(self.FY_DTD)

        self.ui.Filedirectorysatfilesat2.returnPressed.connect(self.SAT)
        self.ui.Filedirectorysatfile_ld1.returnPressed.connect(self.RADAR)

        self.ui.SaveBtnforecast.clicked.connect(self.save_forecast)
        self.ui.SaveBtnpast.clicked.connect(self.save_past)
        self.ui.SaveBtnnow.clicked.connect(self.save_now)
        self.ui.pushButtonsathis.clicked.connect(self.FY)
        self.ui.pushButton_tongdao1.clicked.connect(self.FY_BW)

    def SAT(self):
        # sat = self.ui.Filedirectorysatfile_ld2.text()
        # light = self.ui.Filedirectorysatfile_ld1.text()
        # generate_sat(sat, light)
        self.DisplaySAT()

    def DisplaySAT(self):
        image_path = 'sat.gif'
        # 加载GIF并在 labelsatlite QLabel 中显示
        self.ui.labelsatlight.clear()
        if os.path.exists(image_path):
            self.movie_sat = QtGui.QMovie(image_path)
            # 假设 labelsatlite 是用于显示图像的 QLabel
            self.ui.labelsatlight.setMovie(self.movie_sat)
            self.ui.labelsatlight.setScaledContents(True)  # 自适应
            self.movie_sat.start()

    def RADAR(self):
        # radar = self.ui.Filedirectorysatfilesat1.text()
        # light = self.ui.Filedirectorysatfilesat2.text()
        # generate_sat(radar, light)
        self.DisplayRADAR()

    def DisplayRADAR(self):
        image_path = 'radar.gif'
        # 加载GIF并在 labelsatlite QLabel 中显示
        self.ui.labelradar.clear()
        if os.path.exists(image_path):
            self.movie_radar = QtGui.QMovie(image_path)
            # 假设 labelradar 是用于显示图像的 QLabel
            self.ui.labelradar.setMovie(self.movie_radar)
            self.ui.labelradar.setScaledContents(True)  # 自适应
            self.movie_radar.start()

    def PlotAndDisplayWeatherData(self):
        long = float(self.ui.Filedirectorylong.text())
        lat = float(self.ui.Filedirectorylat.text())
        starttime = self.ui.Filedirectorysattime.text()
        endtime = self.ui.Filedirectoryendtime.text()
        data = read_past(lat, long, starttime, endtime)
        df_data = data[0]

        # 提取数据列
        temperature = df_data['气温(℃)']
        dew_point = df_data['露点温度(℃)']
        relative_humidity = df_data['相对湿度(%)']
        precipitation = df_data['降水量(mm)']
        snow_depth = df_data['积雪深度(cm)']
        wind_direction = df_data['风向(度数，0-360)']
        avg_wind_speed = df_data['平均风速(km/h)']
        pressure = df_data['气压(hpa)']
        time_int = df_data['时间']



        # 绘制数据图
        plt.figure(figsize=(12, 8))  # 调整图像大小

        # 绘制气温与露点温度变化图
        plt.subplot(2, 3, 1)
        plt.plot(time_int, temperature, 'r-', label='气温(℃)')
        plt.plot(time_int, dew_point, 'b-', label='露点温度(℃)')
        plt.xlabel('时间')
        plt.ylabel('温度(℃)')
        plt.xticks([time_int.iloc[0], time_int.iloc[-1]])
        plt.legend()
        plt.title('气温与露点温度变化图')


        # 绘制相对湿度变化图
        plt.subplot(2, 3, 2)
        plt.plot(time_int, relative_humidity, 'g-', label='相对湿度(%)')
        plt.xlabel('时间')
        plt.ylabel('相对湿度(%)')
        plt.xticks([time_int.iloc[0], time_int.iloc[-1]])
        plt.legend()
        plt.title('相对湿度变化图')


        # 绘制降水量与积雪深度变化图
        plt.subplot(2, 3, 3)
        plt.plot(time_int, precipitation, 'c-', label='降水量(mm)')
        plt.plot(time_int, snow_depth, 'm-', label='积雪深度(cm)')
        plt.xlabel('时间')
        plt.ylabel('量(mm/cm)')
        plt.xticks([time_int.iloc[0], time_int.iloc[-1]])
        plt.legend()
        plt.title('降水量与积雪深度变化图')


        # 绘制风向变化图
        plt.subplot(2, 3, 4)
        plt.plot(time_int, wind_direction, 'y-', label='风向(度数，0-360)')
        plt.xlabel('时间')
        plt.ylabel('风向(度数)')
        plt.xticks([time_int.iloc[0], time_int.iloc[-1]])
        plt.legend()
        plt.title('风向变化图')

        plt.subplot(2, 3, 5)
        plt.plot(time_int, avg_wind_speed, 'k-', label='平均风速(km/h)')
        plt.xlabel('时间')
        plt.ylabel('平均风速(km/h)')
        plt.xticks([time_int.iloc[0], time_int.iloc[-1]])
        plt.legend()
        plt.title('平均风速变化图')


        # 绘制气压变化图
        plt.subplot(2, 3, 6)
        plt.plot(time_int, pressure, 'p-', label='气压(hpa)')
        plt.xlabel('时间')
        plt.ylabel('地面大气压(hpa)')
        plt.xticks([time_int.iloc[0], time_int.iloc[-1]])
        plt.legend()
        plt.title('气压变化图')

        # 保存合并后的图像
        plt.savefig('气象变化图.png')
        self.DisplayPlotsInLabels()

    def DisplayPlotsInLabels(self):
        image_path = f"气象变化图.png"
        # 加载图像并在 labelsatlite QLabel 中显示
        self.ui.labelfig.clear()
        self.pix = QtGui.QPixmap(image_path)

        if not self.pix.isNull():
            # 假设 labelsatlite 是用于显示图像的 QLabel
            self.ui.labelfig.setPixmap(self.pix)
            self.ui.labelfig.setScaledContents(True)  # 自适应

    def FY_DTD(self):
        file=self.ui.Filedirectorysatfile.text()
        TD=self.ui.Filedirectorysatfiletongdao.text()
        create_TD_image(file,TD)
        current_time = datetime.now().strftime("%Y%m%d%H%M")
        image_path = f"time{current_time}.png"
        # 加载图像并在 labelsatlite QLabel 中显示
        self.ui.labelsatlite.clear()
        self.pix = QtGui.QPixmap(image_path)

        if not self.pix.isNull():
            # 假设 labelsatlite 是用于显示图像的 QLabel
            self.ui.labelsatlite.setPixmap(self.pix)
            self.ui.labelsatlite.setScaledContents(True)  # 自适应

    def FY_BW(self):
        file=self.ui.Filedirectorysatfile.text()
        TD = self.ui.Filedirectorysatfiletongdao.text()
        create_BW_image(file,TD)
        current_time = datetime.now().strftime("%Y%m%d%H%M")
        image_path = f"time{current_time}.png"
        # 加载图像并在 labelsatlite QLabel 中显示
        self.ui.labelsatlite.clear()
        self.pix = QtGui.QPixmap(image_path)

        if not self.pix.isNull():
            # 假设 labelsatlite 是用于显示图像的 QLabel
            self.ui.labelsatlite.setPixmap(self.pix)
            self.ui.labelsatlite.setScaledContents(True)  # 自适应


    def FY4A(self):
        file=self.ui.Filedirectorysatfile.text()
        create_rgb_image(file)
        current_time = datetime.now().strftime("%Y%m%d%H%M")
        image_path = f"time{current_time}.png"
        # 加载图像并在 labelsatlite QLabel 中显示
        self.ui.labelsatlite.clear()
        self.pix = QtGui.QPixmap(image_path)

        if not self.pix.isNull():
            # 假设 labelsatlite 是用于显示图像的 QLabel
            self.ui.labelsatlite.setPixmap(self.pix)
            self.ui.labelsatlite.setScaledContents(True)  # 自适应


    def FY(self):
        # 获取时间字符串
        time_sat = self.ui.Filedirectorysattime.text()
        print(f'获取到的时间字符串: {time_sat}')  # 调试输出时间字符串
        # 调用获取卫星图像的函数
        get_image(time_sat)  # 获取卫星图
        image_path = f'FY4B True Color Image_{time_sat}.jpg'
        # 加载图像并在 labelsatlite QLabel 中显示
        self.ui.labelsatlite.clear()
        self.pix = QtGui.QPixmap(image_path)

        if not self.pix.isNull():
            # 假设 labelsatlite 是用于显示图像的 QLabel
            self.ui.labelsatlite.setPixmap(self.pix)
            self.ui.labelsatlite.setScaledContents(True)  # 自适应


    def Forecast(self):
        text = self.ui.Filedirectorycity2.text()
        forecastdata = read_forecast(text)
        self.ShowInTableViewForecast(forecastdata)

        dates = forecastdata['日期']
        max_temp = forecastdata['最高温度']
        min_temp = forecastdata['最低温度']

        # Plotting the data
        plt.figure(figsize=(8, 6))
        plt.plot(dates, max_temp, 'r-', label='最高温度', linewidth=2.5)  # Thicker line
        plt.plot(dates, min_temp, 'b-', label='最低温度', linewidth=2.5)  # Thicker line
        plt.xlabel('日期', fontsize=14)  # Larger font for axis labels
        plt.ylabel('温度', fontsize=14)  # Larger font for axis labels
        plt.legend(fontsize=12)  # Larger font for legend
        plt.title('温度变化图', fontsize=16)  # Larger font for title

        for i in range(len(dates)):
            plt.text(dates[i], max_temp[i], f"{max_temp[i]}°C", ha='center', va='bottom', fontsize=16, color='red')
            plt.text(dates[i], min_temp[i], f"{min_temp[i]}°C", ha='center', va='top', fontsize=16, color='blue')

        # Save the plot image
        plot_image_path = 'plot_image.png'
        plt.savefig(plot_image_path)

        # Display the plot image in QLabel
        self.ui.labelforecast.clear()
        self.pix = QtGui.QPixmap(plot_image_path)

        if not self.pix.isNull():
            self.ui.labelforecast.setPixmap(self.pix)
            self.ui.labelforecast.setScaledContents(True)  # 自适应
        else:
            print("加载图像失败，请检查图像路径和文件是否存在。")

    def ShowInTableViewForecast(self, data):
        num_rows = len(data.index)
        num_columns = len(data.columns)
        self.ui.tableWidgetforecast.setRowCount(num_rows)
        self.ui.tableWidgetforecast.setColumnCount(num_columns)
        self.ui.tableWidgetforecast.setHorizontalHeaderLabels(data.columns)
        for i in range(num_rows):
            for j in range(num_columns):
                item = QTableWidgetItem(str(data.iloc[i, j]))
                self.ui.tableWidgetforecast.setItem(i, j, item)

        self.ui.tableWidgetforecast.resizeColumnsToContents()
        self.ui.tableWidgetforecast.resizeRowsToContents()
        self.ui.tableWidgetforecast.resize(1000,1000)

    def save_past(self):
        long = float(self.ui.Filedirectorylong.text())
        lat = float(self.ui.Filedirectorylat.text())
        starttime = self.ui.Filedirectorysattime.text()
        endtime = self.ui.Filedirectoryendtime.text()
        data = read_past(lat, long, starttime, endtime)
        table_data = data[0]
        df = pd.DataFrame(table_data)
        filename, _ = QFileDialog.getSaveFileName(None, 'Save File', '', 'Excel Files (*.xlsx)')
        if filename:
            df.to_excel(filename, index=False)
    def save_forecast(self):
        text = self.ui.Filedirectorycity2.text()
        forecastdata = read_forecast(text)
        table_data=forecastdata
        df = pd.DataFrame(table_data)
        filename, _ = QFileDialog.getSaveFileName(None, 'Save File', '', 'Excel Files (*.xlsx)')
        if filename:
            df.to_excel(filename, index=False)

    def NOW(self):
        text = self.ui.Filedirectorycity1.text()
        nowdata = read_now(text)
        font = QFont("Microsoft YaHei", 16)
        font.setBold(True)
        self.ui.textEdittemper.setFont(font)
        self.ui.textEditprcp.setFont(font)
        self.ui.textEditpresure.setFont(font)
        self.ui.textEditrh.setFont(font)
        self.ui.textEditwinddir.setFont(font)
        self.ui.textEditwinddirdegree.setFont(font)
        self.ui.textEditwindspeed.setFont(font)
        self.ui.textEditwindsca.setFont(font)
        self.ui.textEdittimeupdate.setFont(font)

        self.ui.textEdittemper.setText(str(nowdata["Temperature"])+'℃')
        self.ui.textEditprcp.setText(str(nowdata["Precipitation"])+'mm')
        self.ui.textEditpresure.setText(str(nowdata["Pressure"])+'hpa')
        self.ui.textEditrh.setText(str(nowdata["Humidity"])+'%')
        self.ui.textEditwinddir.setText(str(nowdata["Wind Direction"]))
        self.ui.textEditwinddirdegree.setText(str(nowdata["Wind Direction Degree"])+'°')
        self.ui.textEditwindspeed.setText(str(nowdata["Wind Speed"])+'m/s')
        self.ui.textEditwindsca.setText(str(nowdata["Wind Scale"]))
        self.ui.textEdittimeupdate.setText(str(nowdata["Last Update"]))

    def save_now(self):
        text = self.ui.Filedirectorycity1.text()
        nowdata = read_now(text)

        # Convert nowdata to a DataFrame with keys as index
        df = pd.DataFrame(list(nowdata.items()), columns=['Key', 'Value'])
        df.set_index('Key', inplace=True)

        filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Excel Files (*.xlsx)')
        if filename:
            df.to_excel(filename)


    def update_time(self):
        now = QDateTime.currentDateTime()
        formatted_time = now.toString('yyyy年M月d日 hh：mm')
        self.ui.textEditNowTime1.setPlainText(f'当前时间：{formatted_time}')
        self.ui.textEditNowTime2.setPlainText(f'当前时间：{formatted_time}')
        self.ui.textEditNowTime3.setPlainText(f'当前时间：{formatted_time}')
        self.ui.textEditNowTime4.setPlainText(f'当前时间：{formatted_time}')
        self.ui.textEditNowTime5.setPlainText(f'当前时间：{formatted_time}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

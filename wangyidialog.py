#  下载歌曲相关的库
import os
import sys
from urllib.request import urlretrieve
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from wangyi import *
# mac系统需要ssl权限
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# 歌曲保存路径
def music_savepath(pathedit,songname):
    savepath = pathedit.text()+'/{}.mp3'.format(songname)
    return savepath


# 提示信息
def log(songlist, tip, song_name):
    songlist.addItem(tip.format(song_name))


# 歌曲下载
def song_load(item):
    song_id = item['song_id']
    song_name = item['song_name']
    song_url = 'https://music.163.com/song/media/outer/url?id={}.mp3'.format(song_id)
    path = music_savepath(main.pathedit,song_name)
    log(main.songlist, '歌曲：{},正在下载...', song_name)
    urlretrieve(song_url, path)
    log(main.songlist, '下载完毕：{},请试听...', song_name)


# 调用浏览器
def webtest():
    # 设置火狐为无界面浏览器
    options = Options()
    options.add_argument('--headless')
    # 调用火狐浏览器
    driver = webdriver.Firefox(options=options)
    return driver


# 选择歌曲
def get_music_name(songedit):
    url = 'https://music.163.com/#/search/m/?s={}&type=1'.format(songedit)
    driver = webtest()
    driver.get(url=url)
    driver.switch_to.frame('g_iframe')

    # 获取歌曲id
    req = driver.find_element_by_id('m-search')
    a_id = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//a').get_attribute('href')
    song_id = a_id.split('=')[-1]
    # 获取歌曲名
    song_name = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//b').get_attribute('title')

    item = {'song_id': song_id, 'song_name': song_name}

    # 调用下载函数
    song_load(item)
    # 退出火狐浏览器
    driver.close()


# 使用PyQt5 Designer PyUic生成的Ui_MainWindow类,自定义类
class MyMainDialog(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainDialog, self).__init__()
        self.setupUi(self)

        # 如需使窗口透明，所在类初始化函数中设置如下属性
        # self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 窗口无边框化，所在类初始化函数中设置如下属性
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 开始下载事件绑定
        self.btnstart.clicked.connect(self.btnstartClick)
        # 退出程序事件绑定
        self.btnexit.clicked.connect(self.btnexitClick)
        # 保存路径事件绑定
        self.btnsave.clicked.connect(self.btnsaveClick)
    # 开始下载歌曲函数
    def btnstartClick(self):
        get_music_name(self.songedit.text())

    # 保存路径函数
    def btnsaveClick(self):
        dir_path=QFileDialog.getExistingDirectory(self, "choose directory", "/Users/wulongxiang/PycharmProjects/wangyi")
        self.pathedit.setText(dir_path)

    def btnexitClick(self):
        self.close()

    # 定义鼠标点击事件
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            if event.button() == QtCore.Qt.LeftButton:
                self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
        event.accept()

    # 定义鼠标移动事件
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    # 窗体重绘事件
    def resizeEvent(self, event):
        palette = QPalette()
        pix = QPixmap('/Users/wulongxiang/PycharmProjects/MyDialogCall/background.jpg')
        pix = pix.scaled(self.width(), self.height())
        palette.setBrush(QPalette.Background, QBrush(pix))
        self.setPalette(palette)

    #  设置键盘退出快捷键
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyMainDialog()
    main.show()
    sys.exit(app.exec_())

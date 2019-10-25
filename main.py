import sys, math

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import window


class MyWindow(QMainWindow, window.Ui_QMainWindow):   # msg.msg
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)    # 找到子类（MyWindow）的父类（QMainWindow），
                                            # 然后把MyWindow的对象self转成QMainWindow的对象，然后被转化的self调用自己的init函数
        self.setupUi(self)  # 直接继承界面类，调用类的setupUi方法
        self.center()
        self.checkBox.stateChanged.connect(self.btnstate)   # 连接槽函数
        self.checkBox_2.toggled.connect(self.btnstate)
        self.checkBox_3.toggled.connect(self.btnstate)
        self.comboBox.currentIndexChanged.connect(self.selectionchange)
        self.spinBox.valueChanged.connect(self.spinBoxshow)
        self.doubleSpinBox.valueChanged.connect(self.doubleSpinBoxshow)
        self.horizontalSlider.valueChanged.connect(self.sliderchanged)
        self.showdialog.clicked.connect(self.dialogshow)
        self.QMessageBox.clicked.connect(self.msg)
        # self.QMessageBox.pressed.connect(self.close)
        # QInputDialog
        self.getItem.clicked.connect(self.getitem)
        self.getText.clicked.connect(self.gettext)
        self.getInt.clicked.connect(self.getint)
        self.fonButton.clicked.connect(self.getFont)
        # QFileDialog
        self.loadImage.clicked.connect(self.getimage)
        self.loadText.clicked.connect(self.loadtext)




    def paintEvent(self,event):
        # 初始化绘图工具
        painter = QPainter()
        # 开始在窗口绘制
        painter.begin(self)
        #自定义绘制方法
        self.drawText(event,painter)
        # 结束在窗口的绘制
        painter.end()
    def drawText(self,event,qp):
        #设置画笔的颜色
        qp.setPen(QColor(168, 34, 3))
        #设置字体
        qp.setFont(QFont('SimSun', 20))
        #绘制文字
        qp.drawText(event.rect(),Qt.AlignCenter, '欢迎学习 PyQt5')
    def paintEvent(self, event):
        # 初始化绘图工具
        qp = QPainter()
        # 开始在窗口绘制
        qp.begin(self)
        # 自定义画点方法
        self.drawPoints(qp)
        # 结束在窗口的绘制
        qp.end()
    def drawPoints(self, qp):
        qp.setPen(Qt.red)
        size = self.size()
        for i in range(1000):
            # 绘制正弦函数图像，它的周期是（-100,100）
            x = 100 * (-1 + 2.0 * i / 1000) + size.width() / 2.0
            y = -50 * math.sin((x - size.width() / 2.0) * math.pi / 50) + size.height() / 2.0
            qp.drawPoint(x, y)


    def getimage(self):
        # 从C盘打开文件格式（*.jpg *.gif *.png *.jpeg）文件，返回路径
        # 第一个参数self：用于指定父组件
        # 第二个参数‘open file’：是QFileDialog对话框的标题
        # 第三个参数‘C:\’默认打开的目录，‘.’代表程序运行的目录，‘ / ’代表当前盘下的根目录(window.linux系统), 需要注意的是不同路径的显示方式，比如window平台下的C盘“C:\”等
        # 第四个参数是对话框中文件扩展名过滤器（fliter）, 比如使用’Image files(.jpg.gif.png.jpeg)’表示只能显示扩展名为.jpg,.gif等文件
        image_file, _ = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\', 'Image files (*.jpg *.gif *.png *.jpeg)')
        # 设置标签的图片
        self.Imageshow.setPixmap(QPixmap(image_file))
    def loadtext(self):
        # 实例化QFileDialog
        dig = QFileDialog()
        # 设置可以打开任何文件
        dig.setFileMode(QFileDialog.AnyFile)
        # 文件过滤
        dig.setFilter(QDir.Files)
        if dig.exec_():
            # 接受选中文件的路径，默认为列表
            filenames = dig.selectedFiles()
            # 列表中的第一个元素即是文件路径，以只读的方式打开文件
            f = open(filenames[0], 'r')
            with f:
                # 接受读取的内容，并显示到多行文本框中
                data = f.read()
                self.textEdit.setText(data)


    def getFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.FontTest.setFont(font)


    def getitem(self):
        # 创建元组并定义初始值
        items = ('C', 'C++', 'C#', 'Java', 'Python')
        # 获取item输入的值，以及ok键的点击与否（True 或False）
        # QInputDialog.getItem(self,标题,文本,元组,元组默认index,是否允许更改)
        item, ok = QInputDialog.getItem(self, "select input dialog", '语言列表', items, 0, False)
        if ok and item:
            # 满足条件时，设置单行文本框的文本
            self.lineEdit_getItem.setText(item)
    def gettext(self):
        text, ok = QInputDialog.getText(self, 'Text Input Dialog', '输入姓名：')
        if ok:
            self.lineEdit_getText.setText(str(text))
    def getint(self):
        num, ok = QInputDialog.getInt(self, 'Integer input dualog', '输入数字')
        if ok:
            self.lineEdit_getInt.setText(str(num))


    def msg(self):  # 基本控件_13_QMessageBox
        # information(QWdiget parent,title,text,buttons,defaultButton)
        # 弹出消息对话框
        # parent：指定的父窗口控件
        # title：对话框标题
        # text：对话框文本
        # buttons：多个标准按钮，默认为ok按钮
        # defaultButton：默认选中的标准按钮，默认选中第一个标准按钮
        reply = QMessageBox.information(self, 'title', 'information', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        # question（QWidget parent,title,text,buttons,defaultButton)
        # 弹出问答对话框
        reply1 = QMessageBox.question(self, "title1", "question", QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)

        # warning（QWidget parent,title,text,buttons,defaultButton）
        # 弹出警告对话框
        reply2 = QMessageBox.warning(self, "title2", "warning", QMessageBox.Retry | QMessageBox.Abort, QMessageBox.Retry)
        # 根据不同按钮做出不同的反应
        while reply2 == QMessageBox.Retry:
            reply2 = QMessageBox.warning(self, "title2", "warning", QMessageBox.Retry | QMessageBox.Abort,
                                         QMessageBox.Retry)
            if reply2 == QMessageBox.Abort:
                break

        # critical（QWidget parent,title,text,buttons,defaultButton）
        # 弹出严重错误对话框
        reply3 = QMessageBox.critical(self, "title3", "critical", QMessageBox.Yes | QMessageBox.Ignore, QMessageBox.Yes)

        # about（QWidget parent,title,text）
        # 弹出关于对话框
        reply4 = QMessageBox.about(self, "title4", "about")


    def dialogshow(self):
        # 创建QDialog对象
        dialog = QDialog()
        # 创建按钮到新创建的dialog对象中
        btn = QPushButton('ok', dialog)
        # 移动按钮，设置dialog的标题
        btn.move(50, 50)
        dialog.setWindowTitle("Dialog")
        # 设置窗口的属性为ApplicationModal模态，用户只有关闭弹窗后，才能关闭主界面
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()


    def sliderchanged(self):
        print('current slider value=%s' % self.horizontalSlider.value())
        size = self.horizontalSlider.value()
        self.QMessageBox.setFont(QFont('Arial', size/50))


    def spinBoxshow(self):
        self.Normal.setText('current value:' + str(self.spinBox.value()))
    def doubleSpinBoxshow(self):
        self.Normal.setText('current value:' + str(self.doubleSpinBox.value()))


    def selectionchange(self, i):
        print('Items in the list are:')
        # 输出选项集合中每个选项的索引与对应的内容
        for count in range(self.comboBox.count()):
            print('Item' + str(count) + '=' + self.comboBox.itemText(count))
        # count()：返回选项集合中的数目
        print('current index', i, 'selection changed', self.comboBox.currentText())


    def btnstate(self):
        chk1Status = self.checkBox.text() + ", isChecked=" + str(
            self.checkBox.isChecked()) + ', chekState=' + str(
            self.checkBox.checkState()) + "\n"
        chk2Status = self.checkBox_2.text() + ", isChecked=" + str(
            self.checkBox_2.isChecked()) + ', checkState=' + str(
            self.checkBox_2.checkState()) + "\n"
        chk3Status = self.checkBox_3.text() + ", isChecked=" + str(
            self.checkBox_3.isChecked()) + ', checkState=' + str(
            self.checkBox_3.checkState()) + "\n"
        print(chk1Status + chk2Status + chk3Status)


    # 窗口居中显示
    def center(self):
        # 获取屏幕的大小
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口的大小
        size = self.geometry()
        # 将窗口移动到屏幕中央
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


    # 关闭窗口
    def close(self):
        # sender是发送信号的对象，这里获得的是按钮的名称
        sender = self.sender()
        # 以文本的行书输出按钮的名称
        print(sender.text() + ' 被按下了')
        # 获取QApplication类的对象
        qApp = QApplication.instance()
        # 退出
        qApp.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)    # pyqt窗口必须在QApplication方法中使用
    myshow = MyWindow()    # 生成MyWindow类的实例myshow
    myshow.show()   # myshow调用show方法
    sys.exit(app.exec_())   # 消息结束的时候，结束进程，并返回0，接着调用sys.exit(0)退出程序

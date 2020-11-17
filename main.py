
# AO Background Automator by Yuzuru #

from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageDraw
from pathlib import Path
import webbrowser
import shutil
import os


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(456, 374)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 290, 391, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 311, 20))
        self.lineEdit.setAcceptDrops(False)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setText(f"{os.getcwd()} \\background")
        self.lineEdit.setObjectName("lineEdit")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 20, 75, 23))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 60, 311, 171))
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setAutoFillBackground(True)
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setStyleSheet("background-color: lightgray")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/placeholder.png").scaled(311, 171, QtCore.Qt.KeepAspectRatio))

        self.label.setWordWrap(False)
        self.label.setIndent(-3)
        self.label.setObjectName("label")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 260, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setEnabled(False)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 130, 21, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setHidden(True)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(390, 130, 20, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setHidden(True)
        

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(190, 240, 70, 17))
        self.checkBox.setObjectName("checkBox")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 456, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuFile_2 = QtWidgets.QMenu(self.menubar)
        self.menuFile_2.setObjectName("menuFile_2")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.actionGuide = QtWidgets.QAction(MainWindow)
        self.actionGuide.setObjectName("actionGuide")
        self.actionCredits = QtWidgets.QAction(MainWindow)
        self.actionCredits.setObjectName("actionCredits")
        self.actionChange_Output_Directory = QtWidgets.QAction(MainWindow)
        self.actionChange_Output_Directory.setObjectName("actionChange_Output_Directory")
        self.menuFile.addAction(self.actionGuide)
        self.menuFile.addAction(self.actionCredits)
        self.menuFile_2.addAction(self.actionChange_Output_Directory)
        self.menubar.addAction(self.menuFile_2.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())


        self.pushButton.clicked.connect(lambda: self.saveDirectoryCheck(True))
        self.actionChange_Output_Directory.triggered.connect(self.loadFiles)
        self.actionCredits.triggered.connect(self.actionCredits_)
        self.actionGuide.triggered.connect(self.actionGuide_)
        self.pushButton_2.clicked.connect(lambda: self.executeButton(file_save, looping_bool, first_input, bool_))
        self.pushButton_3.clicked.connect(lambda: self.loopLeft())
        self.pushButton_4.clicked.connect(lambda: self.loopRight())

        self.checkBox.stateChanged.connect(self.transparentDesksCheck)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Task completed!")
        msg.setText("Your backgrounds are ready!")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def actionGuide_(self):
        url = "https://docs.google.com/document/d/17Z8GvJarlIpGeE7jriNIdF2APJns7GnPBY5dqWd9vUI/edit?usp=sharing"
        webbrowser.open(url)

    def actionCredits_(self):
        msg2 = QMessageBox()
        msg2.setWindowTitle("Credits")
        msg2.setText("Program written by Yuzuru. Contact them via Discord or Github to report an issue.")
        msg2.setIcon(QMessageBox.Information)
        msg2.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AO Background Automator"))
        self.pushButton.setToolTip(_translate("MainWindow", "Changes your output location"))
        self.pushButton.setText(_translate("MainWindow", "Output"))
        self.pushButton_2.setToolTip(_translate("MainWindow", "Executes the program"))
        self.pushButton_2.setText(_translate("MainWindow", "Execute"))
        self.checkBox.setToolTip(_translate("MainWindow", "Includes Transparent Desks (TD) / transparent foregrounds"))
        self.checkBox.setText(_translate("MainWindow", "Include TD"))

        self.actionGuide.setText(_translate("MainWindow", "Guide"))
        self.actionCredits.setText(_translate("MainWindow", "Credits"))
        self.actionChange_Output_Directory.setText(_translate("MainWindow", "Open Files"))

        self.pushButton_3.setText(_translate("MainWindow", "<"))
        self.pushButton_4.setText(_translate("MainWindow", ">"))
        self.menuFile.setTitle(_translate("MainWindow", "Help"))
        self.menuFile_2.setTitle(_translate("MainWindow", "File"))

    def loadFiles(self):
        global first_input
        global looping_bool

        names = QFileDialog.getOpenFileNames(self, "Open Files", "C\\Desktop", "Images(*.png *.pns);;Animated Images(*.GIF *.apng *.webp")

        try:
            if bool_ is False:
                pass

        except NameError:
            bool_ = False

        for x in names:
            first_input = x
            break

        if isinstance(first_input, list) is True:
            looping_bool = True

        elif isinstance(first_input, list) is False:
            looping_bool = False

        try:
            self.loopCheck(first_input, looping_bool)
        except:
            pass


    def transparentDesksCheck(self):
        if self.checkBox.isChecked():
            TD_Check = True        
        
        else:
            TD_Check = False

        return TD_Check


    def transparentDesks(self, location_dir, TD_Check=False):

        if TD_Check is False:
            pass

        if TD_Check is True:

            img = Image.new('RGBA', (30, 17), (255, 255, 255, 0))

            draw = ImageDraw.Draw(img)
            draw.ellipse((25, 25, 75, 75), fill=(0, 0, 0, 0))

            transparent_desks = ["defensedesk", "judgedesk", "helperdesk", "prohelperdesk", "stand", "prosecutiondesk"]

            for x in transparent_desks:
                img.save(location_dir + "/" + x + ".png", 'PNG')


    def saveDirectoryCheck(self, perm_):
        global bool_
        bool_ = perm_

        if perm_ is True:
            self.saveDirectory()
            

        elif perm_ is False:
            pass

    
    def saveDirectory(self):
        global file_save
        global file__save
        
        file_save = QFileDialog.getExistingDirectory(self, "Select a folder", "C\\Desktop", QFileDialog.ShowDirsOnly)

        if file_save:
            self.lineEdit.setText(f"{file_save}")
        
        file__save = file_save
        

    def loopRight(self):
        self.loopNumber("right")


    def loopNumber(self, direction):
        global number_

        if direction == "right":
            number_ += 1

            try:
                self.label.setPixmap(QtGui.QPixmap(first_input[number_]).scaled(311, 171, QtCore.Qt.KeepAspectRatio))

            except IndexError:
                number_ = 0
                self.label.setPixmap(QtGui.QPixmap(first_input[number_]).scaled(311, 171, QtCore.Qt.KeepAspectRatio))

        elif direction == "left":
            number_ -= 1

            try:
                self.label.setPixmap(QtGui.QPixmap(first_input[number_]).scaled(311, 171, QtCore.Qt.KeepAspectRatio))

            except IndexError:
                number_ = 0
                self.label.setPixmap(QtGui.QPixmap(first_input[number_]).scaled(311, 171, QtCore.Qt.KeepAspectRatio))


    def loopLeft(self):
        self.loopNumber("left")


    def loopCheck(self, first_input, looping):
        global looping__
        looping__ = looping

        if looping is True:
            self.label.setPixmap(QtGui.QPixmap(first_input[0]).scaled(311, 171, QtCore.Qt.KeepAspectRatio))
            more_than_one = True
            self.pushButton_3.setHidden(False)
            self.pushButton_4.setHidden(False)

        elif looping is False:
            self.label.setPixmap(QtGui.QPixmap(first_input).scaled(311, 171, QtCore.Qt.KeepAspectRatio))
            more_than_one = False
            self.pushButton_3.setHidden(True)
            self.pushButton_4.setHidden(True)
            
        self.pushButton_2.setEnabled(True)
      

    def executeButton(self, file_save, more_than_one, first_input, bool_):

        progressbar_value = 0
        self.progressBar.setProperty("value", progressbar_value)

        pos = ["defenseempty", "helperstand", "judgestand", "prohelperstand", "prosecutorempty", "witnessempty"]

        if bool_ is False:

            if file_save is False:
                file_save = os.getcwd()
                file_save = file_save + "\\background"

        elif bool_ is True:

            if file_save is False:
                file_save = file__save

        try:
            os.mkdir(file_save)

        except:
            pass

        if more_than_one is True:
            for xy in first_input:
                base_name = Path(xy).name
                base_name, extension_name = os.path.splitext(base_name)
                created_directory = str(file_save) + "/" + base_name

                try:
                    os.mkdir(created_directory)
                except: 
                    pass

                if progressbar_value <= 80:
                    progressbar_value += 2
                    self.progressBar.setProperty("value", progressbar_value)

                for yz in pos:
                    if progressbar_value <= 80:
                        progressbar_value += 2
                        self.progressBar.setProperty("value", progressbar_value)

                    shutil.copy(f"{xy}", f"{created_directory}/{yz}{extension_name}" )

                    self.transparentDesks(created_directory, self.transparentDesksCheck())

        elif more_than_one is False:
            base_name = Path(first_input).name
            base_name, extension_name = os.path.splitext(base_name)
            created_directory = file_save + "/" + base_name

            try:
                os.mkdir(created_directory)
            except: 
                pass

            if progressbar_value <= 80:
                progressbar_value += 2
                self.progressBar.setProperty("value", progressbar_value)

            for xz in pose:
                if progressbar_value <= 80:
                    progressbar_value += 2
                    self.progressBar.setProperty("value", progressbar_value)

                shutil.copy(f"{xy}", f"{created_directory}/{yz}{extension_name}" )
                self.transparentDesks(created_directory, TD_Check)

        progressbar_value = 100
        self.progressBar.setProperty("value", progressbar_value)
        self.show_popup()


if __name__ == "__main__":
    import sys

    number_ = 0
    file_save = False
    bool_ = False


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

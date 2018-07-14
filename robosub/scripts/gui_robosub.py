# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from modules.controller.gui_controller import Controller
import subprocess
import time
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.Controller = Controller()  # Initialize gui controller

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1432, 850)
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_layout = QtWidgets.QVBoxLayout()
        self.left_layout.setObjectName("left_layout")
        self.displays = QtWidgets.QHBoxLayout()
        self.displays.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.displays.setObjectName("displays")
        self.display0 = QtWidgets.QGraphicsView(self.central_widget)
        self.display0.setSizeIncrement(QtCore.QSize(0, 0))
        self.display0.setBaseSize(QtCore.QSize(0, 0))
        self.display0.setObjectName("display0")
        self.displays.addWidget(self.display0)
        self.display1 = QtWidgets.QGraphicsView(self.central_widget)
        self.display1.setSizeIncrement(QtCore.QSize(0, 0))
        self.display1.setBaseSize(QtCore.QSize(0, 0))
        self.display1.setObjectName("display1")
        self.displays.addWidget(self.display1)
        self.left_layout.addLayout(self.displays)
        self.cameras = QtWidgets.QHBoxLayout()
        self.cameras.setObjectName("cameras")
        self.camera0 = QtWidgets.QPushButton(self.central_widget)
        self.camera0.setObjectName("camera0")
        self.cameras.addWidget(self.camera0)
        self.camera1 = QtWidgets.QPushButton(self.central_widget)
        self.camera1.setObjectName("camera1")
        self.cameras.addWidget(self.camera1)
        self.camera2 = QtWidgets.QPushButton(self.central_widget)
        self.camera2.setObjectName("camera2")
        self.cameras.addWidget(self.camera2)
        self.left_layout.addLayout(self.cameras)
        self.sensor_data = QtWidgets.QTableWidget(self.central_widget)
        self.sensor_data.setAutoScroll(True)
        self.sensor_data.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.sensor_data.setShowGrid(True)
        self.sensor_data.setCornerButtonEnabled(True)
        self.sensor_data.setRowCount(4)
        self.sensor_data.setColumnCount(7)
        self.sensor_data.setObjectName("sensor_data")
        self.sensor_data.horizontalHeader().setVisible(False)
        self.sensor_data.horizontalHeader().setHighlightSections(False)
        self.sensor_data.verticalHeader().setVisible(False)
        self.sensor_data.verticalHeader().setHighlightSections(False)
        self.left_layout.addWidget(self.sensor_data)
        self.messages = QtWidgets.QTextBrowser(self.central_widget)
        self.messages.setObjectName("messages")
        self.left_layout.addWidget(self.messages)
        self.horizontalLayout.addLayout(self.left_layout)
        self.right_layout = QtWidgets.QVBoxLayout()
        self.right_layout.setObjectName("right_layout")
        self.mode_selection = QtWidgets.QHBoxLayout()
        self.mode_selection.setObjectName("mode_selection")
        self.load_default_button = QtWidgets.QPushButton(self.central_widget)
        self.load_default_button.setObjectName("load_default_button")
        self.mode_selection.addWidget(self.load_default_button)
        self.change_params_button = QtWidgets.QPushButton(self.central_widget)
        self.change_params_button.setObjectName("change_params_button")
        self.mode_selection.addWidget(self.change_params_button)
        self.auto_checkbox = QtWidgets.QCheckBox(self.central_widget)
        self.auto_checkbox.setObjectName("auto_checkbox")
        self.mode_selection.addWidget(self.auto_checkbox)
        self.right_layout.addLayout(self.mode_selection)
        self.tabWidget = QtWidgets.QTabWidget(self.central_widget)
        self.tabWidget.setObjectName("tabWidget")
        self.task_selection = QtWidgets.QWidget()
        self.task_selection.setObjectName("task_selection")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.task_selection)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.start_tasks = QtWidgets.QPushButton(self.task_selection)
        self.start_tasks.setObjectName("start_tasks")
        self.verticalLayout.addWidget(self.start_tasks)
        self.stop_tasks = QtWidgets.QPushButton(self.task_selection)
        self.stop_tasks.setObjectName("stop_tasks")
        self.verticalLayout.addWidget(self.stop_tasks)
        self.task0 = QtWidgets.QPushButton(self.task_selection)
        self.task0.setEnabled(True)
        self.task0.setObjectName("task0")
        self.verticalLayout.addWidget(self.task0)
        self.task1 = QtWidgets.QPushButton(self.task_selection)
        self.task1.setObjectName("task1")
        self.verticalLayout.addWidget(self.task1)
        self.task2 = QtWidgets.QPushButton(self.task_selection)
        self.task2.setObjectName("task2")
        self.verticalLayout.addWidget(self.task2)
        self.task3 = QtWidgets.QPushButton(self.task_selection)
        self.task3.setObjectName("task3")
        self.verticalLayout.addWidget(self.task3)
        self.task4 = QtWidgets.QPushButton(self.task_selection)
        self.task4.setObjectName("task4")
        self.verticalLayout.addWidget(self.task4)
        self.task5 = QtWidgets.QPushButton(self.task_selection)
        self.task5.setObjectName("task5")
        self.verticalLayout.addWidget(self.task5)
        self.task6 = QtWidgets.QPushButton(self.task_selection)
        self.task6.setObjectName("task6")
        self.verticalLayout.addWidget(self.task6)
        self.task7 = QtWidgets.QPushButton(self.task_selection)
        self.task7.setObjectName("task7")
        self.verticalLayout.addWidget(self.task7)
        self.tabWidget.addTab(self.task_selection, "")
        self.controls = QtWidgets.QWidget()
        self.controls.setObjectName("controls")
        self.gridLayout = QtWidgets.QGridLayout(self.controls)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.forward = QtWidgets.QPushButton(self.controls)
        self.forward.setMaximumSize(QtCore.QSize(100, 100))
        self.forward.setObjectName("forward")
        self.gridLayout.addWidget(self.forward, 3, 2, 1, 1)
        self.rotate_l = QtWidgets.QPushButton(self.controls)
        self.rotate_l.setMaximumSize(QtCore.QSize(100, 100))
        self.rotate_l.setObjectName("rotate_l")
        self.gridLayout.addWidget(self.rotate_l, 4, 0, 1, 1)
        self.rotate_r = QtWidgets.QPushButton(self.controls)
        self.rotate_r.setMaximumSize(QtCore.QSize(100, 100))
        self.rotate_r.setObjectName("rotate_r")
        self.gridLayout.addWidget(self.rotate_r, 4, 3, 1, 1)
        self.backward = QtWidgets.QPushButton(self.controls)
        self.backward.setMaximumSize(QtCore.QSize(100, 100))
        self.backward.setObjectName("backward")
        self.gridLayout.addWidget(self.backward, 4, 2, 1, 1)
        self.up = QtWidgets.QPushButton(self.controls)
        self.up.setMaximumSize(QtCore.QSize(100, 100))
        self.up.setObjectName("up")
        self.gridLayout.addWidget(self.up, 3, 4, 1, 1)
        self.strafe_l = QtWidgets.QPushButton(self.controls)
        self.strafe_l.setMaximumSize(QtCore.QSize(100, 100))
        self.strafe_l.setObjectName("strafe_l")
        self.gridLayout.addWidget(self.strafe_l, 3, 0, 1, 1)
        self.strafe_r = QtWidgets.QPushButton(self.controls)
        self.strafe_r.setMaximumSize(QtCore.QSize(100, 100))
        self.strafe_r.setObjectName("strafe_r")
        self.gridLayout.addWidget(self.strafe_r, 3, 3, 1, 1)
        self.down = QtWidgets.QPushButton(self.controls)
        self.down.setMaximumSize(QtCore.QSize(100, 100))
        self.down.setObjectName("down")
        self.gridLayout.addWidget(self.down, 4, 4, 1, 1)
        self.brake = QtWidgets.QPushButton(self.controls)
        self.brake.setMaximumSize(QtCore.QSize(100, 100))
        self.brake.setObjectName("brake")
        self.gridLayout.addWidget(self.brake, 1, 0, 1, 1)
        self.power_layout = QtWidgets.QVBoxLayout()
        self.power_layout.setObjectName("power_layout")
        self.power_label = QtWidgets.QLabel(self.controls)
        self.power_label.setMaximumSize(QtCore.QSize(100, 20))
        self.power_label.setAlignment(QtCore.Qt.AlignCenter)
        self.power_label.setObjectName("power_label")
        self.power_layout.addWidget(self.power_label)
        self.power = QtWidgets.QSpinBox(self.controls)
        self.power.setMaximumSize(QtCore.QSize(100, 80))
        self.power.setAlignment(QtCore.Qt.AlignCenter)
        self.power.setMaximum(200)
        self.power.setSingleStep(20)
        self.power.setProperty("value", 120)
        self.power.setObjectName("power")
        self.power_layout.addWidget(self.power)
        self.gridLayout.addLayout(self.power_layout, 1, 2, 1, 1)
        self.depth_layout = QtWidgets.QVBoxLayout()
        self.depth_layout.setObjectName("depth_layout")
        self.depth_label = QtWidgets.QLabel(self.controls)
        self.depth_label.setMaximumSize(QtCore.QSize(100, 20))
        self.depth_label.setAlignment(QtCore.Qt.AlignCenter)
        self.depth_label.setObjectName("depth_label")
        self.depth_layout.addWidget(self.depth_label)
        self.depth = QtWidgets.QSpinBox(self.controls)
        self.depth.setMaximumSize(QtCore.QSize(100, 80))
        self.depth.setAlignment(QtCore.Qt.AlignCenter)
        self.depth.setMinimum(-500)
        self.depth.setMaximum(500)
        self.depth.setSingleStep(20)
        self.depth.setObjectName("depth")
        self.depth_layout.addWidget(self.depth)
        self.gridLayout.addLayout(self.depth_layout, 1, 4, 1, 1)
        self.rotation_layout = QtWidgets.QVBoxLayout()
        self.rotation_layout.setObjectName("rotation_layout")
        self.rotation_label = QtWidgets.QLabel(self.controls)
        self.rotation_label.setMinimumSize(QtCore.QSize(100, 20))
        self.rotation_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rotation_label.setObjectName("rotation_label")
        self.rotation_layout.addWidget(self.rotation_label)
        self.rotation = QtWidgets.QSpinBox(self.controls)
        self.rotation.setMinimumSize(QtCore.QSize(100, 80))
        self.rotation.setAlignment(QtCore.Qt.AlignCenter)
        self.rotation.setMaximum(180)
        self.rotation.setSingleStep(10)
        self.rotation.setProperty("value", 20)
        self.rotation.setObjectName("rotation")
        self.rotation_layout.addWidget(self.rotation)
        self.gridLayout.addLayout(self.rotation_layout, 1, 3, 1, 1)
        self.tabWidget.addTab(self.controls, "")
        self.computer_vision = QtWidgets.QWidget()
        self.computer_vision.setObjectName("computer_vision")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.computer_vision)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cv_layout = QtWidgets.QGridLayout()
        self.cv_layout.setHorizontalSpacing(2)
        self.cv_layout.setVerticalSpacing(3)
        self.cv_layout.setObjectName("cv_layout")
        self.cv_2_left = QtWidgets.QVBoxLayout()
        self.cv_2_left.setContentsMargins(-1, -1, -1, 100)
        self.cv_2_left.setObjectName("cv_2_left")
        self.label = QtWidgets.QLabel(self.computer_vision)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.cv_2_left.addWidget(self.label)
        self.horizontalSlider = QtWidgets.QSlider(self.computer_vision)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.cv_2_left.addWidget(self.horizontalSlider)
        self.cv_layout.addLayout(self.cv_2_left, 3, 0, 1, 1)
        self.cv_1_left = QtWidgets.QVBoxLayout()
        self.cv_1_left.setContentsMargins(-1, -1, -1, 100)
        self.cv_1_left.setObjectName("cv_1_left")
        self.label_2 = QtWidgets.QLabel(self.computer_vision)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.cv_1_left.addWidget(self.label_2)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.computer_vision)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.cv_1_left.addWidget(self.horizontalSlider_2)
        self.cv_layout.addLayout(self.cv_1_left, 2, 0, 1, 1)
        self.cv_0_left = QtWidgets.QVBoxLayout()
        self.cv_0_left.setContentsMargins(-1, -1, -1, 100)
        self.cv_0_left.setObjectName("cv_0_left")
        self.label_3 = QtWidgets.QLabel(self.computer_vision)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.cv_0_left.addWidget(self.label_3)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.computer_vision)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.cv_0_left.addWidget(self.horizontalSlider_3)
        self.cv_layout.addLayout(self.cv_0_left, 1, 0, 1, 1)
        self.cv_0_right = QtWidgets.QVBoxLayout()
        self.cv_0_right.setContentsMargins(-1, -1, -1, 100)
        self.cv_0_right.setObjectName("cv_0_right")
        self.label_4 = QtWidgets.QLabel(self.computer_vision)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.cv_0_right.addWidget(self.label_4)
        self.horizontalSlider_4 = QtWidgets.QSlider(self.computer_vision)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.cv_0_right.addWidget(self.horizontalSlider_4)
        self.cv_layout.addLayout(self.cv_0_right, 1, 1, 1, 1)
        self.cv_1_right = QtWidgets.QVBoxLayout()
        self.cv_1_right.setContentsMargins(-1, -1, -1, 100)
        self.cv_1_right.setObjectName("cv_1_right")
        self.label_5 = QtWidgets.QLabel(self.computer_vision)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.cv_1_right.addWidget(self.label_5)
        self.horizontalSlider_5 = QtWidgets.QSlider(self.computer_vision)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.cv_1_right.addWidget(self.horizontalSlider_5)
        self.cv_layout.addLayout(self.cv_1_right, 2, 1, 1, 1)
        self.cv_2_right = QtWidgets.QVBoxLayout()
        self.cv_2_right.setContentsMargins(-1, -1, -1, 100)
        self.cv_2_right.setObjectName("cv_2_right")
        self.label_6 = QtWidgets.QLabel(self.computer_vision)
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.cv_2_right.addWidget(self.label_6)
        self.horizontalSlider_6 = QtWidgets.QSlider(self.computer_vision)
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.cv_2_right.addWidget(self.horizontalSlider_6)
        self.cv_layout.addLayout(self.cv_2_right, 3, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.cv_layout)
        self.tabWidget.addTab(self.computer_vision, "")
        self.right_layout.addWidget(self.tabWidget)
        self.horizontalLayout.addLayout(self.right_layout)
        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)

        # Controller connections

        # mode selection
        self.load_default_button.clicked.connect(self.Controller.load_default_params)
        self.change_params_button.clicked.connect(self.Controller.change_params)
        self.auto_checkbox.stateChanged.connect(self.checkbox_state_changed)
        self.tab_state_changed()
        self.tabWidget.currentChanged.connect(self.tab_state_changed)

        # manual mode buttons
        self.forward.clicked.connect(lambda: self.Controller.manual_move('forward', self.power.value(), self.rotation.value(), self.depth.value()))
        self.backward.clicked.connect(lambda: self.Controller.manual_move('backward', self.power.value(), self.rotation.value(), self.depth.value()))
        self.strafe_l.clicked.connect(lambda: self.Controller.manual_move('strafe_l', self.power.value(), self.rotation.value(), self.depth.value()))
        self.strafe_r.clicked.connect(lambda: self.Controller.manual_move('strafe_r', self.power.value(), self.rotation.value(), self.depth.value()))
        self.rotate_l.clicked.connect(lambda: self.Controller.manual_move('rotate_l', self.power.value(), self.rotation.value(), self.depth.value()))
        self.rotate_r.clicked.connect(lambda: self.Controller.manual_move('rotate_r', self.power.value(), self.rotation.value(), self.depth.value()))
        self.up.clicked.connect(lambda: self.Controller.manual_move('up', self.power.value(), self.rotation.value(), self.depth.value()))
        self.down.clicked.connect(lambda: self.Controller.manual_move('down', self.power.value(), self.rotation.value(), self.depth.value()))
        self.brake.clicked.connect(lambda: self.Controller.manual_move('brake', self.power.value(), self.rotation.value(), self.depth.value()))

    def checkbox_state_changed(self):
        if self.auto_checkbox.isChecked():
            self.Controller.start_auto_mode(1)
        else:
            self.Controller.start_auto_mode(0)

    def tab_state_changed(self):
        if self.tabWidget.currentIndex() == 1:
            self.Controller.manual_mode()

        # self.tabWidget.setCurrentIndex(2)
        # self.camera0.clicked.connect(self.display0.update)
        # self.tabWidget.currentChanged['int'].connect(self.forward.animateClick)
        # self.auto_checkbox.stateChanged['int'].connect(self.start_tasks.animateClick)
        # self.power.valueChanged['int'].connect(self.forward.animateClick)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Robosub GUI"))
        self.camera0.setText(_translate("MainWindow", "camera 0"))
        self.camera1.setText(_translate("MainWindow", "camera 1"))
        self.camera2.setText(_translate("MainWindow", "camera 2"))
        self.load_default_button.setText(_translate("MainWindow", "Load Default Params"))
        self.change_params_button.setText(_translate("MainWindow", "Change Params"))
        self.auto_checkbox.setText(_translate("MainWindow", "Start in Auto mode"))
        self.start_tasks.setText(_translate("MainWindow", "start tasks"))
        self.stop_tasks.setText(_translate("MainWindow", "stop tasks"))
        self.task0.setText(_translate("MainWindow", "task 0"))
        self.task1.setText(_translate("MainWindow", "task 1"))
        self.task2.setText(_translate("MainWindow", "task 2"))
        self.task3.setText(_translate("MainWindow", "task 3"))
        self.task4.setText(_translate("MainWindow", "task 4"))
        self.task5.setText(_translate("MainWindow", "task 5"))
        self.task6.setText(_translate("MainWindow", "task 6"))
        self.task7.setText(_translate("MainWindow", "task 7"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.task_selection), _translate("MainWindow", "Auto mode"))
        self.forward.setText(_translate("MainWindow", "Forward"))
        self.rotate_l.setText(_translate("MainWindow", "Rotate L"))
        self.rotate_r.setText(_translate("MainWindow", "Rotate R"))
        self.backward.setText(_translate("MainWindow", "Backward"))
        self.up.setText(_translate("MainWindow", "Up"))
        self.strafe_l.setText(_translate("MainWindow", "Strafe L"))
        self.strafe_r.setText(_translate("MainWindow", "Strafe R"))
        self.down.setText(_translate("MainWindow", "Down"))
        self.brake.setText(_translate("MainWindow", "Brake"))
        self.power_label.setText(_translate("MainWindow", "Power"))
        self.depth_label.setText(_translate("MainWindow", "Depth"))
        self.rotation_label.setText(_translate("MainWindow", "Rotation"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.controls), _translate("MainWindow", "Manual mode"))
        self.label.setText(_translate("MainWindow", "2 left"))
        self.label_2.setText(_translate("MainWindow", "1 left"))
        self.label_3.setText(_translate("MainWindow", "0 left"))
        self.label_4.setText(_translate("MainWindow", "0 right"))
        self.label_5.setText(_translate("MainWindow", "1 right"))
        self.label_6.setText(_translate("MainWindow", "2 right"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.computer_vision), _translate("MainWindow", "Computer Vision"))

def start_roscore():
    """Check if roscore is running. If not starts roscore"""

    name = 'roscore'
    ps = os.popen('ps -Af').read()

    if name not in ps:
        # open roscore in subprocess
        print('Setting up roscore.')
        os.system('killall -9 roscore')
        os.system('killall -9 rosmaster')
        os.system('killall -9 rosout')

        roscore = subprocess.Popen('roscore')
        time.sleep(1)
        return roscore

    return False


if __name__ == "__main__":
    roscore = start_roscore()

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    if(roscore):
        subprocess.Popen.kill(roscore)
        os.system('killall -9 rosmaster')
        os.system('killall -9 rosout')

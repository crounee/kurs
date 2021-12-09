from pymysql import connections
from pymysql import cursors

from PyQt5 import QtWidgets,QtCore,QtGui
import sys

class Main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget2 = QtWidgets.QWidget()
        self.lay2 = QtWidgets.QVBoxLayout(self.widget2)

        self.but_othet = QtWidgets.QPushButton('Отчеты')
        self.but_othet.clicked.connect(self.othet)

        self.but_form = QtWidgets.QPushButton('Формы')
        self.but_form.clicked.connect(self.forms)


        self.name = QtWidgets.QLabel('Строительная компания')
        self.buts_lay = QtWidgets.QHBoxLayout()
        self.buts_lay.addWidget(self.but_othet)
        self.buts_lay.addWidget(self.but_form)

        self.lay2.addWidget(self.name)
        self.lay2.addLayout(self.buts_lay)

        self.setCentralWidget(self.widget2)
        self.setWindowTitle('Строительная компания')
        self.setWindowIcon(QtGui.QIcon('1.jpg'))
        self.resize(800,600)
        self.show()
        self.zastavka()
    def othet(self):
        self.othet = QtWidgets.QMainWindow()
        self.othet.setWindowTitle('Строительная компания')
        self.othet.setWindowIcon(QtGui.QIcon('1.jpg'))
        self.widget = QtWidgets.QWidget()
        self.lay1 = QtWidgets.QVBoxLayout(self.widget)


        self.push_but_1 = QtWidgets.QPushButton('отображениe сотрудников отдельных должностей')
        self.push_but_1.clicked.connect(self.zapros_1)
        self.push_but_1.setFixedSize(500,30)
        self.push_but_1.setStyleSheet('font: bold 14px;')
        self.info_1 = QtWidgets.QLabel('info 1')

        self.push_but_2 = QtWidgets.QPushButton('отображениe отдельных видов работ')
        self.push_but_2.clicked.connect(self.zapros_2)
        self.push_but_2.setFixedSize(500,30)
        self.push_but_2.setStyleSheet('font: bold 14px;')
        self.info_2 = QtWidgets.QLabel('info 2')

        self.push_but_3 = QtWidgets.QPushButton('Фильтры заказов на конкретные работы')
        self.push_but_3.clicked.connect(self.zapros_3)
        self.push_but_3.setFixedSize(500,30)
        self.push_but_3.setStyleSheet('font: bold 14px;')
        self.info_3 = QtWidgets.QLabel('info 3')

        self.push_but_4 = QtWidgets.QPushButton('Фильтры для отображения заказов отдельных заказчиков')
        self.push_but_4.clicked.connect(self.zapros_4)
        self.push_but_4.setFixedSize(500,30)
        self.push_but_4.setStyleSheet('font: bold 14px;')
        self.info_4 = QtWidgets.QLabel('info 4')

        self.push_but_5 = QtWidgets.QPushButton('Фильтры на заказы, выполняемые отдельными бригадами')
        self.push_but_5.clicked.connect(self.zapros_5)
        self.push_but_5.setFixedSize(500,30)
        self.push_but_5.setStyleSheet('font: bold 14px;')
        self.info_5 = QtWidgets.QLabel('info 5')

        self.push_but_6 = QtWidgets.QPushButton('Фильтры для завершённых и не завершённых заказов')
        self.push_but_6.clicked.connect(self.zapros_6)
        self.push_but_6.setFixedSize(500,30)
        self.push_but_6.setStyleSheet('font: bold 14px;')
        self.info_6 = QtWidgets.QLabel('info 6')

        self.push_but_7 = QtWidgets.QPushButton('Фильтры для оплаченных и неоплаченных заказов')
        self.push_but_7.clicked.connect(self.zapros_7)
        self.push_but_7.setFixedSize(500,30)
        self.push_but_7.setStyleSheet('font: bold 14px;')
        self.info_7 = QtWidgets.QLabel('info 7')



        self.lay1.addWidget(self.push_but_1)
        self.lay1.addWidget(self.info_1)

        self.lay1.addWidget(self.push_but_2)
        self.lay1.addWidget(self.info_2)

        self.lay1.addWidget(self.push_but_3)
        self.lay1.addWidget(self.info_3)

        self.lay1.addWidget(self.push_but_4)
        self.lay1.addWidget(self.info_4)

        self.lay1.addWidget(self.push_but_5)
        self.lay1.addWidget(self.info_5)

        self.lay1.addWidget(self.push_but_6)
        self.lay1.addWidget(self.info_6)

        self.lay1.addWidget(self.push_but_7)
        self.lay1.addWidget(self.info_7)

        scrol = QtWidgets.QScrollArea()
        scrol.setWidget(self.widget)
        scrol.setWidgetResizable(True)
        self.othet.setCentralWidget(scrol)

        self.othet.resize(800,600)
        self.othet.show()

    def all_information_bd(self):
        self.all_info = QtWidgets.QMainWindow()
        self.widget4 = QtWidgets.QWidget()
        self.lay5 = QtWidgets.QVBoxLayout(self.widget4)

        self.brigades = QtWidgets.QLabel('brigades')
        self.brigades_information = QtWidgets.QLabel('Info')
        self.brigades_input = QtWidgets.QLineEdit('')




    def forms(self):
        self.form = QtWidgets.QMainWindow()
        self.form.setWindowTitle('Строительная компания')
        self.form.setWindowIcon(QtGui.QIcon('1.jpg'))
        self.widget3 = QtWidgets.QWidget()

        self.lay3 = QtWidgets.QVBoxLayout(self.widget3)

        self.but_about_program = QtWidgets.QPushButton('О программе')
        self.but_about_program.clicked.connect(self.info_a)

        self.but_zastavka = QtWidgets.QPushButton('Заставка')
        self.but_zastavka.clicked.connect(self.zastavka)

        self.info_aboyt_programm = QtWidgets.QLabel('')

        self.lay3.addWidget(self.but_about_program)
        self.lay3.addWidget(self.info_aboyt_programm)
        self.lay3.addWidget(self.but_zastavka)

        self.form.setCentralWidget(self.widget3)

        self.form.resize(800,600)
        self.form.show()

    def zastavka(self):
        self.zastavka_new = QtWidgets.QMainWindow()
        self.zastavka_new.setWindowTitle('Строительная компания')
        self.zastavka_new.setWindowIcon(QtGui.QIcon('1.jpg'))
        self.widget_zastavka = QtWidgets.QWidget()

        self.lay4 = QtWidgets.QVBoxLayout(self.widget_zastavka)
        self.zastavka_info = QtWidgets.QLabel('Это заставка')


        self.lay4.addWidget(self.zastavka_info)


        self.zastavka_new.setCentralWidget(self.widget_zastavka)
        self.zastavka_new.resize(800,600)
        self.zastavka_new.show()


    def info_a(self):
        self.info_aboyt_programm.setText('Это информация о программе')

    def zapros_1(self):
        with connections.Connection(user='root',host='localhost',database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:

                sql = ('SELECT `fio`, `code_position` FROM `staff`')
                cursor.execute(sql)
                g = cursor.fetchall()
                print(g)
                self.info_1.setText(str(g))

    def zapros_2(self):
        with connections.Connection(user='root',host='localhost',database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:

                sql = ('SELECT `code_type`, `name` FROM `types_of_works`')
                cursor.execute(sql)
                g = cursor.fetchall()
                print(g)
                self.info_2.setText(str(g))

    def zapros_3(self):
        with connections.Connection(user='root',host='localhost',database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:

                sql = ('SELECT * FROM `orders`')
                cursor.execute(sql)
                g = cursor.fetchall()
                print(g)
                self.info_3.setText(str(g))

    def zapros_4(self):
        with connections.Connection(user='root',host='localhost',database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:

                sql = ('SELECT * FROM `customers`')
                cursor.execute(sql)
                g = cursor.fetchall()
                print(g)
                self.info_4.setText(str(g))

    def zapros_5(self):
        with connections.Connection(user='root',host='localhost',database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:

                sql = ('SELECT * FROM `brigades`')
                cursor.execute(sql)
                g = cursor.fetchall()
                print(g)
                self.info_5.setText(str(g))

    def zapros_6(self):
        with connections.Connection(user='root',host='localhost',database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:

                sql = ('SELECT `code_customer`, `code_type`, `code_brigades`, `completion_mark`  FROM `orders`')
                cursor.execute(sql)
                g = cursor.fetchall()
                print(g)
                self.info_6.setText(str(g))

    def zapros_7(self):
        with connections.Connection(user='root',host='localhost',database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:

                sql = ('SELECT `code_customer`, `code_type`, `code_brigades`, `pay_mark`  FROM `orders`')
                cursor.execute(sql)
                g = cursor.fetchall()
                print(g)
                self.info_7.setText(str(g))
class App(QtWidgets.QApplication):
    def __init__(self,argv):
        super().__init__(argv)

        self.setStyle('Fusion')

app = App([])
win = Main_window()
app.exec()












from pymysql import connections
from pymysql import cursors

from PyQt5 import QtWidgets,QtCore,QtGui


class Main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.widget = QtWidgets.QWidget()
        self.lay1 = QtWidgets.QVBoxLayout(self.widget)


        self.push_but_1 = QtWidgets.QPushButton('отображениe сотрудников отдельных должностей')
        self.push_but_1.clicked.connect(self.zapros_1)
        self.info_1 = QtWidgets.QLabel('info 1')

        self.push_but_2 = QtWidgets.QPushButton('отображениe отдельных видов работ')
        self.push_but_2.clicked.connect(self.zapros_2)
        self.info_2 = QtWidgets.QLabel('info 2')

        self.push_but_3 = QtWidgets.QPushButton('Фильтры заказов на конкретные работы')
        self.push_but_3.clicked.connect(self.zapros_3)
        self.info_3 = QtWidgets.QLabel('info 3')

        self.push_but_4 = QtWidgets.QPushButton('Фильтры для отображения заказов отдельных заказчиков')
        self.push_but_4.clicked.connect(self.zapros_4)
        self.info_4 = QtWidgets.QLabel('info 4')

        self.push_but_5 = QtWidgets.QPushButton('Фильтры на заказы, выполняемые отдельными бригадами')
        self.push_but_5.clicked.connect(self.zapros_5)
        self.info_5 = QtWidgets.QLabel('info 5')

        self.push_but_6 = QtWidgets.QPushButton('Фильтры для завершённых и не завершённых заказов')
        self.push_but_6.clicked.connect(self.zapros_6)
        self.info_6 = QtWidgets.QLabel('info 6')

        self.push_but_7 = QtWidgets.QPushButton('Фильтры для оплаченных и неоплаченных заказов')
        self.push_but_7.clicked.connect(self.zapros_7)
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
        self.setCentralWidget(scrol)

        self.resize(800,600)
        self.show()

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
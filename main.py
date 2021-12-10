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


        self.but_all = QtWidgets.QPushButton('Подробная информация')
        self.but_all.clicked.connect(self.all_information_bd)

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

        self.lay1.addWidget(self.but_all)

        scrol = QtWidgets.QScrollArea()
        scrol.setWidget(self.widget)
        scrol.setWidgetResizable(True)
        self.othet.setCentralWidget(scrol)

        self.othet.resize(800,600)
        self.othet.show()

    def all_information_bd(self):
        self.all_info = QtWidgets.QMainWindow()
        self.all_info.setWindowTitle('Строительная компания')
        self.all_info.setWindowIcon(QtGui.QIcon('1.jpg'))
        self.widget_info = QtWidgets.QWidget()
        self.lay_info = QtWidgets.QVBoxLayout(self.widget_info)
        ####start

        self.table_1 = QtWidgets.QTableWidget()
        self.table_1.setColumnCount(4)
        self.table_1.setRowCount(len(self.get_info_brigades()))
        self.table_1.setHorizontalHeaderLabels(['code_brigades','code_employee_1','code_employee_2','code_employee_3'])
        self.but_update_table_1 = QtWidgets.QPushButton('Обновить brigadees')
        self.but_update_table_1.clicked.connect(self.update_brigades)


        self.lay_info.addWidget(self.table_1)
        self.lay_info.addWidget(self.but_update_table_1)


        self.table_2 = QtWidgets.QTableWidget()
        self.table_2.setColumnCount(5)
        self.table_2.setRowCount(len(self.get_info_customers()))
        self.table_2.setHorizontalHeaderLabels(['code_customer','fio','	adres','phone','passport'])
        self.but_update_table_2 = QtWidgets.QPushButton('обновить customers')
        self.but_update_table_2.clicked.connect(self.update_customers)

        self.lay_info.addWidget(self.table_2)
        self.lay_info.addWidget(self.but_update_table_2)



        self.table_3 = QtWidgets.QTableWidget()
        self.table_3.setColumnCount(5)
        self.table_3.setRowCount(len(self.get_info_materials()))
        self.table_3.setHorizontalHeaderLabels(['code_customer', 'fio', 'adres', 'phone', 'passport'])
        self.but_update_table_3 = QtWidgets.QPushButton('обновить materials')
        self.but_update_table_3.clicked.connect(self.update_materials)

        self.lay_info.addWidget(self.table_3)
        self.lay_info.addWidget(self.but_update_table_3)



        self.table_4 = QtWidgets.QTableWidget()
        self.table_4.setColumnCount(9)
        self.table_4.setRowCount(len(self.get_info_orders()))
        self.table_4.setHorizontalHeaderLabels(['code_customer', 'code_type', 'code_brigades', 'coast', 'date_start','date_end','completion_mark','pay_mark','code_staff'])
        self.but_update_table_4 = QtWidgets.QPushButton('обновить orders')
        self.but_update_table_4.clicked.connect(self.update_orders)

        self.lay_info.addWidget(self.table_4)
        self.lay_info.addWidget(self.but_update_table_4)



        self.table_5 = QtWidgets.QTableWidget()
        self.table_5.setColumnCount(5)
        self.table_5.setRowCount(len(self.get_info_positions()))
        self.table_5.setHorizontalHeaderLabels(['code_position', 'name_position', 'salary', 'responsibilities', 'requirements'])
        self.but_update_table_5 = QtWidgets.QPushButton('обновить positions')
        self.but_update_table_5.clicked.connect(self.update_positions)

        self.lay_info.addWidget(self.table_5)
        self.lay_info.addWidget(self.but_update_table_5)


        self.table_6 = QtWidgets.QTableWidget()
        self.table_6.setColumnCount(8)
        self.table_6.setRowCount(len(self.get_info_staff()))
        self.table_6.setHorizontalHeaderLabels(['code_staff', 'fio', 'age', 'gender', '	adres', 'phone', 'passport','code_position'])
        self.but_update_table_6 = QtWidgets.QPushButton('обновить staff')
        self.but_update_table_6.clicked.connect(self.update_staff)

        self.lay_info.addWidget(self.table_6)
        self.lay_info.addWidget(self.but_update_table_6)


        self.table_7 = QtWidgets.QTableWidget()
        self.table_7.setColumnCount(7)
        self.table_7.setRowCount(len(self.get_info_types_of_works()))
        self.table_7.setHorizontalHeaderLabels(['code_type', 'name', 'description', 'coast_of_work', 'code_material_1', 'code_material_2', 'code_material_3'])
        self.but_update_table_7 = QtWidgets.QPushButton('обновить types_of_works')
        self.but_update_table_7.clicked.connect(self.update_types_of_works)

        self.lay_info.addWidget(self.table_7)
        self.lay_info.addWidget(self.but_update_table_7)


        ####end
        self.new_scrol = QtWidgets.QScrollArea()
        self.new_scrol.setWidget(self.widget_info)
        self.new_scrol.setWidgetResizable(True)

        self.all_info.setCentralWidget(self.new_scrol)
        self.all_info.resize(800,600)
        self.all_info.show()

##brigadees
    def get_info_brigades(self):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ('SELECT * FROM `brigades`')
                cursor.execute(sql)
                g = cursor.fetchall()

            return g


    def update_brigades(self):
        for i in range(0,len(self.get_info_brigades())):
            for g in range(0,4):
                f = str(self.get_info_brigades()[i][g])

                self.table_1.setItem(i,g,QtWidgets.QTableWidgetItem(f))

###customers
    def get_info_customers(self):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ('SELECT * FROM `customers`')
                cursor.execute(sql)
                g = cursor.fetchall()

            return g


    def update_customers(self):
        for i in range(0,len(self.get_info_customers())):
            for g in range(0,5):
                f = str(self.get_info_customers()[i][g])

                self.table_2.setItem(i,g,QtWidgets.QTableWidgetItem(f))

###materials
    def get_info_materials(self):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ('SELECT * FROM `materials`')
                cursor.execute(sql)
                g = cursor.fetchall()

            return g


    def update_materials(self):
        for i in range(0,len(self.get_info_materials())):
            for g in range(0,5):
                f = str(self.get_info_materials()[i][g])

                self.table_3.setItem(i,g,QtWidgets.QTableWidgetItem(f))

###orders
    def get_info_orders(self):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ('SELECT * FROM `orders`')
                cursor.execute(sql)
                g = cursor.fetchall()

            return g


    def update_orders(self):
        for i in range(0,len(self.get_info_orders())):
            for g in range(0,9):
                f = str(self.get_info_orders()[i][g])

                self.table_4.setItem(i,g,QtWidgets.QTableWidgetItem(f))


###  positions
    def get_info_positions(self):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ('SELECT * FROM `positions`')
                cursor.execute(sql)
                g = cursor.fetchall()

            return g


    def update_positions(self):
        for i in range(0,len(self.get_info_positions())):
            for g in range(0,5):
                f = str(self.get_info_positions()[i][g])

                self.table_5.setItem(i,g,QtWidgets.QTableWidgetItem(f))

###staff
    def get_info_staff(self):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ('SELECT * FROM `staff`')
                cursor.execute(sql)
                g = cursor.fetchall()

            return g


    def update_staff(self):
        for i in range(0,len(self.get_info_staff())):
            for g in range(0,8):
                f = str(self.get_info_staff()[i][g])

                self.table_6.setItem(i,g,QtWidgets.QTableWidgetItem(f))

###types_of_works
    def get_info_types_of_works(self):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ('SELECT * FROM `types_of_works`')
                cursor.execute(sql)
                g = cursor.fetchall()

            return g


    def update_types_of_works(self):
        for i in range(0,len(self.get_info_types_of_works())):
            for g in range(0,7):
                f = str(self.get_info_types_of_works()[i][g])

                self.table_7.setItem(i,g,QtWidgets.QTableWidgetItem(f))

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












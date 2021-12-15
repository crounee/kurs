from pymysql import connections
from pymysql import cursors
from change import Ez_info_1
from PyQt5 import QtWidgets,QtCore,QtGui
import sys

class Main_window(QtWidgets.QMainWindow,Ez_info_1):
    def __init__(self):
        super().__init__()
        self.widget2 = QtWidgets.QWidget()
        self.lay2 = QtWidgets.QVBoxLayout(self.widget2)

        self.but_othet = QtWidgets.QPushButton('Отчеты')
        self.but_othet.setStyleSheet('background-color: green;')
        self.but_othet.clicked.connect(self.othet)

        self.but_form = QtWidgets.QPushButton('Формы')
        self.but_form.setStyleSheet('background-color: green;')
        self.but_form.clicked.connect(self.forms)


        self.name = QtWidgets.QLabel('Строительная компания')
        self.name.setStyleSheet('''
    background-color: white;
    border-style: outset;
    border-width: 20px;
    border-radius: 50px;
    border-color: beige;
    font: bold 25px;
    min-width: 10em;
    padding: 1px;
''')
        self.buts_lay = QtWidgets.QHBoxLayout()
        self.buts_lay.addWidget(self.but_othet,alignment=QtCore.Qt.AlignCenter)
        self.buts_lay.addWidget(self.but_form,alignment=QtCore.Qt.AlignCenter)

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
        self.but_all.setStyleSheet('background-color: green;')
        self.but_all.setFixedSize(500,30)

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
        try:
            self.all_info = QtWidgets.QMainWindow()
            self.all_info.setWindowTitle('Строительная компания')
            self.all_info.setWindowIcon(QtGui.QIcon('1.jpg'))
            self.widget_info = QtWidgets.QWidget()
            self.lay_info = QtWidgets.QVBoxLayout()
            self.lay_grid = QtWidgets.QGridLayout(self.widget_info)
            self.lay_grid.setSpacing(50)
            ####start


            self.table_1 = QtWidgets.QTableWidget()
            self.table_1.setColumnCount(4)
            self.table_1.setRowCount(len(self.get_info_brigades()))
            self.table_1.setHorizontalHeaderLabels(['code_brigades','code_employee_1','code_employee_2','code_employee_3'])
            self.table_1.setFixedSize(600,150)
            self.but_update_table_1 = QtWidgets.QPushButton('Обновить brigadees')
            self.but_update_table_1.clicked.connect(self.update_brigades)

            self.but_save_table_1 = QtWidgets.QPushButton('Сохранить изменения')
            self.but_save_table_1.clicked.connect(self.update_table_1)

            self.but_chose = QtWidgets.QComboBox()
            self.but_1 = QtWidgets.QPushButton('test')
            self.but_1.clicked.connect(self.get_one)

            ##delete_table_1
            self.lay_delete_1 = QtWidgets.QVBoxLayout()
            self.lay_delete_1.setSpacing(0)
            self.delete_table_1 = QtWidgets.QPushButton('Удалить данные')
            self.delete_table_1_line_table = QtWidgets.QLineEdit('Введите Code_brigades для удаления')
            self.delete_table_1.clicked.connect(self.delete_table_1_1)
            self.lay_delete_1.addWidget(self.delete_table_1)
            self.lay_delete_1.addWidget(self.delete_table_1_line_table)
            ##add_table_1
            self.lay_add_brigades = QtWidgets.QVBoxLayout()
            self.lay_add_brigades.setSpacing(0)
            self.add_table_1 = QtWidgets.QPushButton('Добавить запись в brigades')
            self.add_table_1.clicked.connect(self.add_table_1_1)

            self.add_table_1_zapis_1 = QtWidgets.QLineEdit('code_brigades')
            self.add_table_1_zapis_2 = QtWidgets.QLineEdit('code_employee_1')
            self.add_table_1_zapis_3 = QtWidgets.QLineEdit('code_employee_2')
            self.add_table_1_zapis_4 = QtWidgets.QLineEdit('code_employee_3')
            self.lay_add_brigades.addWidget(self.add_table_1)
            self.lay_add_brigades.addWidget(self.add_table_1_zapis_1)
            self.lay_add_brigades.addWidget(self.add_table_1_zapis_2)
            self.lay_add_brigades.addWidget(self.add_table_1_zapis_3)
            self.lay_add_brigades.addWidget(self.add_table_1_zapis_4)

            self.lay_grid.addWidget(self.table_1,0,1)
            self.lay_grid.addWidget(self.but_update_table_1,0,2)
            self.lay_grid.addWidget(self.but_save_table_1,0,3)
            self.lay_grid.addLayout(self.lay_delete_1,0,4)
            self.lay_grid.addLayout(self.lay_add_brigades,0,5)


            self.table_2 = QtWidgets.QTableWidget()
            self.table_2.setColumnCount(5)
            self.table_2.setRowCount(len(self.get_info_customers()))
            self.table_2.setHorizontalHeaderLabels(['code_customer','fio','	adres','phone','passport'])
            self.table_2.setFixedSize(600,150)
            self.but_update_table_2 = QtWidgets.QPushButton('обновить customers')
            self.but_update_table_2.clicked.connect(self.update_customers)

            self.but_save_table_2 = QtWidgets.QPushButton('Сохранить изменения')
            self.but_save_table_2.clicked.connect(self.update_table_2)

            ##delete_table_2
            self.lay_delete_2 = QtWidgets.QVBoxLayout()
            self.lay_delete_2.setSpacing(0)
            self.delete_table_2 = QtWidgets.QPushButton('Удалить данные')
            self.delete_table_2_line_table = QtWidgets.QLineEdit('Введите code_customer для удаления')
            self.delete_table_2.clicked.connect(self.delete_table_2_1)
            self.lay_delete_2.addWidget(self.delete_table_2)
            self.lay_delete_2.addWidget(self.delete_table_2_line_table)
            ##add_table_2
            self.lay_add_customers = QtWidgets.QVBoxLayout()
            self.lay_add_customers.setSpacing(0)
            self.add_table_2 = QtWidgets.QPushButton('Добавить запись в brigades')
            self.add_table_2.clicked.connect(self.add_table_2_1)

            self.add_table_2_zapis_1 = QtWidgets.QLineEdit('code_customer')
            self.add_table_2_zapis_2 = QtWidgets.QLineEdit('fio')
            self.add_table_2_zapis_3 = QtWidgets.QLineEdit('adres')
            self.add_table_2_zapis_4 = QtWidgets.QLineEdit('phone')
            self.add_table_2_zapis_5 = QtWidgets.QLineEdit('passport')
            self.lay_add_customers.addWidget(self.add_table_2)
            self.lay_add_customers.addWidget(self.add_table_2_zapis_1)
            self.lay_add_customers.addWidget(self.add_table_2_zapis_2)
            self.lay_add_customers.addWidget(self.add_table_2_zapis_3)
            self.lay_add_customers.addWidget(self.add_table_2_zapis_4)
            self.lay_add_customers.addWidget(self.add_table_2_zapis_5)


            self.lay_grid.addWidget(self.table_2,1,1)
            self.lay_grid.addWidget(self.but_update_table_2,1,2)
            self.lay_grid.addWidget(self.but_save_table_2,1,3)
            self.lay_grid.addLayout(self.lay_delete_2,1,4)
            self.lay_grid.addLayout(self.lay_add_customers,1,5)



            self.table_3 = QtWidgets.QTableWidget()
            self.table_3.setColumnCount(5)
            self.table_3.setRowCount(len(self.get_info_materials()))
            self.table_3.setHorizontalHeaderLabels(['code_material', 'name', 'packaging', 'description', 'coast'])
            self.table_3.setFixedSize(600,150)
            self.but_update_table_3 = QtWidgets.QPushButton('обновить materials')
            self.but_update_table_3.clicked.connect(self.update_materials)

            self.but_save_table_3 = QtWidgets.QPushButton('Сохранить изменения')
            self.but_save_table_3.clicked.connect(self.update_table_3)

            ##delete_table_3
            self.lay_delete_3 = QtWidgets.QVBoxLayout()
            self.lay_delete_3.setSpacing(0)
            self.delete_table_3 = QtWidgets.QPushButton('Удалить данные')
            self.delete_table_3_line_table = QtWidgets.QLineEdit('Введите code_material для удаления')
            self.delete_table_3.clicked.connect(self.delete_table_3_1)
            self.lay_delete_3.addWidget(self.delete_table_3)
            self.lay_delete_3.addWidget(self.delete_table_3_line_table)
            ##add_table_3
            self.lay_add_materials = QtWidgets.QVBoxLayout()
            self.lay_add_materials.setSpacing(0)
            self.add_table_3 = QtWidgets.QPushButton('Добавить запись в materials')
            self.add_table_3.clicked.connect(self.add_table_3_1)

            self.add_table_3_zapis_1 = QtWidgets.QLineEdit('code_material')
            self.add_table_3_zapis_2 = QtWidgets.QLineEdit('name')
            self.add_table_3_zapis_3 = QtWidgets.QLineEdit('packaging')
            self.add_table_3_zapis_4 = QtWidgets.QLineEdit('description')
            self.add_table_3_zapis_5 = QtWidgets.QLineEdit('coast')
            self.lay_add_materials.addWidget(self.add_table_3)
            self.lay_add_materials.addWidget(self.add_table_3_zapis_1)
            self.lay_add_materials.addWidget(self.add_table_3_zapis_2)
            self.lay_add_materials.addWidget(self.add_table_3_zapis_3)
            self.lay_add_materials.addWidget(self.add_table_3_zapis_4)
            self.lay_add_materials.addWidget(self.add_table_3_zapis_5)

            self.lay_grid.addWidget(self.table_3,3,1)
            self.lay_grid.addWidget(self.but_update_table_3,3,2)
            self.lay_grid.addWidget(self.but_save_table_3,3,3)
            self.lay_grid.addLayout(self.lay_delete_3,3,4)
            self.lay_grid.addLayout(self.lay_add_materials,3,5)



            self.table_4 = QtWidgets.QTableWidget()
            self.table_4.setColumnCount(9)
            self.table_4.setRowCount(len(self.get_info_orders()))
            self.table_4.setHorizontalHeaderLabels(['code_customer', 'code_type', 'code_brigades', 'coast', 'date_start','date_end','completion_mark','pay_mark','code_staff'])
            self.table_4.setFixedSize(600,150)
            self.but_update_table_4 = QtWidgets.QPushButton('обновить orders')
            self.but_update_table_4.clicked.connect(self.update_orders)

            self.but_save_table_4 = QtWidgets.QPushButton('Сохранить изменения')
            self.but_save_table_4.clicked.connect(self.update_table_4)
            ##types_of_works
            self.text_sort_types_of_works = QtWidgets.QLabel('Сортировать по типам работ')
            self.comb_box_table_4 = QtWidgets.QComboBox()
            self.comb_box_table_4.addItems(['1', '2', '3', '4', '5'])
            self.comb_box_table_4.textActivated.connect(self.update_orders_2_0)
            ##zakazhiki
            self.text_sort_kakazhiki = QtWidgets.QLabel('Сортировать по заказчикам')
            self.comb_box_table_4_1 = QtWidgets.QComboBox()
            self.comb_box_table_4_1.addItems(['1', '2', '3', '4', '5'])
            self.comb_box_table_4_1.textActivated.connect(self.update_orders_2_1)
            ##brigades
            self.text_sort_brigades = QtWidgets.QLabel('Сортировать по бригадам')
            self.comb_box_table_4_2 = QtWidgets.QComboBox()
            self.comb_box_table_4_2.addItems(['1', '2', '3', '4', '5'])
            self.comb_box_table_4_2.textActivated.connect(self.update_orders_2_2)

            ##delete_table_4
            self.lay_delete_4 = QtWidgets.QVBoxLayout()
            self.lay_delete_4.setSpacing(0)
            self.delete_table_4 = QtWidgets.QPushButton('Удалить данные')
            self.delete_table_4_line_table = QtWidgets.QLineEdit('Введите code_customer для удаления')
            self.delete_table_4.clicked.connect(self.delete_table_4_1)
            self.lay_delete_4.addWidget(self.delete_table_4)
            self.lay_delete_4.addWidget(self.delete_table_4_line_table)
            ##add_table_4
            self.lay_add_orders = QtWidgets.QVBoxLayout()
            self.lay_add_orders.setSpacing(0)
            self.add_table_4 = QtWidgets.QPushButton('Добавить запись в orders')
            self.add_table_4.clicked.connect(self.add_table_4_1)

            self.add_table_4_zapis_1 = QtWidgets.QLineEdit('code_customer')
            self.add_table_4_zapis_2 = QtWidgets.QLineEdit('code_type')
            self.add_table_4_zapis_3 = QtWidgets.QLineEdit('code_brigades')
            self.add_table_4_zapis_4 = QtWidgets.QLineEdit('coast')
            self.add_table_4_zapis_5 = QtWidgets.QLineEdit('date_start')
            self.add_table_4_zapis_6 = QtWidgets.QLineEdit('date_end')
            self.add_table_4_zapis_7 = QtWidgets.QLineEdit('completion_mark')
            self.add_table_4_zapis_8 = QtWidgets.QLineEdit('pay_mark')
            self.add_table_4_zapis_9 = QtWidgets.QLineEdit('code_staff')
            self.lay_add_orders.addWidget(self.add_table_4)
            self.lay_add_orders.addWidget(self.add_table_4_zapis_1)
            self.lay_add_orders.addWidget(self.add_table_4_zapis_2)
            self.lay_add_orders.addWidget(self.add_table_4_zapis_3)
            self.lay_add_orders.addWidget(self.add_table_4_zapis_4)
            self.lay_add_orders.addWidget(self.add_table_4_zapis_5)
            self.lay_add_orders.addWidget(self.add_table_4_zapis_6)
            self.lay_add_orders.addWidget(self.add_table_4_zapis_7)
            self.lay_add_orders.addWidget(self.add_table_4_zapis_8)
            self.lay_add_orders.addWidget(self.add_table_4_zapis_9)

            self.lay_grid.addWidget(self.table_4,4,1)
            self.lay_grid.addWidget(self.but_update_table_4,4,2)
            self.lay_grid.addWidget(self.but_save_table_4,4,3)
            self.lay_grid.addWidget(self.text_sort_types_of_works,4,4)
            self.lay_grid.addWidget(self.comb_box_table_4,4,5)
            self.lay_grid.addWidget(self.text_sort_kakazhiki,4,6)
            self.lay_grid.addWidget(self.comb_box_table_4_1,4,7)
            self.lay_grid.addWidget(self.text_sort_brigades,4,8)
            self.lay_grid.addWidget(self.comb_box_table_4_2,4,9)
            self.lay_grid.addLayout(self.lay_delete_4,4,10)
            self.lay_grid.addLayout(self.lay_add_orders,4,11)


            self.table_5 = QtWidgets.QTableWidget()
            self.table_5.setColumnCount(5)
            self.table_5.setRowCount(len(self.get_info_positions()))
            self.table_5.setHorizontalHeaderLabels(['code_position', 'name_position', 'salary', 'responsibilities', 'requirements'])
            self.table_5.setFixedSize(600,150)
            self.but_update_table_5 = QtWidgets.QPushButton('обновить positions')
            self.but_update_table_5.clicked.connect(self.update_positions)

            self.but_save_table_5 = QtWidgets.QPushButton('Сохранить изменения')
            self.but_save_table_5.clicked.connect(self.update_table_5)

            ##delete_table_5
            self.lay_delete_5 = QtWidgets.QVBoxLayout()
            self.lay_delete_5.setSpacing(0)
            self.delete_table_5 = QtWidgets.QPushButton('Удалить данные')
            self.delete_table_5_line_table = QtWidgets.QLineEdit('Введите code_position для удаления')
            self.delete_table_5.clicked.connect(self.delete_table_5_1)
            self.lay_delete_5.addWidget(self.delete_table_5)
            self.lay_delete_5.addWidget(self.delete_table_5_line_table)
            ##add_table_5
            self.lay_add_positions = QtWidgets.QVBoxLayout()
            self.lay_add_positions.setSpacing(0)
            self.add_table_5 = QtWidgets.QPushButton('Добавить запись в positions')
            self.add_table_5.clicked.connect(self.add_table_5_1)

            self.add_table_5_zapis_1 = QtWidgets.QLineEdit('code_position')
            self.add_table_5_zapis_2 = QtWidgets.QLineEdit('name_position')
            self.add_table_5_zapis_3 = QtWidgets.QLineEdit('salary')
            self.add_table_5_zapis_4 = QtWidgets.QLineEdit('responsibilities')
            self.add_table_5_zapis_5 = QtWidgets.QLineEdit('requirements')
            self.lay_add_positions.addWidget(self.add_table_5)
            self.lay_add_positions.addWidget(self.add_table_5_zapis_1)
            self.lay_add_positions.addWidget(self.add_table_5_zapis_2)
            self.lay_add_positions.addWidget(self.add_table_5_zapis_3)
            self.lay_add_positions.addWidget(self.add_table_5_zapis_4)
            self.lay_add_positions.addWidget(self.add_table_5_zapis_5)



            self.lay_grid.addWidget(self.table_5,5,1)
            self.lay_grid.addWidget(self.but_update_table_5,5,2)
            self.lay_grid.addWidget(self.but_save_table_5,5,3)
            self.lay_grid.addLayout(self.lay_delete_5,5,4)
            self.lay_grid.addLayout(self.lay_add_positions,5,5)

            self.table_6 = QtWidgets.QTableWidget()
            self.table_6.setColumnCount(8)
            self.table_6.setRowCount(len(self.get_info_staff()))
            self.table_6.setHorizontalHeaderLabels(['code_staff', 'fio', 'age', 'gender', '	adres', 'phone', 'passport','code_position'])
            self.table_6.setFixedSize(600,150)
            self.but_update_table_6 = QtWidgets.QPushButton('обновить staff')
            self.but_update_table_6.clicked.connect(self.update_staff)

            self.but_save_table_6 = QtWidgets.QPushButton('Сохранить изменения')
            self.but_save_table_6.clicked.connect(self.update_table_6)

            self.text_sort_doljnosti = QtWidgets.QLabel('Сортировать по должностям')
            self.but_comb_box_table_6 = QtWidgets.QPushButton('test1')
            self.comb_box_table_6 = QtWidgets.QComboBox()
            self.comb_box_table_6.addItems(['1','2','3','4','5'])
            self.comb_box_table_6.textActivated.connect(self.update_staff_2_0)

            ##delete_table_6
            self.lay_delete_6 = QtWidgets.QVBoxLayout()
            self.lay_delete_6.setSpacing(0)
            self.delete_table_6 = QtWidgets.QPushButton('Удалить данные')
            self.delete_table_6_line_table = QtWidgets.QLineEdit('Введите code_staff для удаления')
            self.delete_table_6.clicked.connect(self.delete_table_6_1)
            self.lay_delete_6.addWidget(self.delete_table_6)
            self.lay_delete_6.addWidget(self.delete_table_6_line_table)
            ##add_table_6
            self.lay_add_staff = QtWidgets.QVBoxLayout()
            self.lay_add_staff.setSpacing(0)
            self.add_table_6 = QtWidgets.QPushButton('Добавить запись в staff')
            self.add_table_6.clicked.connect(self.add_table_6_1)

            self.add_table_6_zapis_1 = QtWidgets.QLineEdit('code_staff')
            self.add_table_6_zapis_2 = QtWidgets.QLineEdit('fio')
            self.add_table_6_zapis_3 = QtWidgets.QLineEdit('age')
            self.add_table_6_zapis_4 = QtWidgets.QLineEdit('gender')
            self.add_table_6_zapis_5 = QtWidgets.QLineEdit('adres')
            self.add_table_6_zapis_6 = QtWidgets.QLineEdit('phone')
            self.add_table_6_zapis_7 = QtWidgets.QLineEdit('passport')
            self.add_table_6_zapis_8 = QtWidgets.QLineEdit('code_position')
            self.lay_add_staff.addWidget(self.add_table_6)
            self.lay_add_staff.addWidget(self.add_table_6_zapis_1)
            self.lay_add_staff.addWidget(self.add_table_6_zapis_2)
            self.lay_add_staff.addWidget(self.add_table_6_zapis_3)
            self.lay_add_staff.addWidget(self.add_table_6_zapis_4)
            self.lay_add_staff.addWidget(self.add_table_6_zapis_5)
            self.lay_add_staff.addWidget(self.add_table_6_zapis_6)
            self.lay_add_staff.addWidget(self.add_table_6_zapis_7)
            self.lay_add_staff.addWidget(self.add_table_6_zapis_8)



            self.lay_grid.addWidget(self.table_6,6,1)
            self.lay_grid.addWidget(self.but_update_table_6,6,2)
            self.lay_grid.addWidget(self.but_save_table_6,6,3)
            self.lay_grid.addWidget(self.text_sort_doljnosti, 6, 4)
            self.lay_grid.addWidget(self.comb_box_table_6,6,5)
            self.lay_grid.addLayout(self.lay_delete_6,6,6)
            self.lay_grid.addLayout(self.lay_add_staff,6,7)


            self.table_7 = QtWidgets.QTableWidget()
            self.table_7.setColumnCount(7)
            self.table_7.setRowCount(len(self.get_info_types_of_works()))
            self.table_7.setHorizontalHeaderLabels(['code_type', 'name', 'description', 'coast_of_work', 'code_material_1', 'code_material_2', 'code_material_3'])
            self.table_7.setFixedSize(600,150)
            self.but_update_table_7 = QtWidgets.QPushButton('обновить types_of_works')
            self.but_update_table_7.clicked.connect(self.update_types_of_works)

            self.but_save_table_7 = QtWidgets.QPushButton('Сохранить изменения')
            self.but_save_table_7.clicked.connect(self.update_table_7)

            ##delete_table_7
            self.lay_delete_7 = QtWidgets.QVBoxLayout()
            self.lay_delete_7.setSpacing(0)
            self.delete_table_7 = QtWidgets.QPushButton('Удалить данные')
            self.delete_table_7_line_table = QtWidgets.QLineEdit('Введите code_type для удаления')
            self.delete_table_7.clicked.connect(self.delete_table_7_1)
            self.lay_delete_7.addWidget(self.delete_table_7)
            self.lay_delete_7.addWidget(self.delete_table_7_line_table)
            ##add_table_7
            self.lay_add_types_of_works = QtWidgets.QVBoxLayout()
            self.lay_add_types_of_works.setSpacing(0)
            self.add_table_7 = QtWidgets.QPushButton('Добавить запись в types_of_works')
            self.add_table_7.clicked.connect(self.add_table_7_1)

            self.add_table_7_zapis_1 = QtWidgets.QLineEdit('code_type')
            self.add_table_7_zapis_2 = QtWidgets.QLineEdit('name')
            self.add_table_7_zapis_3 = QtWidgets.QLineEdit('description')
            self.add_table_7_zapis_4 = QtWidgets.QLineEdit('coast_of_work')
            self.add_table_7_zapis_5 = QtWidgets.QLineEdit('code_material_1')
            self.add_table_7_zapis_6 = QtWidgets.QLineEdit('code_material_2')
            self.add_table_7_zapis_7 = QtWidgets.QLineEdit('code_material_3')

            self.lay_add_types_of_works.addWidget(self.add_table_7)
            self.lay_add_types_of_works.addWidget(self.add_table_7_zapis_1)
            self.lay_add_types_of_works.addWidget(self.add_table_7_zapis_2)
            self.lay_add_types_of_works.addWidget(self.add_table_7_zapis_3)
            self.lay_add_types_of_works.addWidget(self.add_table_7_zapis_4)
            self.lay_add_types_of_works.addWidget(self.add_table_7_zapis_5)
            self.lay_add_types_of_works.addWidget(self.add_table_7_zapis_6)
            self.lay_add_types_of_works.addWidget(self.add_table_7_zapis_7)




            self.lay_grid.addWidget(self.table_7,7,1)
            self.lay_grid.addWidget(self.but_update_table_7,7,2)
            self.lay_grid.addWidget(self.but_save_table_7,7,3)
            self.lay_grid.addLayout(self.lay_delete_7,7,4)
            self.lay_grid.addLayout(self.lay_add_types_of_works,7,5)


            ####end
            self.new_scrol = QtWidgets.QScrollArea()
            self.new_scrol.setWidget(self.widget_info)
            self.new_scrol.setWidgetResizable(True)

            self.all_info.setCentralWidget(self.new_scrol)
            self.all_info.resize(800,600)
            self.all_info.show()
        except:
            self.eroros('Запустите базу данных',window=self.widget)

    def eroros(self,name_error,window):
        error = QtWidgets.QErrorMessage(window)
        error.showMessage(name_error)



##delete_table_1
    def delete_table_1_1(self):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ("DELETE FROM `brigades` WHERE `code_brigades` = %s")
                cursor.execute(sql, (self.delete_table_1_line_table.text()))
                bd.commit()
##add_table_1
    def add_table_1_1(self):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ("INSERT INTO `brigades` (`code_brigades`, `code_employee_1`, `code_employee_2`, `code_employee_3`) VALUES (%s, %s, %s, %s)")
                cursor.execute(sql, (self.add_table_1_zapis_1.text(),self.add_table_1_zapis_2.text(),self.add_table_1_zapis_3.text(),self.add_table_1_zapis_4.text()))
                bd.commit()

##delte_table_2
    def delete_table_2_1(self):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ("DELETE FROM `customers` WHERE `code_customer` = %s")
                cursor.execute(sql, (self.delete_table_2_line_table.text()))
                bd.commit()

##add_table_2
    def add_table_2_1(self):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ("INSERT INTO `customers` (`code_customer`, `fio`, `adres`, `phone`, `passport`) VALUES (%s, %s, %s, %s, %s)")
                cursor.execute(sql, (self.add_table_2_zapis_1.text(), self.add_table_2_zapis_2.text(), self.add_table_2_zapis_3.text(),self.add_table_2_zapis_4.text(),self.add_table_2_zapis_5.text()))
                bd.commit()

##delte_table_3
    def delete_table_3_1(self):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ("DELETE FROM `materials` WHERE `code_material` = %s")
                cursor.execute(sql, (self.delete_table_3_line_table.text()))
                bd.commit()

##add_table_3
    def add_table_3_1(self):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ("INSERT INTO `materials` (`code_material`, `name`, `packaging`, `description`, `coast`) VALUES (%s, %s, %s, %s, %s)")
                cursor.execute(sql, (self.add_table_3_zapis_1.text(), self.add_table_3_zapis_2.text(), self.add_table_3_zapis_3.text(),self.add_table_3_zapis_4.text(), self.add_table_3_zapis_5.text()))
                bd.commit()

##delte_table_4
    def delete_table_4_1(self):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ("DELETE FROM `orders` WHERE `code_customer` = %s")
                cursor.execute(sql, (self.delete_table_4_line_table.text()))
                bd.commit()

##add_table_4
    def add_table_4_1(self):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ("INSERT INTO `orders` (`code_customer`, `code_type`, `code_brigades`, `coast`, `date_start`, `date_end`, `completion_mark`, `pay_mark`, `code_staff`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
                cursor.execute(sql, (self.add_table_4_zapis_1.text(), self.add_table_4_zapis_2.text(), self.add_table_4_zapis_3.text(),self.add_table_4_zapis_4.text(), self.add_table_4_zapis_5.text(),self.add_table_4_zapis_6.text(),self.add_table_4_zapis_7.text(),self.add_table_4_zapis_8.text(),self.add_table_4_zapis_9.text()))
                bd.commit()

##delte_table_5
    def delete_table_5_1(self):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ("DELETE FROM `positions` WHERE `code_position` = %s")
                cursor.execute(sql, (self.delete_table_5_line_table.text()))
                bd.commit()

##add_table_5
    def add_table_5_1(self):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ("INSERT INTO `positions` (`code_position`, `name_position`, `salary`, `responsibilities`, `requirements`) VALUES (%s, %s, %s, %s, %s)")
                cursor.execute(sql, (self.add_table_5_zapis_1.text(), self.add_table_5_zapis_2.text(), self.add_table_5_zapis_3.text(),self.add_table_5_zapis_4.text(), self.add_table_5_zapis_5.text()))
                bd.commit()

##delte_table_6
    def delete_table_6_1(self):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ("DELETE FROM `staff` WHERE `code_staff` = %s")
                cursor.execute(sql, (self.delete_table_6_line_table.text()))
                bd.commit()

##add_table_6
    def add_table_6_1(self):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ("INSERT INTO `staff` (`code_staff`, `fio`, `age`, `gender`, `adres`, `phone`, `passport`, `code_position`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
                cursor.execute(sql, (self.add_table_6_zapis_1.text(), self.add_table_6_zapis_2.text(), self.add_table_6_zapis_3.text(),self.add_table_6_zapis_4.text(), self.add_table_6_zapis_5.text(),self.add_table_6_zapis_6.text(), self.add_table_6_zapis_7.text(), self.add_table_6_zapis_8.text()))
                bd.commit()

##delete_table_7
    def delete_table_7_1(self):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ("DELETE FROM `types_of_works` WHERE `code_type` = %s")
                cursor.execute(sql, (self.delete_table_7_line_table.text()))
                bd.commit()

##add_table_7
    def add_table_7_1(self):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ("INSERT INTO `types_of_works` (`code_type`, `name`, `description`, `coast_of_work`, `code_material_1`, `code_material_2`, `code_material_3`) VALUES (%s, %s, %s, %s, %s, %s, %s)")
                cursor.execute(sql, (self.add_table_7_zapis_1.text(), self.add_table_7_zapis_2.text(), self.add_table_7_zapis_3.text(),self.add_table_7_zapis_4.text(), self.add_table_7_zapis_5.text(),self.add_table_7_zapis_6.text(), self.add_table_7_zapis_7.text()))
                bd.commit()

    ##update_table_1
    def update_table_1(self):
        for i in range(0, len(self.get_info_brigades())):
            with connections.Connection(user='root', host='localhost', database='kurs') as bd:
                with cursors.Cursor(bd) as cursor:
                    sql = ("UPDATE `brigades` SET `code_employee_1` = %s , `code_employee_2` = %s , `code_employee_3` = %s  WHERE `code_brigades` = %s")
                    cursor.execute(sql,(self.table_1.item(i,1).text(),self.table_1.item(i,2).text(),self.table_1.item(i,3).text(),self.table_1.item(i,0).text()))
                    bd.commit()

##update_table_2
    def update_table_2(self):
        for i in range(0, len(self.get_info_customers())):
            with connections.Connection(user='root', host='localhost', database='kurs') as bd:
                with cursors.Cursor(bd) as cursor:
                    sql = ("UPDATE `customers` SET `fio` = %s , `adres` = %s , `phone` = %s , `passport` = %s WHERE `code_customer` = %s")
                    cursor.execute(sql, (self.table_2.item(i, 1).text(), self.table_2.item(i, 2).text(), self.table_2.item(i, 3).text(),self.table_2.item(i, 4).text(),self.table_2.item(i, 0).text()))
                    bd.commit()

##update_table_3
    def update_table_3(self):
        for i in range(0, len(self.get_info_materials())):
            with connections.Connection(user='root', host='localhost', database='kurs') as bd:
                with cursors.Cursor(bd) as cursor:
                    sql = ("UPDATE `materials` SET `name` = %s , `packaging` = %s , `description` = %s , `coast` = %s WHERE `code_material` = %s")
                    cursor.execute(sql, (self.table_3.item(i, 1).text(), self.table_3.item(i, 2).text(), self.table_3.item(i, 3).text(),self.table_3.item(i, 4).text(), self.table_3.item(i, 0).text()))
                    bd.commit()

##update_table_4
    def update_table_4(self):
        for i in range(0, len(self.get_info_orders())):
            with connections.Connection(user='root', host='localhost', database='kurs') as bd:
                with cursors.Cursor(bd) as cursor:
                    sql = ("UPDATE `orders` SET `code_type` = %s , `code_brigades` = %s , `coast` = %s , `date_start` = %s , `date_end` = %s , `completion_mark` = %s , `pay_mark` = %s , `code_staff` = %s WHERE `code_customer` = %s")
                    cursor.execute(sql, (self.table_4.item(i, 1).text(), self.table_4.item(i, 2).text(), self.table_4.item(i, 3).text(),self.table_4.item(i, 4).text(),self.table_4.item(i, 5).text(),self.table_4.item(i, 6).text(),self.table_4.item(i, 7).text(),self.table_4.item(i, 8).text(), self.table_4.item(i, 0).text()))
                    bd.commit()

##update_table_5
    def update_table_5(self):
        for i in range(0, len(self.get_info_positions())):
            with connections.Connection(user='root', host='localhost', database='kurs') as bd:
                with cursors.Cursor(bd) as cursor:
                    sql = ("UPDATE `positions` SET `name_position` = %s , `salary` = %s , `responsibilities` = %s , `requirements` = %s WHERE `code_position` = %s")
                    cursor.execute(sql, (self.table_5.item(i, 1).text(), self.table_5.item(i, 2).text(), self.table_5.item(i, 3).text(),self.table_5.item(i, 4).text(), self.table_5.item(i, 0).text()))
                    bd.commit()
##update_table_6
    def update_table_6(self):
        for i in range(0, len(self.get_info_staff())):
            with connections.Connection(user='root', host='localhost', database='kurs') as bd:
                with cursors.Cursor(bd) as cursor:
                    sql = ("UPDATE `staff` SET `fio` = %s , `age` = %s , `gender` = %s , `adres` = %s , `phone` = %s , `passport` = %s , `code_position` = %s WHERE `code_staff` = %s")
                    cursor.execute(sql, (self.table_6.item(i, 1).text(), self.table_6.item(i, 2).text(), self.table_6.item(i, 3).text(),self.table_6.item(i, 4).text(),self.table_6.item(i, 5).text(),self.table_6.item(i, 6).text(),self.table_6.item(i, 7).text(), self.table_6.item(i, 0).text()))
                    bd.commit()

##update_table_7
    def update_table_7(self):
        for i in range(0, len(self.get_info_types_of_works())):
            with connections.Connection(user='root', host='localhost', database='kurs') as bd:
                with cursors.Cursor(bd) as cursor:
                    sql = ("UPDATE `types_of_works` SET `name` = %s , `description` = %s , `coast_of_work` = %s , `code_material_1` = %s , `code_material_2` = %s , `code_material_3` = %s WHERE `code_type` = %s")
                    cursor.execute(sql, (self.table_7.item(i, 1).text(), self.table_7.item(i, 2).text(), self.table_7.item(i, 3).text(),self.table_7.item(i, 4).text(),self.table_7.item(i, 5).text(),self.table_7.item(i, 6).text(), self.table_7.item(i, 0).text()))
                    bd.commit()
    ##"UPDATE `brigades` SET `code_employee_1` = %s , `code_employee_2` = %s , `code_employee_3` = %s  WHERE `code_brigades` = %s"
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

    def update_orders_2_0(self,name):
        self.table_4.clear()
        for i in range(0,len(self.orders_type_of_works(name))):
            for g in range(0,9):
                f = str(self.orders_type_of_works(name)[i][g])

                self.table_4.setItem(i,g,QtWidgets.QTableWidgetItem(f))
    def update_orders_2_1(self,name):
        self.table_4.clear()
        for i in range(0,len(self.orders_customers(name))):
            for g in range(0,9):
                f = str(self.orders_customers(name)[i][g])

                self.table_4.setItem(i,g,QtWidgets.QTableWidgetItem(f))

    def update_orders_2_2(self,name):
        self.table_4.clear()
        for i in range(0,len(self.orders_brigades(name))):
            for g in range(0,9):
                f = str(self.orders_brigades(name)[i][g])

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

    def update_staff_2_0(self,name):
        self.table_6.clear()
        for i in range(0,len(self.staff_sort(name))):
            for g in range(0,8):
                f = str(self.staff_sort(name)[i][g])

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
        self.zastavka_info = QtWidgets.QLabel('Строительная компания')
        self.zastavka_info.setStyleSheet('''
    background-color: white;
    border-style: outset;
    border-width: 20px;
    border-radius: 50px;
    border-color: beige;
    font: bold 25px;
    min-width: 10em;
    padding: 1px;
''')

        self.zastavka_info_2 = QtWidgets.QLabel('Добро пожаловать')
        self.zastavka_info_2.setStyleSheet('''
    background-color: white;
    border-style: outset;
    border-width: 20px;
    border-radius: 50px;
    border-color: blue;
    font: bold 25px;
    min-width: 10em;
    padding: 1px;
''')


        self.lay4.addWidget(self.zastavka_info)
        self.lay4.addWidget(self.zastavka_info_2)

        self.zastavka_new.setCentralWidget(self.widget_zastavka)
        self.zastavka_new.resize(800,600)
        self.zastavka_new.show()


    def info_a(self):
        self.info_aboyt_programm.setText('Приложение разработано: croune')
        self.info_aboyt_programm.setStyleSheet('background-color: white;')

    def zapros_1(self):
        try:
            with connections.Connection(user='root',host='localhost',database='kurs') as bd:
                with cursors.Cursor(bd) as cursor:

                    sql = ('SELECT `fio`, `code_position` FROM `staff`')
                    cursor.execute(sql)
                    g = cursor.fetchall()
                    print(g)
                    self.info_1.setText(str(g))
        except:
            self.eroros('Запустите базу данных',window=self.widget)

    def zapros_2(self):
        try:
            with connections.Connection(user='root',host='localhost',database='kurs') as bd:
                with cursors.Cursor(bd) as cursor:

                    sql = ('SELECT `code_type`, `name` FROM `types_of_works`')
                    cursor.execute(sql)
                    g = cursor.fetchall()
                    print(g)
                    self.info_2.setText(str(g))
        except:
            self.eroros('Запустите базу данных', window=self.widget)
    def zapros_3(self):
        try:
            with connections.Connection(user='root',host='localhost',database='kurs') as bd:
                with cursors.Cursor(bd) as cursor:

                    sql = ('SELECT * FROM `orders`')
                    cursor.execute(sql)
                    g = cursor.fetchall()
                    print(g)
                    self.info_3.setText(str(g))
        except:
            self.eroros('Запустите базу данных', window=self.widget)

    def zapros_4(self):
        try:
            with connections.Connection(user='root',host='localhost',database='kurs') as bd:
                with cursors.Cursor(bd) as cursor:

                    sql = ('SELECT * FROM `customers`')
                    cursor.execute(sql)
                    g = cursor.fetchall()
                    print(g)
                    self.info_4.setText(str(g))
        except:
            self.eroros('Запустите базу данных', window=self.widget)
    def zapros_5(self):
        try:
            with connections.Connection(user='root',host='localhost',database='kurs') as bd:
                with cursors.Cursor(bd) as cursor:

                    sql = ('SELECT * FROM `brigades`')
                    cursor.execute(sql)
                    g = cursor.fetchall()
                    print(g)
                    self.info_5.setText(str(g))
        except:
            self.eroros('Запустите базу данных', window=self.widget)

    def zapros_6(self):
        try:
            with connections.Connection(user='root',host='localhost',database='kurs') as bd:
                with cursors.Cursor(bd) as cursor:

                    sql = ('SELECT `code_customer`, `code_type`, `code_brigades`, `completion_mark`  FROM `orders`')
                    cursor.execute(sql)
                    g = cursor.fetchall()
                    print(g)
                    self.info_6.setText(str(g))
        except:
            self.eroros('Запустите базу данных', window=self.widget)

    def zapros_7(self):
        try:
            with connections.Connection(user='root',host='localhost',database='kurs') as bd:
                with cursors.Cursor(bd) as cursor:

                    sql = ('SELECT `code_customer`, `code_type`, `code_brigades`, `pay_mark`  FROM `orders`')
                    cursor.execute(sql)
                    g = cursor.fetchall()
                    print(g)
                    self.info_7.setText(str(g))
        except:
            self.eroros('Запустите базу данных', window=self.widget)





class App(QtWidgets.QApplication):
    def __init__(self,argv):
        super().__init__(argv)
        self.setFont(QtGui.QFont('Helvetica [Cronyx]', 10))
        self.setStyle('Fusion')

app = App([])
win = Main_window()
app.exec()












from pymysql import connections
from pymysql import cursors

class Ez_info_1:
    def __init__(self):
        super().__init__()

    def get_one(self):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ('SELECT * FROM `brigades`')
                cursor.execute(sql)
                g = cursor.fetchall()
                new = []
                for i in g:
                    new.append(str(i[0]))

                self.but_chose.addItems(new)

    def staff_sort(self,name):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ('SELECT * FROM `staff` WHERE `code_position`= %s ')
                cursor.execute(sql,(name))
                g = cursor.fetchall()
                return g

    def orders_type_of_works(self,name):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ('SELECT * FROM `orders` WHERE `code_type`= %s ')
                cursor.execute(sql,(name))
                g = cursor.fetchall()
                return g

    def orders_customers(self,name):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ('SELECT * FROM `orders` WHERE `code_customer`= %s ')
                cursor.execute(sql,(name))
                g = cursor.fetchall()
                return g

    def orders_brigades(self,name):
        with connections.Connection(user='root', host='localhost', database='kurs') as bd:
            with cursors.Cursor(bd) as cursor:
                sql = ('SELECT * FROM `orders` WHERE `code_brigades`= %s ')
                cursor.execute(sql,(name))
                g = cursor.fetchall()
                return g
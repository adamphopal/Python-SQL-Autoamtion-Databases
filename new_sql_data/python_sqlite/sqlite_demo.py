import sqlite3
from bruin import Bruin

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE bruins (
            first text,
            last text,
            username text
            )""")


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO bruins VALUES (:first, :last, :username)", {'first': emp.first, 'last': emp.last, 'username': emp.username})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM bruins WHERE last=:last", {'last': lastname})
    return c.fetchall()


def update_username(emp, username):
    with conn:
        c.execute("""UPDATE bruins SET username = :username
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'username': username})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from bruins WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

bruin_1 = Bruin('Kim', 'Kardashian', 'kimkardashian')
bruin_2 = Bruin('Jen', 'Selter', 'jenselter')
bruin_3 = Bruin('Jamie', 'Stone', 'jamiestone')


insert_emp(bruin_1)
insert_emp(bruin_2)

bruins = get_emps_by_name('Selter')
print(bruins)

update_username(bruin_3, 'imjamiestone')



conn.close()

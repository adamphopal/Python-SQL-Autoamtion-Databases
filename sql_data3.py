import sqlite3
from employee import Employee
from PIL import Image
from pydub import AudioSegment
from pydub.playback import play


#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('employee.db')

c = conn.cursor()

#c.execute('''CREATE TABLE employees
 #           (first text, last text, photo blob, song blob)''')


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :photo, :song)", {'first': emp.first, 'last': emp.last, 'photo': emp.photo, 'song': emp.song})
        image = Image.open(emp.photo)
        image.show()
        song = AudioSegment.from_mp3(emp.song)
        play(song)

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()




def update_pay(emp, photo):
    with conn:
        c.execute("""UPDATE employees SET photo = :photo
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'photo': photo})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

emp_1 = Employee('Hamim', 'Phopal',  "/Users/hamimphopal/automation/hamim.jpg", "/Users/hamimphopal/automation/j.cole.mp3",)
#emp_2 = Employee('Adam', 'Phopal',  "/Users/hamimphopal/automation/hamim2.jpg", "/Users/hamimphopal/automation/drake.mp3",)
#insert_emp(emp_2)
insert_emp(emp_1)



#insert_emp(emps)

#update_pay(emp_1, "/Users/hamimphopal/automation/hamim2.jpg")
#remove_emp(emp_1)

emps = get_emps_by_name('Phopal')
print(emps)

conn.close()

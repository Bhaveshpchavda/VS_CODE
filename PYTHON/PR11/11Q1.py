import mysql.connector
from mysql.connector import Error

class StudentDatabase:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="shreehari@6591",
                database="Yagna"
            )
            self.cursor = self.conn.cursor()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS students1(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, grade INT)")
        except Error as err:
            print(err)

    def create(self, data):
        try:
            sql = "INSERT INTO students1 (name, age, grade) VALUES (%s, %s, %s)"
            values = (data['name'], data['age'], data['grade'])
            self.cursor.execute(sql, values)
            self.conn.commit()
            return self.cursor.lastrowid
        except Error as err:
            print(err)

    def read(self, id=None):
        try:
            if id:
                self.cursor.execute("SELECT * FROM students1 WHERE id = %s", (id,))
            else:
                self.cursor.execute("SELECT * FROM students1")
            rows = self.cursor.fetchall()
            print(rows)
        except Error as err:
            print(err)

    def update(self, id, data):
        try:
            sql = "UPDATE students1 SET name = %s, age = %s, grade = %s WHERE id = %s"
            values = (data['name'], data['age'], data['grade'], id)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print(self.cursor.rowcount)
        except Error as err:
            print(err)

    def delete(self, id):
        try:
            self.cursor.execute("DELETE FROM students1 WHERE id = %s", (id,))
            self.conn.commit()
            print(self.cursor.rowcount)
        except Error as err:
            print(err)

db = StudentDatabase()

# adding data to database
db.create(data={"name":'Yagna',"age":19,"grade":22})
db.create(data={"name":'!@@',"age":16,"grade":34})
db.create(data={"name":'Xyz',"age":19,"grade":45})
db.create(data={"name":'BBQ',"age":20,"grade":24})

# reading from the database
db.read(2)
db.read(4)

# updating the database
db.update(2, data={"name":'Yagna',"age":19,"grade":22})

# deleting from the database
db.delete(3)
db.delete(4)

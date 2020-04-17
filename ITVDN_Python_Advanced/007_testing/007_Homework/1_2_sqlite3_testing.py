import sqlite3
import smtplib
import datetime


conn = sqlite3.connect(':memory:')
conn.execute("""CREATE TABLE "users" (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                first_name, 
                second_name, 
                last_name, 
                birthday)"""
             )


class User:

    def __init__(self, name: str, birthday: str):
        self.first_name = name.split()[0]
        self.second_name = name.split()[1]
        self.last_name = name.split()[2]
        self.birthday = datetime.date(*(int(_) for _ in birthday.split()))
        self._check_age()

    def get_full_name(self):
        return ' '.join((self.first_name, self.second_name, self.last_name))

    def get_short_name(self):
        return ' '.join((self.first_name, self.second_name[0] + '.', self.last_name[0] + '.'))

    def get_age(self):
        age = (datetime.date.today() - self.birthday).days // 365
        return age

    def _check_age(self):
        if datetime.date.today() < self.birthday:
            raise ValueError("Birth in future")

    def __str__(self):
        age = self.get_age()
        if age == 1:
            suffix = ''
        else:
            suffix = 's'
        return f"{self.get_full_name()} - {age} year{suffix}"


def send_email(message):

    host = "smtp.mail.ru"
    port = "587"
    addr_from = "osyapov@bk.ru"
    password = "NevadA61764"
    addr_to = "osyapov@bk.ru"

    message = 'Subject: {}\n\n{}'.format('New user', message)

    server = smtplib.SMTP(host, port)
    server.starttls()
    server.login(addr_from, password)
    server.sendmail(addr_from, addr_to, message)
    print(f'Отправлено сообщение на адрес {addr_to}\n')
    server.quit()


def register_user(user: User, connection: sqlite3.Connection):

    sql = """INSERT INTO users (first_name, second_name, last_name, birthday) VALUES ("{}", "{}", "{}", "{}")
        """.format(
            user.first_name,
            user.second_name,
            user.last_name,
            user.birthday,
    )

    connection.execute(sql)

    message = f"New user: {user.get_full_name()}, age: {user.get_age()}"
    send_email(message)


def find_user(connection: sqlite3.Connection, first_name, last_name):

    users = connection.execute('SELECT * FROM users WHERE first_name = :fn AND last_name = :ln',
                                {'fn': first_name, 'ln': last_name}).fetchall()
    # users = connection.execute('SELECT * FROM users').fetchall()

    return tuple(User(' '.join(user[1:4]), user[4].replace('-', ' ')) for user in users)


user = User("Andrey Alekseevich Osipov", "1992 07 29")
register_user(user, conn)
user = User("Andrey Victorovich Osipov", "1982 07 29")
register_user(user, conn)

user = find_user(conn, "Andrey", "Osipov")
print(user)
import sqlite3

connect = sqlite3.connect("DATA.db")

cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    status TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS computers (
    id INTEGER PRIMARY KEY,
    code TEXT,
    model TEXT,
    SN TEXT
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS tablets (
    id INTEGER PRIMARY KEY,
    code TEXT,
    model TEXT,
    SN TEXT
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS acts (
    id INTEGER PRIMARY KEY,
    actNum INT
)
''')


#------------ Computers -------------#
def GetComputerByCode(code):
    cursor.execute("SELECT * FROM computers WHERE code = ?", (code,))
    comp = cursor.fetchone()
    if comp:
        return comp
    return ["NO data", "NO data", "NO data","NO data"]


def get_computers(types='*'):
    cursor.execute(f'SELECT {types} FROM computers')
    comp = cursor.fetchall()
    if comp:
        return comp
    return ["NO data", "NO data", "NO data","NO data"]

def add_computers(code,model,sn):
    cursor.execute('''
        INSERT INTO computers (code,model, SN) VALUES (?,?,?)
    ''', (code, model, sn))
    connect.commit()


def delete_computer(id):
    cursor.execute("DELETE FROM computers WHERE id = ?", (id,))
    connect.commit()


#------------ Tablets -------------#

def get_tablets(types='*'):
    cursor.execute(f'SELECT {types} FROM tablets')
    comp = cursor.fetchall()
    if comp:
        return comp
    return ["NO data", "NO data", "NO data","NO data"]

def add_tablet(code,model,sn):
    cursor.execute('''
            INSERT INTO tablets (code,model, SN) VALUES (?,?,?)
        ''', (code, model, sn))
    connect.commit()

def delete_tablet(id):
    cursor.execute("DELETE FROM tablets WHERE id = ?", (id,))
    connect.commit()


def GetTabletByCode(code):
    cursor.execute("SELECT * FROM tablets WHERE code = ?", (code,))
    comp = cursor.fetchone()
    if comp:
        return comp
    return ["NO data", "NO data", "NO data","NO data"]




#------------ Users -------------#
def add_user(name, surname, status):
    cursor.execute('''
           INSERT INTO users (name, surname, status) VALUES (?,?,?)
       ''', (name, surname, status))
    connect.commit()

def get_users():
    cursor.execute(f'SELECT * FROM users')
    users = cursor.fetchall()
    if users:
        formated_users = []
        for i in range(len(users)):
            formated_users.append([users[i][2],users[i][1]])
        return formated_users
    return ["NO data", "NO data", "NO data", "NO data"]

def get_users_by_typeOf(types='*'):
    cursor.execute(f'SELECT {types} FROM users')
    users = cursor.fetchall()
    if users:
        return users
    return ["NO data", "NO data", "NO data", "NO data"]

def get_a_user_by(type, value):
    query = f"SELECT * FROM users WHERE {type} = ?"
    cursor.execute(query, (value,))
    user = cursor.fetchone()
    if user:
        return user
    return "NO data"


def delete_user(id):
    print(f"Got data {id}")
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    connect.commit()


#acts
def save_act(act_num):
    cursor.execute("DELETE FROM acts")
    cursor.execute('''
               INSERT INTO acts (actNum) VALUES (?)
           ''', (act_num,))
    connect.commit()

def get_last_act():
    cursor.execute("SELECT actNum FROM acts")
    act = cursor.fetchone()
    if act:
        return [int(act[0]) + 1]
    return [1]

connect.commit()
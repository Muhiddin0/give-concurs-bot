
import sqlite3

BOT_TOKEN = "5718681400:AAHfkc3xNsdRT9fgX9yR55zs8z8RsTIko3o"

db = sqlite3.connect("data/adminlar.db")
sql = db.cursor()
sql.execute("""SELECT * FROM adminlar""")

ADMINS = [
    5752098078
]
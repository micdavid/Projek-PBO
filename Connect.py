import sqlite3

class DataBase:
    def __init__(self):
        self.ConDb = sqlite3.connect('manajementoko.db')
        self.Cursor = self.ConDb.cursor()
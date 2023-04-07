import sqlite3

class DataManager:
    def __init__(self):
        self.dbpath="Fantasycricket.db"
        self.conn = sqlite3.connect('Fantasycricket.db')
        self.cur = self.conn.cursor()

    def FetchTeams(self):
        query="select different name;"
        self.cur.execute(query)
        teams = self.cur.fetchall()
        return teams

    def FetchItems(self,query):
        self.cur.execute(query)
        teams = self.cur.fetchall()
        return teams

    def Fetchcoloumns(self,query):
        self.cur.execute(query)
        teams = self.cur.fetchall()
        return self.curser

    def InsertItems(self,query,data):

        try:
            print(query,data)
            self.cursor.execute(query, data)
            self.conn.commit()
            return "1"
        except:
            return "0"

# dbpath # conn # cursor


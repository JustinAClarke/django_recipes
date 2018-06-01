import sqlite3
import os
from pathlib import Path

def parse_db_rows(rows):
    out=[]
    for row in rows:
        row_tmp={}
        #get keys, build new array
        #add to existing arrar
        #return new complete array
        keys = row.keys()
        for key in row.keys():
            row_tmp[key]=row[key]
        out.append(row_tmp)
    return out
        
class db(object):
    def __init__(self, config = False):
        print(__file__)
        self.connect = False
        
        self.config = {'DATABASE':'/home/justinfc/dev/django/mysite/recipes/old.db'}
        

    #------------------------------------
    #Init DB       
    #def init(self):
        #self.config =conf
        
        self.connect =  sqlite3.connect(self.config['DATABASE'])
        self.connect.row_factory = sqlite3.Row
 #       return self.connect

    def __del__(self):
        connect=self.get_db()
        connect.close()


    def get_db(self):
        connect =  sqlite3.connect(self.config['DATABASE'])
        connect.row_factory = sqlite3.Row
        return connect

    #------------------------------------
    #Categories
    def getAll_notice_boards(self):
        connect=self.get_db()
        cur = connect.execute('SELECT * FROM notice_boards')
        return parse_db_rows(cur.fetchall())

    def getAll_notice_board_notices(self):
        connect=self.get_db()
        cur = connect.execute('SELECT * FROM notice_board_notices')
        return parse_db_rows(cur.fetchall())

    def getAll_notice_board_notices_From_notice_board(self,Board):
        connect=self.get_db()
        cur = connect.execute('SELECT * FROM notice_board_notices WHERE Board = {}'.format(Board))
        return parse_db_rows(cur.fetchall())

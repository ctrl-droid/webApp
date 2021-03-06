import pymysql
class Board:
    def __init__(self, code=None, date=None , content=None , member_id=None, aptinfo_sn=None):
        self.code = code
        self.date = date
        self.content = content
        self.member_id = member_id
        self.aptinfo_sn = aptinfo_sn

    def __str__(self):
        return self.code+' / '+self.date+' / '+self.content+' / '+self.member_id+' / '+self.aptinfo_sn

class BoardDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='1234', db='hogetnono', charset='utf8')

    def disconnect(self):
        self.conn.close()

    def insert(self,board):
        self.connect()
        cur = self.conn.cursor()
        sql = "insert into board(date, content, member_id, aptinfo_sn) value(now(), %s, %s, %s)"
        vals = (board.content, board.member_id, board.aptinfo_sn)
        cur.execute(sql,vals)
        self.conn.commit()
        self.disconnect()

    def selectAll(self):
        self.connect()
        cur = self.conn.cursor()
        sql = "select * from board order by code desc"
        cur.execute(sql)
        boards = []
        for row in cur:
            boards.append(Board(row[0], row[1], row[2], row[3], row[4]))
        self.disconnect()
        return boards

    def select_sn(self, aptinfo_sn):
        self.connect()
        cur = self.conn.cursor()
        sql = "select * from board where aptinfo_sn=%s"
        vals = (aptinfo_sn,)
        cur.execute(sql, vals)
        boards = []
        for row in cur:
            boards.append(Board(row[0], row[1], row[2], row[3], row[4]))
        self.disconnect()
        return boards

    def select_code(self, code):
        self.connect()
        cur = self.conn.cursor()
        sql = "select * from board where code=%s"
        vals = (code,)
        cur.execute(sql, vals)
        boards = []
        for row in cur:
            boards.append(Board(row[0], row[1], row[2], row[3], row[4]))
        self.disconnect()
        return boards

    def select_member_id(self, member_id):
        self.connect()
        cur = self.conn.cursor()
        sql = "select * from board where member_id=%s"
        vals = (member_id,)
        cur.execute(sql, vals)
        boards = []
        for row in cur:
            boards.append(Board(row[0], row[1], row[2], row[3], row[4]))
        self.disconnect()
        return boards

    def edit(self, board):
        self.connect()
        cur = self.conn.cursor()
        sql = "update board set content=%s where code=%s"
        vals = (board.content, board.code)
        cur.execute(sql,vals)
        self.conn.commit()
        self.disconnect()

    def delete(self, code):
        self.connect()
        cur = self.conn.cursor()
        sql = 'delete from board where code=%s'
        vals = (code,)
        cur.execute(sql, vals)
        self.conn.commit()
        self.disconnect()

class BoardService:
    def __init__(self):
        self.dao = BoardDao()

    def board_insert(self, board):
        self.dao.insert(board)

    def board_select_sn(self, aptinfo_sn):
        return self.dao.select_sn(aptinfo_sn)

    def board_select_code(self,code):
        return self.dao.select_code(code)

    def board_select_member_id(self, member_id):
        return self.dao.select_member_id(member_id)

    def board_selectAll(self):
        return self.dao.selectAll()

    def board_edit(self,board):
        self.dao.edit(board)

    def board_delete(self,code):
        self.dao.delete(code)
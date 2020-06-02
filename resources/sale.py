import datetime
from orm.query import Connection, Query


class Sale:
    def __init__(self, line_items=[]):
        self.date = datetime.datetime.now().strftime('%x')
        self.line_items = line_items
        self.connection = Connection()
        self.id = self.get_prospective_id()

    def add_line_item(self, line_item):
        self.line_items.append(line_item)

    def get_prospective_id(self):
        query_string = 'SELECT MAX(Id)+1 FROM Sale'
        query = Query(self.connection, query_string)
        next_id = query.run()[0]['?column?']
        return next_id

    def commit(self):
        self.__insert_self()
        line_item_values = ''
        for i, line_item in enumerate(self.line_items):
            line_item_values += '('
            line_item_values += f'{self.id}, {line_item.album_id}, \'${line_item.price}\''
            line_item_values += ')'
            line_item_values += ', ' if len(self.line_items) > i+1 else ';'
        line_item_insert = f'INSERT INTO LineItem (SaleId, AlbumId, Price) VALUES {line_item_values}'
        Query(self.connection, line_item_insert).execute_no_return()
        self.connection.close()

    def __insert_self(self):
        query_string = f'INSERT INTO Sale (Id, DateOfSale) VALUES ({self.id}, \'{self.date}\')'
        q = Query(self.connection, query_string)
        q.execute_no_return()


class LineItem:
    def __init__(self, album_id, price):
        self.price = price
        self.album_id = album_id


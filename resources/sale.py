import datetime
from orm.query import Connection, Query


class Sale:
    def __init__(self, line_items=[]):
        self.date = datetime.datetime.now().strftime('%x')
        self.connection = Connection()
        self.id = self.get_prospective_id()
        self.line_items = []
        self.__map_line_items(line_items)

    def add_line_item(self, line_item):
        self.line_items.append(line_item)

    def get_prospective_id(self):
        query_string = 'SELECT MAX(Id)+1 FROM Sale'
        query = Query(self.connection, query_string)
        next_id = query.run()[0]['?column?']
        return next_id

    def commit(self):
        insert_self = self.__insert_self()
        if insert_self['success'] == 'true':
            line_item_values = ''
            for i, line_item in enumerate(self.line_items):
                line_item_values += '(' + line_item.insert_command_partial() + ')'
                line_item_values += ', ' if len(self.line_items) > i + 1 else ';'
            line_item_insert = f'INSERT INTO LineItem (SaleId, AlbumId, Price) VALUES {line_item_values}'
            try:
                Query(self.connection, line_item_insert).execute_no_return()
                self.connection.close()
                return {'success': 'true', 'Sale': f'{self.id}'}
            except ValueError as err:
                self.connection.close()
                return {'success': 'false', 'insert LineItem failed': err}
        else:
            return insert_self

    def __insert_self(self):
        query_string = f'INSERT INTO Sale (Id, DateOfSale) VALUES ({self.id}, \'{self.date}\')'
        q = Query(self.connection, query_string)
        try:
            q.execute_no_return()
            return {'success': 'true'}
        except ValueError as err:
            return {'success': 'false', 'Sale': f'insert id: {self.id}', 'error': err}

    def __map_line_items(self, line_items):
        for line_item in line_items:
            self.add_line_item(LineItem(self, line_item['album_id']))


class LineItem:
    def __init__(self, sale: Sale, album_id, price=None):
        self.sale = sale
        self.album_id = album_id
        self.price = self.get_saved_price() if price is None else price

    def get_saved_price(self):
        query_string = f'SELECT Price FROM PriceMap WHERE AlbumId = {self.album_id}'
        query = Query(self.sale.connection, query_string)
        saved_price = query.run()[0]['price']
        return saved_price

    def insert_command_partial(self):
        query_string = f'{self.sale.id}, {self.album_id}, \'{self.price}\''
        return query_string

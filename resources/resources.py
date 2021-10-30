from datetime import datetime

from orm.query import Connection, Query


# Make class to enforce singleton connection object
class Resources:
    def __init__(self):
        self.connection = Connection()

    def songs(self, song_id):
        query_string = self.__query_string('*', 'song', song_id)
        return self.__query(query_string)

    def bands(self, band_id):
        query_string = self.__query_string('*', 'band', band_id)
        return self.__query(query_string)

    def band_create(self, band_name: str):
        return self.__execute(f"INSERT INTO Band (BandName) VALUES ('{band_name}');")

    def band_by_name(self, band_name: str):
        return self.__query(f"SELECT * FROM Band WHERE bandname = '{band_name}';")

    def brand_delete(self, id: int):
        return self.__execute(f"DELETE FROM band WHERE id =  {id}")

    def band_update(self, band_id: int, band_name: str):
        return self.__execute(f"UPDATE Band SET bandname = '{band_name}' WHERE id = '{band_id}'")

    def albums(self):
        query_string = self.__query_string('*', 'album', None)
        return self.__query(query_string)

    def album_create(self, album_name: str, release_date: datetime, band_id: int):
        return self.__execute(f"INSERT INTO Album (AlbumName, ReleaseDate, BandId) VALUES ('{album_name}', '{release_date}', '{band_id}');")

    def album_view(self):
        q_albums = self.__query_string('*', 'album', None)
        q_songs = lambda album_id: f'SELECT * FROM song  WHERE albumid = {album_id}'
        q_artist = lambda band_id: self.__query_string('bandname', 'band', band_id)
        albums = self.__query(q_albums)
        for album in albums:
            artist = self.__query(q_artist(album['bandid']))
            artist = artist[0]['bandname']
            album['artist'] = artist
            songs = self.__query(q_songs(album['id']))
            for song in songs:
                song['releasedate'] = song['releasedate'].isoformat()
            album['songs'] = songs
        return albums

    def album(self, album_id):
        query_string = self.__query_string('*', 'album', album_id)
        return self.__query(query_string)

    def album_delete(self, id):
        return self.__execute(f"DELETE FROM album WHERE id = {id}")

    def album_by_band(self, band_id):
        query_string = self.__query_string('*', 'album', None)
        query_string += f' WHERE bandid = {band_id}'
        return self.__query(query_string)

    def song_by_album(self, album_id):
        query_string = self.__query_string('*', 'song', None)
        query_string += f' WHERE albumid = {album_id}'
        return self.__query(query_string)

    def track_list(self, album_id='', band_id=''):
        query_string = self.__query_string('"Band", "Album", "ReleaseDate", "Track"', 'tracklist', None)
        query_string += f' WHERE "albumid" = {album_id}' if album_id else ''
        query_string += f' WHERE "bandid" = {band_id}' if band_id else ''
        return self.__query(query_string)

    def sales(self):
        q = 'SELECT * FROM sale ORDER BY dateofsale DESC'
        sales = self.__query(q)
        return_data = []
        for sale in sales:
            line_items = self.__query(self.__line_items_query(sale['id']))
            li_hash = []
            for li in line_items:
                li_hash.append({
                    'album_id': li['albumid'],
                    'album_name': li['albumname'],
                    'price': li['price']
                })

            sale_hash = {
                'sale_id': sale['id'],
                'date': sale['dateofsale'].isoformat(),
                'line_items': li_hash
            }
            return_data.append(sale_hash)
        return return_data

    def album_sale_hash(self):
        query_string = f'SELECT al.albumname, p.price FROM album al JOIN pricemap p on al.id = p.albumid;'
        return self.__query(query_string)

    @staticmethod
    def __query_string(params, table, table_id, column='id'):
        q_string = f'SELECT {params} FROM {table}'
        q_string += f' WHERE {column} = {table_id}' if table_id else ''
        return q_string

    def __query(self, query_string):
        q = Query(self.connection, query_string)
        return q.run()

    def __execute(self, query: str):
        Query(self.connection, query).execute_no_return()

    @staticmethod
    def __line_items_query(sale_id):
        query = """
            SELECT
                s.dateOfSale,
                li.albumId,
                album.albumname,
                pm.price
            FROM sale s
            JOIN lineItem li ON li.saleId = s.id
            JOIN album ON album.id = li.albumId
            JOIN priceMap pm ON pm.albumId = li.albumId
        """
        query += f'WHERE s.id = {sale_id}'
        return query



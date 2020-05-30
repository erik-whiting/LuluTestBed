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

    def albums(self, album_id):
        query_string = self.__query_string('*', 'album', album_id)
        return self.__query(query_string)

    def track_list(self, album_id='', band_id=''):
        query_string = self.__query_string('"Band", "Album", "ReleaseDate", "Track"', 'tracklist', None)
        query_string += f' WHERE "albumid" = {album_id}' if album_id else ''
        query_string += f' WHERE "bandid" = {band_id}' if band_id else ''
        return self.__query(query_string)

    @staticmethod
    def __query_string(params, table, table_id):
        q_string = f'SELECT {params} FROM {table}'
        q_string += f' WHERE id = {table_id}' if table_id else ''
        return q_string

    def __query(self, query_string):
        q = Query(self.connection, query_string)
        return q.run()

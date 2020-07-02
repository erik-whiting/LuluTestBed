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

    def albums(self):
        query_string = self.__query_string('*', 'album', None)
        return self.__query(query_string)

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

    @staticmethod
    def __query_string(params, table, table_id):
        q_string = f'SELECT {params} FROM {table}'
        q_string += f' WHERE id = {table_id}' if table_id else ''
        return q_string

    def __query(self, query_string):
        q = Query(self.connection, query_string)
        return q.run()

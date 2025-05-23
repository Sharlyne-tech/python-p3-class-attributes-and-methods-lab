class Song:
    pass
    count = 0
    artists = []
    artist_count = {}
    genres = []
    genre_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre= genre
        Song.add_songs()
        Song.add_to_genres(self)
        Song.add_to_artists(self)

    @classmethod
    def add_songs(cls):
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, self):
        if self.genre not in cls.genres:
            cls.genres.append(self.genre)
            cls.genre_count[self.genre] = 1
        else:
            cls.genre_count[self.genre] += 1  
        
    
    @classmethod
    def add_to_artists(cls, self):
        if self.artist not in cls.artists:
            cls.artists.append(self.artist)
            cls.artist_count[self.artist] = 1
        else:
            cls.artist_count[self.artist] += 1

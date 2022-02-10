from core.reading_loading import artists
from core.reading_loading import albums
from core.reading_loading import songs

def artists():
    return artists

def albums_by_artist(artist_id):
    return artists[artist_id[albums]]

# def ten_most_popular_songs_by_artist(artist_id):
#     artist_albums = artists[artist_id][albums]
#     artist_songs = []
#     for album in albums:
#         album_songs = {}
#         for song in album[songs]:
#             artist_songs.append(song.popularity=song.id)
#     return ten_most_poular_songs

def songs_in_album(album_id):
    return albums[album_id][songs]
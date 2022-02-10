import json
from core import config
from core.music import Artist
from core.music import Album
from core.music import Song

artists = {}
albums = {}
songs = {}

def load_songs():
    with open(config.songs_path + "/song_0C9jZPUv4SuaXkuEQw6L40.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    song = jsonObject["track"]

    song_artists = song["artists"]
    for artist in song_artists:
        artists[artist["id"]] = Artist(artist["id"], artist["name"])
        artists[artist["id"]].__add__(song["album"]["id"])

    song_album = song["album"]
    albums[song_album["id"]] = Album(song_album["id"], song_album["name"])
    albums[song_album["id"]].__add__(song["id"])

    songs[song["id"]] = Song(song["id"], song["name"], song["popularity"])

    return artists, albums, songs
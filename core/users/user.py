from core.users.playlist import Playlist

class User:
  def __init__(self, id, name, is_premuim):
    self.id = id
    self.name = name
    self.is_premuim = is_premuim
    self.playlists_ids = []

  def add_playlist(self, playlist_id, playlist_name):
    Playlist(playlist_id, playlist_name)

  def add_song_to_playlisyt(self, playlist_id, song_id):
    if playlist_id in self.playlists_ids:
      #need to use existing list of playlists
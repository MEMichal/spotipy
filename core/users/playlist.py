class Playlist:
  def __init__(self, id, name):
    self.id = id
    self.name = name
    self.songs_ids = []

    def add_song(song_name):
      import uuid
      song_id = uuid.uuid1()
      self.songs_ids.append(song_id)

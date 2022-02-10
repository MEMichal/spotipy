class Album:
  def __init__(self, id, name):
    self.id = id
    self.name = name
    self.songs_ids = []

  def __add__(self, song_id):
    self.songs_ids.append(song_id)
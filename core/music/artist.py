class Artist:
  def __init__(self, id, name):
    self.id = id
    self.name = name
    self.albums_ids = []

  def __add__(self, album_id):
    self.albums_ids.append(album_id)
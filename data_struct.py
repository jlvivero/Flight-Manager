class Airport(object):
  def __init__(self, id, name):
    self.id = id
    self.name = name

  def id_exist(self, fid):
    return self.id == fid

  def exists(self, airport):
    return self.id_exist(airport.id)

  def change_name(self, new_name):
    self.name = new_name

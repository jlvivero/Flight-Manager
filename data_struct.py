class Airport(object):
  def __init__(self, id, name):
    self.id = id
    self.name = name

  def id_exist(self, fid):
    return self.id == fid

  def exists(self, airport):
    return self.id_exist(airport.id)

  def change_off_value(self, new_name):
    self.name = new_name

class Flight_Str(object):
  def __init__(self,origin,destination,cost):
    self.id = origin + "-" + destination
    self.origin = origin
    self.destination = destination
    self.cost = cost

  def id_exist(self, fid):
    return self.id == fid

  def exists(self, flight):
    return self.id_exist(flight.id)

  def change_off_value(self, new_cost):
    self.cost = new_cost

from pyswip import Prolog, Functor, Variable, Query, call
from pyswip.easy import getList, registerForeign
from flight import Flight

class Prolog_manager(object):
  def __init__(self, file_name):
    self.file_name = file_name
    self.Scales = Variable()
    self.Path = Variable()
    self.Cost = Variable()
    self.assertz = Functor("assertz",1)
    self.vuelos = Functor("vuelos",5)
    self.edge = Functor("edge",3)
    self.prolog = Prolog()
    prolog.consult(self.file_name)

  def add_flight(self, origin, destination, cost):
    call(self.assertz(self.edge(origin,destination,cost)))

  def query_flight_with_scale(self, origin, destination, scales):
    call(self.assertz(self.edge(origin, destination, scales, self.Path, self.Cost)))
    flight = Flight()
    flight_list = []
    while q.nextSolution():
      flight.scale_number = scales
      flight.path_list = [node.chars for node in Path.value]
      flight.cost = Cost.value
      flight_list.append(flight)
    return flight_list

  def query_flight_any_scale(self, origin, destination):
    call(self.assertz(self.edge(origin,destination,self.Scales,self.Path,self.Cost)))
    flight = Flight()
    flight_list = []
    while q.nextSolution():
      flight.scale_number = self.Scales
      flight.path_list = [node.chars for node in Path.value]
      flight.cost = Cost.value
      flight_list.append(flight)
    return flight_list

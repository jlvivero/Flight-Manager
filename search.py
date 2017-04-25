import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from gi.repository import Gdk
from vuelos2 import Prolog_manager
from flight import Flight

class Queries(Gtk.Window):
  def __init__(self, airports, flights):
    Gtk.Window.__init__(self, title = "welcome_screen")
    self.set_size_request(800,600)
    self.set_border_width(5)
    self.grid = Gtk.Grid()
    self.add(self.grid)
    self.grid.props.column_homogeneous = True
    self.grid.props.row_homogeneous = True

    self.airports = airports
    self.flights = flights
    self.title = Gtk.Label("Query")
    self.empty = Gtk.Label(" ")
    self.empty2 = Gtk.Label("write -1 to show all the layovers")
    self.empty3 = Gtk.Label(" ")
    self.manager = Prolog_manager("vuelos2")

    self.origin_label = Gtk.Label("Origin")
    self.destination_label = Gtk.Label("Destination")
    self.layover_label = Gtk.Label("Layover")

    self.layover_entry = Gtk.Entry()

    self.origin_list = Gtk.ListStore(str,str)
    self.origin_list = self.populate_combo2(self.airports)
    self.destination_list = Gtk.ListStore(str,str)
    self.destination_list = self.populate_combo2(self.airports)
    self.origin_box = Gtk.ComboBox.new_with_model_and_entry(self.origin_list)
    self.origin_box.connect("changed", self.origin_change)
    self.origin_box.set_entry_text_column(0)
    self.destination_box = Gtk.ComboBox.new_with_model_and_entry(self.destination_list)
    self.destination_box.connect("changed", self.destination_change)
    self.destination_box.set_entry_text_column(0)

    self.search_button = Gtk.Button(label = "Query")
    self.search_button.connect("clicked",self.start_query)
    self.result_label = Gtk.Label(" ")

    self.grid.attach(self.title,0,0,14,1)
    self.grid.attach(self.empty,0,1,14,1)
    self.grid.attach(self.origin_label,0,2,2,1)
    self.grid.attach(self.origin_box,2,2,4,1)
    self.grid.attach(self.destination_label,7,2,2,1)
    self.grid.attach(self.destination_box,9,2,4,1)
    self.grid.attach(self.empty2,0,3,14,1)
    self.grid.attach(self.layover_label,0,4,2,1)
    self.grid.attach(self.layover_entry,2,4,4,1)
    self.grid.attach(self.empty3,0,5,14,1)
    self.grid.attach(self.search_button,1,6,3,1)
    self.grid.attach(self.result_label,0,7,13,5)
    self.grid.show_all()

    self.origin = None
    self.destination = None

  def origin_change(self, combo):
    tree_iter = combo.get_active_iter()
    if tree_iter != None:
        model = combo.get_model()
        row_id,name = model[tree_iter][:2]
        self.origin = (row_id,name)
        print("Selected: ID=%s, name=%s" % (row_id, name))
    else:
        entry = combo.get_child()
        print("Entered: %s" % entry.get_text())

  def destination_change(self, combo):
    tree_iter = combo.get_active_iter()
    if tree_iter != None:
        model = combo.get_model()
        row_id,name = model[tree_iter][:2]
        self.destination = (row_id, name)
        print("Selected: ID=%s, name=%s" % (row_id, name))
    else:
        entry = combo.get_child()
        print("Entered: %s" % entry.get_text())

  def start_query(self,widget):
    origin_id = self.origin[0]
    destination_id = self.destination[0]
    other_flight = []

    #add all the current existing flights to prolog
    for i in self.flights:
      self.manager.add_flight(i.origin,i.destination, i.cost)

    #TODO: validate that this is an integer
    layover = int(self.layover_entry.get_text())
    if layover >= 0 and layover <= 3:
      other_flight = self.manager.query_flight_with_scale(origin_id,destination_id,layover)
    else:
      other_flight = self.manager.query_flight_any_scale(origin_id,destination_id)
    for i in self.flights:
      self.manager.delete_flight(i.origin,i.destination,i.cost)
    self.populate_answer(other_flight)

  def populate_combo(self, lst):
    temp = Gtk.ListStore(str)
    for i in lst:
      temp.append([i.id])
    return temp

  def populate_combo2(self, lst):
    temp = Gtk.ListStore(str,str)
    for i in lst:
      temp.append([i.id, i.name])
    return temp

  def populate_answer(self, flight_object):
    print "omg"
    answer = ""
    for i in flight_object:
      answer = answer + "path: " + str(i.path_list) + "total cost: " + str(i.cost) + "scale number: " + str(i.scale_number) + "\n"
    print answer
    self.result_label = Gtk.Label(answer)
    for i in range(7,12):
      self.grid.remove_row(7)
    self.grid.attach(self.result_label,0,7,13,5)
    self.grid.show_all()
    #TODO: redraw the grid so that the new label appears

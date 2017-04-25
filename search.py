import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from gi.repository import Gdk
from vuelos2 import Prolog_manager

class Queries(Gtk.Window):
  def __init__(self):
    Gtk.Window.__init__(self, title = "welcome_screen")
    self.set_size_request(800,600)
    self.set_border_width(5)
    self.grid = Gtk.Grid()
    self.add(self.grid)
    self.grid.props.column_homogeneous = True
    self.grid.props.row_homogeneous = True

    self.title = Gtk.Label("Query")
    self.empty = Gtk.Label(" ")
    self.empty2 = Gtk.Label("write -1 to show all the layovers")
    self.empty3 = Gtk.Label(" ")

    self.origin_label = Gtk.Label("Origin")
    self.destination_label = Gtk.Label("Destination")
    self.layover_label = Gtk.Label("Layover")

    self.layover_entry = Gtk.Entry()

    self.origin_list = Gtk.ListStore(str)
    self.origin_list.append(["mxl"])
    self.origin_list.append(["sd"])
    self.destination_list = Gtk.ListStore(str)
    self.destination_list.append(["mxl"])
    self.destination_list.append(["sd"])
    self.origin_box = Gtk.ComboBox.new_with_model_and_entry(self.origin_list)
    self.origin_box.connect("changed", self.origin_change)
    self.origin_box.set_entry_text_column(0)
    self.destination_box = Gtk.ComboBox.new_with_model_and_entry(self.destination_list)
    self.destination_box.connect("changed", self.destination_change)
    self.destination_box.set_entry_text_column(0)

    self.search_button = Gtk.Button(label = "Query")
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

  def origin_change(self, combo):
    tree_iter = combo.get_active_iter()
    if tree_iter != None:
        model = combo.get_model()
        name = model[tree_iter][0]
        print("Selected: name=%s" % (name))
    else:
        entry = combo.get_child()
        print("Entered: %s" % entry.get_text())

  def destination_change(self, combo):
    tree_iter = combo.get_active_iter()
    if tree_iter != None:
        model = combo.get_model()
        name = model[tree_iter][0]
        print("Selected: name=%s" % (name))
    else:
        entry = combo.get_child()
        print("Entered: %s" % entry.get_text())

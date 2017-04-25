import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from gi.repository import Gdk
from crud_window import Crud
from tutorial import Tutorial
from search import Queries

class welcome_screen(Gtk.Window):
  def __init__(self):
    Gtk.Window.__init__(self, title = "welcome_screen")
    self.set_size_request(800,600)
    self.set_border_width(5)
    self.grid = Gtk.Grid()
    self.add(self.grid)
    self.grid.props.column_homogeneous = True
    self.grid.props.row_homogeneous = True
    self.air_list = []
    self.fl_list = []

    #declaration of buttons and texts
    self.add_airport_button = Gtk.Button(label = "Airports")
    self.add_flight_button = Gtk.Button(label = "Flights")
    self.tutorial_button = Gtk.Button(label = "Tutorial")
    self.search_button = Gtk.Button(label = "Search")
    self.add_airport_button.connect("clicked", self.add_airport_clicked)
    self.add_flight_button.connect("clicked", self.add_flight_clicked)
    self.tutorial_button.connect("clicked", self.tutorial)
    self.search_button.connect("clicked", self.search)


    self.grid.attach(self.tutorial_button,1,0,2,1)
    self.grid.attach(self.add_airport_button,1,1,1,1)
    self.grid.attach(self.add_flight_button,2,1,1,1)
    self.grid.attach(self.search_button,1,2,2,1)
    self.grid.show_all()

  def add_airport_clicked(self, widget):
    #self.add_airport_button.props.label = "test"
    airport_window = Crud("airprt",self.air_list,self.fl_list)
    airport_window.connect("delete-event", self.return_lists)
    airport_window.show_all()
    #win.destroy()
  def add_flight_clicked(self, widget):
    #self.add_flight_button.props.label = "test"
    flight_window = Crud("flight",self.air_list,self.fl_list)
    flight_window.connect("delete-event", self.return_lists)
    flight_window.show_all()
    #win.destroy()

  def tutorial(self,widget):
    tutorial_window = Tutorial()
    tutorial_window.connect("delete-event", Gtk.main)
    tutorial_window.show_all()
    #win.destroy()

  def search(self, widget):
    search_window = Queries()
    search_window.connect("delete-event", Gtk.main)
    search_window.show_all()

  def return_lists(self,info_win,b):
    print info_win
    print b
    self.air_list = info_win.air_list
    self.fl_list = info_win.fl_list
    info_win.destroy()


win = welcome_screen()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

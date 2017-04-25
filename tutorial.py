import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from gi.repository import Gdk

class Tutorial(Gtk.Window):
  def __init__(self):
    Gtk.Window.__init__(self, title = "tutorial")
    self.set_size_request(800,600)
    self.set_border_width(5)
    self.grid = Gtk.Grid()
    self.add(self.grid)
    self.grid.props.column_homogeneous = True
    self.grid.props.row_homogeneous = True

    #declaration of texts
    self.explanation = Gtk.Label("tutorial goes here \n yep")
    self.grid.attach(self.explanation,1,1,1,1)
    self.grid.show_all()

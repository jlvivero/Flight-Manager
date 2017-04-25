import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
from gi.repository import Gdk
from data_struct import Airport, Flight_Str
#TODO: add a list of airports and flights, but make sure it's shared on all windows, for now it'll be a local variable
class Crud(Gtk.Window):
  def __init__(self,context):
    Gtk.Window.__init__(self, title = context)
    #change this to be global-ish
    self.air_list = []
    self.fl_list = []

    self.set_size_request(800,600)
    self.set_border_width(5)
    self.grid = Gtk.Grid()
    self.add(self.grid)
    self.action = -1
    #declaration of buttons and texts
    if context == "airprt":
      self.context = "Airport Crud"
    else:
      self.context = "Flight Crud"

    #TODO: fill the combobox with actual values
    ######################airport stuff#########################################
    #airport add
    self.airport_id_label = Gtk.Label("ID")
    self.airport_name_label = Gtk.Label("Name")
    self.airport_id = Gtk.Entry()
    self.airport_save = Gtk.Button(label = "Save")
    self.airport_save.connect("clicked",self.save_changes)
    self.airport_name = Gtk.Entry()

    #airport delete
    self.airport_list = Gtk.ListStore(str, str)
    self.airport_list = self.populate_combo2(self.air_list)
    self.airport_del_combo = Gtk.ComboBox.new_with_model_and_entry(self.airport_list)
    self.airport_del_combo.connect("changed",self.airport_delete_changed)
    self.airport_del_combo.set_entry_text_column(1)

    #aiport modify
    self.airport_mod_list = Gtk.ListStore(str,str)
    self.airport_mod_list = self.populate_combo2(self.air_list)
    self.airport_mod_name_label = Gtk.Label("Name")
    self.airport_mod_name = Gtk.Entry()
    self.airport_combo_box = Gtk.ComboBox.new_with_model_and_entry(self.airport_mod_list)
    self.airport_combo_box.connect("changed",self.airport_combo_changed)
    self.airport_combo_box.set_entry_text_column(1)

    ########################Flight components###################################
    #save button
    self.flight_save = Gtk.Button(label = "Save")
    #add flights
    self.origin_label = Gtk.Label("Origin")
    self.origin_list = Gtk.ListStore(str, str)
    self.origin_list = self.populate_combo2(self.air_list)

    self.flight_cost_label = Gtk.Label("Cost")
    self.flight_cost = Gtk.Entry()

    self.destination_label = Gtk.Label("Destination")
    self.destination_list = Gtk.ListStore(str,str)
    self.destination_list = self.populate_combo2(self.air_list)

    self.origin_combo_box = Gtk.ComboBox.new_with_model_and_entry(self.origin_list)
    self.origin_combo_box.connect("changed", self.origin_change)
    self.origin_combo_box.set_entry_text_column(1)
    self.destination_combo_box = Gtk.ComboBox.new_with_model_and_entry(self.destination_list)
    self.destination_combo_box.connect("changed", self.destination_change)
    self.destination_combo_box.set_entry_text_column(1)

    #delete flight
    self.flight_del_label = Gtk.Label("Flight")
    self.flight_list = Gtk.ListStore(str)
    self.flight_list = self.populate_combo(self.fl_list)

    self.flight_combo_box = Gtk.ComboBox.new_with_model_and_entry(self.flight_list)
    self.flight_combo_box.connect("changed", self.flight_change)
    self.flight_combo_box.set_entry_text_column(0)


    #modify flight
    self.mod_flight_list = Gtk.ListStore(str)
    self.mod_flight_list = self.populate_combo(self.fl_list)
    self.mod_flight_combo = Gtk.ComboBox.new_with_model_and_entry(self.mod_flight_list)
    self.mod_flight_combo.connect("changed", self.flight_mod_change)
    self.mod_flight_combo.set_entry_text_column(0)

    self.mod_cost_label = Gtk.Label("Cost")
    self.mod_cost = Gtk.Entry()


    ########################Normal components###################################
    self.title = Gtk.Label(self.context)
    self.add_button = Gtk.Button(label = "Add")
    self.modify_button = Gtk.Button(label = "Modify")
    self.delete_button = Gtk.Button(label = "Delete")
    self.add_button.connect("clicked", self.adding)
    self.modify_button.connect("clicked", self.modify)
    self.delete_button.connect("clicked", self.delete)
    self.grid.attach(self.title,0,0,3,1)
    self.grid.attach(self.add_button,0,1,1,3)
    self.grid.attach(self.delete_button,1,1,1,3)
    self.grid.attach(self.modify_button,2,1,1,3)

    self.grid.props.column_homogeneous = True
    self.grid.props.row_homogeneous = True
    self.grid.show_all()

  def adding(self, widget):
    self.action = 0
    self.clean_lower_grid()
    if self.context == "Airport Crud":
      self.grid.attach(self.airport_id_label,0,4,1,1)
      self.grid.attach(self.airport_id,1,4,2,1)
      self.grid.attach(self.airport_name_label,0,5,1,1)
      self.grid.attach(self.airport_name,1,5,2,1)
      self.grid.attach(self.airport_save,0,6,3,1)
    else:
      self.grid.attach(self.origin_label,0,4,1,1)
      self.grid.attach(self.origin_combo_box,1,4,2,1)
      self.grid.attach(self.destination_label,0,5,1,1)
      self.grid.attach(self.destination_combo_box,1,5,2,1)
      self.grid.attach(self.flight_cost_label,0,6,1,1)
      self.grid.attach(self.flight_cost,1,6,2,1)
      self.grid.attach(self.flight_save,0,7,3,1)
    self.grid.show_all()

  def modify(self, widget):
    self.action = 1
    self.clean_lower_grid()
    if self.context == "Airport Crud":
      self.grid.attach(self.airport_combo_box,0,4,1,1)
      self.grid.attach(self.airport_mod_name_label,0,5,1,1)
      self.grid.attach(self.airport_mod_name,1,5,1,1)
      self.grid.attach(self.airport_save,0,6,3,1)
    else:
      self.grid.attach(self.mod_flight_combo,0,4,3,1)
      self.grid.attach(self.mod_cost_label,0,5,1,1)
      self.grid.attach(self.mod_cost,1,5,2,1)
      self.grid.attach(self.flight_save,0,6,3,1)
    self.grid.show_all()


  def delete(self, widget):
    self.action = 2
    self.clean_lower_grid()
    if self.context == "Airport Crud":
      self.grid.attach(self.airport_del_combo,0,4,3,1)
      self.grid.attach(self.airport_save,0,6,3,1)
    else:
      self.grid.attach(self.flight_del_label,0,4,1,1)
      self.grid.attach(self.flight_combo_box,1,4,2,1)
      self.grid.attach(self.flight_save,0,6,3,1)
    self.grid.show_all()

  def airport_combo_changed(self, combo):
    #TODO: probably save the resulting tuple on a variable toknow what to modify or something.
    tree_iter = combo.get_active_iter()
    if tree_iter != None:
        model = combo.get_model()
        row_id, name = model[tree_iter][:2]
        print("Selected: ID=%s, name=%s" % (row_id, name))
    else:
        entry = combo.get_child()
        print("Entered: %s" % entry.get_text())

  def airport_delete_changed(self, combo):
    #TODO: probably save the resulting tuple on a variable toknow what to modify or something.
    tree_iter = combo.get_active_iter()
    if tree_iter != None:
        model = combo.get_model()
        row_id, name = model[tree_iter][:2]
        print("Selected: ID=%s, name=%s" % (row_id, name))
    else:
        entry = combo.get_child()
        print("Entered: %s" % entry.get_text())

  def destination_change(self, combo):
    tree_iter = combo.get_active_iter()
    if tree_iter != None:
        model = combo.get_model()
        row_id, name = model[tree_iter][:2]
        print("Selected: ID=%s, name=%s" % (row_id, name))
    else:
        entry = combo.get_child()
        print("Entered: %s" % entry.get_text())

  def origin_change(self, combo):
    tree_iter = combo.get_active_iter()
    if tree_iter != None:
        model = combo.get_model()
        row_id, name = model[tree_iter][:2]
        print("Selected: ID=%s, name=%s" % (row_id, name))
    else:
        entry = combo.get_child()
        print("Entered: %s" % entry.get_text())

  def flight_change(self, combo):
    tree_iter = combo.get_active_iter()
    if tree_iter != None:
        model = combo.get_model()
        name = model[tree_iter][0]
        print("Selected: name=%s" % (name))
    else:
        entry = combo.get_child()
        print("Entered: %s" % entry.get_text())

  def flight_mod_change(self, combo):
    tree_iter = combo.get_active_iter()
    if tree_iter != None:
        model = combo.get_model()
        name = model[tree_iter][0]
        print("Selected: name=%s" % (name))
    else:
        entry = combo.get_child()
        print("Entered: %s" % entry.get_text())

  def clean_lower_grid(self):
    for i in range(4,8):
      self.grid.remove_row(4)

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

  def update_boxes(self):
    self.airport_list = self.populate_combo2(self.air_list)
    self.airport_mod_list = self.populate_combo2(self.air_list)
    self.origin_list = self.populate_combo2(self.air_list)
    self.destination_list = self.populate_combo2(self.air_list)
    self.flight_list = self.populate_combo(self.fl_list)
    self.mod_flight_list = self.populate_combo(self.fl_list)
    
    self.airport_del_combo = Gtk.ComboBox.new_with_model_and_entry(self.airport_list)
    self.airport_combo_box = Gtk.ComboBox.new_with_model_and_entry(self.airport_mod_list)
    self.origin_combo_box = Gtk.ComboBox.new_with_model_and_entry(self.origin_list)
    self.destination_combo_box = Gtk.ComboBox.new_with_model_and_entry(self.destination_list)
    self.flight_combo_box = Gtk.ComboBox.new_with_model_and_entry(self.flight_list)
    self.mod_flight_combo = Gtk.ComboBox.new_with_model_and_entry(self.mod_flight_list)

    self.airport_del_combo.set_entry_text_column(1)
    self.airport_combo_box.set_entry_text_column(1)
    self.origin_combo_box.set_entry_text_column(1)
    self.destination_combo_box.set_entry_text_column(1)
    self.flight_combo_box.set_entry_text_column(0)
    self.mod_flight_combo.set_entry_text_column(0)

  def save_changes(self,widget):
    if self.context == "Airport Crud":
      self.air_save()
    else:
      self.flight_save()

  def air_save(self):
    if self.action == 0:
      self.air_add()
    elif self.action == 1:
      self.air_mod()
    else:
      self.air_del()
  def flight_save(self):
    if self.action == 0:
      self.flight_add()
    elif self.action == 1:
      self.flight_mod()
    else:
      self.flight_del()

  def air_add(self):
    a_id = self.airport_id.get_text()
    a_name = self.airport_name.get_text()
    airport = Airport(a_id,a_name)
    exists = False
    for air in self.air_list:
      if air.exists(airport):
        exists = True
    if not exists:
      self.air_list.append(airport)
    print self.air_list
    self.update_boxes()

  def air_mod(self):
    new_name = self.airport_mod_name.get_text()
    #TODO: change fake val to the actual value chosen from the combobox
    fake_val = "mxl"
    ln = len(self.air_list)
    for i in range(ln):
      if self.air_list[i].id_exist(fake_val):
        self.air_list[i].change_off_value(new_name)
        break
    self.update_boxes()
    print self.air_list

  def air_del(self):
    #TODO: change fake val to the actual value chosen from the combobox
    fake_val = "mxl"
    ln = len(self.air_list)
    for i in range(ln):
      if self.air_list[i].id_exist(fake_val):
        del self.air_list[i]
        break
    self.update_boxes()
    print self.air_list

  def flight_add(self):
    #TODO: maybe make a subroutine of this so that you don't repeat yourself with flight/airports
    fake_val1 = Airport("mxl","mexicali")
    fake_val2 = Airport("sd", "San Diego")
    #TODO: validate that flight cost is a number
    new_cost = int(self.flight_cost.get_text())
    flight = Flight_Str(fake_val1,fake_val2,100)
    exist = False
    for flight in self.fl_list:
      if flight.exists(flight):
        exists = True
    if not exists:
      self.fl_list.append(flight)
    self.update_boxes()
    print self.fl_list

  def flight_mod(self):
    fake_flight_id = "mxl-sd"
    #TODO: validate that the cost is a number
    new_cost = int(self.mod_cost.get_text())
    ln = len(self.fl_list)
    for i in range(ln):
      if self.ln_list[i].id_exist(fake_flight_id):
        self.ln_list[i].change_off_value(new_cost)
        break
    self.update_boxes()
    print self.fl_list

  def flight_del(self):
    fake_val = "mxl-sd"
    ln = len(self.fl_list)
    for i in range(ln):
      if self.fl_list[i].id_exist(fake_val):
        del self.fl_list[i]
        break
    self.update_boxes()
    print self.fl_list

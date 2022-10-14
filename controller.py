import gui
import math_f
import db


def button_click():
    global name
    global surname
    global mobile
    type=gui.var_of_operation()
    if type=='w':
        name = gui.get_value_name()
        surname = gui.get_value_surname()
        mobile = gui.get_value_mobile()
        math_f.init(name, surname, mobile)
        result = gui.type_of_operation()
    elif type=='f':
        name = gui.get_value_name()
        db.find_in_db(name)
   

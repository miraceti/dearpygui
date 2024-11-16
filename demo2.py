import dearpygui.dearpygui as dpg

def save_callback1():
    print("Save Clicked")

def save_callback2():
    print("Save Clicked")

dpg.create_context()
dpg.create_viewport(title='mon titre', width=500, height=500)
dpg.setup_dearpygui()

with dpg.window(label="Example Window", pos=(100,50)):
    dpg.add_text("Hello world")
    dpg.add_button(label="Save", callback=save_callback1)
    dpg.add_input_text(label="string")
    dpg.add_slider_float(label="float")

with dpg.window(label="Example Window", pos=(300,100)):
    dpg.add_text("Hello world")
    dpg.add_button(label="Save", callback=save_callback2)
    dpg.add_input_text(label="string")
    dpg.add_slider_float(label="float")


dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
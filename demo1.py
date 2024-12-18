import dearpygui.dearpygui as dpg

def save_callback():
    print("Save Clicked")


dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.window(label="Example Window"):
    dpg.add_text("Hello, world")
    dpg.add_button(label="Save", callback=save_callback)
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
import dearpygui.dearpygui as dpg

from urllib.request import urlopen
import json

urlexo1 = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+count(pl_name)+as+nbe+from+ps+where+default_flag=1&format=json"
print(urlexo1)
data = json.loads(urlopen(urlexo1).read().decode("utf-8"))
# print(data)
data0=data[0]
# print(data0)
nb_exoplanets= data0['nbe']
print(nb_exoplanets)

urlexo7 = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+\
pl_name,hostname,pl_letter,pl_bmasse,pl_bmassj,pl_rade,pl_radj,pl_orbper,pl_dens,pl_trandur,pl_ratror,\
sy_snum,sy_pnum,sy_mnum,st_mass,st_lum,st_age,st_dens,sy_dist,disc_year,disc_telescope,discoverymethod,\
releasedate\
+from+ps+where+default_flag=1&format=json"

print(urlexo7)
list7 = json.loads(urlopen(urlexo7).read().decode("utf-8"))

dist0 = 100000
p1 ="vide"
p=0
planete_dist=[]
for planete in list7:
    if planete['sy_dist'] is None: 
        pass
    else:
        p+=1
        planete_dist.append((planete['pl_name'],planete['sy_dist'],planete['pl_bmasse'], planete['pl_rade'], planete['pl_dens']))
        if planete['sy_dist'] < dist0:
           p1 = planete['pl_name']
           dist0 =  planete['sy_dist']
        
sorted_list = sorted(planete_dist, key= lambda x: x[1])

masse_rayon = [(t[2],t[3]) for t in sorted_list if t[2] is not None and t[3] is not None]
print(masse_rayon)

liste_masse = [t[0] for t in masse_rayon]
liste_rayon = [t[1] for t in masse_rayon]

liste_masse_min, liste_masse_max = min(liste_masse), max(liste_masse)
liste_rayon_min, liste_rayon_max = min(liste_rayon), max(liste_rayon)

print(f"masse min : {liste_masse_min} , masse max : {liste_masse_max}")
print(f"rayon min : {liste_rayon_min} , rayon max : {liste_rayon_max}")

dpg.create_context()

def print_val(sender):
    print(dpg.get_value(sender))

with dpg.window(label="tools",width=100, height=100, collapsed=True) :
			#Create a menu bar with debugging tools
			with dpg.menu_bar(): 
				with dpg.menu(label="Tools") :
					dpg.add_menu_item(label="Show Debug", callback=lambda:dpg.show_tool(dpg.mvTool_Debug))
					dpg.add_menu_item(label="Show Font Manager", callback=lambda:dpg.show_tool(dpg.mvTool_Font))
					dpg.add_menu_item(label="Show Item Registry", callback=lambda:dpg.show_tool(dpg.mvTool_ItemRegistry))
					dpg.add_menu_item(label="Show Metrics", callback=lambda:dpg.show_tool(dpg.mvTool_Metrics))
					dpg.add_menu_item(label="Toggle Fullscreen", callback=lambda:dpg.toggle_viewport_fullscreen())
					
with dpg.window(label="Tutorial", width=200, height=200, collapsed=True,pos=(100,0)):
    with dpg.plot(label="Drag Lines/Points", height=-1, width=-1):
        dpg.add_plot_legend()
        dpg.add_plot_axis(dpg.mvXAxis, label="x")
        dpg.set_axis_limits(dpg.last_item(), -5, 5)
        dpg.add_plot_axis(dpg.mvYAxis, label="y")
        dpg.set_axis_limits(dpg.last_item(), -5, 5)

        # drag lines/points belong to the plot NOT axis
        dpg.add_drag_line(label="dline1", color=[255, 0, 0, 255], default_value=2.0, callback=print_val)
        dpg.add_drag_line(label="dline2", color=[255, 255, 0, 255], vertical=False, default_value=-2, callback=print_val)
        dpg.add_drag_point(label="dpoint1", color=[255, 0, 255, 255], default_value=(1.0, 1.0), callback=print_val)
        dpg.add_drag_point(label="dpoint2", color=[255, 0, 255, 255], default_value=(-1.0, 1.0), callback=print_val)
        dpg.add_drag_point(label="dpoint3", color=[255, 0, 0, 255], default_value=(-1.0, -1.0), callback=print_val)

with dpg.window(label="simple plot", width=500, height=500,pos=(0,50),collapsed=True):
    dpg.add_simple_plot(label="Simpleplot1", default_value=(0.3, 0.9, 0.5, 0.3), height=300)
    dpg.add_simple_plot(label="Simpleplot2", default_value=(0.3, 0.9, 2.5, 8.9), overlay="Overlaying", height=180,
                        histogram=True)

with dpg.window(label="Example001", width=200, height=200, collapsed=True, pos=(300,0)):
    with dpg.plot(label="Drag Lines/Points", height=-1, width=-1):
        dpg.add_plot_legend()
        dpg.add_plot_axis(dpg.mvXAxis, label="fois masse terre")
        dpg.set_axis_limits(dpg.last_item(), 0, 1000)
        dpg.add_plot_axis(dpg.mvYAxis, label="fois rayon terre")
        dpg.set_axis_limits(dpg.last_item(), 0, 20)

        # drag lines/points belong to the plot NOT axis
        dpg.add_drag_line(label="dline1", color=[255, 0, 0, 255], default_value=2.0, callback=print_val)
        dpg.add_drag_line(label="dline2", color=[255, 255, 0, 255], vertical=False, default_value=-2, callback=print_val)
        dpg.add_drag_point(label="dpoint1", color=[255, 0, 255, 255], default_value=(1.0, 1.0), callback=print_val)
        dpg.add_drag_point(label="dpoint2", color=[255, 0, 255, 255], default_value=(-1.0, 1.0), callback=print_val)
        dpg.add_drag_point(label="dpoint3", color=[255, 0, 0, 255], default_value=(-1.0, -1.0), callback=print_val,no_inputs=True)#point non deplacable
        n=1
        for i,j in masse_rayon:
              n=n+1
              dpg.add_drag_point(label="dpoint_"+str(n), color=[255, 0, 0, 255], default_value=(i, j),no_inputs=True)



dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
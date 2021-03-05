import subprocess
import tkinter as tk


'''creates simple gui to excute Kibanna'''

root= tk.Tk() 
   
canvas_el = tk.Canvas(root, width = 350, height = 250) 
canvas_el.pack()
path_kibanna = r'C:\Users\jeron\OneDrive\Desktop\university\CE306\Elastic_search\kibana-7.10.2-windows-x86_64\bin\kibana.bat'

def start_kibanna(path=path_kibanna): 
       
       root.destroy()
       subprocess.call([path]),        

button_1 = tk.Button (
                     root, 
                     text='Run Kibanna ',
                     command=start_kibanna,
                     bg='blue',fg='white')

canvas_el.create_window(170, 130, window=button_1)

root.mainloop()
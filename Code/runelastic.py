import subprocess
import tkinter as tk

root= tk.Tk() 
   
canvas_el = tk.Canvas(root, width = 350, height = 250) 
canvas_el.pack()
path_elastic=r'C:\Users\jeron\OneDrive\Desktop\university\CE306\Elastic_search\elasticsearch-7.10.2\bin\elasticsearch.bat'
path_kibanna = r'C:\Users\jeron\OneDrive\Desktop\university\CE306\Elastic_search\kibana-7.10.2-windows-x86_64\bin\kibana.bat'

def start_elastic(path=path_elastic): 
       root.destroy()
       subprocess.call([path])
               
button_1 = tk.Button (root, text='Run Elastic Search ',command=start_elastic,bg='blue',fg='white')
canvas_el.create_window(170, 130, window=button_1)


root.mainloop()
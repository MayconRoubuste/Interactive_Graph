import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#create the 'window' and the text boxes to insert text as well as the graph type selection
root = tk.Tk()
root.title('Graph generator')
root.geometry('500x500')

label = tk.Label(root, text='Insert the data for the graph separated by comas: ')
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

label_type = tk.Label(root, text='Select the type of graph you desire: ')
label_type.pack(pady=10)

graph_type = ['lines', 'bars', 'scatter', 'pie']
combobox = ttk.Combobox(root, values=graph_type)
combobox.set('lines')
combobox.pack(pady=5)


but = tk.Button(root, text='Create Graph', command=lambda: create_graphs((entry.get())))
but.pack(pady=20)

# This function create the graphs
def create_graphs(data):
    try:
        data = list(map(float, data.split(',')))
        if not data:
            raise ValueError('No data found')
    except ValueError as e:
        return

    type1 = combobox.get()
    fig, ax = plt.subplots()

    if type1 == 'lines':
        ax.plot(data)
    elif type1 == 'bars':
        ax.bar(range(len(data)), data)
    elif type1 == 'scatter':
        ax.scatter(range(len(data)), data)
    elif type1 == 'pie':
        ax.pie(data, labels=[f'item {i+1}' for i in range(len(data))])

# Final integration
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

#Loops the code
root.mainloop()
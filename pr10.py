from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import Menu
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter.ttk import Radiobutton

window = Tk()
window.title("Вдовиков Александр Витальевич")
window.geometry('1280x720')

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control) 
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text = '1')
tab_control.add(tab2, text = '2')
tab_control.add(tab3, text = '3')
tab_control.pack(expand = 1, fill = 'both')

def clicked1():
    t = 0
    x = number1.get()
    y = number2.get()
    v = combo.get()
    if v == '+':
        t =  int(x) + int(y)
    elif v == '-':
        t = int(x) - int(y)
    elif v == '*':
        t = int(x) * int(y)
    elif v == '/':
        t = int(x) / int(y)
    lbl1['text'] = t
 
btn1 = Button(tab1, text = '=', command = clicked1)
btn1.grid(column = 3, row = 0)

combo = Combobox(tab1)
combo['values'] = ('+', '-', '*', '/')
combo.grid(column = 1, row = 0)
combo.current(0)

lbl1 = Label(tab1, text = '')
lbl1.grid(column = 4, row = 0) 

number1 = Entry(tab1, width = 5)                 
number1.grid(column= 0, row = 0)
number2 = Entry(tab1, width = 5)
number2.grid(column= 2, row = 0)

def clicked2():                                                                                       
    messagebox.showerror('Результат', 'Вы выбрали ' + str(selected.get()) + ' вариант ответа')                                  

selected = StringVar()
rad1 = Radiobutton(tab2, text = '1', value = 'первый', variable = selected)
rad2 = Radiobutton(tab2, text = '2', value = 'второй', variable = selected)
rad3 = Radiobutton(tab2, text = '3', value = 'третий', variable = selected)
rad1.grid(column = 0, row = 1)
rad2.grid(column = 0, row = 2)
rad3.grid(column = 0, row = 3)
btn2 = Button(tab2, text = 'Далее', command = clicked2)
btn2.grid(column = 0, row = 4)

txt = scrolledtext.ScrolledText(tab3, width = 70, height = 70)                      
txt.grid(column =  0, row = 0)

def clicked3():
    txt.delete('1.0', END)
    u = filedialog.askopenfilename(filetypes = (("Text files", "*.txt"),("All files", "*.*")))
    file = open(u, 'r')
    lines = file.readlines()
    row = len(lines)
    for i in range(row):
        txt.insert(INSERT, lines[i]) 

menu = Menu(tab3)
new_item = Menu(menu)
menu.add_cascade(label = 'Меню', menu = new_item)
new_item.add_command(label = 'Загрузить файл', command = clicked3)
new_item.add_separator() 
window.config(menu = menu) 

window.mainloop() 
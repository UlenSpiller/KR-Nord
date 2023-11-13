import os
import tkinter as tk
from tkinter import Checkbutton
from tkinter import Label
from tkinter import filedialog
from procedures5 import BDP

file_name = None  # Объявляем переменную как глобальную

def open_file_dialog():
    global file_name
    # global name_xml
    file_path = filedialog.askopenfilename(filetypes=[("XML files", "*.xml")])
    if file_path:
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        name_xml = file_path  # Сохраняем путь к файлу XML
        print(f"Выбран файл: {file_path}")
        print(f"Имя файла без расширения: {file_name}")
        selected_file_label.config(text=f"Selected File: {file_name}.xml")  # Обновляем Label с именем файла
    # return file_name

def start_execution(file_name):
    name_db = file_name + '.db'  # Объявляем переменные name_db, name_xml и name_new_xml
    name_xml = file_name + '.xml'
    name_new_xml = file_name + '_new.xml'
    print('name_db= ', name_db )
    print('name_xml', name_xml)
    print('name_new_xml',name_new_xml)

    BDP.delete_temp_db(name_db)
    BDP.create_table(name_db)
    BDP.pars_file(name_db, name_xml)
    # Проверяем состояние чекбокса, если активирован, выполняем rotate_ang
    if checkbox_state.get() == 1:
        BDP.rotate_ang(name_db)
    BDP.make_new_xml(name_db, name_new_xml)
    print("Execution completed.")


root = tk.Tk()
root.geometry('400x200')
root.title("Optimization of the cutting sheet")

selected_file_label = Label(root, text="Selected File: no file selected", font=("Helvetica", 9))  # Label для выбранного файла
selected_file_label.grid(row=0, column=1, padx=10, pady=10)

button_select = tk.Button(root, text="Select XML file", command=open_file_dialog)
button_select.grid(row=0, column=0, padx=10, pady=10)


button_start = tk.Button(root, text="Start Execution", command=lambda: start_execution(file_name))
button_start.grid(row=1, column=0, padx=10, pady=10)

# Создайте переменную для состояния чекбокса
checkbox_state = tk.IntVar()
# Создайте чекбокс и свяжите его с переменной состояния
checkbox = Checkbutton(root, text="Execute rotate_ang", variable=checkbox_state)
checkbox.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()

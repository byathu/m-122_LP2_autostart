# Hilf bei starten des Apps
import os
import re as re
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

root = tk.Tk()
save_file_directory = os.path.dirname(os.path.abspath(__file__)) + "\\templates\\"

root.title("Autostart")
name = "Create Template"


def deleteApp():
    global name

    for widget in frame.winfo_children():
        widget.destroy()

    e1.delete(0, "end")
    dropdown.delete(0, "end")

    name = "Create Template"


def show_apps(apps):
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def get_apps():
    path = "templates\\" + e1.get()
    if os.path.isfile(path):
        with open(path, "r") as f:
            tempApps = f.read()
            tempApps = tempApps.split(",")
            # Entfernt alle leerschläge
            return [x for x in tempApps if x.strip()]


def loadFile():
    global name

    e1.insert(0, dropdown.get())
    show_apps(get_apps())


def CreateTemplate():
    if e1.get() == '':
        label = tk.Label(frame,
                         text="Du hast noch keinen name für dein Template ausgesucht \n Erstelle noch mals einen Template",
                         bg="gray")
        label.pack()
        return
    else:
        addApp()


def addApp():
    if e1.get() == '':
        label = tk.Label(frame, text="Du hast noch keinen Template ausgesucht \n Wähle ein Template",
                         bg="gray")
        label.pack()
        return

    match = re.findall("(\w)", e1.get())
    if len(match) != len(e1.get()):
        label = tk.Label(frame, text="Invalid filename",
                         bg="gray")
        label.pack()
        return

    # Löscht das Text file und wiederherstelltes mit dem hinzugefügten damit es nicht Doppelt angezwigt wird.
    for widget in frame.winfo_children():
        widget.destroy()

    # Man kan nur Ausführbare datein anwenden.
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))

    apps = get_apps() if get_apps() is not None else []
    apps.append(filename)

    show_apps(apps)

    with open(save_file_directory + e1.get(), "w") as f:
        for app in apps:
            f.write(app + ",")


def runapp():
    for app in get_apps():
        os.startfile(app)


canvas = tk.Canvas(root, height=500, width=500, bg="#A9BCF5")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.76, relx=0.1, rely=0.1)

Createtemplate = tk.Button(root, text="Create Template", padx=8, pady=8, fg="black", bg="#A9BCF5",
                           command=CreateTemplate)
Createtemplate.place(x=50, y=455)

openFile = tk.Button(root, text="Add App", padx=8, pady=8, fg="black", bg="#A9BCF5", command=addApp)
openFile.place(x=163, y=455)

openFile = tk.Button(root, text="LoadFile", padx=8, pady=8, fg="black", bg="#A9BCF5", command=loadFile)
openFile.place(x=235, y=455)

runApp = tk.Button(root, text="Start App", padx=8, pady=8, fg="black", bg="#A9BCF5", command=runapp)
runApp.place(x=305, y=455)

deleteApp = tk.Button(root, text="Delete All", padx=8, pady=8, fg="black", bg="#A9BCF5", command=deleteApp)
deleteApp.place(x=380, y=455)

dropdown = ttk.Combobox(root, values=[f for f in os.listdir(save_file_directory)])
dropdown.pack()

TemplateName = tk.Label(root, text="Template Name", padx=11, pady=1, fg="black", bg="#A9BCF5")
TemplateName.pack()
TemplateName.place(x=50, y=30)

e1 = tk.Entry(root)
e1.place(x=160, y=30)

root.mainloop()

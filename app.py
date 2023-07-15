from tkinter import *
from tkinter import ttk

import os

class Monitor:
    def __init__(self, name) -> None:
        self.name = name
        self.file = self.name + ".config"

    def up(self):
        if os.path.isfile(self.file):
            value = 50
            with open(self.file, "r") as f:
                v = int(f.readline())

                if isinstance(v, int):
                    if v < 90:
                        v += 10
                        with open(self.file, "w") as f:
                            f.write(str(v))
                        os.system("xrandr --output " + self.name + " --brightness "+str(v/100))

        else:
            os.system("xrandr --output " + self.name + " --brightness 0.5")
            with open(self.file, "w") as f:
                f.write("50")

    def down(self):
        if os.path.isfile(self.file):
            value = 50
            with open(self.file, "r") as f:
                v = int(f.readline())

                if isinstance(v, int):
                    if v > 10:
                        v -= 10
                        with open(self.file, "w") as f:
                            f.write(str(v))
                        os.system("xrandr --output " + self.name + " --brightness "+str(v/100))
                        

        else:
            os.system("xrandr --output " + self.name + " --brightness 0.5")
            with open(self.file, "w") as f:
                f.write("50")



    def __str__(self):
        return self.name


def listMonitors():
    command = 'xrandr -q | grep " connected"'
    mnt = os.popen(command).read().splitlines()
    monitors = []
    for m in mnt:
        name = m.split()[0]
        monitors.append(Monitor(name))
    return monitors


monitors = listMonitors()
m1 = monitors[0]
m2 = monitors[1]


root = Tk()
root.title = "Brightless"
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text=m1.name, padding=3).grid(column=0, row=0)
ttk.Button(frm, text="UP", command=m1.up).grid(column=1, row=0)
ttk.Button(frm, text="DOWN", command=m1.down).grid(column=2, row=0)

ttk.Label(frm, text=m2.name, padding=3).grid(column=0, row=1)
ttk.Button(frm, text="UP", command=m2.up).grid(column=1, row=1)
ttk.Button(frm, text="DOWN", command=m2.down).grid(column=2, row=1)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2)
root.mainloop()
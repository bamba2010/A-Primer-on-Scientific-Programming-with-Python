
import tkinter
root = tkinter
C_entry = tkinter.Entry(root, width=4)
C_entry.pack(side="left")
Cunit_label = label(root, text ="Celsius")
Cunit_label.pack(side="left")
def compute():
    C =float(C_entry.get())
    F = (9./5)*C +32
    F_label.configure(text='%g' %F)
compute = Buttom (root, text='is', command = compute)
compute.pack(side ='left',padx=4)

F_label =Label(root, width =4)
F_label.pack(side ='left')
Funit_label = Label(root, text ='Fahrenheit')
Funit_label.pack (side ='left')
root.mainloop()
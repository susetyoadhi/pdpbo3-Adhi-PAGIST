from tkinter import *

root = Tk()
root.title("PAGIST")

main = LabelFrame(root, text="Input Data", padx=10, pady=10, borderwidth = 5)
main.grid(row = 0, column = 0, padx = 10, pady = 10)

side = LabelFrame(root, relief = "flat")
side.grid(row = 0,column = 1, padx = 10, pady = 10, sticky = "ns")

# input text
L1 = Label(main, text = "Nama",anchor = "w", width = 7).grid(row = 0, column = 0)
L2 = Label(main, text = "TTL",anchor = "w", width = 7).grid(row = 1, column = 0)
L3 = Label(main, text = "Alamat",anchor = "w", width = 7).grid(row = 2, column = 0)
L4 = Label(main, text = ":",width = 2).grid(row = 0, column = 1)
L5 = Label(main, text = ":",width = 2).grid(row = 1, column = 1)
L6 = Label(main, text = ":",width = 2).grid(row = 2, column = 1)
E1 = Entry(main, bd = 5, width = 30).grid(row = 0, column = 2)
E2 = Entry(main, bd = 5, width = 30).grid(row = 1, column = 2)
E3 = Entry(main, bd = 5, width = 30).grid(row = 2, column = 2)
L9 = Label(main, text = "Spesialis",anchor = "w", width = 7).grid(row = 3, column = 0)
L10 = Label(main, text = ":",width = 2).grid(row = 3, column = 1)

# def untuk about
def about():
    top = Toplevel()
    top.title("About")

    a_frame = LabelFrame(top, text="", padx=10, pady=10, relief = "flat")
    a_frame.pack(padx=10, pady=10)

    a_app = Label(a_frame, text = "Patient Registration System",font = ("arial", 15), fg = "#194350").grid(row = 0)
    a_desc = Label(a_frame, text="Adalah sebuah aplikasi yang digunakan untuk memasukkan data pasien di dalam rumah sakit", anchor = "w").grid(row=1, column=0, sticky="w")
    a_nama = Label(a_frame, text="Developer : ", anchor = "w").grid(row=2, column=0, sticky="w")
    a_nama = Label(a_frame, text="Adhi Susetyo P", anchor = "w").grid(row=3, column=0, sticky="w")
    a_nim = Label(a_frame, text="1903287", anchor = "w").grid(row=4, column=0, sticky="w")

# def untuk exit
def exit():
    top = Toplevel()
    top.title("Exit Confirmation")

    a = LabelFrame(top,text = "", padx=10, pady=10, relief = "flat")
    a.pack(padx=10, pady=5)

    a_text = Label(a, text = "Are You Sure Want To Quit?").grid(row=0, column=0, sticky="w")
    opts = LabelFrame(top, padx=10, pady=10, relief = "flat")
    opts.pack(padx=10, pady=5)

    b_yes = Button(opts, text = "YES", command = root.quit).grid(row = 1, column = 0, padx = 3)
    b_no = Button(opts, text = "NO", command = top.destroy).grid(row = 1, column = 1, padx = 3)

# dropdown menu
def show():
    print(clicked.get())
clicked = StringVar(root)
choices = {"Ginjal", "Paru", "Jantung", "Anak"}
clicked.set("Ginjal")
drop = OptionMenu(main, clicked, *choices)
drop.grid(row = 3, column = 2, sticky = "ew")
clicked.trace = ("w", show)

L11 = Label(main, text = "gaktau",anchor = "w", width = 7).grid(row = 4, column = 0)
L12 = Label(main, text = ":",width = 2).grid(row = 4, column = 1)

# checkbox
box = LabelFrame(main, relief = "flat")
box.grid(row = 4, column = 2)
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
c1 = Checkbutton(box, text = "apa", variable = var1, onvalue = 1, offvalue = 0,).grid(row = 4, column = 2)
c2 = Checkbutton(box, text = "tuh", variable = var2, onvalue = 1, offvalue = 0).grid(row = 4, column = 3)
c3 = Checkbutton(box, text = "hayo", variable = var3, onvalue = 1, offvalue = 0).grid(row = 4, column = 4)

# radiobutton
radio = LabelFrame(main, relief = "flat")
radio.grid(row = 5, column = 2)
L13 = Label(main, text = "Kelamin",anchor = "w", width = 7).grid(row = 5, column = 0)
L14 = Label(main, text = ":",width = 2).grid(row = 5, column = 1)
var = IntVar()
r1 = Radiobutton(radio, text = "wanita", variable = var, value = 1).grid(row = 5, column = 2)
r2 = Radiobutton(radio, text = "Pria", variable = var, value = 2).grid(row = 5, column = 4)

#side menu
L7 = Label(side, text = "Patient Registration System",font = ("arial", 15), fg = "#194350").grid(row = 0)
L8 = Label(side, text = "System for registering patient data in hospital", anchor = "w", width = 35).grid(row = 1)
L15 = Label(side, text = "\n", anchor = "w", width = 35).grid(row = 2)
L16 = Label(side, text = "\n", anchor = "w", width = 35).grid(row = 3)

# button open dan submit dan exit
btn_opn = Button(root, text = "Open Photo File", state = "disabled", relief = "ridge", bd = 5).grid(row = 1, sticky = "ew", padx = 10)
btn_submit = Button(root, text = "Submit",relief = "ridge", bd = 5).grid(row = 2, sticky = "ew", padx = 10, pady = 5)
btn_exit = Button(root, text = "Exit",relief = "ridge", bd = 5, command = exit).grid(row = 2, column = 1, sticky = "ew", padx = 10, pady = 5)

    
# side button
btn_opn = Button(side, text = "see all submission",relief = "ridge", bd = 5).grid(row = 5, sticky = "ew", padx = 10, pady = 1)
btn_clr = Button(side, text = "clear submission",relief = "ridge", bd = 5).grid(row = 6, sticky = "ew", padx = 10, pady = 1)
btn_about = Button(side, text = "about",relief = "ridge", bd = 5, command = about).grid(row = 7, sticky = "ew", padx = 10, pady = 1)

root.mainloop()
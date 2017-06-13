from tkinter import *
from PIL import Image, ImageTk
import functions

class MainWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("pyTicket")

# CONTEXT MENU ###############################################
        self.menu = Menu(self.parent, tearoff=0)
        self.menu.add_command(label="Beep", command=self.bell)
        self.menu.add_command(label="Exit", command=self.onExit)

        self.parent.bind("<Button-3>", self.showMenu)
        self.pack()
# CONTEXT MENU ###############################################

# FILE MENU ##################################################
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar, tearoff=False)

        submenu = Menu(fileMenu, tearoff=False)
        submenu.add_command(label="New feed")
        submenu.add_command(label="Bookmarks")
        submenu.add_command(label="Mail")
        fileMenu.add_cascade(label='Import', menu=submenu, underline=0)

        fileMenu.add_separator()

        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)
# FILE MENU ##################################################

# TOOLBAR ####################################################
        toolbar = Frame(self.parent, bd=1, relief=RAISED)

        self.img = Image.open("Icons\create_new.png")
        eimg = ImageTk.PhotoImage(self.img)
        newButton = Button(toolbar, text="New ", image=eimg, compound="left", relief=RAISED, command=self.quit)
        newButton.image = eimg
        newButton.pack(side=LEFT, padx=2, pady=2)

        self.img = Image.open("Icons\edit.png")
        eimg = ImageTk.PhotoImage(self.img)
        editButton = Button(toolbar, text="Edit ", image=eimg, compound="left", relief=RAISED, command=self.quit)
        editButton.image = eimg
        editButton.pack(side=LEFT, padx=2, pady=2)

        self.img = Image.open("Icons\list_all.png")
        eimg = ImageTk.PhotoImage(self.img)
        list_allButton = Button(toolbar, text="List All ", image=eimg, compound="left", relief=RAISED, command=functions.ListAllTickets)
        list_allButton.image = eimg
        list_allButton.pack(side=LEFT, padx=2, pady=2)

        self.img = Image.open("Icons\exit.png")
        eimg = ImageTk.PhotoImage(self.img)
        exitButton = Button(toolbar, text="Exit ", image=eimg, compound="left", relief=RAISED, command=self.quit)
        exitButton.image = eimg
        exitButton.pack(side=RIGHT, padx=2, pady=2)

        self.img = Image.open("Icons\startupcheck.png")
        eimg = ImageTk.PhotoImage(self.img)
        startupButton = Button(toolbar, text="Re-Check ", image=eimg, compound="left", relief=RAISED, command=self.StartUpChecker)
        startupButton.image = eimg
        startupButton.pack(side=RIGHT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X)

        self.parent.config(menu=menubar)
        self.pack(anchor=N, side=TOP, fill=X, expand=False)
# TOOLBAR ####################################################

# TEXTBOX ####################################################
        self.textbox = Text(self, wrap="word", height=5)
        self.textbox.pack(side="bottom", fill="both", expand=True)
        self.textbox.tag_configure("TextBox", foreground="#b22222")
        self.pack(anchor=S, side=BOTTOM, fill=BOTH, expand=True)
# TEXTBOX ####################################################

# TEXTBOX2 ###################################################
        b1 = Entry(self)
        b1.pack(anchor=W, fill=X, expand=False)
# TEXTBOX2 ###################################################

        sys.stdout = TextRedirector(self.textbox, "stdout")
        sys.stderr = TextRedirector(self.textbox, "stderr")

# Functions ###################################################
    def StartUpChecker(self):
        self.clear_text()
        #functions.StartUpChecker()

    def clear_text(self):
        self.textbox.delete("1.0", END)

    def showMenu(self, e):
        self.menu.post(e.x_root, e.y_root)

    def onExit(self):
        self.quit()

    def print_stdout(self):
        '''Illustrate that using 'print' writes to stdout'''
        print("this is stdout")

    def print_stderr(self):
        '''Illustrate that we can write directly to stderr'''
        sys.stderr.write("this is stderr\n")

class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")

def main():
    root = Tk()
    #Width X Height
    root.geometry("500x300+300+300")
    root.update()
    root.minsize(400,200)
    app = MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()
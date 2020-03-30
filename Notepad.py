from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
class Notepad(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("644x600")
        self.title("Untitled - Notepad")

    def text(self):
        self.TextArea = Text(self, font="lucida 13")
        file = None
        self.TextArea.pack(fill=BOTH, expand=True)

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.sbar = Label(self,textvar=self.var,relief=SUNKEN,
                          anchor="w")
        self.sbar.pack(side=BOTTOM,fill=X)


    def scrollbar(self):
        Scroll = Scrollbar(self.TextArea)
        Scroll.pack(side=RIGHT, fill=Y)
        Scroll.config(command=self.TextArea.yview)
        self.TextArea.config(yscrollcommand=Scroll.set)

    def newFile(self):
        global file
        self.title("Untitled-Notepad")
        file = None
        self.TextArea.delete(1.0, END)

    def openFile(self):
        global file
        file = askopenfilename(defaultextension=".txt",
                               filetypes=[("All Files", "*.*"),
                                          ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            self.title(os.path.basename(file) + "-Notepad")
            self.TextArea.delete(1.0, END)
            f = open(file, "r")
            self.TextArea.insert(1.0, f.read())
            f.close()

    def saveFile(self):
        global file
        if file == None:
            file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                                     filetypes=[("All Files", "*.*"),
                                                ("Text Documents", "*.txt")])
            if file == "":
                file = None
            else:
                f = open(file, "w")
                f.write(self.TextArea.get(1.0, END))
                f.close()

                self.title(os.path.basename(file) + " - Notepad")
                print("File Saved")
        else:
            f = open(file, "w")
            f.write(self.TextArea.get(1.0, END))
            f.close()

    def quitApp(self):
        self.destroy()

    def cut(self):
        self.TextArea.event_generate(("<<Cut>>"))

    def copy(self):
        self.TextArea.event_generate(("<<Copy>>"))

    def paste(self):
        self.TextArea.event_generate(("<<Paste>>"))

    def about(self):
        showinfo("Notepad", "Notepad developed by Rishabh Jain")


    def menu(self):
        # lets create a menubar
        MenuBar = Menu(self)

        # file menu starts
        FileMenu = Menu(MenuBar, tearoff=0)
        # to open new file

        FileMenu.add_command(label="New", command=self.newFile)

        # to open already exisiting file
        FileMenu.add_command(label="open", command=self.openFile)

        # to save the current file
        FileMenu.add_command(label="save", command=self.saveFile)
        FileMenu.add_separator()
        FileMenu.add_command(label="Exit", command=self.quitApp)
        MenuBar.add_cascade(label="File", menu=FileMenu)

        # file menu ends

        # edit menu starts
        EditMenu = Menu(MenuBar, tearoff=0)
        # to give a feature of cut,copy,paste
        EditMenu.add_command(label="Cut", command=self.cut)
        EditMenu.add_command(label="Copy", command=self.copy)
        EditMenu.add_command(label="paste", command=self.paste)
        MenuBar.add_cascade(label="Edit", menu=EditMenu)

        # edit menu ends
        # help menu starts

        HelpMenu = Menu(MenuBar, tearoff=0)
        HelpMenu.add_command(label="About Notepad", command=self.about)

        MenuBar.add_cascade(label="Help", menu=HelpMenu)

        # help menu ends

        self.config(menu=MenuBar)


if __name__ == "__main__":
    window = Notepad()

    # add a text area
    window.text()
    file=None
    # add menu
    window.status()
    window.menu()

    window.scrollbar()

    window.mainloop()

from tkinter import *
from tkinter import filedialog as fdialog
import os
from tkinter import messagebox as msg

class Notepad(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500+450+120")
        self.configure(bg="white")
        self.iconbitmap("notepad.ico")
        self.title("Untitled - Notepad")

        # Functions of -File Menu
        def openFile():
            Path = fdialog.askopenfilename(defaultextension=".txt",filetypes=[("Text file","*.txt")])
            if Path == '':
                pass
            else:
                fileName = os.path.basename(Path)
                if fileName.endswith(".txt"):
                    self.title(fileName+" - Notepad")
                    with open(Path,"r") as file:
                        content = file.read()
                        textArea.delete(1.0,END)
                        textArea.insert(END,content)

        def Save_As():
            Path = fdialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text File","*.txt")])
            if Path == "":
                pass
            else:
                with open(Path,"w") as file:
                    file.write(textArea.get(1.0,END))
                fileName = os.path.basename(Path)
                self.title(f'{fileName} - Notepad')

        def newFile():
            self.title("Untitled - Notepad")
            textArea.delete(1.0,END)

        
        def exitFile():
            yes_no = msg.askyesno("Save","Do you want to Save the file?")
            if yes_no == False:
                self.destroy()            
            else:
                Save_As()

        def Help():
            msg.showinfo("Help","Contact: 982661xxxx\nEmail: bishaljaiswal0408@gmail.com")
        
        # menuBar
        mainMenu = Menu(self)
        fileMenu = Menu(mainMenu,tearoff=0)
        # openFile
        fileMenu.add_command(label="Open",command=openFile,background="pink")
        # saveFile
        fileMenu.add_command(label="Save As",command=Save_As,background="lightgreen")
        # newFile
        fileMenu.add_command(label="Newfile",command=newFile,background="skyblue")
        # separator
        fileMenu.add_separator()
        # exitWindow
        fileMenu.add_command(label="Exit",command=exitFile,background="red")



        mainMenu.add_cascade(menu=fileMenu,label="File")
        mainMenu.add_command(label="Help",command=Help)
        self.config(menu=mainMenu)

        # scrollBar
        scrollBar = Scrollbar(self)
        scrollBar.pack(side=RIGHT,fill=Y)

        # textArea
        textArea = Text(self,yscrollcommand=scrollBar.set)
        textArea.pack(expand=True,fill=BOTH)
        scrollBar.config(command=textArea.yview)


if __name__ == "__main__":
    window = Notepad()
    window.mainloop()
from tkinter import  Tk , scrolledtext , Menu , filedialog , END , messagebox , simpledialog
import os


root = Tk(className = " REMEMBER")
textArea = scrolledtext.ScrolledText(root,width=100,height=80)

def newfile():
    if len(textArea.get('1.0',END+'-1c'))>0:
        if messagebox.askyesno("SAVE?","DO YOU WANT TO SAVE" ) :
            savefile()
        else:
            textArea.delete('1.0',END)
    root.title("REMEMBER")


def openfile():
    file = filedialog.askopenfile(parent=root , title = "select a text file", filetypes = (("Text files","*.txt"),("All files","*.*")))
    
    if file != None:
        contents = file.read()
        textArea.insert('1.0',contents)
        file.close()

def savefile():
        file = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt', filetypes = (('HTML file','*.html'), ("TEXT file",'*.txt')))

        if file != None:
            data = textArea.get('1.0',END+'-1c')
            file.write(data)
            file.close()

def find():
    findString = simpledialog.askstring("Find...","Enter text")
    textData = textArea.get('1.0',END)

    occurance  = textData.upper().count(findString.upper())

    if textData.upper().count(findString.upper())> 0:
        label = messagebox.showinfo("Results", findString + '   has multiple occurance ,' + str(occurance))
                                    
    else:
        label = messagebox.showinfo("results","no result")
                                    
def about():
    label =messagebox.showinfo("This product is created on 16 june 2018 for the purpose of making notes and editing text  ")

def exitt():
    if messagebbox.askyesno("baahar jaana h","pakka soch lia naa"):
        root.destroy()



menu = Menu(root)
root.config(menu =menu)
fileMenu = Menu(menu)

menu.add_cascade(label="file",menu=fileMenu)
fileMenu.add_command(label="New", command = newfile)
fileMenu.add_command(label="Open" , command = openfile)
fileMenu.add_command(label="Save" , command = savefile)
fileMenu.add_command(label="Find" , command = find)
fileMenu.add_command(label="Print")
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command = exitt)
helpMenu = Menu(menu)
menu.add_cascade(label="Help")
menu.add_cascade(label = 'About',command = about)


textArea.pack()
root.mainloop()








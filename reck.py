#!/usr/bin/python3
#Recipe Keeper


import tkinter as tk
import tkinter.filedialog as tkFileDialog


root = tk.Tk()
root.title("Recipe Keeper")
root.geometry("544x680")
root.option_add("*Font", "TkDefaultFont 9")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.resizable(0,0)

my_entries = []

#Main Frame
mainframe = tk.Frame(root, bd=1, relief='solid')
mainframe.grid(row=0, column=0, sticky='n', padx=2, pady=2)


#labels
lab = tk.Label(mainframe, text="Recipe Keeper", font='Arial 10 bold')
lab.grid(row=0, column=0, sticky='nw', padx=12, pady=6)
lab1 = tk.Label(mainframe, text="Create and Keep Recipes")
lab1.grid(row=1, column=0, sticky='nw', padx=12, pady=(4,24))

#recipe name
rec = tk.Label(mainframe, text="Recipe Name:")
rec.grid(row=2, column=0, sticky='nw', padx=18, pady=4)
rec = tk.Entry(mainframe, bd=1, width='24')
rec.grid(row=2, column=0, columnspan=3, sticky='n', padx=2, pady=2)
rec.focus_set()

#category
cat = tk.Label(mainframe, text="Category:")
cat.grid(row=3, column=0, sticky='nw', padx=18, pady=4)
cat = tk.Entry(mainframe, bd=1, width='24')
cat.grid(row=3, column=0, columnspan=3, sticky='n', padx=2, pady=2)

#difficulty/time
diff = tk.Label(mainframe, text="Difficulty/Time:")
diff.grid(row=4, column=0, sticky='nw', padx=18, pady=4)
diff = tk.Entry(mainframe, bd=1, width='24')
diff.grid(row=4, column=0, columnspan=3, sticky='n', padx=2, pady=(2, 28))

#items needed
items_lbl = tk.Label(mainframe, text="Items Needed:", 
					fg='#1A1A1A', font=('Arial 10 bold'))
items_lbl.grid(row=5, column=0, sticky='nw', padx=12, pady=4)



def clear_fields(event=None):
	rec.delete('0', 'end')
	cat.delete('0', 'end')
	diff.delete('0', 'end')
	my_entries[0].delete('0', 'end')
	my_entries[1].delete('0', 'end')
	my_entries[2].delete('0', 'end')
	my_entries[3].delete('0', 'end')
	my_entries[4].delete('0', 'end')
	my_entries[5].delete('0', 'end')
	my_entries[6].delete('0', 'end')
	my_entries[7].delete('0', 'end')
	my_entries[8].delete('0', 'end')
	my_entries[9].delete('0', 'end')
	my_entries[10].delete('0', 'end')
	my_entries[11].delete('0', 'end')
	my_entries[12].delete('0', 'end')
	my_entries[13].delete('0', 'end')
	my_entries[14].delete('0', 'end')
	my_entries[15].delete('0', 'end')
	my_entries[16].delete('0', 'end')
	my_entries[17].delete('0', 'end')
	my_entries[18].delete('0', 'end')
	my_entries[19].delete('0', 'end')
	my_entries[20].delete('0', 'end')
	my_entries[21].delete('0', 'end')
	my_entries[22].delete('0', 'end')
	my_entries[23].delete('0', 'end')
	my_entries[24].delete('0', 'end')
	my_entries[25].delete('0', 'end')
	my_entries[26].delete('0', 'end')
	tex.delete('1.0', 'end')
	rec.focus_set()



#file menu
def exit_com(event=None):
    win = tk.Toplevel()
    win.title("Exit")
    xit = tk.Label(win, text="\n\nAre you sure you want to exit?\n")
    xit.pack()
    ex = tk.Button(win, text="Exit", width=4, command=root.destroy)
    ex.pack(side='left', padx=28, pady=4)
    ex.focus_set()
    ex.bind("<Return>", (lambda event: root.destroy()))
    can = tk.Button(win, text="Cancel", width=4, command=win.destroy)
    can.pack(side='right', padx=28, pady=4)
    win.transient(root)
    win.geometry('240x120')
    win.wait_window()



def save_com(event=None):
    file = tkFileDialog.asksaveasfile(mode='w', defaultextension='.txt',
    filetypes = (("Text Files", "*.txt"),("All Files", "*.*")))
    if file:
        file.write("\n")
        file.write("Recipe Name:      " + (rec.get()) + "\n\n")
        file.write("Category:         " + (cat.get()) + "\n\n")
        file.write("Difficulty/Time:  " + (diff.get()) + "\n\n\n")

        file.write("Ingredients: ".ljust(28) + "Utensils: ".ljust(28) + "Other: ".ljust(28) + "\n\n")

        file.write(my_entries[0].get().ljust(28) + (my_entries[9].get().ljust(28) + (my_entries[18].get().ljust(28) + "\n")))
        file.write(my_entries[1].get().ljust(28) + (my_entries[10].get().ljust(28) + (my_entries[19].get().ljust(28) + "\n")))
        file.write(my_entries[2].get().ljust(28) + (my_entries[11].get().ljust(28) + (my_entries[20].get().ljust(28) + "\n")))
        file.write(my_entries[3].get().ljust(28) + (my_entries[12].get().ljust(28) + (my_entries[21].get().ljust(28) + "\n")))
        file.write(my_entries[4].get().ljust(28) + (my_entries[13].get().ljust(28) + (my_entries[22].get().ljust(28) + "\n")))
        file.write(my_entries[5].get().ljust(28) + (my_entries[14].get().ljust(28) + (my_entries[23].get().ljust(28) + "\n")))
        file.write(my_entries[6].get().ljust(28) + (my_entries[15].get().ljust(28) + (my_entries[24].get().ljust(28) + "\n")))
        file.write(my_entries[7].get().ljust(28) + (my_entries[16].get().ljust(28) + (my_entries[25].get().ljust(28) + "\n")))
        file.write(my_entries[8].get().ljust(28) + (my_entries[17].get().ljust(28) + (my_entries[26].get().ljust(28) + "\n\n\n")))

        file.write("Instructions: " +  "\n\n")
        data = tex.get('1.0', 'end-1c')
        file.write(data)
        file.close()


#help menu
def about_com(event=None):
    win = tk.Toplevel()
    win.title("About")
    bout = tk.Label(win, text="""\n\nRecipe Keeper
    \nA Recipe Management System
    \nCreate and Keep Recipes
    \n\nMade in Python\n\n""")
    bout.pack()
    clo = tk.Button(win, text="Close", width=4, command=win.destroy)
    clo.pack(padx=8, pady=4)
    win.transient(root)
    win.geometry('300x220+638+298')
    win.wait_window()


def trouble_com(event=None):
    win = tk.Toplevel()
    win.title("Troubleshooting")
    trouble = tk.Label(win, justify='left', text="""\n\n
One problem that may occur is the use of
long words/phrases typed in entry fields. 
This may force the text in the next column
over, and out of alignment within the columns.\n
Note: This is noticeable only in the saved 
text file, not the program itself.\n
To avoid this, use short words in entry fields.\n
Example: 
Lg spoon instead of large wooden spoon.\n
The saved text file is formatted in a way 
that this shouldn't happen often.

\n\n""")
    trouble.pack()
    cls = tk.Button(win, text="Close", command=win.destroy)
    cls.pack()
    win.transient(root)
    win.geometry('354x360+612+230')
    win.wait_window()


#Labels for entry fields
#Ingredients
ing = tk.Label(mainframe, text="Ingredients:")
ing.grid(row=6, column=0, sticky='nw', padx=18, pady=2)

#Utensils
uten = tk.Label(mainframe, text="Utensils:")
uten.grid(row=6, column=1, sticky='nw', padx=4, pady=2)

#Other
other = tk.Label(mainframe, text="Other:")
other.grid(row=6, column=2, sticky='nw', padx=104, pady=2)



#midFrame (contains entry boxes)
midframe = tk.Frame(mainframe, bd=0, relief='flat')
midframe.grid(row=7, column=0, columnspan=3, sticky='ew', padx=0, pady=(0,18))

#column loop
for y in range(3):
	
	#row loop
	for x in range(9):
		my_entry = tk.Entry(midframe, bd=1, width='17')
		my_entry.grid(row=x, column=y, padx=18, pady=2)
		my_entries.append(my_entry)


#Text box
inst = tk.Label(mainframe, text="Instructions:")
inst.grid(row=8, column=0,  sticky='nw', padx=18, pady=0)
tex = tk.Text(mainframe, bd=1, width=55, height='10')
tex.grid(row=9, column=0, columnspan=3, sticky='ew', padx=18, pady=(2, 20))
tex.config(wrap="word")



#Menubar
menu = tk.Menu(root, bd=1, relief='flat')
root.config(menu=menu, bd=2)

#Filemenu
filemenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File ", menu=filemenu)
filemenu.add_command(label="Clear Fields",
                    command=clear_fields,
                    accelerator="Ctrl+C ".rjust(8))
filemenu.add_command(label="Save As",
                    command=save_com,
                    accelerator="Ctrl+S ".rjust(8))
filemenu.add_command(label="Exit",
                    command=exit_com, underline=1,
                    accelerator="Ctrl+Q ".rjust(8))

#Helpmenu
helpmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help ", menu=helpmenu)
helpmenu.add_command(label="About", command=about_com)
helpmenu.add_command(label="Troubleshooting", command=trouble_com)


#bindings
root.bind_all('<Control-c>', clear_fields)
root.bind_all('<Control-s>', save_com)
root.bind_all('<Control-q>', exit_com)

root.protocol("WM_DELETE_WINDOW")
root.mainloop()

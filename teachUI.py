import tkinter as tk
from Teacher import *

def login():
    login_screen.pack_forget()
    operation_screen.pack()
root = tk.Tk()
login_screen = tk.Frame(root)
operation_screen = tk.Frame(root)
start_class_screen = tk.Frame(root)
create_class_screen = tk.Frame(root)
class_in_progress_screen = tk.Frame(root)


#login screen
login_label = tk.Label(login_screen, text = "Please Enter your Teacher's ID:")
login_label.grid(row=0, column=0)

login_id = tk.StringVar()
logininp = tk.Entry(login_screen, textvariable= login_id)
logininp.grid(row=0, column=1)

pass_label = tk.Label(login_screen, text = "Enter your password: ")
pass_label.grid(row=1, column=0)

pass_id = tk.StringVar()
passinp = tk.Entry(login_screen, textvariable= pass_id)
passinp.grid(row=1, column=1)

login_failed = tk.Label(login_screen, text = 'Login again?')
login_failed.grid(row = 3, column = 0)

login_button = tk.Button(login_screen, width = 20, text = 'Login', command=login)
login_button.grid(row=2 ,column=1, columnspan= 1)

login_again_yes = tk.Button(login_screen,width = 12, text = 'Yes')
login_again_yes.grid(row=4 ,column=0, columnspan= 1)
login_again_no = tk.Button(login_screen, width = 12, text = 'No')
login_again_no.grid(row=5 ,column=0, columnspan= 1)

login_screen.pack()

#operation screen

Operations_label = tk.Label(operation_screen, text = "Operations:")
Operations_label.grid(row=0, column=0)

create_class_button = tk.Button(operation_screen, width = 12, text = 'Create Class')
create_class_button.grid(row=1 ,column=0, columnspan= 1)

start_class_button = tk.Button(operation_screen, width = 12, text = 'Start Class')
start_class_button.grid(row=2 ,column=0, columnspan= 1)

exit_button = tk.Button(operation_screen, width = 12, text = 'Exit', command=root.destroy)
exit_button.grid(row=4 ,column=0, columnspan= 1)

class_code_label = tk.Label(operation_screen, text = "Class Created, The code is CLASS12")
class_code_label.grid(row=1, column=1, columnspan=2)

enter_code_label = tk.Label(operation_screen, text = "Enter class code to start: ")
enter_code_label.grid(row=2, column=1)

class_id = tk.StringVar()
codeinp = tk.Entry(operation_screen, textvariable= class_id)
codeinp.grid(row=2, column=2)
root.mainloop()
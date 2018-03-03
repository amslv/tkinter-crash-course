from tkinter import messagebox
res = messagebox.askquestion('Message title','Message content')
res = messagebox.askyesno('Message title','Message content')
res = messagebox.askyesnocancel('Message title','Message content')
res = messagebox.askokcancel('Message title','Message content')
res = messagebox.askretrycancel('Message title','Message content')

messagebox.showwarning('Message title', 'Message content')  #shows warning message
messagebox.showerror('Message title', 'Message content')    #shows error message
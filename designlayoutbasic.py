import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

label1 = tk.Label(root, text="Label 1", bg="red")
label1.pack(fill=tk.BOTH, expand=True)

label2 = tk.Label(root, text="Label 2", bg="blue")
label2.pack(fill=tk.BOTH, expand=True)

root.mainloop()



import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

label1 = tk.Label(root, text="Label 1", bg="red")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Label 2", bg="blue")
label2.grid(row=1, column=1)

root.mainloop()





import tkinter as tk

root = tk.Tk()
root.title("Testing place layout")
root.geometry("300x200")

label1 = tk.Label(root, text="Label 1", bg="red")
label1.place(x=0, y=0)

label2 = tk.Label(root, text="Label 2", bg="blue")
label2.place(x=0, y=100)

root.mainloop()

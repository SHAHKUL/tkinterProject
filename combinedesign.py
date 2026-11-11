import tkinter as tk

root = tk.Tk()
root.title("Combined Layout Example")
root.geometry('300x400')

frame_top = tk.Frame(root)
frame_bottom = tk.Frame(root)

frame_top.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

label1 = tk.Label(frame_top, text="Top Frame - Label 1",bg='red')
label2 = tk.Label(frame_top, text="Top Frame - Label 2")
label3 = tk.Label(frame_bottom, text="Bottom Frame - Label 3")
label4 = tk.Label(frame_bottom, text="Bottom Frame - Label 4")

label5 = tk.Label(frame_bottom, text="for place - Label 5")
label6 = tk.Label(frame_bottom, text="Bottom Frame - Label 6")

label1.pack(side=tk.LEFT)
label2.pack(side=tk.RIGHT)
label3.grid(row=0, column=0)
label4.grid(row=0, column=1)

label5.place(x=40,y=60)
label6.place(x=80,y=80)

root.mainloop()

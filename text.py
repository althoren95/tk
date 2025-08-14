import tkinter as tk

def print_text():
    content = text_widget.get("1.0", tk.END)
    print(content)

root = tk.Tk()
root.title('My GUI Application')
root.geometry('600x400')

root.minsize(200, 150)

text_widget = tk.Text(root, font=('Arial', 16), height=10, width=40)
text_widget.pack(pady=20)

scrollbar = tk.Scrollbar(root, command=text_widget.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_widget.configure(yscrollcommand=scrollbar.set)


btn_print = tk.Button(root, text='Print Text', font=('Arial', 16), command=print_text)
btn_print.pack(pady=10)




root.mainloop()
import customtkinter as ctk 

root = ctk.CTk()
root.title('To do list')
root.geometry('700x400')

daily_label = ctk.CTkLabel(root, text='Daily Task', font=ctk.CTkFont(size=30, weight='bold'))
daily_label.pack(padx = 20, pady = 20)

scroll_frame = ctk.CTkScrollableFrame(root, width=400, height=200)
scroll_frame.pack()

entry = ctk.CTkEntry(scroll_frame, placeholder_text='add task')
entry.pack(fill ='x')

def todo():
    entry_get = entry.get()
    entry_lable = ctk.CTkLabel(scroll_frame, text=entry_get)
    entry_lable.pack()
    entry.delete(0, ctk.END)
    

add_btn = ctk.CTkButton(root, text='Add Task', width=400, command=todo)
add_btn.pack()

root.mainloop()
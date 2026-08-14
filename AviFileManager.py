from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
window = Tk()
window.title("codingal's text editer")
window.geometry("600x500")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
def open_file():
    """open a file for editing."""
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All files", "*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
        input_file.close()
    window.title(f"codingal's text editor - {filepath}")
def save_file():
     filepath = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All files", "*.*")])
    if not filepath:
        return
    with open(filepath, "W") as output_file:
      text = txt_edit.get(1.0, END)
      output_file.write(text)
    window.title(f"codingal's text editor - {filepath}")
wxt_edit = text(window)
fr_buttons = frame(window, relief=raised, bd=2)
btn_open = button(fr_buttons, text="open", command=open_file)
btn_save = button(fr_buttons, text="save as...", command=save_file)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
window.mainloop()
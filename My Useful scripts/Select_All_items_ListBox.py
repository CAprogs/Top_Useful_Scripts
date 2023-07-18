import tkinter as tk

def select_all():
    if select_all_var.get() == 1:
        result_box.select_set(0, tk.END)  # Sélectionner tous les éléments de la ListBox
    else:
        result_box.selection_clear(0, tk.END)  # Désélectionner tous les éléments de la ListBox

window = tk.Tk()

select_all_var = tk.IntVar()

select_all_checkbox = tk.Checkbutton(window, text="Sélectionner tout", variable=select_all_var, command=select_all)
select_all_checkbox.pack()

result_box = tk.Listbox(window, selectmode=tk.MULTIPLE)
result_box.pack()

# Ajouter des éléments à la ListBox (exemple)
for i in range(10):
    result_box.insert(tk.END, f"Élément {i+1}")

window.mainloop()

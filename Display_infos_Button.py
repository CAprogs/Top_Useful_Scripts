# display some informations when a button is entered for a certain time

import tkinter as tk

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.schedule_show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)
        self.after_id = None

    def schedule_show_tooltip(self, event):
        self.after_id = self.widget.after(1200, self.show_tooltip)

    def show_tooltip(self):
        self.after_id = None
        x, y, _, _ = self.widget.bbox(tk.ALL)
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        label = tk.Label(self.tooltip, text=self.text, background="Lightgrey", relief="groove", borderwidth=1)
        label.pack()

    def hide_tooltip(self, event):
        if self.after_id:
            self.widget.after_cancel(self.after_id)
            self.after_id = None
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

# Création de la fenêtre tkinter
root = tk.Tk()

# Création d'un bouton avec le tooltip
button = tk.Button(root, text="Bouton")
button.pack()

tooltip_text = "Ceci est un bouton"
tooltip = ToolTip(button, tooltip_text)

# Lancement de la boucle principale de tkinter
root.mainloop()

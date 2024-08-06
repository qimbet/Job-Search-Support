import tkinter as tk
from tkinter import filedialog, Text

class TextEditor:
    def __init__(self, root=None):
        if root is None:
            self.root = tk.Tk()
        else:
            self.root = root
        self.root.title("Simple Text Editor")

        self.text_area = Text(self.root, undo=True)
        self.text_area.pack(expand=True, fill='both')

        # Set focus on the text_area widget
        self.text_area.focus_set()

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_editor)

        # Bind the Enter key to the event handler
        self.text_area.bind("<Return>", self.exit_on_enter)

        self.current_text = ""  # Variable to store the text

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", 
                                               filetypes=[("Text files", "*.txt"), 
                                                          ("All files", "*.*")])
        if file_path:
            self.text_area.delete(1.0, tk.END)
            with open(file_path, "r") as file:
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                                 filetypes=[("Text files", "*.txt"), 
                                                            ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))

    def exit_on_enter(self, event=None):
        # Handle the Enter key press
        self.current_text = self.text_area.get(1.0, tk.END).strip()
        print("Current text stored in variable:", self.current_text)
        self.exit_editor()
        return "break"  # Prevents the default behavior of the Enter key

    def exit_editor(self):
        self.root.quit()  # Exit the Tkinter event loop

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    # Code to run the editor standalone
    root = tk.Tk()
    editor = TextEditor(root)
    editor.run()

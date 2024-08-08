import tkinter as tk
from tkinter import scrolledtext

class TextEditorInstance:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text Editor") 
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD) #initilizes the window
        self.text_area.pack(expand=True, fill='both')   #window sizing
        self.current_text = ""
        self.text_area.bind("<Return>", self.export)
        self.text_area.focus_set()

    def run(self):
        print("running main")
        self.setFocus()
        #ctShTb()
        self.root.mainloop()

    def export(self, event=None):
        print("begin export function")
        self.current_text = self.text_area.get("1.0", tk.END).strip()
        print("current text is: " + self.current_text)
        self.root.quit()

    def cleanup(self):
        self.root.destroy()
    
    def setFocus(self):
        self.text_area.focus_force()
        print("focus set")

if __name__ == "__main__":
    editor = TextEditorInstance()
    editor.run()
    print("First instance done. destroying")
    editor.cleanup()

    q = input("\n\npress enter to continue with the second window: \n")
    editor2 = TextEditorInstance()
    editor2.run()
    editor2.setFocus()
    print("running editor2")
    editor2.cleanup()
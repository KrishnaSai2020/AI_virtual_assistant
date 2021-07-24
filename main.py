from tkinter import *
from modules.AI_Speech import speak
from modules.User_Input import get_command


class Window(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.master = master
        master.title("AI rev 0.1")
        a = Label(master, text="try saying *what can you do*")
        a.pack(side="top")
        Button(master, text="listen", width=100, relief="groove", command=self.main).pack(side="bottom")

    def main(self):
        command = get_command(self)
        pass


root = Tk()
app = Window(root)
root.geometry("300x50")
root.mainloop()

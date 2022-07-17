import tkinter as tk
from tkinter import ttk, Text

from mailer import Mailer

class CounselWindow:
    def __init__(self):
        self.counsel_window = tk.Tk()
        self.mailer = Mailer()
        self.counsel_window.geometry("500x650+650+250")
        self.counsel_window.resizable(False, False)
        self.counsel_window.title("Mental Health Care Program v1.0.1 - Counseling Request")

        self.text = ''
        self.name = ''

        self.text_box = None
        self.checkbox = None
        self.name_label = None
        self.name_text_box = None
        self.submit_button = None

        self.set_layout()

    def set_layout(self):
        self.set_instruction_label()
        self.set_name_label()
        self.set_text_box()
        self.set_name()
        self.set_button()

    def set_instruction_label(self):
        instruction = ttk.Label(self.counsel_window, text="Please enter your message to the counselor.")
        instruction.place(x=50, y=50)

    def set_name_label(self):
        self.name_label = ttk.Label(self.counsel_window, text="Please enter your name.")
        self.name_label.place(x=50, y=470)

    def set_text_box(self):
        self.text_box = Text(self.counsel_window, height=20, width=50)
        self.text_box.place(x=50, y=100)

    def set_name(self):
        self.name_text_box = Text(self.counsel_window, height=1, width=50)
        self.name_text_box.place(x=50, y=500)

    def set_button(self):
        self.submit_button = ttk.Button(self.counsel_window, text="Submit", command=self.on_click)
        self.submit_button.place(x=215, y=580)

    def on_click(self):
        content = self.text_box.get('1.0', 'end-1c')
        name = self.name_text_box.get('1.0', 'end-1c')
        recipient = "tmiyazato@hotmail.com"
        subject = f"Request for Counseling: [{name}]"

        if content and name:
            self.mailer.send_message(content, recipient, subject)

        self.counsel_window.destroy()

    def run(self):
        self.counsel_window.mainloop()


if __name__ == '__main__':
    counsel = CounselWindow()
    counsel.run()

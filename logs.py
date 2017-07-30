from tkinter import END
exit_thread = False
exit_success = False
class Std_redirector(object):
    def __init__(self, widget):
        self.widget = widget
    def write(self, string):
        if not exit_thread:
            self.widget.insert(END, string)
            self.widget.see(END)
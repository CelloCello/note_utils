# -*- coding: utf-8 -*-
import Tkinter
from datetime import datetime
import sys, getopt


class NoteCreator(Tkinter.Frame):
  def __init__(self, master=None):
    Tkinter.Frame.__init__(self, master)
    self.master = master
    master.title('Note Creator')
    if len(sys.argv) > 1:
      path = sys.argv[1] + "\\"
      time_str = datetime.strftime(datetime.now(), '%Y%m%d')
      fullpath = path + time_str + "_.md"
      self.label = Tkinter.Label(master, text=fullpath)
      self.label.pack()
      self.text_filename = Tkinter.Entry(master, width=50)
      self.text_filename.bind("<Return>", self.save_note)
      self.text_filename.insert(0, fullpath)
      self.text_filename.icursor(len(path)+len(time_str)+1)
      self.text_filename.focus_set()
      self.text_filename.pack()
      

  def save_note(self, event):
    fullpath = event.widget.get()
    file = open(fullpath, 'w+')
    self.master.destroy()
    pass


if __name__ == '__main__':
  root = Tkinter.Tk()
  app = NoteCreator(master=root)
  app.mainloop()
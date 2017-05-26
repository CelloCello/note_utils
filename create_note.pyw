# -*- coding: utf-8 -*-
import Tkinter
from datetime import datetime
import sys, getopt, os


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
    filename = os.path.basename(fullpath)
    name_split = filename.split('.')[0].split('_')
    title = name_split[1]
    datetime_str = name_split[0]
    file = open(fullpath, 'w+')
    file.write('<div style="display:none">\n')
    file.write('<p>title: '+title.encode('utf-8')+'</p>\n')
    file.write('<p>datetime: '+datetime_str+'</p>\n')
    file.write('</div>\n\n')
    self.master.destroy()
    pass


if __name__ == '__main__':
  root = Tkinter.Tk()
  app = NoteCreator(master=root)
  app.mainloop()
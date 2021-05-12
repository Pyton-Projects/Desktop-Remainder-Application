from tkinter import*
import datetime
from tkinter.font import Font
import time
from tkinter import messagebox
root=Tk()
root.maxsize(900,400)
root.minsize(900,400)
root.title('Remainder Application For Windows')
heading_label=Label(root,text='Desktop Remainder App',font=('Times',15))
heading_label.pack()# use after() functon to remaind the user.
start=Spinbox(root,from_=0,to=24,width=3,font=Font(family='times',size=15))
start.place(x=150,y=65)
start['state']='readonly'
hour=Label(root,text='Hour',font=('Times',13))
hour.place(x=100,y=65)
time_=Label(root,text='Timer Type',font=('Times',13)) # notifaction type
time_.place(x=150,y=30)
boder=Label(root,
text=
'''
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
|
|
|
|
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
''') # symbols form -http://www.i2symbol.com/symbols/line/x254D-box-drawings-heavy-double-dash-horizontal-symbol-line-symbol-smiley-face

boder.pack()
root.mainloop()# video resizer









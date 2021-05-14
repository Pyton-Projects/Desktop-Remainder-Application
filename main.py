from tkinter import*
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
from plyer import*
from ttkthemes import ThemedTk,THEMES
import datetime
import sys
facts=['The world’s oldest toy is a stick',]
def x():
	question=messagebox.askquestion('Message','Are You Sure To Quit? Timer Will Be Disabled If You Quit')
	if question=='yes':
		sys.exit()
	if question!='no':
		None
def notification_():
	
	try:
		notification.notify(
            	title = "Your Remainder!",
            	message=F"""{task_value_}
Do You Know? 
{str(facts)} Thats a Fact!""")# create button called increase knowledge mode is on or off
	except Exception:
		messagebox.showinfo('Message','Please Set A Task Then Cilck On Set Task Button')
def timer():
	if len(task.get("1.0", "end-1c")) ==0:
		messagebox.showinfo('Message','Please Set A Task Then Cilck On Set Task Button')
	else:
		formula_to_find_seconds=sec_value.get()*1000
		formula_to_find_minutes=min_value.get()*60000
		formula_to_find_hours=hour_value.get()*3600000
		time=formula_to_find_seconds+formula_to_find_minutes+formula_to_find_hours
		root.after(time,notification_)
def task_value():
	global task_value_
	task_value_=task.get(1.0,END)
	if len(task.get("1.0", "end-1c")) == 0:# This Logic Came From https://stackoverflow.com/questions/38539617/tkinter-check-if-text-widget-is-empty
		question=messagebox.showinfo('Message','Please Put Something For Your Task!')
	if len(task.get("1.0", "end-1c")) != 0:
		messagebox.showinfo('Message','Task Set Suceesfully! Now Go And Set Your Timer! ')# create a menu 
root=ThemedTk(themebg=True)
root.set_theme('arc')
root.protocol('WM_DELETE_WINDOW',x)
root.maxsize(900,400)
root.minsize(900,400)
min_value=IntVar()
sec_value=IntVar()
hour_value=IntVar()
task=Text(root,width=15,height=5)
task.place(x=750+19+3)
root.title('Remainder Application For Windows')
heading_label=ttk.Label(root,text='Desktop Remainder App',font=('Times',15))
heading_label.pack()
start=ttk.Spinbox(root,from_=0,to=23,width=3,textvariable=hour_value,font=Font(family='times',size=15))
start.place(x=150,y=65)
start['state']='readonly'
hour=ttk.Label(root,text='Hour',font=('Times',13))# go and find some facts
hour.place(x=95,y=65)
min_=ttk.Label(root,text='Minutes',font=('Times',13))
min_.place(x=85,y=100)
sec_=ttk.Label(root,text='Seconds',font=('Times',13))
sec_.place(x=85,y=139)
Task_Identity=ttk.Label(root,text='Put Your Task Down Below When Time Hits The Task Will Show In The Notifaction')
Task_Identity.pack()
start_min=ttk.Spinbox(root,from_=0,to=59,width=3,textvariable=min_value,font=Font(root,family='times',size=15))
start_min.place(x=150,y=100)
start_min['state']='readonly'
start_sec=ttk.Spinbox(root,from_=0,to=59,width=3,textvariable=sec_value,font=Font(root,family='times',size=15))
start_sec.place(x=150,y=140)
start_sec['state']='readonly'
set_=ttk.Button(root,text='Set Timer',command=timer)
set_.place(x=135,y=175)
set_task=ttk.Button(root,text='Set Task',command=task_value)
set_task.place(x=750+19+3+6+3+3+6+3+3,y=50+12+19+5,)
root.mainloop()
# like time now 12:00:1 15 minutes of timer 12:15:00
# 12:00 to 12:15 
# ideas in diary
# notifaction type
# set task to do progject
# a software that can get the color value form a int
# complete image commpresser.
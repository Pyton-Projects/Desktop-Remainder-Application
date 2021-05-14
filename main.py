from tkinter import*
from tkinter.font import Font
from tkinter import messagebox
from plyer import*
def notification_():
	try:
		notification.notify(
            	title = "Your Remainder!",
            	message=F"{task_value_}boiii".title())
	except Exception:
		messagebox.showinfo('Message','Please Set A Task Then Cilck On Set Task Button')
def timer():
		formula_to_find_seconds=sec_value.get()*1000
		formula_to_find_minutes=min_value.get()*60000
		formula_to_find_hours=hour_value.get()*3600000
		time=formula_to_find_seconds+formula_to_find_minutes+formula_to_find_hours
		root.after(time,notification_).
def task_value():
	global task_value_
	task_value_=task.get(1.0,END)
	if len(task.get("1.0", "end-1c")) == 0:# This Logic Came From https://stackoverflow.com/questions/38539617/tkinter-check-if-text-widget-is-empty
    		question=messagebox.askquestion('Question','Are You Sure To Create A Empty Task?')
    		if question=='yes':
    			task.insert(1.0,'')
    		if question=='no':
    			None
root=Tk()
root.maxsize(900,400)
root.minsize(900,400)
min_value=IntVar()
sec_value=IntVar()
hour_value=IntVar()
text_value=StringVar()
task=Text(root,width=15,height=5)
task.pack()
all_value=(sec_value.get(),min_value.get(),hour_value.get)
root.title('Remainder Application For Windows')
heading_label=Label(root,text='Desktop Remainder App',font=('Times',15))
heading_label.pack()
start=Spinbox(root,from_=0,to=23,width=3,textvariable=hour_value,font=Font(family='times',size=15))
start.place(x=150,y=65)
start['state']='readonly'
hour=Label(root,text='Hour',font=('Times',13))
hour.place(x=95,y=65)
min_=Label(root,text='Minutes',font=('Times',13))
min_.place(x=85,y=100)
sec_=Label(root,text='Seconds',font=('Times',13))
sec_.place(x=85,y=139)
start_min=Spinbox(root,from_=0,to=59,width=3,textvariable=min_value,font=Font(root,family='times',size=15))
start_min.place(x=150,y=100)
start_min['state']='readonly'
start_sec=Spinbox(root,from_=0,to=59,width=3,textvariable=sec_value,font=Font(root,family='times',size=15))
start_sec.place(x=150,y=140)
start_sec['state']='readonly'
set_=Button(root,text='Set Timer',command=timer)
set_.place(x=135,y=175)
set_task=Button(root,text='Set Task',command=task_value)
set_task.pack()
root.mainloop()
# like time now 12:00:1 15 minutes of timer 12:15:00
# 12:00 to 12:15 
# ideas in diary
# notifaction type
# set task to do progject
# a software that can get the color value form a int
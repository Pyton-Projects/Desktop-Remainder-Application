from tkinter import*
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
from plyer import*
from ttkthemes import ThemedTk,THEMES
from datetime import datetime, timedelta
import random
import winsound
facts='The world’s oldest toy is a stick','Moon flowers actually bloom in response to the moon','The biggest Dalmatian litter ever was 18 puppies','Sea otters hold hands while they sleep','The largest sand castle in the world measured 54 feet high','There are over 10 holidays that celebrate chocolate','Chocolate is (kinda) a fruit','The voices of Mickey and Minnie Mouse got married in real life','Lazy people actually think more','Fall leaf colors are present year-round','Two Buck Chuck once won a wine competition','The way you eat Oreos says something about your personality','The Queen drinks champagne almost every day','The moon has its own time zones','Americans eat 100 acres of pizza a day','Smiling is actually contagious','A team of six women programmed the first digital computer','Baby elephants suck their trunks for comfort','''There's a 107-acre forest made up of a single tree''','Tomatoes are both a fruit and a vegetable','''There's an official rock paper scissors league'''
def x():
	question=messagebox.askquestion('Message','Are You Sure To Quit? Remainder Will Be Disabled If You Quit')
	if question=='yes':
		exit()
	if question!='no':
		None
def notification_():
	try:
		notification.notify(
            	title = "Your Remainder!",
            	message=F"""{task_value_}Do You Know? 
{random.choice(facts)} Thats a Fact!""")
		print('Here Is Your Remainder!')
		frequency = 2000
		duration = 2000 
		winsound.Beep(frequency, duration)

	except Exception:
		messagebox.showinfo('Message','Please Set A Task Then Cilck On Set Task Button')
def info():
	messagebox.showinfo('Message','Please Set A Task Then Cilck On Set Task Button')
def Remainder():
	print('''Remainder Is Running.... Please Don't Quit The Application. ''')
	formula_to_find_seconds=sec_value.get()*1000
	formula_to_find_minutes=min_value.get()*60000
	formula_to_find_hours=hour_value.get()*3600000
	time=formula_to_find_seconds+formula_to_find_minutes+formula_to_find_hours
	root.after(time,notification_)
	updated = ( datetime.now() +timedelta(hours=int(hour_value.get()),minutes=int(min_value.get()),seconds=sec_value.get())).strftime('%r')
	time_in_right_fromats=datetime.now().strftime('%r')
	messagebox.showinfo(f'Message',f'The Time Set At {time_in_right_fromats} And You Will Get A Notifaction At {updated}')
def task_value():
	global task_value_
	task_value_=task.get(1.0,END)
	if len(task.get("1.0", "end-1c")) == 0:# This Logic Came From https://stackoverflow.com/questions/38539617/tkinter-check-if-text-widget-is-empty
		question=messagebox.showinfo('Message','Please Put Something For Your Task!')
		set_.config(command=info)
	if len(task.get("1.0", "end-1c")) != 0:
		messagebox.showinfo('Message','Task Set Suceesfully! Now Go And Set Your Remainder! ')
		set_.config(command=Remainder)
		# create a menu 
root=ThemedTk(themebg=True)
root.set_theme('arc')
root.protocol('WM_DELETE_WINDOW',x)
root.maxsize(900,400)
root.minsize(900,400)
min_value=IntVar()
sec_value=IntVar()
hour_value=IntVar()
task=Text(root,width=15,height=5)
task.place(x=365,y=250)
root.title('Remainder Application For Windows')
heading_label=ttk.Label(root,text='Desktop Remainder App',font=('Times',15))
heading_label.pack()
start=ttk.Spinbox(root,from_=0,to=23,width=3,textvariable=hour_value,font=Font(family='times',size=15))
start.place(x=400,y=65)
start['state']='readonly'
hour=ttk.Label(root,text='Hour',font=('Times',13))# go and find some facts
hour.place(x=340,y=65)
min_=ttk.Label(root,text='Minutes',font=('Times',13))
min_.place(x=330,y=100)
sec_=ttk.Label(root,text='Seconds',font=('Times',13))
sec_.place(x=330,y=139)
Task_Identity=ttk.Label(root,text='Put Your Task Down Below When Time Hits The Task Will Show In The Notifaction',font=('Times',11))
Task_Identity.place(x=165,y=220)
start_min=ttk.Spinbox(root,from_=0,to=59,width=3,textvariable=min_value,font=Font(root,family='times',size=15))
start_min.place(x=400,y=100)
start_min['state']='readonly'
start_sec=ttk.Spinbox(root,from_=0,to=59,width=3,textvariable=sec_value,font=Font(root,family='times',size=15))
start_sec.place(x=400,y=140)
start_sec['state']='readonly'
set_=ttk.Button(root,text='Set Remainder',command=info)
set_.place(x=375,y=180)
set_task=ttk.Button(root,text='Set Task',command=task_value)
set_task.place(x=385,y=340,)
root.mainloop()
# End!

# the code will dismange for some time!
# from tkinter import*
# from tkinter import ttk
# import os
# from tkinter.ttk import Progressbar,Label
# from twilio.rest import Client
# from tkinter.font import Font
# from tkinter.dialog import*
# from tkinter import messagebox
# from plyer import*
# from ttkthemes import ThemedTk
# from datetime import datetime, timedelta
# from tkinter import simpledialog
# root=ThemedTk(themebg=True)
# root.set_theme('arc')
# min_value=IntVar()
# sec_value=IntVar()
# hour_value=IntVar()
# t_1=ttk.Label(root)
# t=ttk.Label(root)
# def Tital_your_reminder():
# 	global Tital
# 	Tital=simpledialog.askstring(Tital='Tital',prompt='Tital Of Your Reminder')
# 	if ques=='no':
# 		global t_1
# 		global t
# 		t_1.config(text=datetime.now().strftime('%r'))
# 		t.config(text=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r'))
# 		t_1.place(x=570,y=80)
# 		cancel_.place(x=665,y=80)
# 		t.place(x=825,y=80)
# 	if ques=='yes':
# 		pass

# def which_alert():
# 	d = Dialog(None, {'Tital': 'Question',
#                       'text':'Which Alert Do You Want? You Will Remind For Your Task Through Your Selected Alert',
#                       'bitmap': DIALOG_ICON,
#                       'default': 'None',
#                       'strings': ('Sms Alert (Requires Network)',
#                                   'Call Alert (Requires Network)',
#                                   'Windows Notifaction Alert')})
# 	set_.config(command=info1)
# 	global Selected_Val
# 	Selected_Val=d.num

# def ask_phone_number():
# 	global phone_number
# 	phone_number=simpledialog.askstring(Tital='Phone Number',prompt='Enter Your Phone Number (With Contury Code Incuded)')
# 	if ques=='no':
# 		global t_1
# 		global t
# 		t_1.config(text=datetime.now().strftime('%r'))
# 		t.config(text=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r'))
# 		t_1.place(x=570,y=80)
# 		cancel_.place(x=665,y=80)
# 		t_1.config(text=datetime.now().strftime('%r'))
# 		t.config(text=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r'))
# 		t.place(x=825,y=80)
# 	if ques=='yes':
# 		pass
# def sms_alert():
# 	cancel_.place(x=0,y=54444)
# 	t_1.place(x=3333333333)
# 	t.place(x=22222)
# 	root.deiconify()
# 	pro_1.stop()
# 	set_.config(command=reminder)
# 	auccont_Id=os.environ.get('MY_SID')
# 	auth_token=os.environ.get('MY_AUTH_TOKEN')
# 	c=Client(auccont_Id,auth_token)
# 	try:
# 		if check==False:
# 			c.messages.create(body=F"Hey! user You Need To Do {task_value_} At This Time.",from_='+19563985957',to=phone_number)

# 		if check==True:
# 			c.messages.create(body=F"Hey! user You Need To Do {new_task} At This Time.",from_='+19563985957',to=phone_number)
# 	except Exception as e:
# 		messagebox.showinfo('Info','Check Your Network Connection It Is On Or Off. Or Check  The Phone Number You Entered (Phone Number You Entered-{number})'.format(number=phone_number))	
# 		print(f'The Error Is:{e}')	
	
# 	question=messagebox.askquestion('Info','Do You Want To Repat This Remind again?')#create a new reminder a option.
# 	if question=='no':
# 		None
# 	if question=='yes':
# 		root.withdraw()
# 		root.after(time,sms_alert)

# def phone_alert():
# 	cancel_.place(x=0,y=54444)
# 	t_1.place(x=3333333333)
# 	t.place(x=22222)
# 	root.deiconify()
# 	pro_1.stop()
# 	set_.config(command=reminder)
# 	auccont_Id=os.environ.get('MY_SID')
# 	auth_token=os.environ.get('MY_AUTH_TOKEN')
# 	c=Client(str(auccont_Id),str(auth_token))#say the task
# 	try: 
# 		c.calls.create(from_='+19563985957',url='https://demo.twilio.com',to=phone_number)
# 		question=messagebox.askquestion('Info','Do You Want To Repat This Remind again?')#create a new reminder a option.
# 		if question=='no':
# 			None
# 		if question=='yes':
# 			root.withdraw()
# 			root.after(time,phone_alert)
# 	except Exception as e:
# 		messagebox.showinfo('Info','Check Your Network Connection It Is On Or Off. Or Check The Phone Number You Entered (Phone Number You Entered-{number})'.format(number=phone_number))		
# 		print(f'The Error Is:{e}')
# def x():
# 	question=messagebox.askquestion('Message','Are You Sure To Quit? Reminder OR reminderS wILL Disabled!'.Tital())
# 	if question=='yes':
# 		exit()
# 	if question=='no':
# 		None
# def notification_():
# 	cancel_.place(x=0,y=54444)
# 	t_1.place(x=3333333333)
# 	t.place(x=22222)
# 	try:
# 		root.deiconify()
# 		set_.config(command=reminder)
# 		if check==True:
# 			set_.config(command=reminder)
# 			pro_1.stop()
# 			notification.notify(
# 	            	Tital = f"{Tital}",
# 	                message=F"""{str(new_task)}""",)
# 		if check==False:
# 			set_.config(command=reminder)

# 			pro_1.stop()
# 			notification.notify(
# 	            		Tital = f"{Tital}",
# 	            		message=F"""{str(task_value_)}""",)
# 		set_.config(command=reminder)
# 		question=messagebox.askquestion('Info','Do You Want To Repat This Remind again?')#create a new reminder a option.
# 		if question=='no':
# 			None
# 		if question=='yes':
# 			root.withdraw()
# 			root.after(time,notification_)
	
# 	except:
# 		pass

# def info():
# 	messagebox.showinfo('Message','Please Set A Task From Down Below Then Cilck On Set Remaind Button')
# def main_pros():
# 	l.place(x=660,y=30)
# 	sez=(min_value.get())
# 	for_mula=sez*600
# 	sez_1=(sec_value.get())
# 	for_mula_1=sez_1*10
# 	sez_2=(hour_value.get())
# 	for_mula_2=sez_2*6000
# 	pro_1['mode']='determinate'
# 	pro_1['value']=1000
# 	pro_1.start(for_mula+for_mula_1+for_mula_2)
# 	root.update()
# def info1():
# 	messagebox.showinfo('Message','Another Remind Is Running... Please Wait Some Time Till The Running Remind Not Remind You!')
# def cancel():
# 	pro_1.stop()
# 	if Selected_Val==0:
# 		root.after_cancel(called_1)
# 		set_.config(command=reminder)
# 		cancel_.place(x=0,y=54444)
# 		t_1.place(x=3333333333)
# 		t.place(x=22222)
# 		messagebox.showinfo('Info','Canceled The Reminder!!')

# 	if Selected_Val==1:
# 		root.after_cancel(called_2)
# 		set_.config(command=reminder)
# 		cancel_.place(x=0,y=54444)
# 		t_1.place(x=3333333333)
# 		t.place(x=22222)
# 		messagebox.showinfo('Info','Canceled The Reminder!!')

# 	if Selected_Val==2:
# 		root.after_cancel(called_3)
# 		set_.config(command=reminder)
# 		cancel_.place(x=0,y=54444)
# 		t_1.place(x=3333333333)
# 		t.place(x=22222)
# 		messagebox.showinfo('Info','Canceled The Reminder!!')

# def reminder():
# 	if sec_value.get()==0 and min_value.get()==0 and hour_value.get()==0:
# 			messagebox.showinfo('Message','Please Add More Time!')	
# 	else:
# 		global called_1
# 		global called_2
# 		global called_3
# 		global t_1
# 		global t
# 		global time
# 		global ques
# 		formula_to_find_seconds=sec_value.get()*1000
# 		formula_to_find_minutes=min_value.get()*60000
# 		formula_to_find_hours=hour_value.get()*3600000
# 		time=formula_to_find_seconds+formula_to_find_minutes+formula_to_find_hours
# 		which_alert()
# 		ques=messagebox.askquestion('Info','App Will Hide It self Do You Want To Hide It?')
		
# 		if Selected_Val==0:
# 			ask_phone_number()
# 			if ques=='no':
# 				updated=datetime.now().strftime('%r')
# 				timee=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r')
# 				messagebox.showinfo('Info',f'Time Set At {updated} And You Will Get A Sms At {timee}')
# 				called_1=root.after(time,sms_alert)
# 				main_pros()
# 			if ques=='yes':
# 				updated=datetime.now().strftime('%r')
# 				timee=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r')
# 				messagebox.showinfo('Info',f'Time Set At {updated} And You Will Get A Sms At {timee}')
# 				root.withdraw()
# 				called_1=root.after(time,sms_alert)
# 		if Selected_Val==1:
# 			ask_phone_number()
# 			if ques=='yes':
# 				updated=datetime.now().strftime('%r')
# 				timee=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r')
# 				messagebox.showinfo('Info',f'Time Set At {updated} And You Will Get A Call At {timee}')
# 				root.withdraw()
# 				called_2=root.after(time,phone_alert)
# 			if ques=='no':
# 				updated=datetime.now().strftime('%r')
# 				timee=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r')
# 				messagebox.showinfo('Info',f'Time Set At {updated} And You Will Get A Call At {timee}')
# 				called_2=root.after(time,phone_alert)
# 				main_pros()
# 		if Selected_Val==2:
# 			Tital_your_reminder()
# 			if ques=='yes':
# 				updated=datetime.now().strftime('%r')
# 				timee=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r')
# 				messagebox.showinfo('Info',f'Time Set At {updated} And You Will Get A Notifaction At {timee}')
# 				root.withdraw()
# 				called_3=root.after(time,notification_)
# 				main_pros()
# 			if ques=='no':
# 				updated=datetime.now().strftime('%r')
# 				timee=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r')
# 				messagebox.showinfo('Info',f'Time Set At {updated} And You Will Get A Notifaction At {timee}')
# 				called_3=root.after(time,notification_)
# 				main_pros()
# def task_value():
# 	global check
# 	check=False
# 	global task_value_
# 	task_value_=task.get(1.0,END)
# 	if len(task.get("1.0", "end-1c")) == 0:# This Logic Came From https://stackoverflow.com/questions/38539617/tkinter-None-if-text-widget-is-empty
# 		question=messagebox.showinfo('Message','Please Put Something For Your Task!')
# 		set_.config(command=info)
# 	elif str(task.get(1.0,END)).isspace():
# 		question=messagebox.showinfo('Message','Please Put Something For Your Task!')
# 		set_.config(command=info)
# 	else:
# 		messagebox.showinfo('Message','Remind Set Successfully! Now Go And Set Your reminder')
# 		set_.config(command=reminder)
# 		update.place(x=500,y=340)
# def update_task():
# 	global check
# 	global new_task
# 	new_task=task.get(1.0,END)
# 	check=True
# 	messagebox.showinfo('Info','Task Updated!')
# root.protocol('WM_DELETE_WINDOW',x)
# pro_1=Progressbar(root,length=250)
# pro_1.place(x=600,y=60)
# dat=StringVar()
# l=ttk.Label(root,text='Progress Of Your Remind',font=('Time',10))
# l.place(x=660,y=30)
# menus = Menu(root)
# root.maxsize(900,400)
# root.minsize(900,400)
# min_value=IntVar()
# sec_value=IntVar()
# hour_value=IntVar()
# task=Text(root,width=15,height=5)
# task.place(x=365,y=250)
# root.Tital('Reminder Application For Windows')
# start=ttk.Spinbox(root,from_=0,to=23,width=3,textvariable=hour_value,font=Font(family='times',size=15))
# start.place(x=400,y=65)
# start['state']='readonly'
# hour=ttk.Label(root,text='Hour',font=('Times',13))
# hour.place(x=340,y=65)
# min_=ttk.Label(root,text='Minutes',font=('Times',13))
# min_.place(x=330,y=100)
# sec_=ttk.Label(root,text='Seconds',font=('Times',13))
# sec_.place(x=330,y=139)
# Task_Identity=ttk.Label(root,text='What shall I remind you about? Write Down Below',font=('Times',11)).place(x=300,y=220)
# start_min=ttk.Spinbox(root,from_=0,to=59,width=3,textvariable=min_value,font=Font(root,family='times',size=15))
# start_min.place(x=400,y=100)
# start_min['state']='readonly'
# start_sec=ttk.Spinbox(root,from_=0,to=59,width=3,textvariable=sec_value,font=Font(root,family='times',size=15))
# start_sec.place(x=400,y=140)
# start_sec['state']='readonly'
# set_=ttk.Button(root,text='Set reminder',command=info)
# set_.place(x=375,y=180)
# set_task=ttk.Button(root,text='Set Remind',command=task_value)
# set_task.place(x=385,y=340,)
# update=ttk.Button(root,text='Click Me For Update Your Old Remind!',command=update_task)
# cancel_=ttk.Button(root,text='Cancel The Remaind',command=cancel)
# HEAd=ttk.Label(root,text="""After how long did you need a reminder from now?
# 	Set From Down Below""",font=('times',13)).pack()
# mainloop()
# # End!
# # CREATE bUTTON fOR  FOR CREATING NEW reminder
# # use elif when there is a chance to get both satement true
# # a softwarre that can short english sentence!
# # use cd to switch in different folders use ; to add diffrent paths in one varible!!,a website that can load webpages faster!!!
# # create bakend of alerts
# # push
# # add millseond option.
# # create countdown timer is this app.
# # create new reminder option.
# # buy a voice api,sms api
# # push this one again.
# # clean github repo
# # check reminder app is sending notifaction in a hour
# # run tkinter in background when pc/laptop is turing on
# # check all repos working fine.
# # buy a voice api and create that api sayable
# # check all projects and repos have no bugs!
# # pythonw run remainder app.py
# # tommrow task create new reminder option.
# # create a website extenstion. addiction remover extenstion like a person watch youtube for 2+ hour the extenstion will say wait some time you watched youtube soo many time please take a short break!
# # create a option for repating a reminder.
# # create a new reminder option and how to link this python script to task sheduler.
# # check the reminder if this app have bug then fix the bug
# # buy voice api.
# # task complete in 2 days:
# # buy a voice,text api.
# # create new reminder option.. 
# # create top level a python program that can short english sentence
from tkinter import*
from plyer import*
from tkcalendar import*
import datetime
from tkinter import messagebox
root=Tk()
root.title('Reminder App')
root.geometry('500x350')
indexes=0
data1=IntVar()
data2=IntVar()
data3=IntVar()
data4=StringVar()
datai=StringVar()
def save_the_reminder():
	global indexes
	messagebox.showinfo('Message','Reminder Set Successfully!!')
	# do things then add!
	l1.insert(indexes,Tital_input.get(1.0,END)+' at'+f' {data1.get()}:{data2.get()}:{data3.get()} {data4.get()}')
	indexes+=1
	t1.destroy()


def add_reminder():
	# global time_input
	global t1,Tital_input
	t1=Toplevel()
	t1.geometry('500x250')
	Tital_lab=Label(t1,text='Tital:-',font=('Arial Rounded MT bold',20,'bold'))
	Tital_lab.place(x=1)

	Tital_input=Text(t1,width=15,height=2,font=('Arial',10,'bold'))
	Tital_input.place(x=90)
	

	content_label=Label(t1,text='Paragraph:-',font=('Arial Rounded MT bold',20,'bold'))
	content_label.place(x=1,y=45)

	content_input=Text(t1,width=15,height=2,font=('Arial',10,'bold'))
	content_input.place(y=45,x=180)

	time_label=Label(t1,text='Time:-',font=('Arial Rounded MT bold',20,'bold'))
	time_label.place(x=1,y=95)

	s1=Spinbox(t1,from_=0,to_=12,font=('Arial',20,'bold'),width=3,textvariable=data1)
	s1.place(x=93,y=95)

	s2=Spinbox(t1,from_=0,to_=59,font=('Arial',20,'bold'),width=3,textvariable=data2)
	s2.place(x=93+93,y=95)

	s3=Spinbox(t1,from_=0,to_=59,font=('Arial',20,'bold'),width=3,textvariable=data3)
	s3.place(x=93+93+93,y=95)

	a=Label(t1,text=':',font=('Arial Rounded MT bold',25,'bold')).place(x=164,y=90)
	b=Label(t1,text=':',font=('Arial Rounded MT bold',25,'bold')).place(x=160+95,y=90)
	am_or_pm=Spinbox(t1,values=('AM','PM'),font=('Arial',20,'bold'),width=3,textvariable=data4)
	am_or_pm.place(x=365,y=95)
	date=PhotoImage(file='calendar-icon (1).png')
	pick_date=Button(t1,image=date,borderwidth=0)
	pick_date.place(x=95,y=95+44)
	date_lab=Label(t1,text='Date:-',font=('Arial Rounded MT bold',19,'bold'))
	date_lab.place(x=1,y=95+47)
	save=Button(t1,text='Save',font=('Arial Rounded MT bold',15,'bold'),fg='white',bg='red',command=save_the_reminder).place(x=185,y=200)
	# manish sha.
	#a.b

	# cal=Calendar(t1,selectmode="day",year=int(datetime.datetime.now().strftime('%Y')),month=5,day=22).pack()
	mainloop()
def get_the_value(event):
	print('Okay!!')
l1=Listbox(root,width=45,font=('Arial Rounded MT bold',15,'bold'))
your_reminders=Label(root,text='Your Reminders:',fg='gold',font=('Arial Rounded MT bold',21,'bold')).pack()
l1.pack()
root.bind('<Button-3>',get_the_value)
add=Button(root,text='Add Reminder',fg='White',bg='black',font=('Arial Rounded MT bold',15,'bold'),command=add_reminder)
add.place(x=155,y=285)
mainloop()
# add new sound in timer app and naming option.

from tkinter import*
from tkinter import ttk
import os
from tkinter.ttk import Progressbar,Label
from twilio.rest import Client
from tkinter.font import Font
from tkinter.dialog import*
from tkinter import messagebox
from plyer import*
from ttkthemes import ThemedTk
from datetime import datetime, timedelta
from tkinter import simpledialog
root=ThemedTk(themebg=True)
root.set_theme('arc')
min_value=IntVar()
sec_value=IntVar()
hour_value=IntVar()
def which_alert():
	d = Dialog(None, {'title': 'Question',
                      'text':'Which Alert Do You Want? You Will Remind For Your Task Through Your Selected Alert',
                      'bitmap': DIALOG_ICON,
                      'default': 'None',
                      'strings': ('Sms Alert (Requires Network)',
                                  'Call Alert (Requires Network)',
                                  'Windows Notifaction Alert')})
	set_.config(command=info1)
	global Selected_Val
	Selected_Val=d.num
def ask_phone_number():
	global phone_number
	phone_number=simpledialog.askstring(title='Phone Number',prompt='Enter Your Phone Number (With Contury Code Incuded)')
	t_1=ttk.Label(root,text=datetime.now().strftime('%r'))#HIDE TH AUTH_TOKEN
	t_1.place(x=570,y=80)
	cancel.place(x=665,y=80)
	t=ttk.Label(root,text=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r'))
	t.place(x=825,y=80)
def sms_alert():
	t_1.place(x=4444)
	t.place(x=4444)
	cancel.place(x=44444)
	root.deiconify()
	pro_1.stop()
	set_.config(command=reminder)
	auccont_Id=os.environ.get('MY_SID')
	auth_token=os.environ.get('MY_AUTH_TOKEN')
	c=Client(auccont_Id,auth_token)
	try:
		if check==False:
			c.messages.create(body=F"Hey! user You Need To Do {task_value_} At This Time Reply Yes To Confrom That You Reviced The Alert!",from_='+19563985957',to=phone_number)
		if check==True:
			c.messages.create(body=F"Hey! user You Need To Do {update_task} AT This Time Reply Yes To Confrom That You Reviced The Alert!",from_='+19563985957',to=phone_number)
	except:
		messagebox.showinfo('Info','None Your Network Connection. Or None The Phone Number You Entered (Your Phone Number-{number})'.format(number=phone_number))		
def phone_alert():
	t_1.place(x=4444)
	t.place(x=4444)
	cancel.place(x=44444)
	root.deiconify()
	pro_1.stop()
	set_.config(command=reminder)
	auccont_Id=os.environ.get('MY_SID')
	auth_token=os.environ.get('MY_AUTH_TOKEN')
	c=Client(str(auccont_Id),str(auth_token))#say the task
	try:
		c.calls.create(from_='+19563985957',url='https://demo.twilio.com/docs/voice.xml',to=phone_number)
	except:
		messagebox.showinfo('Info','None Your Network Connection Or None The Phone Number You Entered (Your Phone Number-{number})'.format(number=phone_number))
		
def new_reminder():
	pass
def x():
	question=messagebox.askquestion('Message','Are You Sure To Quit? Reminder Will Be Run In BackGround If You Quit')
	if question=='yes':
		exit()
	if question=='no':
		None
def notification_():
	t_1.place(x=4444)
	t.place(x=4444)
	cancel.place(x=44444)
	root.deiconify()
	set_.config(command=reminder)
	if check==True:
		set_.config(command=reminder)
		pro_1.stop()
		notification.notify(
            	title = "Your reminder!",
                message=F"""{str(new_task)}""",)
	if check==False:
		set_.config(command=reminder)

		pro_1.stop()
		notification.notify(
            		title = "Your reminder!",
            		message=F"""{str(task_value_)}""",)
	set_.config(command=reminder)
def info():
	messagebox.showinfo('Message','Please Set A Task From Down Below Then Cilck On Set Remaind Button')
def main_pros():
	l.place(x=660,y=30)
	sez=(min_value.get())
	for_mula=sez*600# number genereter
	sez_1=(sec_value.get())
	for_mula_1=sez_1*10# create a stick man animtion!
	sez_2=(hour_value.get())
	for_mula_2=sez_2*6000
	pro_1['mode']='determinate'# create top level a python program that can short english sentence
	pro_1['value']=1000
	pro_1.start(for_mula+for_mula_1+for_mula_2)
	root.update()
def info1():
	messagebox.showinfo('Message','Another Remind Is Running Do You Want To Set Another reminder? If Yes Then Go To File Menu Then Click On New reminder Option.')
def cancel():#push this aganin
	pro_1.stop()
	global None_11
	None_11=True
	if Selected_Val==0:
		root.after_cancel(called_1)
		set_.config(command=reminder)
	if Selected_Val==1:
		root.after_cancel(called_2)
		set_.config(command=reminder)
	if Selected_Val==2:
		root.after_cancel(called_3)
		set_.config(command=reminder)
def reminder():
	if sec_value.get()>4 and min_value.get()>4 and hour_value.get()>4:
			messagebox.showinfo('Message','Please Add More Time!')	
	else:
		global time#
		global updated
		global called_1
		global called_2
		global called_3
		global t_1
		global t
		formula_to_find_seconds=sec_value.get()*1000
		formula_to_find_minutes=min_value.get()*60000
		formula_to_find_hours=hour_value.get()*3600000
		time=formula_to_find_seconds+formula_to_find_minutes+formula_to_find_hours
		which_alert()
		if Selected_Val==0:
			ask_phone_number()
			ques_1=messagebox.askquestion('Info','App Will Hide It self Do You Want To Hide It?')
			if ques_1=='no':
				updated=datetime.now().strftime('%r')
				timee=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r')
				messagebox.showinfo('Info',f'Time Set At {updated} And You Will Get A Sms At {timee}')
				t_1=ttk.Label(root,text=datetime.now().strftime('%r'))#HIDE TH AUTH_TOKEN
				t_1.place(x=570,y=80)
				cancel.place(x=665,y=80)
				t=ttk.Label(root,text=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r'))
				t.place(x=825,y=80)
				called_1=root.after(time,sms_alert)
				main_pros()
			if ques_1=='yes':
				updated=datetime.now().strftime('%r')
				timee=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r')
				messagebox.showinfo('Info',f'Time Set At {updated} And You Will Get A Sms At {timee}')
				root.withdraw()
				t_1=ttk.Label(root,text=datetime.now().strftime('%r'))#HIDE TH AUTH_TOKEN
				t_1.place(x=570,y=80)
				cancel.place(x=665,y=80)
				t=ttk.Label(root,text=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r'))
				t.place(x=825,y=80)
				called_1=root.after(time,sms_alert)
				main_pros()
		if Selected_Val==1:
			ask_phone_number()
			ques_2=messagebox.askquestion('Info','App Will Hide It self Do You Want To Hide It?')
			if ques_2=='yes':
				updated=datetime.now().strftime('%r')
				timee=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r')
				messagebox.showinfo('Info',f'Time Set At {updated} And You Will Get A Sms At {timee}')
				root.withdraw()
				t_1=ttk.Label(root,text=datetime.now().strftime('%r'))#HIDE TH AUTH_TOKEN
				t_1.place(x=570,y=80)
				cancel.place(x=665,y=80)
				t=ttk.Label(root,text=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r'))
				t.place(x=825,y=80)
				called_2=root.after(time,phone_alert)
				main_pros()
			if ques_2=='no':
				updated=datetime.now().strftime('%r')
				timee=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r')
				messagebox.showinfo('Info',f'Time Set At {updated} And You Will Get A Sms At {timee}')
				t_1=ttk.Label(root,text=datetime.now().strftime('%r'))#HIDE TH AUTH_TOKEN
				t_1.place(x=570,y=80)
				cancel.place(x=665,y=80)
				t=ttk.Label(root,text=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r'))
				t.place(x=825,y=80)
				called_2=root.after(time,phone_alert)
				main_pros()
		if Selected_Val==2:
			ques=messagebox.askquestion('Info','App Will Hide It self Do You Want To Hide it?')
			if ques=='yes':
				updated=datetime.now().strftime('%r')
				timee=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r')
				messagebox.showinfo('Info',f'Time Set At {updated} And You Will Get A Sms At {timee}')
				root.withdraw()
				t_1=ttk.Label(root,text=datetime.now().strftime('%r'))#HIDE TH AUTH_TOKEN
				cancel.place(x=665,y=80)
				t=ttk.Label(root,text=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r'))
				t_1.place(x=570,y=80)
				t.place(x=825,y=80)
				called_3=root.after(time,notification_)
				main_pros()
			if ques=='no':
				updated=datetime.now().strftime('%r')
				timee=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r')
				messagebox.showinfo('Info',f'Time Set At {updated} And You Will Get A Sms At {timee}')
				t_1=ttk.Label(root,text=datetime.now().strftime('%r'))#HIDE TH AUTH_TOKEN
				cancel.place(x=665,y=80)
				t=ttk.Label(root,text=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r'))
				t_1.place(x=570,y=80)
				t.place(x=825,y=80)
				called_3=root.after(time,notification_)
				main_pros()
def task_value():
	global check
	check=False
	global task_value_
	task_value_=task.get(1.0,END)
	if len(task.get("1.0", "end-1c")) == 0:# This Logic Came From https://stackoverflow.com/questions/38539617/tkinter-None-if-text-widget-is-empty
		question=messagebox.showinfo('Message','Please Put Something For Your Task!')
		set_.config(command=info)
	elif str(task.get(1.0,END)).isspace():
		question=messagebox.showinfo('Message','Please Put Something For Your Task!')
		set_.config(command=info)
	else:
		messagebox.showinfo('Message','Remind Set Successfully! Now Go And Set Your reminder')
		set_.config(command=reminder)
		update.place(x=500,y=340)
def update_task():
	global check
	global new_task
	new_task=task.get(1.0,END)
	check=True
	messagebox.showinfo('Info','Task Updated!')
root.protocol('WM_DELETE_WINDOW',x)
pro_1=Progressbar(root,length=250)
pro_1.place(x=600,y=60)
dat=StringVar()
l=ttk.Label(root,text='Progress Of Your Remind',font=('Time',10))
l.place(x=660,y=30)
menus = Menu(root)
m1 = Menu(menus, tearoff=0)
m1.add_command(label='New reminder')
root.config(menu=menus)
menus.add_cascade(label='File', menu=m1, )
root.maxsize(900,400)
root.minsize(900,400)
min_value=IntVar()
sec_value=IntVar()
hour_value=IntVar()
task=Text(root,width=15,height=5)
task.place(x=365,y=250)
root.title('Reminder Application For Windows')
start=ttk.Spinbox(root,from_=0,to=23,width=3,textvariable=hour_value,font=Font(family='times',size=15))
start.place(x=400,y=65)
start['state']='readonly'
hour=ttk.Label(root,text='Hour',font=('Times',13))
hour.place(x=340,y=65)
min_=ttk.Label(root,text='Minutes',font=('Times',13))
min_.place(x=330,y=100)
sec_=ttk.Label(root,text='Seconds',font=('Times',13))
sec_.place(x=330,y=139)# today sutdy-goal!!
Task_Identity=ttk.Label(root,text='What shall I remind you about? Write Down Below',font=('Times',11))
Task_Identity.place(x=300,y=220)
start_min=ttk.Spinbox(root,from_=0,to=59,width=3,textvariable=min_value,font=Font(root,family='times',size=15))
start_min.place(x=400,y=100)
start_min['state']='readonly'
start_sec=ttk.Spinbox(root,from_=0,to=59,width=3,textvariable=sec_value,font=Font(root,family='times',size=15))
start_sec.place(x=400,y=140)
start_sec['state']='readonly'
set_=ttk.Button(root,text='Set reminder',command=info)
set_.place(x=375,y=180)
set_task=ttk.Button(root,text='Set Remind',command=task_value)
set_task.place(x=385,y=340,)
update=ttk.Button(root,text='Click Me For Update Your Old Remind!',command=update_task)
cancel=ttk.Button(root,text='Cancel The Remaind',command=cancel)# None speelings,study today.
HEAd=ttk.Label(root,text="""After how long did you need a reminder from now?
	Set From Down Below""",font=('times',13))
HEAd.pack()
mainloop()# check at 1:20 am notifaction is send!
# End!
# CREATE bUTTON fOR  FOR CREATING NEW reminder
# use elif when there is a chance to get both satement true
# a softwarre that can short english sentence!
# use cd to switch in different folders use ; to add diffrent paths in one varible!!,a website that can load webpages faster!!!
# create bakend of alerts
# push
# add millseond option.
# create countdown timer is this app.
# create new reminder option.
# buy a voice api,sms api
# push this one again.
# clean github repo
# check reminder app is sending notifaction in a hour
# run tkinter in background when pc/laptop is turing on
# check all repos working fine.
# buy a voice api and create that api sayable
# check all projects and repos have no bugs!
# pythonw run remainder app.py
# tommrow task create new reminder option.

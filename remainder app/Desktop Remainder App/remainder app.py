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
min_value=IntVar()# create menus in reminder app and deice roling simulator
sec_value=IntVar()# ansea lib for sync audio to text!
hour_value=IntVar()#create stickman animation
get__=StringVar()
check_11=False

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
def c():
	notification.notify(title='Canceled..!',message='')
check_22=False#fix bugs.
def ask_phone_number():
	global check_22
	global phone_number
	phone_number=simpledialog.askstring(title='Phone Number',prompt='Enter Your Phone Number (With Contury Code Incuded)')
	check_22=True
	t_1=ttk.Label(root,text=datetime.now().strftime('%r'))#HIDE TH AUTH_TOKEN
	t_1.place(x=570,y=80)
	cancel.place(x=665,y=80)
	t=ttk.Label(root,text=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r'))
	t.place(x=825,y=80)
def sms_alert():
	global check_11
	pro_1.stop()
	set_.config(command=reminder)
	auccont_Id=os.environ.get('MY_SID')
	auth_token=os.environ.get('MY_AUTH_TOKEN')
	c=Client(auccont_Id,auth_token)
	if check_11==False:
		try:
			if check==False:
				c.messages.create(body=F"Hey! user You Need To Do {task_value_} At This Time Reply Yes To Confrom That You Reviced The Alert!",from_='+19563985957',to=phone_number)
			if check==True:
				c.messages.create(body=F"Hey! user You Need To Do {update_task} AT This Time Reply Yes To Confrom That You Reviced The Alert!",from_='+19563985957',to=phone_number)
		
		except:
			messagebox.showinfo('Info','Check Your Network Connection. Or Check The Phone Number You Entered (Your Phone Number-{number})'.format(number=phone_number))
			
	if check_11==True:
		pass
	# check anonther reminder app,correct sppelings,rename repo,small
		
def phone_alert():
	pro_1.stop()
	set_.config(command=reminder)
	auccont_Id=os.environ.get('MY_SID')
	auth_token=os.environ.get('MY_AUTH_TOKEN')
	print(auth_token,auccont_Id)
	c=Client(str(auccont_Id),str(auth_token))#say the task
	try:
		c.calls.create(from_='+19563985957',url='https://demo.twilio.com/docs/voice.xml',to=phone_number)
	except:
		messagebox.showinfo('Info','Check Your Network Connection Or Check The Phone Number You Entered (Your Phone Number-{number})'.format(number=phone_number))
		
def new_reminder():
	pass
def x():
	question=messagebox.askquestion('Message','Are You Sure To Quit? reminder Will Be Disabled If You Quit')
	if question=='yes':
		exit()
	if question=='no':
		None
def notification_():
	set_.config(command=reminder)
	if check==True:
		set_.config(command=reminder)

		pro_1.stop()
		notification.notify(
            	title = "Your reminder!",
                message=F"""{str(new_task)}""",)
		print('Here Is Your reminder!')
	if check==False:
		set_.config(command=reminder)

		pro_1.stop()
		notification.notify(
            		title = "Your reminder!",
            		message=F"""{str(task_value_)}""",)
		print('Here Is Your reminder!')
		# print(f'The Time Is Now {updated} Your Remaind Time!')
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
	root.update()#clean github repotries

def info1():
	messagebox.showinfo('Message','Another Remind Is Running Do You Want To Set Another reminder? If Yes Then Go To File Menu Then Click On New reminder Option.')
get__.set('Intaial value')
def cancel():
	pro_1.stop()
	global check_11
	check_11=True
	if Selected_Val==0:
		if check_22==True:
			pass
		if check_22==False:
			sms_alert()
		else:
			pass
	if Selected_Val==1:
		phone_alert()
	if Selected_Val==2:
		notification_()
def reminder():

	if sec_value.get()==0 and min_value.get()==0 and hour_value.get()==0:
			messagebox.showinfo('Message','Please Add More Time!')	
	#  a most used word in a programmer lif is ;
	else:
		global time# how to give a python to give 
		global updated
		global check_11
		print(check_11)
		print('''Remaind Is Running.... Please Don't Quit The Application. ''')
		formula_to_find_seconds=sec_value.get()*1000
		formula_to_find_minutes=min_value.get()*60000
		formula_to_find_hours=hour_value.get()*3600000
		time=formula_to_find_seconds+formula_to_find_minutes+formula_to_find_hours
		which_alert()
		if Selected_Val==0:
			check_11=False
			t_1=ttk.Label(root,text=datetime.now().strftime('%r'))#HIDE TH AUTH_TOKEN
			t_1.place(x=570,y=80)
			cancel.place(x=665,y=80)
			t=ttk.Label(root,text=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r'))
			t.place(x=825,y=80)
			ask_phone_number()
			root.after(time,sms_alert)
			main_pros()
		if Selected_Val==1:
			check_11=False
			t_1=ttk.Label(root,text=datetime.now().strftime('%r'))#HIDE TH AUTH_TOKEN
			t_1.place(x=570,y=80)
			cancel.place(x=665,y=80)
			t=ttk.Label(root,text=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r'))
			t.place(x=825,y=80)
			ask_phone_number()
			root.after(time,phone_alert)
			main_pros()
		if Selected_Val==2:
			t_1=ttk.Label(root,text=datetime.now().strftime('%r'))#HIDE TH AUTH_TOKEN
			cancel.place(x=665,y=80)
			print(time)
			t=ttk.Label(root,text=(datetime.now()+timedelta(seconds=sec_value.get(),minutes=min_value.get(),hours=hour_value.get())).strftime('%r'))
			t_1.place(x=570,y=80)
			t.place(x=825,y=80)
			root.after(time,notification_)
			main_pros()
def task_value():
	global check 
	check=False
	global task_value_
	task_value_=task.get(1.0,END)
	if len(task.get("1.0", "end-1c")) == 0:# This Logic Came From https://stackoverflow.com/questions/38539617/tkinter-check-if-text-widget-is-empty
		question=messagebox.showinfo('Message','Please Put Something For Your Task!')
		set_.config(command=info)
	elif str(task.get(1.0,END)).isspace():
		question=messagebox.showinfo('Message','Please Put Something For Your Task!')
		set_.config(command=info)
	else:
		messagebox.showinfo('Message','Remind Set Successfully! Now Go And Set Your reminder')
		set_.config(command=reminder)
		update.place(x=500,y=340)#stopwatch
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
print(sec_value)
l=ttk.Label(root,text='Progress Of Your Remind',font=('Time',10))
l.place(x=660,y=30)
# use elf when thre is a chance to get both satement true
menus = Menu(root)
m1 = Menu(menus, tearoff=0)
m1.add_command(label='New reminder')
m1.add_command(label='How To Use The Software?', command=quit)
root.config(menu=menus)
menus.add_cascade(label='File', menu=m1, )

root.maxsize(900,400)
root.minsize(900,400)
min_value=IntVar()
sec_value=IntVar()
hour_value=IntVar()
task=Text(root,width=15,height=5)
task.place(x=365,y=250)
root.title('reminder Application For Windows')
heading_label=ttk.Label(root,text='Desktop reminder App',font=('Times',19))
heading_label.pack()
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
cancel=ttk.Button(root,text='Cancel The Remaind',command=cancel)# check speelings,study today.
mainloop()
# End!
# CREATE bUTTON fOR  FOR CREATING NEW reminder
# use elif when there is a chance to get both satement true

# a softwarre that can short english sentence!
# use cd to switch in different folders use ; to add diffrent paths in one varible!!,a website that can load webpages faster!!!
# create bakend of alerts

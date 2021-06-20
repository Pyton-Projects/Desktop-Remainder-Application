from tkinter import*
from tkinter import ttk
import os
import json
from tkinter.ttk import Progressbar,Label
from twilio.rest import Client
from tkinter.font import Font
from tkinter import messagebox
from plyer import*
from ttkthemes import ThemedTk,THEMES
from datetime import datetime, timedelta
from tkinter import simpledialog
root=ThemedTk(themebg=True)
root.set_theme('arc')
min_value=IntVar()# create menus in remainder app and deice roling simulator
sec_value=IntVar()# ansea lib for sync audio to text!
hour_value=IntVar()
get__=StringVar()
def ask_phone_number():
	global phone_number
	phone_number=simpledialog.askstring(title='Phone Number',prompt='Enter Your Phone Number (With Contury Code Incuded)')


def sms_alert():
	
	pro_1.stop()
	set_.config(command=Remainder)
	auccont_Id='ACc40d20513c749b4a83d9beabae995ac1'
	auth_token='af5d09561c84a9e5d49a27a1144cd901'
	c=Client(auccont_Id,auth_token)
	c.messages.create(body="Hey! user It's Your Remainder!! Reply Yes To Confrom That You Reviced The Alert!",from_='+19563985957',to='+918896547119')

		
	
	# try:
	# 	if len(phone_number)<14:
	# 		messagebox.showinfo('Info','Please Enter A Vaild Phone Number')
	# 		pro_1.stop()
	# 	else:
	# 		pass
		
	# except:
	# 	pass
def phone_alert():#password:bts&&txt11bts&&txt11bts&&txt11
	

	pro_1.stop()
	set_.config(command=Remainder)
	"""Algorithm:
		ask a phone number
		wait till the timer hits the time
		if timer hits the time call the user"""
		
	auccont_Id='ACc40d20513c749b4a83d9beabae995ac1'
	auth_token='af5d09561c84a9e5d49a27a1144cd901'
	c=Client(auccont_Id,auth_token)
			
	c.calls.create(from_='+19563985957',url='https://demo.twilio.com/docs/voice.xml',to=phone_number)



def new_remainder():
	pass
			# CREATE bUTTON fOR  FOR CREATING NEW REMAINDER
		# use elif when there is a chance to get both satement true

		# a softwarre that can short english sentence!
		# use cd to switch in different folders use ; to add diffrent paths in one varible!!,a website that can load webpages faster!!!
		# create bakend of alerts
		#ask a question called how to install multiple packges at once in pip/python

def x():
	question=messagebox.askquestion('Message','Are You Sure To Quit? Remainder Will Be Disabled If You Quit')
	if question=='yes':
		exit()
	if question!='no':
		None
def notification_():
	l.config(text='')
	set_.config(command=Remainder)
	if check==True:
		set_.config(command=Remainder)

		pro_1.stop()
		notification.notify(
            	title = "Your Remainder!",
                message=F"""{str(new_task)}""",)
		print('Here Is Your Remainder!')
	if check==False:
		set_.config(command=Remainder)

		pro_1.stop()
		notification.notify(
            		title = "Your Remainder!",
            		message=F"""{str(task_value_)}""",)
		print('Here Is Your Remainder!')
		# print(f'The Time Is Now {updated} Your Remaind Time!')
	set_.config(command=Remainder)
def info():
	messagebox.showinfo('Message','Please Set A Task From Down Below Then Cilck On Set Remaind Button')
def main_pros():
	sez=(min_value.get())
	for_mula=sez*600# number genereter
	sez_1=(sec_value.get())
	for_mula_1=sez_1*10# create a stick man animtion!
	sez_2=(hour_value.get())
	for_mula_2=sez_2*6000
	pro_1['mode']='determinate'# create top level a python program that can short english sentence
	pro_1['length']=350
	pro_1['value']=1000
	pro_1.start(for_mula+for_mula_1+for_mula_2)
	root.update()
def info1():
	messagebox.showinfo('Message','Another Remind Is Running Do You Want To Set Another Remainder? If Yes Then Go To File Menu Then Click On New Remainder Option.')
l=Label(root)
get__.set('Intaial value')
def Remainder():
	print(get__.get())
	if sec_value.get()<4 and min_value.get()<4 and hour_value.get()<4:
			messagebox.showinfo('Message','Please Add More Time!')	
	#  a most used word in a programmer lif is ;
	else:
		global time# how to give a python to give 
		global updated
		print('''Remaind Is Running.... Please Don't Quit The Application. ''')
		formula_to_find_seconds=sec_value.get()*1000
		formula_to_find_minutes=min_value.get()*60000
		formula_to_find_hours=hour_value.get()*3600000
		time=formula_to_find_seconds+formula_to_find_minutes+formula_to_find_hours
		# # if sec_value.get()!=0 :
		if get__.get()=='2':
			#create a stickman animation.
			ask_phone_number()
			root.after(time,phone_alert)
			main_pros()#add memus!
				
			updated = ( datetime.now() +timedelta(hours=int(hour_value.get()),minutes=int(min_value.get()),seconds=sec_value.get())).strftime('%r')
			time_in_right_fromats=datetime.now().strftime('%r')

			set_.config(command=info1)#FIX WHEN WE CREATE ONE SECOND TIMER THE NOTIFACTION POPUP!

			l.config(text=f'The Time Set At {time_in_right_fromats} And You Will Get A Call At {updated}')
			l.pack()
	 

		if get__.get()=='3':
			ask_phone_number()
			root.after(time,sms_alert)

			main_pros()#add memus!

			

			updated = ( datetime.now() +timedelta(hours=int(hour_value.get()),minutes=int(min_value.get()),seconds=sec_value.get())).strftime('%r')
			time_in_right_fromats=datetime.now().strftime('%r')

			set_.config(command=info1)#FIX WHEN WE CREATE ONE SECOND TIMER THE NOTIFACTION POPUP!
			l.config(text=f'The Time Set At {time_in_right_fromats} And You Will Get A Sms At {updated}')
			l.pack()


		if get__.get()=='1':

			root.after(time,notification_)
			main_pros()#add memus!
			

			updated = ( datetime.now() +timedelta(hours=int(hour_value.get()),minutes=int(min_value.get()),seconds=sec_value.get())).strftime('%r')
			time_in_right_fromats=datetime.now().strftime('%r')

			set_.config(command=info1)#FIX WHEN WE CREATE ONE SECOND TIMER THE NOTIFACTION POPUP!

			l.config(text=f'The Time Set At {time_in_right_fromats} And You Will Get A Notifaction At {updated}')
			l.pack()


		if get__.get()=='Intaial value':
		
			messagebox.showinfo('Info','Please Select A Alert Type! (Beside The UI)  If You Already Selected A Alert Type Click On Set Remainder')
		


	
		# else:
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
		messagebox.showinfo('Message','Remind Set Suceesfully! Now Go And Set Your Alert Type!')
		set_.config(command=Remainder)
		update.place(x=500,y=340)
def update_task():
	global check
	global new_task
	new_task=task.get(1.0,END)
	check=True
	messagebox.showinfo('Info','Task Updated!')
root.protocol('WM_DELETE_WINDOW',x)
pro_1=Progressbar(root)	
pro_1.place(x=250,y=385)
l=Label(root,text='Remind Is Running...')# create stick man animation
root.maxsize(900,400)
root.minsize(900,400)
task=Text(root,width=17,height=5)
task.place(x=50,y=210)
root.title('Remainder Application For Windows')
heading_label=ttk.Label(root,text='Desktop Remainder App',font=('Times',19))
heading_label.pack()
start=ttk.Spinbox(root,from_=0,to=23,width=3,textvariable=hour_value,font=Font(family='times',size=15))
start.place(x=1,y=100)
start['state']='readonly'
hour=ttk.Label(root,text='Hour',font=('Times',13))
hour.place(x=10,y=70)
min_=ttk.Label(root,text='Minutes',font=('Times',13))
min_.place(x=70,y=70)
sec_=ttk.Label(root,text='Seconds',font=('Times',13))
sec_.place(x=140,y=70)#asepa lib to recgnize song by lyrics (:
Task_Identity=ttk.Label(root,text='Put Your Remaind Down Below I Will Remind You Through Your Selected Alert',font=('times',10,'bold'))
Task_Identity.place(x=1,y=185)
start_min=ttk.Spinbox(root,from_=0,to=59,width=3,textvariable=min_value,font=Font(root,family='times',size=15))
start_min.place(x=70,y=100)
start_min['state']='readonly'
start_sec=ttk.Spinbox(root,from_=0,to=59,width=3,textvariable=sec_value,font=Font(root,family='times',size=15))
start_sec.place(x=140,y=100)
start_sec['state']='readonly'
set_=ttk.Button(root,text='Set Remainder',command=info)
set_.place(x=50,y=140)# how to know mail is sent!
set_task=ttk.Button(root,text='Set Remind',command=task_value)
set_task.place(x=70,y=300,)
update=ttk.Button(root,text='Click Me For Update Your Old Remind!',command=update_task)
menus=Menu(root)
m1=Menu(menus,tearoff=0)
m1.add_command(label='New Remainder',command=new_remainder)
m1.add_command(label='How To Use The Software?',command=new_remainder)
root.config(menu=menus)# WHAT WE CALLED A ELEMNT IN A MENU.. # BEST BOOKS ON INOVOTION!
menus.add_cascade(label='File',menu=m1)
L=Label(root,text='Alert Type:-',font=('Times',13))
L.place(x=225,y=70)
l_1=Label(root,text='Sms Alert',font=('Times',12))
radio_sms=ttk.Radiobutton(root,value='3',variable=get__)
l_1.place(x=338,y=70)
radio_sms.place(x=310,y=70)
radio_call=ttk.Radiobutton(root,value='2',variable=get__)
radio_call.place(x=405,y=90)
l_2=Label(root,text='Call Alert',font=('Times',12))
l_2.place(x=433,y=90)
radio_email=ttk.Radiobutton(root,value='1',variable=get__)
radio_email.place(x=433+67,y=70)
l_3=Label(root,text='Windows Notifaction Alert',font=('Times',12))
l_3.place(x=433+95,y=70)

root.mainloop()
# CREATE bUTTON fOR  FOR CREATING NEW REMAINDER
# use elif when there is a chance to get both satement true

# a softwarre that can short english sentence!
# use cd to switch in different folders use ; to add diffrent paths in one varible!!,a website that can load webpages faster!!!
# create bakend of alerts

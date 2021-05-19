# Start
# -----------------------------------------------------------------------
from tkinter import*
from tkinter import filedialog
import tkinter.ttk
import PIL
import os
from PIL import Image 
root=Tk()
filters=('Blur','Smooth','Detail','Sharpen')
root.geometry('800x200')
root.maxsize(800,200)
root.minsize(800,200)
root.title('Image Compresser')
opend_file_path=Label(root,text=None)
saved_file_path=Label(root,text=None,fg='purple1')
quality=Label(root,text='Quality')
filters=Label(root,text='')
quality.place(x=510,y=65+2+2)
i=StringVar()
root.title("testing the combobox")
root.geometry('300x300+50+50')
filters='Blur','Smooth','Detail','Sharpen'
filters_ = tkinter.ttk.Combobox(root, values=filters,text=i,width=9)
filters_['state']='readonly'
quality=(50,60,70,80,90,100)
int_=IntVar()
int_.set(80)
quality_=tkinter.ttk.Combobox(root,values=quality,text=int_,width=9)
quality_['state']='readonly'
def closed():
    from tkinter import messagebox
    question=messagebox.askquestion('Question','Are You Sure To Quit?')
    if question=='yes':
        import sys
        sys.exit()
    else:
        None
root.protocol('WM_DELETE_WINDOW',closed)
def compress():
	try:
		img=PIL.Image.open(f'{filename.name}')
		my_1,my_2=img.size
		img=img.resize((my_1,my_2),PIL.Image.ANTIALIAS)
		save_=filedialog.asksaveasfilename()
		print(int_.get())
		img.save(save_+'.jpg',optimize=True,quality=int_.get())
		saved_file_path.config(text=f'Saved File Path- {save_}.jpg')
		saved_file_path.place(x=1,y=150)
		os.startfile(f'{save_}.jpg')
	except Exception:
		import tkinter.messagebox
		tkinter.messagebox.showwarning('Info','File Not Saved!')
		saved_file_path.config(text='')
def open_file_name():
    global filename
    filename=filedialog.askopenfile(filetypes=(('JPG Image','*.jpg'),(('JPG Image','*.jpg'))))
    if filename==None:
        compression_button.config(command='')
        opend_file_path.config(text='')
        import tkinter.messagebox
        tkinter.messagebox.showwarning('info','File Not Imported!')
    if filename!=None:
        compression_button.config(command=compress)
        opend_file_path.config(text=f'''Opened File Path- {filename.name}''')
        opend_file_path.place(x=1,y=175)# How To file is converted or not
heading=Label(root,text='Image Compresser',fg='Cyan4',font=("helvatica", 16, "bold italic"))
heading.pack()
compression_button=Button(root,text='Comprees',activeforeground='white',activebackground='black',fg='white',bg='black')
import_button=Button(root,text='Select A Image File',command=open_file_name,activeforeground='black',activebackground='light blue',fg='black',bg='light blue')# if filname is none then show then show a popup to  use my image converter to convert image you have if yes then import image converter.else:do nothing
import_button.place(x=300+10+5+5+10+10,y=49)
compression_button.place(x=310+10+10+10+10+10+5,y=89)# black white
quality_.place(x=500,y=90)
filters_.place(x=500,y=49)
mainloop()

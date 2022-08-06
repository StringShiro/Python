from tkinter import *

def show_frame(frame): #khai báo hàm đẩy frame nhờ vào .tkraise()
	frame.tkraise()

def quit():
	window.destroy()

	Label(typebox, text='Your name: ').place(x=20,y=0)
	entry1 = Entry(typebox,bd = 5).place(x=140,y=70)
def show_aboutus():
	win = Tk()
	win.geometry("500x500")
	win.configure(height=500, width=500)
	win.columnconfigure(0, weight =1)
	win.rowconfigure(0, weight =1)
	win.title('About us')
	
	AU_canvas = Canvas(win, bg ='Grey', height = 720, width = 1280, relief = 'ridge')
	AU_canvas.place(x=0,y=0)
	AU_title1 = Label(win,text='Thành viên nhóm:').pack()
	AU_title2 = Label(win,text='Nguyễn Phan Bảo Quý').pack()
	AU_title3 = Label(win,text='Vương Minh Trí').pack()
	AU_title4 = Label(win,text='Trần Gia Bảo').pack()
	AU_title5 = Label(win,text='Phạm Hồ Tấn Đạt').pack()
	AU_title6 = Label(win,text='----------------').pack()
	AU_title7 = Label(win,text='Lớp 20BITV02').pack()
	AU_title8 = Label(win,text='Giảng viên: Lê Hoàng Việt Tuấn').pack()
	return_btn = Button(win, text = 'RETURN', command = lambda:win.destroy())
	return_btn.place(x = 177, y = 407,width = 160,height=66)

#tạo cửa sổ tkinter, định nghĩa lại vị trí xuất hiện
window = Tk()
window.geometry("1280x720")
window.configure(height=720 , width =1280)
window.columnconfigure(0, weight =1)
window.rowconfigure(0, weight =1)
window.title('Treasure Hunter')

#tạo các frame
Frame_bg = Frame(window)
Frame_correct = Frame(window)
Frame_incorrect = Frame(window)
Frame_replay = Frame(window)
Frame_intro = Frame(window,bg='black')
Frame_q1 = Frame(window)
Frame_q2 = Frame(window)
Frame_q3 = Frame(window)
Frame_q4 = Frame(window)
Frame_q5 = Frame(window)

#vòng lặp để hiển thị các frame liên tục
for frame in (Frame_bg,Frame_correct,Frame_incorrect,Frame_q1,Frame_q2,Frame_intro,
				Frame_replay,Frame_q3,Frame_q4,Frame_q5):
	frame.grid(row=0,column=0, sticky = 'nsew')

#-------------------------------------------------------------------------------------------------------
#tạo introduction
Intro = Label(Frame_intro, text= 'Đây là quiz game',fg ='white',bg = 'black', font = "Helvetica 30 bold").pack()
Intro1 = Label(Frame_intro, text= 'Được làm bởi team từ lớp 20BITV02',fg ='white',bg = 'black', font = "Helvetica 30 bold").pack()
Intro2 = Label(Frame_intro, text= 'Giảng viên hướng dẫn chúng em là thầy Lê Hoàng Việt Tuấn',fg ='white',bg = 'black', font = "Helvetica 30 bold").pack()
intro_btn = Button(Frame_intro,text='Play', command = lambda:question1())
intro_btn.place(x=490,y=300, width=307, height=58)
#-------------------------------------------------------------------------------------------------------

#tạo frame thắng game
Frame_replay_canvas = Canvas(Frame_replay, height = 720, width = 1280, relief = 'ridge')
Frame_replay_canvas.pack(anchor='center')
replay_img = PhotoImage(file = f'C:/Users/Dell/Downloads/Giao dien Final/Win/background.png')
replay_canvas = Frame_replay_canvas.create_image(640.0,360.0,image=replay_img)

replay_btn = Button(Frame_replay,text='Replay', command = lambda:show_frame(Frame_q1))
replay_btn.place(x = 470, y = 300,width = 307,height = 58)

menu_btn = Button(Frame_replay,text='Return to Menu', command = lambda:show_frame(Frame_bg))
menu_btn.place(x = 470, y = 500,width = 307,height = 58)

#-------------------------------------------------------------------------------------------------------
#tạo frame trả lời đúng
Frame_c_canvas = Canvas(Frame_correct, height = 720, width = 1280, relief = 'ridge')
Frame_c_canvas.pack(anchor='center')
correct_img = PhotoImage(file = f'C:/Users/Dell/Downloads/Giao dien Final/Right/background.png')
correct_canvas = Frame_c_canvas.create_image(640.0,360.0,image=correct_img)

#tạo frame trả lời sai
Frame_i_canvas = Canvas(Frame_incorrect, height = 720, width = 1280, relief = 'ridge')
Frame_i_canvas.pack(anchor='center')
incorrect_img = PhotoImage(file = f'C:/Users/Dell/Downloads/Giao dien Final/Wrong/background.png')
incorrect_canvas = Frame_i_canvas.create_image(640.0,360.0,image=incorrect_img)

#-------------------------------------------------------------------------------------------------------

# tạo background và menu
Frame_bg_canvas = Canvas(Frame_bg, height = 720, width = 1280, relief = 'ridge')
Frame_bg_canvas.pack(anchor='center')
bg_img = PhotoImage(file = f'C:/Users/Dell/Downloads/Giao dien Final/game_entry/background.png')
bg_canvas = Frame_bg_canvas.create_image(640.0,360.0,image=bg_img)

#nút start
start_btn = Button(Frame_bg,text='Start', command = lambda:show_frame(Frame_intro))
start_btn.place(x = 512, y = 400,width = 307,height = 58)

#nút About us
AU_btn = Button(Frame_bg, text = 'About us', command = lambda:show_aboutus())
AU_btn.place(x = 512, y = 486,width = 307,height = 58)

#nút Quit
Quit_btn = Button(Frame_bg, text = 'Quit', command = lambda:quit())
Quit_btn.place(x = 512, y = 571,width = 307,height = 58)

#-------------------------------------------------------------------------------------------------------
def question1():
	show_frame(Frame_q1)
	Frame_q1_canvas = Canvas(Frame_q1, bg ='#c94747', height = 720, width = 1280, relief = 'ridge')
	Frame_q1_canvas.place(x=0,y=0)
	Frame_q1_title1 = Label(Frame_q1,text='BÁC HỒ RA ĐI TÌM ĐƯỜNG CỨU NƯỚC',fg='white',bg = '#c94747', font = "Helvetica 50 bold")
	Frame_q1_title1.pack()
	Frame_q1_title2 = Label(Frame_q1,text='VÀO NGÀY THÁNG NĂM NÀO?',fg='white',bg = '#c94747', font = "Helvetica 50 bold")
	Frame_q1_title2.pack()

	A_q1_btn = Button(Frame_q1, text = '05/06/1911', command = lambda:show_frame(Frame_correct))
	A_q1_btn.place(x=150,y=432,width = 300,height=87)
	B_q1_btn = Button(Frame_q1, text = '04/05/1991', command = lambda:show_frame(Frame_incorrect))
	B_q1_btn.place(x=750,y=432,width = 300,height=87)
	C_q1_btn = Button(Frame_q1, text = '14/05/1911', command = lambda:show_frame(Frame_incorrect))
	C_q1_btn.place(x = 150, y = 560,width = 300,height=87)
	D_q1_btn = Button(Frame_q1, text = '15/06/1991', command = lambda:show_frame(Frame_incorrect))
	D_q1_btn.place(x = 750, y = 560,width = 300,height=87)
	Cnext1_btn = Button(Frame_correct,text='Next', command = lambda:question2())
	Cnext1_btn.place(x = 240, y = 220,width = 307,height = 58)

	Inext1_btn = Button(Frame_incorrect,text='Next', command = lambda:question2())
	Inext1_btn.place(x = 500, y = 350,width = 307,height = 58)

#-------------------------------------------------------------------------------------------------------
	def question2():
		show_frame(Frame_q2)
		Frame_q2_canvas = Canvas(Frame_q2, bg ='#c94747', height = 720, width = 1280, relief = 'ridge')
		Frame_q2_canvas.place(x=0,y=0)
		Frame_q2_title = Label(Frame_q2,text='Game of the year 2021?',fg='white',bg = '#c94747', font = "Helvetica 50 bold")
		Frame_q2_title.pack()

		A_q2_btn = Button(Frame_q2, text = 'Control', command = lambda:show_frame(Frame_incorrect))
		A_q2_btn.place(x=150,y=432,width = 300,height=87)
		B_q2_btn = Button(Frame_q2, text = 'Hitman 3', command = lambda:show_frame(Frame_incorrect))
		B_q2_btn.place(x=750,y=432,width = 300,height=87)
		C_q2_btn = Button(Frame_q2, text = 'It takes two', command = lambda:show_frame(Frame_correct))
		C_q2_btn.place(x = 150, y = 560,width = 300,height=87)
		D_q2_btn = Button(Frame_q2, text = 'Resident Evil Village', command = lambda:show_frame(Frame_incorrect))
		D_q2_btn.place(x = 750, y = 560,width = 300,height=87)

		Cnext2_btn = Button(Frame_correct,text='Next', command = lambda:question3())
		Cnext2_btn.place(x = 240, y = 220,width = 307,height = 58)

		Inext2_btn = Button(Frame_incorrect,text='Next', command = lambda:question3())
		Inext2_btn.place(x = 500, y = 350,width = 307,height = 58)
#-------------------------------------------------------------------------------------------------------
		def question3():
			show_frame(Frame_q3)
			Frame_q3_canvas = Canvas(Frame_q3, bg ='#c94747', height = 720, width = 1280, relief = 'ridge')
			Frame_q3_canvas.place(x=0,y=0)
			Frame_q3_title1 = Label(Frame_q3,text='Có bao nhiêu đại dương',fg='white',bg = '#c94747', font = "Helvetica 50 bold")
			Frame_q3_title1.pack()
			Frame_q3_title2 = Label(Frame_q3,text='được công nhận trên thế giới?',fg='white',bg = '#c94747', font = "Helvetica 50 bold")
			Frame_q3_title2.pack()


			A_q3_btn = Button(Frame_q3, text = '3', command = lambda:show_frame(Frame_incorrect))
			A_q3_btn.place(x=150,y=432,width = 300,height=87)
			B_q3_btn = Button(Frame_q3, text = '7', command = lambda:show_frame(Frame_incorrect))
			B_q3_btn.place(x=750,y=432,width = 300,height=87)
			C_q3_btn = Button(Frame_q3, text = '5', command = lambda:show_frame(Frame_correct))
			C_q3_btn.place(x = 150, y = 560,width = 300,height=87)
			D_q3_btn = Button(Frame_q3, text = '6', command = lambda:show_frame(Frame_incorrect))
			D_q3_btn.place(x = 750, y = 560,width = 300,height=87)

			Cnext3_btn = Button(Frame_correct,text='Next', command = lambda:question4())
			Cnext3_btn.place(x = 240, y = 220,width = 307,height = 58)

			Inext3_btn = Button(Frame_incorrect,text='Next', command = lambda:question4())
			Inext3_btn.place(x = 500, y = 350,width = 307,height = 58)

#-------------------------------------------------------------------------------------------------------
			def question4():
				show_frame(Frame_q4)
				Frame_q4_canvas = Canvas(Frame_q4, bg ='#c94747', height = 720, width = 1280, relief = 'ridge')
				Frame_q4_canvas.place(x=0,y=0)
				Frame_q4_title = Label(Frame_q4,text='Có gan ăn cắp,có gan____________',fg='white',bg = '#c94747', font = "Helvetica 50 bold")
				Frame_q4_title.pack()
				A_q4_btn = Button(Frame_q4, text = 'ăn vạ', command = lambda:show_frame(Frame_incorrect))
				A_q4_btn.place(x=150,y=432,width = 300,height=87)
				B_q4_btn = Button(Frame_q4, text = 'phản đòn', command = lambda:show_frame(Frame_incorrect))
				B_q4_btn.place(x=750,y=432,width = 300,height=87)
				C_q4_btn = Button(Frame_q4, text = 'chịu đựng', command = lambda:show_frame(Frame_incorrect))
				C_q4_btn.place(x = 150, y = 560,width = 300,height=87)
				D_q4_btn = Button(Frame_q4, text = 'chịu đòn', command = lambda:show_frame(Frame_correct))
				D_q4_btn.place(x = 750, y = 560,width = 300,height=87)

				Cnext4_btn = Button(Frame_correct,text='Next', command = lambda:question5())
				Cnext4_btn.place(x = 240, y = 220,width = 307,height = 58)

				Inext4_btn = Button(Frame_incorrect,text='Next', command = lambda:question5())
				Inext4_btn.place(x = 500, y = 350,width = 307,height = 58)
#-------------------------------------------------------------------------------------------------------
				def question5():
					show_frame(Frame_q5)
					Frame_q5_canvas = Canvas(Frame_q5, bg ='#c94747', height = 720, width = 1280, relief = 'ridge')
					Frame_q5_canvas.place(x=0,y=0)
					Frame_q5_title1 = Label(Frame_q5,text='Đội bóng nào có số lần vô địch',fg='white',bg = '#c94747', font = "Helvetica 50 bold")
					Frame_q5_title1.pack()
					Frame_q5_title2 = Label(Frame_q5,text='Champions League nhiều nhất?',fg='white',bg = '#c94747', font = "Helvetica 50 bold")
					Frame_q5_title2.pack()

					A_q5_btn = Button(Frame_q5, text = 'Manchester United', command = lambda:show_frame(Frame_incorrect))
					A_q5_btn.place(x=150,y=432,width = 300,height=87)
					B_q5_btn = Button(Frame_q5, text = 'Real Madrid', command = lambda:show_frame(Frame_correct))
					B_q5_btn.place(x=750,y=432,width = 300,height=87)
					C_q5_btn = Button(Frame_q5, text = 'Liverpool', command = lambda:show_frame(Frame_incorrect))
					C_q5_btn.place(x = 150, y = 560,width = 300,height=87)
					D_q5_btn = Button(Frame_q5, text = 'Paris Saint-Germain', command = lambda:show_frame(Frame_incorrect))
					D_q5_btn.place(x = 750, y = 560,width = 300,height=87)
		
					Cnext5_btn = Button(Frame_correct,text='Next', command = lambda:show_frame(Frame_replay))
					Cnext5_btn.place(x = 240, y = 220,width = 307,height = 58)

					Inext5_btn = Button(Frame_incorrect,text='Next', command = lambda:show_frame(Frame_replay))
					Inext5_btn.place(x = 500, y = 350,width = 307,height = 58)

show_frame(Frame_bg)


window.resizable(False, False)
window.mainloop()


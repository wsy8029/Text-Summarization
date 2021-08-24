from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

win = Tk()
win.geometry("1200x550+100+100")
win.title("자기소개서 요약 v0.1")

frame = Frame(win)
frame.pack()
canvas = Canvas(frame, bd=0, width=500, height=120)
canvas.pack()

# 로고 이미지 파일 리사이즈
logo_img= Image.open("logo.png")
resized_image= logo_img.resize((250,60), Image.ANTIALIAS)
new_logo= ImageTk.PhotoImage(resized_image)
canvas.create_image(250,50,anchor=CENTER, image=new_logo)
# label = Label(win)
# label.pack()
# label.img= PhotoImage(file = 'logo.png')
# label.config(image = label.img,compound = 'bottom', fg='black')

win.mainloop()



# from tkinter import *
# from PIL import Image, ImageTk
# root = Tk()
# root.title("Game")
# frame = Frame(root)
# frame.pack()
# canvas = Canvas(frame, bd=0, width=1000, height=400)
# canvas.pack()

# img= Image.open("logo.png")
# resized_image= img.resize((500,120), Image.ANTIALIAS)
# new_image= ImageTk.PhotoImage(resized_image)

# background = PhotoImage(file="logo.png")
# canvas.create_image(350,200,image=new_image)
# # character = PhotoImage(file="hero.png")
# # canvas.create_image(30,30,image=character)
# root.mainloop()
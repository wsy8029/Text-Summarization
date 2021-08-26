from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

# win = Tk()
# win.geometry("1200x550+100+100")
# win.title("LUXROBO 자기소개서 요약 시스템 v0.1")

# frame = Frame(win)
# frame.pack()
# canvas = Canvas(frame, bd=0, width=500, height=120)
# canvas.pack()

# # 로고 이미지 파일 리사이즈
# logo_img= Image.open("logo.png")
# resized_image= logo_img.resize((250,60), Image.ANTIALIAS)
# new_logo= ImageTk.PhotoImage(resized_image)
# canvas.create_image(250,50,anchor=CENTER, image=new_logo)

# win.mainloop()

class MyFrame(Frame):
    def __init__(self, master):
        self.master = master
        self.master.title("LUXROBO 자기소개서 요약 시스템 v0.1")
        # self.pack(fill=BOTH, expand=True)
        frame = Frame(self)
        # frame.pack()



def main():
    root = Tk()
    root.geometry("1200x550+100+100")

    label = Label(root)
    label.pack()

    app = MyFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

class MyFrame():
    def __init__(self):
        self.win = Tk()
        self.win.geometry("1200x550+100+100")
        self.win.title("LUXROBO 자기소개서 요약 시스템 v0.1")
        self.frame = Frame(self.win)
        self.frame.pack(fill=X)
        # self.canvas = Canvas(self.frame, bd=0, width=500, height=120)
        self.canvas = Canvas(self.frame, bd=0, width=500, height=120)
        self.canvas.pack(fill=X)
        
        # 로고 이미지 파일 리사이즈
        self.logo_img= Image.open("logo.png")
        self.resized_image= self.logo_img.resize((250,60), Image.ANTIALIAS)
        self.new_logo= ImageTk.PhotoImage(self.resized_image)
        self.canvas.create_image(600,60,anchor=CENTER, image=self.new_logo)


        labeltext = Label(self.frame, text="원문 텍스트 입력", width=10)
        labeltext.pack(side=LEFT, padx=10, pady=10)
 
        self.inputURL = StringVar()
        entryURL = Entry(self.frame, textvariable = self.inputURL)
        entryURL.pack(fill=X, padx=10, expand=True)



        self.win.mainloop()



def main():

    app = MyFrame()
    # root.mainloop()

if __name__ == '__main__':
    main()
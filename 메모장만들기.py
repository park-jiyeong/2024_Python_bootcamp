import tkinter as tkt
from tkinter import messagebox

def new_file():
      text_area.delete('1.0', tkt.END)
def save_file():
     file_content = text_area.get('1.0', tkt.END)
     try:
        with open("saved_file.txt", "w") as file:
            file.write(file_content)
        messagebox.showinfo("저장 완료", "파일이 성공적으로 저장되었습니다.")
     except Exception as e:
        messagebox.showerror("에러", f"파일 저장 중 오류가 발생하였습니다: {e}")

def maker():
     messagebox.showinfo("제작자 정보", "이 프로그램은 사용자가 직접 작성했습니다.")


#윈도우 생성하기
window = tkt.Tk()
window.title("Notepad")
window.geometry('400x400+800+300') #창의 크기(너비 높이) 창의 위치
window.resizable(0,0)


#아이콘 넣기
window.iconbitmap("D:/부트캠프/notepad-icon_34386.ico")


#텍스트 창 만들기
text_area = tkt.Text(window)
#공백 설정하기
window.grid_rowconfigure(0, weight = 1)
window.grid_columnconfigure(0, weight = 1)
#텍스트 화면을 윈도우에 동서남북으로 붙인다
text_area.grid(sticky = "N"+"E"+"S"+"W")

#메뉴 생성
menuMaker = tkt.Menu(window)
#첫번째 메뉴 만들기
first_menu =tkt.Menu(menuMaker, tearoff = 0)

first_menu.add_command(label = '새 파일', command = new_file)
first_menu.add_command(label = '저장', command = save_file)

menuMaker.add_cascade(label='파일', menu=first_menu)

window.config(menu =menuMaker)
window.mainloop() #항상 마지막에 꼭 써줘야함, 안하면 창 안열림
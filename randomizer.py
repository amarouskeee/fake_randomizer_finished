from tkinter import *
from tkinter import Tk



checkmates = {1:'penis',
               2: ' boop',
               3:'cheee'}


print(f'Победитель:{checkmates[3]}')

root = Tk()
root.title('RandSpot')


root.geometry('800x520')
#bg_photo = PhotoImage(file='(G:\w11.jpg)')
#root_bg  = Label(root, bg=)
photo = ()
root.config(bg='photo')

frame_b = Frame()
frame_a = Frame()

label_a = Label(master=frame_a, text='Розыгрыш Iphone 13')
label_b = Label(master=frame_b, text=f'Всего участников: 11 957')
label_b.pack()
label_a.pack()


frame_b.pack()
frame_a.pack()


textBox = Text(root)
textBox.pack()

lab = Label(root)
lab.pack()

btn = Button(root, text='Выбрать')
btn.frame = Frame(root,
                  relief=RAISED,
                  borderwidth=2,
                  width=20,
                  height=15)
btn.pack(pady=5,padx=3)


def getting_text(event):
    res = 'wh.r.uu'
    textBox.delete('1.0', END)
    lab['text'] = res


btn.bind('<Button-1>', getting_text)


root.mainloop()
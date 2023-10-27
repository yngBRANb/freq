#импортируем библиотеки в проект(мусор если честно)
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import fileinput
import matplotlib as mpl

mpl.rcParams['font.family'] = 'fantasy'
mpl.rcParams['font.fantasy'] = 'Comic Sans MS, Arial'
#Рисуем картинки
def w_open_ing():
    aa=ord('a')
    bb=ord('z')
    op = askopenfilename()
    main(op,aa,bb)
#Открываем русский алфавит
def w_open_rus():
    aa=ord('а')
    bb=ord('ё')
    op = askopenfilename()
    main(op,aa,bb)
#Обработка и отрисовка данных в таблицу
def main(op,aa,bb):
    alpha = [chr(w) for w in range(aa,bb+1)]   
    f = open(op , 'r') 
    text = f.read()
    f.close()
    alpha_text = [w.lower() for w in text if w.isalpha()]   
    k={}      
    for i in alpha:     
        alpha_count =0
        for item in alpha_text:
            if item==i:
                alpha_count = alpha_count + 1
        k[i]= alpha_count
    z=0
    #рисуем табличку
    for i in   alpha:      
        z=z+k[i]
    a_a=[]
    b_b=[]
    t= ('|\tсимвол\t|\tкол-во\t|\tпроценты,%\t\n')
    txt.insert(END,t)
    t=('|----------------------------|-----------------------------|---------------------------|\n')
    txt.insert(END,t)
    #Считаем проценты попадания букв в тексте
    for i in  alpha:       
        persent = round(k[i] * 100.0 / z,2)
        t=( '|\t%s\t|\t%d\t|\t%s\t\n' % (i, k[i], persent))
        txt.insert(END,t)
        a_a.append(i)
        b_b.append(k[i])
    t=('|----------------------------|-----------------------------|---------------------------|\n' )
    txt.insert(END,t)
    t=('Total letters: %d\n' % z)
    txt.insert(END,t)
    people=a_a     
    y_pos = np.arange(len(people))
    performance =b_b     
    #еще одна отрисовка визуала
    plt.barh(y_pos, performance)
    plt.yticks(y_pos, people)
    plt.xlabel('ХЫ, надо бы сопоставлять их с таблицей, но я устал это делать')
    plt.title('Частотность')
    plt.show()       
#очистка текста
def clear_text():
    txt.delete(1.0, END)
#Сохранение файла, но пока сыровато    
def save_file():
    save_as = asksaveasfilename()
    try:
        x =txt.get(1.0, END) 
        f = open(save_as, "w")
        f.writelines(x.encode('utf8'))
        f.close()
    except:
        pass
#Закрываем программу
def close_win():
    if askyesno("Выйти", "рофлишь?"):
        tk.destroy()
#Отрисовка программы и подвязка функций к кнопкам        
tk= Tk()
main_menu = Menu(tk)
tk.config(menu=main_menu)
file_menu = Menu(main_menu)
main_menu.add_cascade(label="Меню", menu=file_menu)
file_menu.add_command(label="English text", command= w_open_ing)
file_menu.add_command(label="Русский текст", command= w_open_rus)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_command(label="очистить", command=clear_text)
file_menu.add_command(label="Выйти", command=close_win)
txt = Text(tk, width=72,height=10,font="Arial 12",wrap=WORD)
txt.pack()
tk.mainloop()

print("\n--------------------------\n     MADE BY yngBRANb \n      Никита Карпов\n--------------------------\n")
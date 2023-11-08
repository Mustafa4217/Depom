import tkinter as tk
import time

def button1():
    global para
    global al
    ekrana_yazdir.config(text="Su Seçildi Fiyat 5 TL")
    ekrana_yazdir2.config(text='Lütfen bakiye giriniz.')
    para = int(odeme_giris.get())
    def al():
        global para
        if para >= 5 :
            para -= 5
            ekrana_yazdir2.config(text='Suyunuz Veriliyor...')
            ekrana_yazdir1.config(text=f"Kalan bakiye {para}")
        elif para < 5:
            ekrana_yazdir2.config(text='Yetersiz bakiye')
        odeme_giris.delete(0, tk.END)
        odeme_giris.insert(0, para)
        

def button2():
    global para
    global al
    ekrana_yazdir.config(text="Gazoz Seçildi Fiyat 7 TL")
    ekrana_yazdir2.config(text='Lütfen bakiye giriniz.')
    para = int(odeme_giris.get())
    def al():
        global para
        if para >= 7 :
            para -= 7
            ekrana_yazdir2.config(text='Gazozunuz Veriliyor...')
            ekrana_yazdir1.config(text=f"Kalan bakiye {para}")
        elif para < 7:
            ekrana_yazdir2.config(text='Yetersiz bakiye')
        odeme_giris.delete(0, tk.END)
        odeme_giris.insert(0, para)
def button3():
    global para
    global al
    ekrana_yazdir.config(text="Kola Seçildi Fiyat 8 TL")
    ekrana_yazdir2.config(text='Lütfen bakiye giriniz.')
    para = int(odeme_giris.get())
    def al():
        global para
        if para >= 8 :
            para -= 8
            ekrana_yazdir2.config(text='Kolanız Veriliyor...')
            ekrana_yazdir1.config(text=f"Kalan bakiye {para}")
        elif para < 8:
            ekrana_yazdir2.config(text='Yetersiz bakiye')
        odeme_giris.delete(0, tk.END)
        odeme_giris.insert(0, para)

def button4():
    global para
    global al
    ekrana_yazdir.config(text="Soğuk Kahve Seçildi Fiyat 24 TL")
    ekrana_yazdir2.config(text='Lütfen bakiye giriniz.')
    para = int(odeme_giris.get())
    def al():
        global para
        if para >= 24 :
            para -= 24
            ekrana_yazdir2.config(text='Soğuk Kahveniz Veriliyor...')
            ekrana_yazdir1.config(text=f"Kalan bakiye {para}")
        elif para < 24:
            ekrana_yazdir2.config(text='Yetersiz bakiye')
        odeme_giris.delete(0, tk.END)
        odeme_giris.insert(0, para)

def button5():
    global para
    global al
    ekrana_yazdir.config(text="Soda Seçildi Fiyat 4 TL")
    ekrana_yazdir2.config(text='Lütfen bakiye giriniz.')
    para = int(odeme_giris.get())
    def al():
        global para
        if para >= 4 :
            para -= 4
            ekrana_yazdir2.config(text='Sodanız Veriliyor...')
            ekrana_yazdir1.config(text=f"Kalan bakiye {para}")
        elif para < 4:
            ekrana_yazdir2.config(text='Yetersiz bakiye')
        odeme_giris.delete(0, tk.END)
        odeme_giris.insert(0, para)

def button6():
    global para
    global al
    ekrana_yazdir.config(text="Kek Seçildi Fiyat 6 TL")
    ekrana_yazdir2.config(text='Lütfen bakiye giriniz.')
    para = int(odeme_giris.get())
    def al():
        global para
        if para >= 6 :
            para -= 6
            ekrana_yazdir2.config(text='Kekiniz Veriliyor...')
            ekrana_yazdir1.config(text=f"Kalan bakiye {para}")
        elif para < 6:
            ekrana_yazdir2.config(text='Yetersiz bakiye')
        odeme_giris.delete(0, tk.END)
        odeme_giris.insert(0, para)

def button7():
    global para
    global al
    ekrana_yazdir.config(text="Çikolata Seçildi Fiyat 7 TL")
    ekrana_yazdir2.config(text='Lütfen bakiye giriniz.')
    para = int(odeme_giris.get())
    def al():
        global para
        if para >= 7 :
            para -= 7
            ekrana_yazdir2.config(text='Çikolatanız Veriliyor...')
            ekrana_yazdir1.config(text=f"Kalan bakiye {para}")
        elif para < 7:
            ekrana_yazdir2.config(text='Yetersiz bakiye')
        odeme_giris.delete(0, tk.END)
        odeme_giris.insert(0, para)

def button8():
    global para
    global al
    ekrana_yazdir.config(text="Meyve Suyu Seçildi Fiyat 4 TL")
    ekrana_yazdir2.config(text='Lütfen bakiye giriniz.')
    para = int(odeme_giris.get())
    def al():
        global para
        if para >= 4 :
            para -= 4
            ekrana_yazdir2.config(text='Meyve Suyunuz Veriliyor...')
            ekrana_yazdir1.config(text=f"Kalan bakiye {para}")
        elif para < 4:
            ekrana_yazdir2.config(text='Yetersiz bakiye')
        odeme_giris.delete(0, tk.END)
        odeme_giris.insert(0, para)

def button9():
    global para
    global al
    ekrana_yazdir.config(text="Kraker Seçildi Fiyat 5 TL")
    ekrana_yazdir2.config(text='Lütfen bakiye giriniz.')
    para = int(odeme_giris.get())
    def al():
        global para
        if para >= 5 :
            para -= 5
            ekrana_yazdir2.config(text='Krakeriniz Veriliyor...')
            ekrana_yazdir1.config(text=f"Kalan bakiye {para}")
        elif para < 5:
            ekrana_yazdir2.config(text='Yetersiz bakiye')
        odeme_giris.delete(0, tk.END)
        odeme_giris.insert(0, para)


def button10():
    global para
    if para > 0:
        ekrana_yazdir1.config(text=f'para üstünüz {para} TL veriliyor... ')
        para = 0

    if para == 0:
        komut()
    
def button11():
    al()

# yarisi bana ait olmayan kod--------------------------------------
def wait(f):
    def start():
        g = f()
        def repeater():
            try:
                pencere.after(next(g) * 1000, repeater)
            except StopIteration:
                pass
        repeater()
    return start

@wait
def komut():
    yield 3 # bir saniye bekliyor
    ekrana_yazdir1.config(text=f'Bakiyeniz 0 ekran temizleniyor... ')
    odeme_giris.delete(0, tk.END)
    yield 3 # üç saniye bekliyor
    ekrana_yazdir.configure(text="")
    ekrana_yazdir1.configure(text="")
    ekrana_yazdir2.configure(text="")
#------------------------------------------------------------

pencere = tk.Tk()
pencere.geometry('605x450')
pencere.title('Otomat Makinesi')

resim = tk.PhotoImage(file = "eklee.png")

arka_plan = tk.Label(pencere, image = resim).pack()

yazi = tk.Label(text='Bakiye Giriş', font='Times 16 ')
yazi.place(x=358, y=170)

ekrana_yazdir = tk.Label(text="", bg="#0191c5", font='Times 16 ')
ekrana_yazdir.place(x=300, y=25)

ekrana_yazdir1 = tk.Label(text="", bg='#0191c5', font='Times 16 ')
ekrana_yazdir1.place(x=300, y=75)

ekrana_yazdir2 = tk.Label(text="", bg='#0191c5', font='Times 16 ')
ekrana_yazdir2.place(x=300, y=50)

odeme_giris = tk.Entry(font='Times 18 bold')
odeme_giris.place(x=300, y=200)

buton1 = tk.Button(text=' 1 ', bg='black', fg='white', font='Times 24 bold', command=button1)
buton1.place(x=50, y=190)

buton2 = tk.Button(text=' 2 ', bg='black', fg='white', font='Times 24 bold', command=button2)
buton2.place(x=130, y=190)

buton3 = tk.Button(text=' 3 ', bg='black', fg='white', font='Times 24 bold', command=button3)
buton3.place(x=210, y=190)

buton4 = tk.Button(text=' 4 ', bg='black', fg='white', font='Times 24 bold', command=button4)
buton4.place(x=50, y=270)

buton5 = tk.Button(text=' 5 ', bg='black', fg='white', font='Times 24 bold', command=button5)
buton5.place(x=130, y=270)

buton6 = tk.Button(text=' 6 ', bg='black', fg='white', font='Times 24 bold', command=button6)
buton6.place(x=210, y=270)

buton7 = tk.Button(text=' 7 ', bg='black', fg='white', font='Times 24 bold', command=button7)
buton7.place(x=50, y=350)

buton8 = tk.Button(text=' 8 ', bg='black', fg='white', font='Times 24 bold', command=button8)
buton8.place(x=130, y=350)

buton9 = tk.Button(text=' 9 ', bg='black', fg='white', font='Times 24 bold', command=button9)
buton9.place(x=210, y=350)

buton10 = tk.Button(text='para üstünü al ve temizle', bg="black", fg="white", font='Times 16 bold', command=button10)
buton10.place(x=300, y=280)

buton11 = tk.Button(text='Seçileni Al', bg="black", fg="white", font='Times 16 bold', command=button11)
buton11.place(x=300, y=235)

pencere.mainloop()

import turtle, time, random



pencere = turtle.Screen()
pencere.title('Araba Yarışı LVL2')
pencere.bgcolor('gray')
pencere.setup(height=700, width=700)
pencere.tracer(0)

pencere.register_shape('racingback.gif')
pencere.register_shape('racingcar.gif')
pencere.register_shape('car.gif')


araba = turtle.Turtle()
araba.speed(0)
araba.shape('racingcar.gif')
araba.shapesize(2)
araba.color('red')
araba.setheading(90)
araba.penup()
araba.goto(0, -200)

arka = turtle.Turtle()
arka.speed(0)
arka.pensize(3)
arka.color('white')
arka.shape('racingback.gif')
arka.penup()
arka.hideturtle()
arka.goto(0, 0)

skor = 0
hasar = 1
hedef = 200
lvl_2 = 80


yaz = turtle.Turtle()
yaz.speed(0)
yaz.color('white')
yaz.penup()
yaz.goto(300, 200)
yaz.clear()
yaz.write(f'Puan\n{skor}\nHedef\n100', align='center', font=('Courier', 24, 'bold'))
yaz.hideturtle()

yaz1 = turtle.Turtle()
yaz1.speed(0)
yaz1.shapesize(5)
yaz1.color('black')
yaz1.penup()
yaz1.goto(0, 200)
yaz1.clear()
yaz1.write('', align='center', font=('Courier', 24, 'bold'))
yaz1.hideturtle()

kamera_dy = 0
kamera_y = 0

def sol():
    x = araba.xcor()
    x = x -30
    if x < -170:
        x = -170
    araba.setx(x)

def sag():
    x = araba.xcor()
    x = x +30
    if x > 170:
        x = 170
    araba.setx(x)

def yukari():
    y = araba.ycor()
    y = y +15
    if y > 250:
        y = 250
    araba.sety(y)

def assagi():
    y = araba.ycor()
    y = y -15
    if y < -250:
        y = -250
    araba.sety(y)


sayi = 0

def devam():
    global sayi
    sayi += 1
    global bekleme
    yaz1.clear()
    yaz1.write('3 saniye içinde başlıyor...\n.\n.', align='center', font=('Courier', 24, 'bold'))
    bekleme = time.sleep(1)
    yaz1.clear()

def pause():
    global sayi
    sayi = 0
    deger = True
    while deger:
        if sayi == 0:
            yaz1.clear()
            yaz1.write('OYUN DURAKLARILDI DEVAM\nETMEK İÇİN "." ya BASIN', align='center', font=('Courier', 24, 'bold'))
            bekleme = time.sleep(1)
        else:
            devam()
            deger = False
    


engeller = []
for i in range(10):
    engel = turtle.Turtle()
    engel.speed(1)
    engel.shape('car.gif')
    engel.shapesize(3, 6)
    engel.color('blue')
    engel.setheading(90)
    engel.penup()
    engel.dx = random.randint(-175, 175)
    engel.dy = 600
    engel.goto(engel.dx, engel.dy)
    engeller.append(engel)

engeller1 = []
for ii in range(10):
    engel1 = turtle.Turtle()
    engel1.speed(1)
    engel1.shape('car.gif')
    engel1.shapesize(3, 6)
    engel1.color('red')
    engel1.setheading(90)
    engel1.penup()
    engel1.dx = random.randint(-150, 150)
    engel1.dy = 600
    engel1.goto(engel1.dx, engel1.dy)
    engeller1.append(engel1)

engeller2 = []
for iii in range(10):
    engel2 = turtle.Turtle()
    engel2.speed(1)
    engel2.shape('car.gif')
    engel2.shapesize(3, 6)
    engel2.color('red')
    engel2.setheading(90)
    engel2.penup()
    engel2.dx = random.randint(-165, 165)
    engel2.dy = 600
    engel2.goto(engel2.dx, engel2.dy)
    engeller2.append(engel2)

engeller3 = []
for iiii in range(10):
    engel3 = turtle.Turtle()
    engel3.speed(1)
    engel3.shape('car.gif')
    engel3.shapesize(3, 6)
    engel3.color('red')
    engel3.setheading(90)
    engel3.penup()
    engel3.dx = random.randint(-165, 165)
    engel3.dy = 600
    engel3.goto(engel3.dx, engel3.dy)
    engeller3.append(engel3)


engeller4 = []
for iiiii in range(10):
    engel4 = turtle.Turtle()
    engel4.speed(1)
    engel4.shape('car.gif')
    engel4.shapesize(3, 6)
    engel4.color('red')
    engel4.setheading(90)
    engel4.penup()
    engel4.dx = random.randint(-165, 165)
    engel4.dy = 600
    engel4.goto(engel4.dx, engel4.dy)
    engeller4.append(engel4)


pencere.listen()
pencere.onkeypress(sol, 'Left')
pencere.onkeypress(sag, 'Right')
pencere.onkeypress(yukari, 'Up')
pencere.onkeypress(assagi, 'Down')
pencere.onkey(pause, 'space')
pencere.onkey(devam, '.')
baslangic_zaman = time.time()
baslangic_zaman1 = time.time()
baslangic_zaman2 = time.time()
baslangic_zaman3 = time.time()
baslangic_zaman4 = time.time()



while True:
    kamera_dy = -1
    kamera_y += kamera_dy
    kamera_y %= 700

    arka.goto(0, kamera_y - 700)
    arka.shape('racingback.gif')
    arka.stamp()
    araba.shape('racingcar.gif')
    araba.stamp()
    engeller[i].shape('car.gif')
    engeller[i].stamp()
    engeller1[ii].shape('car.gif')
    engeller1[ii].stamp()
    engeller2[iii].shape('car.gif')
    engeller2[iii].stamp()
    engeller3[iiii].shape('car.gif')
    engeller3[iiii].stamp()
    engeller4[iiiii].shape('car.gif')
    engeller4[iiiii].stamp()
  

    arka.goto(0, kamera_y)
    arka.shape('racingback.gif')
    arka.stamp()
    araba.shape('racingcar.gif')
    araba.stamp()
    engeller[i].shape('car.gif')
    engeller[i].stamp()
    engeller1[ii].shape('car.gif')
    engeller1[ii].stamp()
    engeller2[iii].shape('car.gif')
    engeller2[iii].stamp()
    engeller3[iiii].shape('car.gif')
    engeller3[iiii].stamp()
    engeller4[iiiii].shape('car.gif')
    engeller4[iiiii].stamp()

    

    if time.time()-baslangic_zaman > random.randint(4, 7):
        baslangic_zaman = time.time()
        
        engel.dx = random.randint(-160, 175)
        engel.dy = 525
        engel.goto(engel.dx, engel.dy)
    
    y = engeller[i].ycor()
    y -= 1
    engeller[i].sety(y)

    if engeller[i].distance(araba) < 42:
        hasar -= 1
        if hasar <= 0:
            skor = 0
            yaz.clear()
            yaz.write('KAZA\nYAPTIN', align='center', font=('Courier', 24, 'bold'))
            time.sleep(3)
            break

    if engel.ycor() == araba.ycor():
        skor += 1
        yaz.clear()
        yaz.write(f'Puan\n{skor}\nHedef\n{hedef}', align='center', font=('Courier', 24, 'bold'))
        if skor >= hedef:
            yaz.clear()
            yaz.write(f'KAZ-\nANDIN', align='center', font=('Courier', 24, 'bold'))
            time.sleep(3)
            break
        
   
    if time.time()-baslangic_zaman1 > random.randint(3, 7):
        baslangic_zaman1 = time.time()
        
        engel1.dx = random.randint(-150, 155)
        engel1.dy = 575
        engel1.goto(engel1.dx, engel1.dy)
    
    y = engeller1[ii].ycor()
    y -= 1
    engeller1[ii].sety(y)

    if engeller1[ii].distance(araba) < 42:
        hasar -= 1
        if hasar <= 0:
            skor = 0
            yaz.clear()
            yaz.write('KAZA\nYAPTIN', align='center', font=('Courier', 24, 'bold'))
            time.sleep(3)
            break


    if engel1.ycor() == araba.ycor():
        skor += 1
        yaz.clear()
        yaz.write(f'Puan\n{skor}\nHedef\n{hedef}', align='center', font=('Courier', 24, 'bold'))
        if skor >= hedef:
            yaz.clear()
            yaz.write(f'KAZ-\nANDIN', align='center', font=('Courier', 24, 'bold'))
            time.sleep(3)
            break
    
    

    if time.time()-baslangic_zaman2 > random.randint(4, 6):
        baslangic_zaman2 = time.time()
        engel2.dx = random.randint(-150, 170)
        engel2.dy = 560
        engel2.goto(engel2.dx, engel2.dy)

    y = engeller2[iii].ycor()
    y -= 1
    engeller2[iii].sety(y)
    if engeller2[iii].distance(araba) < 42:
        hasar -= 1
        if hasar <= 0:
            skor = 0
            yaz.clear()
            yaz.write('KAZA\nYAPTIN', align='center', font=('Courier', 24, 'bold'))
            time.sleep(3)
            break
    if engel2.ycor() == araba.ycor():
        skor += 1
        yaz.clear()
        yaz.write(f'Puan\n{skor}\nHedef\n{hedef}', align='center', font=('Courier', 24, 'bold'))
        if skor >= hedef:
            yaz.clear()
            yaz.write(f'KAZ-\nANDIN', align='center', font=('Courier', 24, 'bold'))
            time.sleep(3)
            break


    if time.time()-baslangic_zaman3 > random.randint(4, 7):
        baslangic_zaman3 = time.time()
        engel3.dx = random.randint(-130, 145)
        engel3.dy = 600
        engel3.goto(engel3.dx, engel3.dy)

    y = engeller3[iiii].ycor()
    y -= 1
    engeller3[iiii].sety(y)
    if engeller3[iiii].distance(araba) < 42:
        hasar -= 1
        if hasar <= 0:
            skor = 0
            yaz.clear()
            yaz.write('KAZA\nYAPTIN', align='center', font=('Courier', 24, 'bold'))
            time.sleep(3)
            break
    if engel3.ycor() == araba.ycor():
        skor += 1
        yaz.clear()
        yaz.write(f'Puan\n{skor}\nHedef\n{hedef}', align='center', font=('Courier', 24, 'bold'))
        if skor >= hedef:
            yaz.clear()
            yaz.write(f'KAZ-\nANDIN', align='center', font=('Courier', 24, 'bold'))
            time.sleep(3)
            break


    if skor >= lvl_2:

        if time.time()-baslangic_zaman4 > random.randint(3, 6):
            baslangic_zaman4 = time.time()
            engel4.dx = random.randint(-150, 160)
            engel4.dy = 550
            engel4.goto(engel4.dx, engel4.dy)
    
        y = engeller4[iiiii].ycor()
        y -= 1
        engeller4[iiiii].sety(y)

        if engeller4[iiiii].distance(araba) < 42:
            hasar -= 1
            if hasar <= 0:
                skor = 0
                yaz.clear()
                yaz.write('KAZA\nYAPTIN', align='center', font=('Courier', 24, 'bold'))
                time.sleep(3)
                break

        if engel4.ycor() == araba.ycor():
            skor += 1
            yaz.clear()
            yaz.write(f'Puan\n{skor}\nHedef\n{hedef}', align='center', font=('Courier', 24, 'bold'))
            if skor >= hedef:
                yaz.clear()
                yaz.write(f'KAZ-\nANDIN', align='center', font=('Courier', 24, 'bold'))
                time.sleep(3)
                break
    

    pencere.update()

    arka.clear()
    araba.clear()
    engeller[i].clear()
    engeller1[ii].clear()
    engeller2[iii].clear()
    engeller3[iiii].clear()
    engeller4[iiiii].clear()
    
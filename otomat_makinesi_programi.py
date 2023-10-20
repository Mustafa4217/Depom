######## OTOMAT MAKİNESİ #########

while True:

    import time


    print("Hoşgeldiniz.")
    print("""--------------------
1-Çikolata / 5TL
2-Süt / 4TL
3-soğuk kahve / 7TL
4-kola / 6TL
5-kek / 5TL
6-biskivü / 8TL
7-kraker / 4TL
8-meyve suyu / 3TL
-------------------- """)

    print("""EN AZ 10 TL YÜKLENEBİLİR EN ÇOK 200TL""")
    alici = 0 
    if alici >= 1 :
        pass
    alici = int(input("Ne almak istersiniz 1.../8? :"))
    if alici == 1111 :
        print("Makine Kapatılıyor...")
        time.sleep(2)
        break

    bakiye = int(input("Bakiyenizi Giriniz. :"))

    if bakiye < 10 :
        print("Bakiye geçersiz lütfen geçerli bir bakiye yükleyiniz!!! YÜKLEDİĞİNİZ PARA İADE EDİLİYOR...")
        time.sleep(5)
    elif bakiye > 200 :
        print("Bakiye geçersiz lütfen geçerli bir bakiye yükleyiniz!!! YÜKLEDİĞİNİZ PARA İADE EDİLİYOR...")
        time.sleep(5)
        break
    
    elif alici == 1 :
        print("Çikolatanız Veriliyor...")
        time.sleep(4)
        kalan_bakiye = bakiye - 5
        print(f"Para Üstü :{kalan_bakiye}")
        time.sleep(1)
        print("Para üstünüz veriliyor...")
        time.sleep(2)
        

    elif alici == 2 :
        print("Sütünüz Veriliyor...")
        time.sleep(4)
        kalan_bakiye = bakiye - 4
        print(f"Para Üstü :{kalan_bakiye}")
        time.sleep(1)
        print("Para üstünüz veriliyor...")
        time.sleep(2)
    

    elif alici == 3 :
        print("Soğuk Kahveniz Veriliyor...")
        time.sleep(4)
        kalan_bakiye = bakiye - 7
        print(f"Para Üstü :{kalan_bakiye}")
        time.sleep(1)
        print("Para üstünüz veriliyor...")
        time.sleep(2)
        

    elif alici == 4 :
        print("Kolanız Veriliyor...")
        time.sleep(4)
        kalan_bakiye = bakiye - 6
        print(f"Para Üstü :{kalan_bakiye}")
        time.sleep(1)
        print("Para üstünüz veriliyor...")
        time.sleep(2)
        

    elif alici == 5 :
        print("Kekiniz Veriliyor...")
        time.sleep(4)
        kalan_bakiye = bakiye - 5
        print(f"Para Üstü :{kalan_bakiye}")
        time.sleep(1)
        print("Para üstünüz veriliyor...")
        time.sleep(2)
        

    elif alici == 6 :
        print("Biskivünüz Veriliyor...")
        time.sleep(4)
        kalan_bakiye = bakiye - 8
        print(f"Para Üstü :{kalan_bakiye}")
        time.sleep(1)
        print("Para üstünüz veriliyor...")
        time.sleep(2)
        

    elif alici == 7 :
        print("Krakeriniz Veriliyor...")
        time.sleep(4)
        kalan_bakiye = bakiye - 4
        print(f"Para Üstü :{kalan_bakiye}")
        time.sleep(1)
        print("Para üstünüz veriliyor...")
        time.sleep(2)
        

    elif alici == 8 :
        print("Meyve Suyunuz Veriliyor...")
        time.sleep(4)
        kalan_bakiye = bakiye - 3
        print(f"Para Üstü :{kalan_bakiye}")
        time.sleep(1)
        print("Para üstünüz veriliyor...")
        time.sleep(2)
    
    else:
        print("!!!BİLİNMEYEN BİR HATA OLUŞTU LÜTFEN TEKRAR DENEYİNİZ!!! YİNE OLMUYORSA YETKİLİYE BİLDİRİNİZ.")
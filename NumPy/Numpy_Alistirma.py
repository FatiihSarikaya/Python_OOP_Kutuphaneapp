import numpy as np
("""

1) Manuel değerleri el ile girerek 3 boyutlu bir array oluşturup bir değişkene atayın. Ardından 3 boyutlu olup olmadığına bakmak için dimension'ını kontrol edin
2) 34, 40, 46, 52... 112 şeklinde devam eden 1 boyutlu bir array oluşturun.
3) 50-500 arasında lineer artış gösteren 91 tane tam sayıdan oluşan bir array oluşturun.(dtype'ı int olsun)
4) 100(10**2) ile 10000(10**5) arasında logaritmik artış gösteren 8 sayıdan oluşan bir array oluşturun.
5) 0-8 tam arasındaki ardışık tam sayılardan oluşan(0 ve 8 dahil toplam 9 değer) 3x3 shape'inde bir matris oluşturun.
6) 6x6 formatında bir sıfır matrisi oluşturun. (dtype'ı int olsun)
7) 4x4 formatında bir bir matrisi oluşturun. (dtype'ı int olsun)
8) 8x8 formatında bir birim matris oluşturun. (Sadece sol köşegeni 1 geri kalan değerleri 0 olan matris'e birim matris deniyor.) (dtype'ı int olsun)
9) 5x5 formatında bir köşegen matrisi oluşturun (Sadece sol üstten sağ alta doğru olan köşegendeki değerleri 3 olsun diğer bütün değerleri 0) (Bunu henüz görmediniz ama birim matrise benziyor, sadece köşegen değerleri 1 değil 3 olacak. Bir şeyler düşünün)
10) np.random modülünden uygun fonksiyonu kullanarak 0-1 arasında toplam 6 tane değerden oluşan 1 boyutlu bir array oluşturun.
11) np.random modülünden uygun fonksiyonu kullanarak 50-100 arasındaki(50 ve 100 dahil) tam sayılardan 10 tanesiyle oluşan (5,2) shape'inde bir array oluşturun. Ardından bu arrayin shape'ini kontrol edin.
12) np.random modülünden uygun fonksiyonu kullanarak 100-1000(1000 dahil değil) arasındaki tam sayılardan rastgele 50 tanesinden oluşan (2,5,5) shape'inde 3 boyutlu bir array oluşturun. Ardından bu array'in dimension'ını(boyutunu) ve shape'ini kontrol edin.
13) np.random modülünden uygun fonksiyonu kullanarak 0-100(0 ve 100 dahil) arasındaki tam sayılardan 10 tane seçerek bir array oluşturun. Bu array'in maximum, mininmum değerlerine ve bu değerlerin indexlerine bakın.
14) np.random modülünden uygun fonksiyonu kullanarak 300-500(300 ve 500 dahil) arasındaki tam sayılardan 20 tane seçerek (2,2,5) shape'inde 3 boyutlu bir array oluşturun. Ardından bu array'in içindeki 20 tam sayı arasından maximum ve minimum değerleri manuel olarak tespit edin ve indexleme yaparak çekmeye çalışın.
15) 0-50(50 dahil) arasındaki ardışık tam sayılardan oluşan bir array oluşturun. Ardından bu arrayin 20. ve 35. indexleri arasındaki değerleri 500'e eşitleyin ve yeni oluşan array'i ekrana yazdırarak broadcasting işleminin yapılıp yapılmadığını test edin.

""")
print("***************************************************************************")

arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
print(arr.ndim)

print("***************************************************************************")

arr2 =np.arange(34,113,6)
print(arr2)

print("***************************************************************************")

arr3 = np.linspace(50,500,91,dtype=int)
print(arr3 ," ",len(arr3))

print("***************************************************************************")

arr4 = np.logspace(2,5,8)
print(arr4)

print("***************************************************************************")

arr5= np.arange(9).reshape(3,3)
print(arr5)

print("***************************************************************************")

arr6 = np.zeros((6,6),dtype=int)
print(arr6)

print("***************************************************************************")

arr7 = np.ones((4,4),dtype=int)
print(arr7)

print("***************************************************************************")

arr8 = np.eye(8,dtype=int)
print(arr8)

print("***************************************************************************")

arr9 = np.eye(5,dtype=int)
print(arr9*3)

print("***************************************************************************")

arr10 =np.random.rand(6)
print(arr10)

print("***************************************************************************")

arr11 = np.random.randint(50,101,10).reshape(5,2)
print(arr11)
print(arr11.shape)

print("***************************************************************************")

arr12 = np.random.randint(100,1000,50).reshape(2,5,5)
print(arr12.shape)
print(arr12.ndim)

print("***************************************************************************")

arr13 = np.random.randint(0,101,10)
print(arr13.max())
print(arr13.min())
print(arr13.argmax())
print(arr13.argmin())

print("***************************************************************************")

arr14 = np.random.randint(300,501,20).reshape(2,2,5)
print(arr14)
("""
[[[470 471 482 326 426]
  [466 383 339 425 372]]

 [[332 469 433 486 499]
  [404 427 409 374 383]]]

""")
max = arr14[1][0][4]
min = arr14[0][0][3]
print(max)
print(min)

print("***************************************************************************")

arr15 = np.arange(51)
arr15[20:35]=500
print(arr15)





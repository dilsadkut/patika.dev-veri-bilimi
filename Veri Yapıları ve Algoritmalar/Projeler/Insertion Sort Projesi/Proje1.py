"""
[22,27,16,2,18,6] -> Insertion Sort

1-Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.
2-Big-O gösterimini yazınız.
3-Time Complexity: Average case: Aradığımız sayının ortada olması,Worst case: Aradığımız sayının sonda olması, Best case: Aradığımız sayının dizinin en başında olması.
4-Dizi sıralandıktan sonra 18 sayısı hangi case kapsamına girer? Yazınız.
"""
"""
[22,27,16,2,18,6] dizisinin Insertion Sort'a göre aşamaları:

22 27 16 2 18 6  ----> Bu sırasız ham dizimiz
22* 27 16 2 18 6 ----> Dizinin ilk indisi olan 22 seçildi. Öncesinde başka bir değer olmadığı için bir sonraki aşamaya geçiliyor.
22 27 16 2 18 6
22 27* 16 2 18 6 ----> Dizinin ikinci indisi olan 27 seçildi ve dizinin daha önce tuttuğumuz değer daha küçük olduğu için bir değişiklik olmayacak.
22 27 16 2 18 6
22 27 16* 2 18 6 ----> Dizinin üçüncü indisi olan 16 seçildi ve bu değer önceki tuttuğumuz diğer iki değerden daha küçük bu yüzden en başa sıralanması gerekir.
16 22 27 2 18 6
22 27 16 2* 18 6 ----> Dizinin dördüncü indisi olan 2 seçildi ve bu değer önceki tuttuğumuz üç değerden daha küçük bu yüzden en başa sıralanması gerekir.
2 16 22 27 18 6
22 27 16 2 18* 6 ----> Dizinin beşinci indisi olan 18 seçildi ve bu değer bir önceki tuttuğumuz 22 değerinden küçük bu yüzden 22'den önceye sıralıyoruz.
2 16 18 22 27 6
22 27 16 2 18 6* ----> Dizinin altıncı indisi olan 6 seçildi ve bu değer bir önceki tuttuğumuz 16 değerinden küçük bu yüzden 16'dan önceye sıralıyoruz.
2 6 16 18 22 27 
"""
"""
Eklemeli sıralama algoritmasının zaman karmaşıklığı hesaplanırken, yapılan karşılaştırmalar ve yer değiştirmeler dikkate alınır. Eklemeli sıralamalı algoritması n elemanlı bir listede, ikinci eleman için en fazla 1 karşılaştırma ve 1 yer değiştirme yapar, üçüncü eleman için 2 karşılaştırma ve 2 yer değiştirme, dördüncü eleman için 3 karşılaştırma ve 3 yer değiştirme yapar.
Bu şekilde son eleman için en fazla n-1 karşılaştırma ve n-1 yer değiştirme yapar. Listedeki bütün elemanlar için yapılan karşılaştırmaların ve yer değiştirmelerin toplamı

  2(1+2+3+4+...+(n-2)+(n-1)) = 2(n(n-1)/2) = n(n-1)

yapar. Hesaplamaların sonucunda elde edilen

  n(n-1)

değerinin asimptotik üst sınırı O(n^2) değerini verir.
"""
"""
En kötü başarım:Eklemeli sıralama algoritması en kötü durumda, örneğin liste tersten sıralıysa O(n^2) karmaşıklıkla çalışır.
En iyi başarım:Eklemeli sıralama algoritması en iyi durumda, örneğin liste sıralıysa n-1 karşılaştırma yapar ve O(n) karmaşıklıkla çalışır.
Ortalama başarım:Eklemeli sıralama algoritması ortalama O(n^2) karmaşıklıkla çalışır. 
"""
def insert(ary):

    for i in range(1,len(ary)):
        key = ary[i]

        j = i-1
        while j >= 0 and key < ary[j]:
            ary[j+1] = ary[j]
            j-=1
        ary[j+1] = key

ary = [22,27,16,2,18,6]
insert(ary)
for i in range(len(ary)):
    print(ary[i])


#--------------------------------------------------------------------------------------------------
"""
[7,3,5,8,2,9,4,15,6] dizisinin Insertion sort'a göre ilk 4 adımını yazınız.
"""

"""
[7,3,5,8,2,9,4,15,6] dizisinin Insertion Sort'a ilk 4 adımı:

7 3 5 8 2 9 4 15 6 -------> Bu sırasız ham dizimiz
7* 3 5 8 2 9 4 15 6 ------> Dizinin ilk indisi olan 7 seçildi. Öncesinde başka bir değer olmadığı için bir sonraki aşamaya geçiliyor.
7 3 5 8 2 9 4 15 6
7 3* 5 8 2 9 4 15 6 ------> Dizinin ikinci indisi olan 3 seçildi ve dizinin daha önce tuttuğumuz 7 değeri daha büyük olduğu için yer değiştirecek.
3 7 5 8 2 9 4 15 6
7 3 5* 8 2 9 4 15 6 ------> Dizinin üçüncü indisi olan 5 seçildi ve dizinin daha önce tuttuğumuz 7 değeri daha büyük olduğu için yer değiştirecek.
3 5 7 8 2 9 4 15 6 
7 3 5 8* 2 9 4 15 6 ------> Dizinin dördüncü indisi olan 8 seçildi ve dizinin daha önce tuttuğumuz diğer elemanları bu değerden daha küçük olduğu için sıralama değişmeyecek.
3 5 7 8 2 9 4 15 6
7 3 5 8 2* 9 4 15 6 ------> Dizinin beşinci indisi olan 2 seçildi ve dizinin daha önce tuttuğumuz tüm elemanlarından daha küçük bir değer olduğu için yer değiştirecek.
2 3 5 7 8 9 4 15 6 
7 3 5 8 2 9* 4 15 6 ----> Dizinin altıncı indisi olan 9 seçildi ve dizinin daha önce tuttuğumuz diğer elemanları bu değerden daha küçük olduğu için sıralama değişmeyecek.
2 3 5 7 8 9 4 15 6 
7 3 5 8 2 9 4* 15 6 ----> Dizinin yedinci indisi olan 4 seçildi ve dizinin daha önce tuttuğumuz 5 değerinden küçük olduğu için yer değiştirecek.
2 3 4 5 7 8 9 15 6 
7 3 5 8 2 9 4 15* 6 ----> Dizinin sekizinci indisi olan 15 seçildi ve dizinin daha önce tuttuğumuz diğer elemanları bu değerden daha küçük olduğu için sıralama değişmeyecek.
2 3 4 5 7 8 9 15 6 
7 3 5 8 2 9 4 15 6* ----> Dizinin dokuzuncu indisi olan 6 seçildi ve dizinin daha önce tuttuğumuz 7 değerinden küçük olduğu için yer değiştirecek.
2 3 4 5 6 7 8 9 15

"""
def insert(ary):

    for i in range(1,len(ary)):
        key = ary[i]

        j = i-1
        while j >= 0 and key < ary[j]:
            ary[j+1] = ary[j]
            j-=1
        ary[j+1] = key

ary = [7,3,5,8,2,9,4,15,6]
insert(ary)
for i in range(len(ary)):
    print(ary[i])
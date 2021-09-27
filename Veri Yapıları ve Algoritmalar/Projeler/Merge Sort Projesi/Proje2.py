"""
[16,21,11,8,12,22] -> Merge Sort

Yukarıdaki dizinin sort türüne göre aşamalarını yazınız.
Big-O gösterimini yazınız.
"""

"""
[16,21,11,8,12,22] Merge Sort'a göre aşamaları:

1.adım: Diziyi ikiye böl.
16 21 11          8 12 22 
2.adım: Tekrar böl.
16    21 11       8    12 22
3.adım: Tekrar böl.
16    21    11    8    12    22
4.adım: Parçaları sıralayarak birleştir.
16 21    8 11    12 22
5.adım: Parçaları sıralayarak birleştir.
8 16 21    11 12 22    
6.adım: Parçaları sıralayarak birleştir.
8 11 12 16 21 22
"""

"""
Big O Gösterimi:
Bu özyinelemeli(recursive) bir fonksiyon olduğu için sürekli kendini çağırarak hep diziyi ikiye bölüyor. Böylelikle en fazla log2(N) kere bölme işlemi yapmış oluyor.
Her bölünmüş dizinin Merge işlemi içinde dizinin uzunluğu olan N işlem yapıldığı için bu algoritmanın karmaşıklık maliyeti büyük O notasyonunda O(N*log(N)) oluyor.
Merge sort sayesinde çok kısa sürede 1 000 000 uzunluğundaki dizileri bile sıralayabiliyoruz.
"""

def merge(ar, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    L = [0] * (n1)
    R = [0] * (n2)
 
   
    for i in range(0, n1):
        L[i] = ar[l + i]
 
    for j in range(0, n2):
        R[j] = ar[m + 1 + j]
 
    i = 0     
    j = 0     
    k = l    
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            ar[k] = L[i]
            i += 1
        else:
            ar[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        ar[k] = L[i]
        i += 1
        k += 1
 
    while j < n2:
        ar[k] = R[j]
        j += 1
        k += 1
 
def mergesrt(ar, l, r):
    if l < r:       
        m = l+(r-l)//2
        
        mergesrt(ar, l, m)
        mergesrt(ar, m+1, r)
        merge(ar, l, m, r)
 
ar = [16,21,11,8,12,22]
n = len(ar)
print("Başlangıç Dizisi")
for i in range(n):
    print("%d" % ar[i]),
 
mergesrt(ar, 0, n-1)
print("\n\nSıralanmış dizi")
for i in range(n):
    print("%d" % ar[i]),
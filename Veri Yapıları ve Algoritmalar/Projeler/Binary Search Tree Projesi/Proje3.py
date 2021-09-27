"""
[7, 5, 1, 8, 3, 6, 0, 9, 4, 2] dizisinin Binary-Search-Tree aşamalarını yazınız.

Örnek olarak, root x'dir. root'un sağından y bulunur. Solunda z bulunur vb.
"""

"""
root 5'dir. root'un bir sağında 6 değeri bulunur. 6 düğümünün bir sağında 9 değeri bulunur. 9 düğümünün bir solunda 7 değeri bulunur. 

6 düğümünün solunda 2 değerinin olduğu düğüm bulunur. 2 değerinin olduğu düğümün sağında 3 değeri bulunur. 2 değerinin olduğu düğümün solunda 1 değeri bulunur. 

5 değerinin olduğu root düğümün solunda 4 değeri bulunur. 4 değerinin olduğu düğümün solunda 0 değeri bulunur. 4 değerinin olduğu düğümün sağında 8 değeri bulunur.
"""

"""  Ağacın yapısı:
         5              
   4            6
0     8     2       9
         1    3  7
"""

#inorder sıralama
class Dugum:
    def __init__(self, deger):
        self.deger = deger 
        self.sol = None 
        self.sag = None 


def inorder(dugum):
    
    if dugum.sol:
        inorder(dugum.sol)

   
    print(dugum.deger)

    
    if dugum.sag:
        inorder(dugum.sag)


kok = Dugum(5) 

kok.sol = Dugum(4)
kok.sol.sol = Dugum(0)
kok.sol.sag = Dugum(8)
kok.sag = Dugum(6)
kok.sag.sol = Dugum(2)
kok.sag.sag = Dugum(9)
kok.sag.sol.sol = Dugum(1)
kok.sag.sol.sag = Dugum(3)
kok.sag.sag.sol = Dugum(7)

inorder(kok)

#0 4 8 5 1 2 3 6 7 9
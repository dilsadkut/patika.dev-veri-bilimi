
"""
Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listtlerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]
"""

def flatten(top_l):
    for elem in top_l:
        if isinstance(elem, list):
            yield from flatten(elem)
        else:
            yield elem


l = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
flat_list = [a for a in flatten(l)]
print(flat_list) 

#return yerine yield kullanınca normal bir fonksiyonu generator'e dönüştürmüş oluyoruz.

#bu sayede list comprehension içinde kullanabildik.

#eğer karşılaştığımız nesne liste (isinstance(x, list)) ise de yinelemeli yapı kullanarak listenin içine yine baktık.
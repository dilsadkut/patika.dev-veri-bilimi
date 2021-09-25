
"""
Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]
"""

def deep_reverse(l: list):
    l.reverse()
    for i in l:
        if isinstance(i, list):
            deep_reverse(i)
    return l

xlist=[[1, 2], [3, 4], [5, 6, 7]]
deep_reverse(xlist)
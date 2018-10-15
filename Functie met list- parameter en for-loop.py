grondgetallen = [4, 5, 3, -81]



def kwadraten_som(grondgetallen):
    getal = int()
    for item in grondgetallen:
        if item < 0:
            grondgetallen.remove(item)
        else:
            getal += item ** 2
    return getal


print(kwadraten_som(grondgetallen))








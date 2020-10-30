class Tall:
    def __init__(self,verdi):
        self._num = verdi

    def __str__(self):
        return self._num

def hovedprogram():
    verdi = input("skriv tall")
    ny = Tall(verdi)

    print(ny)

    if input("test") == "q":

        hovedprogram()
    else:
        print("Ferdig")

hovedprogram()

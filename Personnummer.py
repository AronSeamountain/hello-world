def kontrolls(nummer):
    print(len(nummer))
    if len(nummer) == 12:
        print("12 siffror")
        return True
    else:
        print("Personnummret har fel antal siffror")
        print(len(nummer))
        return False

numbers = '0123456789'
def siffror(pnummer):
    for i in pnummer:
        if i in numbers:
            pass
        else:
            print("incorrect characters")
            return False
    return True


def renskriv(nummer):
    nummer = nummer.replace('-', '')
    nummer = nummer.replace(' ','')

    return nummer
def kontrolla(nummer):
    if nummer[0] =="1":
        print("the year is correct")
        return True
    elif nummer[0] =="2":
        if nummer[1] == "0":
            if nummer[2] == "0":
                print("the year is correct")
                return True
            elif nummer[2] == "1":

                if int(nummer[3]) <8 :
                    print("the year is correct *")
                    return True


    print("The year is wrong ")
    return False


def kontrollm(nummer):

        if nummer[4] == "0" and nummer[5] != "0":

            print("month correct #1")
            return True
        elif nummer[4] == "1" and (nummer[5] == "0" or nummer[5]== "1" or nummer[5]== "2"):
            print("month correct #2")
            return True
        else:
            print("bajs")


def kontrolld(nummer):
    if nummer[6] == "0":
        if not nummer[7] == "0":
            print("the day is correct #1")
    elif nummer[6] == "1":
        print("the day is correct #2")
    elif nummer[6] == "2":
        if nummer[4] == "0" and nummer[5] == "2":
            if nummer[7] == "9":
                print("the day is incorrect")
                return


        if not nummer[5] == 2:
            print("the day is correct#3")
    elif nummer[6] == "3":
        if nummer[4] == "0" and (nummer[5] == "1" or nummer[5] == "3" or nummer[5] == "5" or nummer[5] == "7", nummer[5] == "9"):
            if nummer[7] == "0" or nummer[7] == "1":
                print("the day is correct #4")
            else:
                print("the day is wrong #1")
        elif nummer[4] == "1" and nummer[5]== "1":
            if nummer[7] == "0" or nummer[7] == "1":
                print("the day is correct #5")
            else:
                print("the day is wrong #2")

        elif nummer[4] == "0" and (nummer[5] == "4" or  nummer[5] == "6" or nummer[5] == "8"):
            if nummer[7] == "0":
                print("the day is correct #6")
            else:
                print("the day is wrong #3")
        elif nummer[4] == "1" and (nummer[5] == "0" or nummer[5] == "2"):
                if nummer[7] == "0":
                    print("the day is correct #7")
                else:
                    print("the day is wrong #4")
        else:
            print("the day is wrong #5")






print("Skriv in ditt personnummer")
pnummer = input()
pnummer = renskriv(pnummer)
p = siffror(pnummer)
if p == True:
    print(pnummer)
    p = kontrolls(pnummer)
if p == True:
    p = kontrolla(pnummer)
if p == True:

    p = kontrollm(pnummer)

if p == True:
    kontrolld(pnummer)
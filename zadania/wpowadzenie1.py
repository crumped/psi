import formatowanie

def liczba_liter(zmienna, litera):
    return zmienna.count(litera)

def zad2():
    zmienna = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker'
    imie_string = 'Kornel'
    nazwisko_string = 'Pietrzyk'
    imie = list(imie_string)
    nazwisko = list(nazwisko_string)
    litera_1 = liczba_liter(zmienna, imie[2])
    litera_2 = liczba_liter(zmienna, nazwisko[3])
    print("W tekście jest {} liter ... oraz {} liter ...".format(litera_1, litera_2))
# Press the green button in the gutter to run the script.

def zad3():
    formatowanie.zad3()

def zad4():
    zmienna_typu_string="dowolny ciąg tekstowy"
    print(dir(zmienna_typu_string))
    help(zmienna_typu_string.strip())

def zad5():
    imie="Kornel"
    nazwisko="Pietrzyk"
    print((imie[::-1].lower()).capitalize() + " "+ (nazwisko[::-1].lower()).capitalize())

def zad6_7():
    random_list = list(range(1, 11))
    print(random_list)
    new_list = random_list[len(random_list)//2:]
    random_list = random_list[:len(random_list)//2]
    print(new_list)
    print(random_list)
    concat_list = random_list + new_list
    concat_list.insert(0,0)
    print(concat_list)

def zad8_9():
    lista_uczniow = (('Kornel P', ' 1551'), ('Monika Z', '9565'), ('Eustachy G', '9277'), ('Tomasz H.', '64618'))
    lista_uczniow = dict((y, x) for x, y in lista_uczniow)
    # lista_uczniow = ['Kornel P', ' 1551', 'Monika Z', '9565', 'Eustachy G', '9277', 'Tomasz H.', '64618']
    # lista_uczniow = {lista_uczniow[i]: lista_uczniow[i + 1] for i in range(0, len(lista_uczniow), 2)}
    print(lista_uczniow)
    lista_uczniow['wiek'] = '13'
    lista_uczniow['email'] = 'dwiadaw@gmail.com'
    lista_uczniow['rok'] = '1999'
    lista_uczniow['adres'] = 'adres'

def zad10():
    new_phones = [1111, 1584, 54845, 815, 54845, 8458454, 511, 1111, 8484, 511]
    final_new_phones = list(set(new_phones))
    print(final_new_phones)

def zad11():
    for i in range(1, 11):
        print(i, end=', ')

def zad12():
    for i in range(100, 19, -5):
        print(i, end=', ')

def zad13():
    variable = ''
    lista1 = [{"slow1": ":O", "hmm": "surprise"}, {"slow2": ":)"}, {"slow3": "xd"}]
    for elem in lista1:
        for item in elem:
            print(item)
            variable += item
            variable += ' '
            variable += elem[item]
            variable += ' '

    print(variable)

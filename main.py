from zadania import wpowadzenie1, wprowadzenie2, file_manager

if __name__ == '__main__':
    # lista1 = ['w','w', 'w','w', 'w','w']
    # lista2 = ['a','a', 'a','a', 'a','a']
    # lista3 = wprowadzenie2.zad1(lista1, lista2)
    # print(lista3)

    # data = wprowadzenie2.zad2('oki doki')

    # data = wprowadzenie2.zad3('texttat2t', 't')

    # data = wprowadzenie2.zad4(20, 'Rankine')

    # data = wprowadzenie2.zad7('Rankine')
    data = file_manager.FileManager('text.txt').read_file()
    file_manager.FileManager('text.txt').update_file('sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaammmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')
    print(data)
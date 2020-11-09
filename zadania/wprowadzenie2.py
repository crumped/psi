
def zad1(a_list, b_list):
    lista = []
    for x in range(len(a_list)):
        if x%2 == 0:
            lista.append(a_list[x])
        else:
            lista.append(b_list[x])
    return lista

def zad2(data_text):
    data = {
        'length': len(data_text),
        'letters': list(data_text),
        'big_letters': data_text.upper(),
        'small_letters':data_text.lower()
    }
    return data

def zad3(text, letter):
    new_text = text.replace(letter, '')
    return new_text

def zad4(temperature, temperature_type):
    types=['Fahrenheit', 'Rankine', 'Kelvin']
    if temperature_type not in types:
        return 'The temperature type is not valid'

    if temperature_type == types[0]:
        multiplier = 33.8
    elif temperature_type == types[1]:
        multiplier = 493.47
    else:
        multiplier = 274.15

    converted_temp = temperature * multiplier
    return 'Temperature: {} in {}'.format(converted_temp, temperature_type)


class Calculator:

    def add(self, a,b):
        return a+b

    def difference(self, a,b):
        return a - b

    def multiply(self, a,b):
        return a * b

    def divide(self, a,b):
        return a / b

class ScienceCalculator(Calculator):

    def potegowanie(self, a, b):
        return a^b


def zad7(text):
    lista = list(text)
    lista.reverse()
    return ''.join(lista)

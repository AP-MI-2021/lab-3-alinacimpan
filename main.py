from typing import List


def show_menu():
    print('1. Citire lista')
    print('2. Afisare cea mai lunga subsecventa cu toate numerele pare')
    print('3. Afisare cea mai lungă subsecvență in care toate elementele sunt formate din cifre prime.')
    print('4. Afisare cea mai lungă subsecvență cu proprietatea ca suma numerelor sa fie prima')
    print('x. Exit')


def read_list() -> List[int]:
    lst = []
    lst_str = input('Dati numerele separate prin spatiu:')
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst


def is_even(n: int) -> bool:
    '''
    Determina daca un numar dat este par.
    :param n: numarul dat
    :return: True daca e par si False altfel
    '''

    if n % 2 == 1:
            return False
    return True


def test_is_even():
    assert is_even(7) == False
    assert is_even(2) == True
    assert is_even(15) == False
    assert is_even(97) == False
    assert is_even(1000) == True


def get_longest_all_even(lst: list[int]) -> list[int]:
    '''
    Determina cea mai lunga subsecventa in care toate elementele sunt pare.
    :param lst: lista in care se cauta subsecventa
    :return: subsecventa gasita
    '''

    n = len(lst)
    result = []
    for st in range(n):
        for dr in range(st, n):
            all_even = True
            for num in lst[st:dr+1]:
                if is_even(num) == False:
                    all_even = False
                    break
            if all_even:
                if dr - st + 1 > len(result):
                    result = lst[st:dr+1]
    return result


def is_prime_digits(nr):
    '''
    Determina daca un numar are toate cifrele prime.
    :param nr: numarul dat
    :return: True daca e format din cifre prime si False altfel
    '''
    while(nr!=0):
        if(nr%10!=2 and nr%10!=3 and nr%10!=5 and nr%10!=7):
            return False
        nr=nr//10
    return True


def test_is_prime_digits():
    assert is_prime_digits(24) == False
    assert is_prime_digits(2) == True
    assert is_prime_digits(18) == False
    assert is_prime_digits(39) == False
    assert is_prime_digits(77) == True


def get_longest_prime_digits(lst: list[int]) -> list[int]:
    '''
    Determina cea mai lunga subsecventa in care toate elementele sunt formate din cifre prime.
    :param lst: lista in care se cauta subsecventa
    :return: subsecventa gasita
    '''

    n = len(lst)
    result = []
    for st in range(n):
        for dr in range(st, n):
            all_prime = True
            for nr in lst[st:dr+1]:
                if is_prime_digits(nr) == False:
                    all_prime = False
                    break
            if all_prime:
                if dr - st + 1 > len(result):
                    result = lst[st:dr+1]
    return result


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([23, 25, 45, 5]) == [23, 25]
    assert get_longest_prime_digits([2, 7, 5, 9, 22, 25]) == [2, 7 ,5]
    assert get_longest_prime_digits([18, 29, 26,77]) == [77]
    assert get_longest_prime_digits([11, 23, 11, 35]) == [23]

def is_prime(n: int) -> bool:
    '''
    Determina daca un numar dat este prim.
    :param n: numarul dat
    :return: True daca e prim si False altfel
    '''
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(4) == False
    assert is_prime(15) == False
    assert is_prime(29) == True

def sum_of_list(lst: list[int]) -> int:
    '''
    Calculeaza suma elementelor unei liste
    :param lst: lista de numere intregi
    :return: suma: nr intreg
    '''
    suma = 0
    for i in lst:
        suma = suma + i
    return suma

def get_longest_sum_is_prime(lst: list[int]) -> list[int]:
    '''
    Returneaza cea mai lunga subsecventa cu proprietatea sa aiba suma elementelor prima
    :param lst: lista de numere intregi
    :return: subsecventa_maxima: lista de numere intregi
    '''
    subsecventa_maxima = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if is_prime(sum_of_list(lst[i:j + 1])) == True and len(lst[i:j + 1]) > len(subsecventa_maxima):
                subsecventa_maxima = lst[i:j + 1]
    return subsecventa_maxima

def test_get_longest_sum_is_prime():
    assert get_longest_sum_is_prime([13, 1, 9, 2, 6]) == [13, 1, 9, 2, 6]
    assert get_longest_sum_is_prime([3, 3, 3]) == [3]
    assert get_longest_sum_is_prime([7, 1, 1, 1, 1, ]) == [7, 1, 1, 1, 1]


def main():
    lst = []
    while True:
        show_menu()
        opt = input('Optiunea: ')
        if opt == '1':
            lst = read_list()
        elif opt == '2':
            print('Cea mai lunga subsecventa in care toate elementele sunt pare:', get_longest_all_even(lst))
        elif opt == '3':
            print('Cea mai lunga subsecventa in care toate elementele sunt formate din cifre prime:',get_longest_prime_digits(lst))
        elif opt == '4':
            print('Cea mai lungă subsecvență cu proprietatea ca suma numerelor sa fie prima',get_longest_sum_is_prime(lst))
        elif opt == 'x':
            break
        else:
            print('Optiune invalida.')

if __name__ == '__main__':
    test_is_even()
    test_is_prime_digits()
    test_get_longest_prime_digits()
    test_is_prime()
    test_get_longest_sum_is_prime()
    main()
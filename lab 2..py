
'''
Problema 5: Determina daca un nr dat este palindrom
returneaza True daca numarul este palindrom sau False in caz contrar
'''
def is_palindrome(n):
    copie_n = n
    #fac o copie a numarului n pentru a-l putea compara cu inversul sau
    invers_n = 0
    #calculez in variabila "invers_n" inversul numarului n
    while(n>0):
        ultima_cifra = n%10
        invers_n = invers_n*10 + ultima_cifra
        n = n//10
    if copie_n == invers_n:
        return True
    return False
def test_is_palindrome():
    assert is_palindrome(7) is True
    assert is_palindrome(122) is False
    assert is_palindrome(292) is True
    assert is_palindrome(2972) is False


'''
Problema 6: Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime. De exemplu, 233 este superprim, deoarece 2, 23 și 233 sunt toate prime, dar 237 nu este superprim, deoarece 237 nu este prim.
returneaza True daca numarul este superprim sau False in caz contrar
'''
def is_superprime(n):
    if n<2:
        return False
        #daca numarul este mai mic decat 2 el nu este prim
    else:
        while (n>0):
            #cat timp numarul este diferit de 0 îi extragem prefixele
            for i in range (2,n//2+1):
                if n%i==0:
                    return False
                #dacă găsim un prefix care nu este prim se returnează False pentru tot numărul
            n = n//10
        return True
    #dacă nu am găsit niciun prefix care să nu fie neprim înseamnă că numărul este superprim și se returnează True

def test_is_superprime():
    assert is_superprime(233) is True
    assert is_superprime(237) is False


'''
Problema 7: Determină dacă un număr este antipalindrom
returneaza True daca numarul este antipalindrom sau False in caz contrar
'''
def is_antipalindrome(n):
    copie_n = n
    #fac o copie a numarului n pentru a putea compara cifrele egal departate ale numarului cu cele ale inversului sau
    invers = 0
    contor_cifre = 0
    while (n>0):
        ultima_cifra = n%10
        invers = invers*10 + ultima_cifra
        n = n//10
        contor_cifre = contor_cifre +1
        #contorizez numarul de cifre
    contor_cifre = contor_cifre //2
    #accesez cifrele doar pana la jumatatea numarului
    while (contor_cifre >0):
        if(copie_n%10==invers%10):
            return False
        copie_n = copie_n //10
        invers = invers //10
        contor_cifre = contor_cifre - 1
    return True

def test_is_antipalindrome():
    assert is_antipalindrome(2783) is True
    assert is_antipalindrome(2773) is False
    assert is_antipalindrome(27573) is False
    assert is_antipalindrome(321) is True

def main():
    print(is_palindrome(1))
    test_is_palindrome()
    print(is_superprime(237))
    test_is_superprime()
    print(is_antipalindrome(27583))
    test_is_antipalindrome()
    shouldRun = True
    while shouldRun :
        print ("1. Palindrom ")
        print ("2. Superprim")
        print ("3. Antipalindrom")
        print ("4. Test daca este palindrom")
        print ("5. Test daca este superprim")
        print ("6. Test daca este antipalindrom")
        print ("x. Iesire")
        option = input("Introduceti optiunea: ")
        if option == "x":
            shouldRun = False
        elif option== "1":
            numar = int(input("Introduceti un numar spre verificare: "))
            print(is_palindrome(numar))
        elif option == "2":
            numar = int(input("Introduceti un numar spre verificare: "))
            print(is_superprime(numar))
        elif option == "3":
            numar = int(input("Introduceti un numar spre verificare: "))
            print(is_antipalindrome(numar))
        elif option == "4":
            print("Se ruleaza testele daca functia palindrom este corecta")
            test_is_palindrome()
        elif option == "5":
            print("Se ruleaza testele daca functia superprim este corecta")
            test_is_superprime()
        elif option == "6":
            print("Se ruleaza testele daca functia antipalindrom este corecta")
            test_is_antipalindrome()
        else:
            print("Optiunea este gresita!")

if __name__ == "__main__":
    main()
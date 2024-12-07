"""
 Klucze w szyfrze afinicznym

W szyfrze afinicznym mamy dwa klucze:

    aa: klucz mnożący, który musi być względnie pierwszy z nn (rozmiarem alfabetu),
    bb: klucz przesunięcia, który może przyjmować dowolną wartość z zakresu {0,1,…,n−1}{0,1,…,n−1}.

Dlatego:

    bb ma nn możliwych wartości.
    aa musi być wybrany spośród liczb, które są względnie pierwsze z nn.

2. Liczba możliwych kluczy aa

Funkcja ϕ(n)ϕ(n) (funkcja Eulera) zwraca liczbę liczb względnie pierwszych z nn w zakresie od 11 do nn. Oznacza to, że:
ϕ(n)=∣{x∈Z:1≤x<n i gcd(x,n)=1}∣
ϕ(n)=∣{x∈Z:1≤x<n i gcd(x,n)=1}∣

Dla każdego nn:

    Istnieje ϕ(n)ϕ(n) możliwych wartości dla klucza aa.

3. Całkowita liczba kluczy

Każda wartość aa może być sparowana z dowolną wartością bb, co daje ϕ(n)×nϕ(n)×n możliwych kombinacji. Ostateczna liczba kluczy wynosi:
Liczba kluczy=n⋅ϕ(n)
Liczba kluczy=n⋅ϕ(n)
Przykłady

Rozważmy kilka przykładów, aby zobaczyć to w praktyce:

    Dla n=26n=26 (alfabet angielski):
        n=26n=26, a ϕ(26)=ϕ(2⋅13)=(2−1)(13−1)=1⋅12=12ϕ(26)=ϕ(2⋅13)=(2−1)(13−1)=1⋅12=12.
        Klucz aa ma 12 możliwych wartości (np. 1,3,5,7,9,11,15,17,19,21,23,251,3,5,7,9,11,15,17,19,21,23,25).
        Klucz bb ma 26 możliwych wartości (0,1,2,…,250,1,2,…,25).
        Całkowita liczba kluczy: 26⋅12=31226⋅12=312.

    Dla n=9n=9:
        n=9n=9, a ϕ(9)=ϕ(32)=9⋅(1−13)=9⋅23=6ϕ(9)=ϕ(32)=9⋅(1−31​)=9⋅32​=6.
        Klucz aa ma 6 możliwych wartości (1,2,4,5,7,81,2,4,5,7,8).
        Klucz bb ma 9 możliwych wartości (0,1,2,…,80,1,2,…,8).
        Całkowita liczba kluczy: 9⋅6=549⋅6=54.
"""


def euler_phi(n):
    """
    Oblicza funkcję Eulera φ(n), czyli liczbę liczb względnie pierwszych z `n`.
    """
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def possible_keys_count(n):
    """
    Oblicza całkowitą liczbę możliwych kluczy w szyfrze afinicznym dla alfabetu rozmiaru `n`.
    """
    phi_n = euler_phi(n)
    return n * phi_n

# Przykłady
n1 = 26
n2 = 9
print(f"Dla n = {n1}, liczba możliwych kluczy: {possible_keys_count(n1)}")
print(f"Dla n = {n2}, liczba możliwych kluczy: {possible_keys_count(n2)}")

# Calendier Mathématique Janvier 2021

## 4 Janvier

### Mise en équation

martina = 2 * roger
martina = raphaël + 5
martina + roger + raphaël = 70

### Solution

[solution](https://www.wolframalpha.com/input/?i=a%3D2+b%2Ca%3Dc%2B5%2Ca%2Bb%2Bc%3D70)

martina = 30
roger = 15
raphaël = 25

## 6 Janvier

### solution

Soit H1, B1 = nombre de points des surfaces haute et basse du premier dé

Soit H2, B2 = nombre de points des surfaces haute et basse du deuxième dé

On a:
- H1 (1 à 6)
- B1 = 7 - H1
- H2 = 5 - (7 - H1) = H1 - 2
- B2 = 7 - H2 = 7 - H1 + 2 = 9 - H1

D'où: H1 + B2 = 9

réponse: 9


Nota: tous les empilements ne sont pas possibles

## 12 Janvier

### Solution

3^x - 3^(x-1) = 162

=> 3 * 3^(x-1) - 3^(x-1) = 162

=> (3 - 1) * 3^(x-1) = 162

=> 2 * 3^(x-1) = 162

=> 3^(x-1) = 81

=> x = 5


## 19 Janvier

### Solution

4 triangles équilatéraux de 1cm de côté:
    hauteur = √3/2
    base = 1
    S = (√3/2 * 1 / 2) * 4 = √3 cm²

1 carré central de 1cm de côté:
    S = 1 cm²

réponse: 1+√3 cm²


## 29 Janvier

### solution

p^q + 1 premier ?

si p impair p^q = impair, donc p^q+1 pair et donc pas premier

donc p est forcément pair, et donc vaut 2 (seul premier pair)

q=2  2^q+1=5 ok
q=3  2^3+1=9 ko
q=5  2^5+1=33 ko
q=7  2^7+1=129 ko
q=11 2^11+1=2049 ko

toujours divisible par 3 si q impair

supposons qu'il existe X tel que 2^(2k+1) + 1 = 3*X

c'est vrai pour k = 1 (X = 3)

2^(2k+2+1) + 1 = 2^(2k+1) * 2^2 + 1 = 4 * 2^(2k+1) + 4 - 3 =  4 * (2^(2k+1) + 1) - 3 = 4 * (3 * X) - 3 = 3 * (4 * X - 1)

on montre donc qu'il existe X' tel que 2^(2(k+1)+1) + 1 = 3*X'

par récurrence on conclut que 2^q+1 est multiple de 3 si q est impair.


réponse: 1 seul couple (2, 2)


## 26 Janvier

### Solution

hexagone de 2 cm de côté

rayon du cercle circonscrit = 2 cm,
surface = πr² = 4π

rayon du cercle inscrit = hauteur du triangle équilatéral de côté 2 cm,
h = √3/2 * r = √3,
surface = √3² π = 3π

surface anneau = 4π - 3π = π

réponse: π cm²

## 28 Janvier

### solution

```
    /|\
 a / | \ a
  /  |h \
 /-------\
     b

h=8
```

On a:
- 2a + b = 32
- (b/2)² + 8² = a²

On résout ce système:
- b = 32 - 2a
- ((32-2a)/2)² + 64 = a² ⇒ 16² - 32a + a² + 64 = a² ⇒ 320 = 32a

D'où:
- a = 10
- b = 32 - 2*10 = 12

L'aire du triangle est h * b/2 = 8 * 6 = 48

réponse: 48 cm²

## 29 Janvier

### solution

∑x / n = 4850

∑(x - 10) / n = (∑x - 10 * n) / n = (∑x / n) - (10 * n / n) = 4850 - 10 = 4840

réponse: 4840

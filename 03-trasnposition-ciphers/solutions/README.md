# Solutions - Transposition Ciphers

Ky dokument i jep shpjegimet konceptuale per algoritmet baze te javes:
- si organizohet plaintext ne struktura (matrice)
- si kthehet kjo logjike ne kod Python

## Ideja baze

Ndryshe nga substitution ciphers, ketu karakteret nuk zevendesohen me karaktere te tjera.
Transposition ciphers:
- ruajne te njejtat karaktere
- ndryshojne vetem renditjen e tyre

Nese `P` eshte plaintext dhe `C` ciphertext:
- `multiset(P) = multiset(C)`
- ndryshon vetem pozicioni i secilit karakter

## 1) Simple (Columnar) Transposition

Le te jete:
- `n = len(P)` pas heqjes se hapesirave
- `k =` numri i kolonave
- `r = ceil(n / k)` numri i rreshtave

### Perkufizimi i enkriptimit
Plaintext shkruhet ne nje matrice `M[r][k]` rresht pas rreshti:

`M[i][j] = P[i * k + j]`, kur ky indeks ekziston.

Pastaj ciphertext lexohet kolone pas kolone:

`C = M[0][0], M[1][0], ..., M[r-1][0], M[0][1], ...`

### Si transformohet ne kod
- `row_count = math.ceil(len(text) / key)`
- krijohet nje matrice bosh me `row_count` rreshta dhe `key` kolona
- teksti vendoset ne matrice rresht pas rreshti
- ciphertext ndertohet duke iteruar fillimisht kolonat, pastaj rreshtat

### Si behet dekriptimi
- llogaritet perseri `row_count`
- percaktohet sa kolona kane gjatesi te plote
- ciphertext ndahet ne segmente sipas gjatesise se seciles kolone
- plaintext rindertohet duke lexuar rresht pas rreshti

## Shenim

Transposition ciphers jane te rendesishme per te kuptuar historine e kriptografise,
por nuk konsiderohen te sigurta per perdorim modern pa kombinime ose mekanizma me te forte.

# Solutions — Substitution Ciphers

Ky dokument i jep zgjidhjet konceptuale per algoritmet e javes:
- perkufizimi matematikor
- si formula kthehet ne kod Python

## Notacioni bazik

Per te gjithe algoritmet (A-Z):
- `A = 0, B = 1, ..., Z = 25`
- `idx(X)` = pozita numerike e shkronjes `X`
- `chr26(n)` = shkronja qe korrespondon me `n mod 26`

Ne kod, kjo behet zakonisht keshtu:
- `idx = ord(ch) - ord('A')` (ose `ord('a')` per lowercase)
- `new_idx = (...) % 26`
- `new_ch = chr(new_idx + ord('A'))`

## 1) Caesar Cipher

### Perkufizimi matematikor
- Enkriptim: `C_i = (P_i + k) mod 26`
- Dekriptim: `P_i = (C_i - k) mod 26`

`k` eshte celesi (zhvendosja fikse).

### Si transformohet ne kod
- `ord(ch) - ord('A')`: shkronja ne numer
- `+ key` ose `- key`: zbatim i formules
- `% 26`: rikthim ne intervalin `0..25`
- `chr(... + ord('A'))`: numer ne shkronje
- Karakteret jo-alfabetike kalohen pa ndryshim.

## 2) Caesar Brute Force

### Perkufizimi matematikor
Per nje ciphertext `C`, provohen te gjithe celesat:
- `P^(k) = D_k(C)`, per `k in {0, 1, ..., 25}`

Rezultati i sakte eshte ai qe jep tekst kuptimplote.

### Si transformohet ne kod
- `for key in range(26):`
- `plain_text = decrypt(cipher_text, key)`
- printohet secili kandidat.

## 3) Frequency Analysis

### Perkufizimi matematikor
Per secilen shkronje `L`:
- `count(L) =` sa here paraqitet `L`
- `freq(L) = count(L) / N`, ku `N` eshte numri total i shkronjave

Ky perdoret per te vleresuar celesin me statistika te gjuhes.

### Si transformohet ne kod
- Iterim karakter per karakter
- Filtrim me `isalpha()`
- Normalizim me `upper()`
- Numerim me dictionary:
  - `statistics[upper_ch] = statistics.get(upper_ch, 0) + 1`

## 4) Atbash Cipher

### Perkufizimi matematikor
- Enkriptim dhe dekriptim: `C_i = 25 - P_i`
- E njejta formule vlen ne te dy drejtimet:
  - `T(T(x)) = x` (involucion)

### Si transformohet ne kod
- Per uppercase:
  - `chr(ord('Z') - (ord(ch) - ord('A')))`
- Per lowercase:
  - `chr(ord('z') - (ord(ch) - ord('a')))`

Kjo realizon pasqyrimin `A<->Z`, `B<->Y`, ...

## 5) Vigenere Cipher

Le te jete celesi `K = (K_0, K_1, ..., K_{m-1})`.

### Perkufizimi matematikor
- Enkriptim: `C_i = (P_i + K_{i mod m}) mod 26`
- Dekriptim: `P_i = (C_i - K_{i mod m}) mod 26`

Ndryshe nga Caesar, zhvendosja ndryshon per cdo shkronje sipas celesit.

### Si transformohet ne kod
- `key = key.upper()`: normalizim
- `internal_key = ord(key[key_index % len(key)]) - ord('A')`
- Aplikohet `+ internal_key` (encrypt) ose `- internal_key` (decrypt)
- `key_index` rritet vetem kur karakteri eshte shkronje.

## 6) One-Time Pad (OTP)

Le te kemi plaintext `P` dhe celes `K` me te njejten gjatesi `n`.

### Perkufizimi matematikor
- Enkriptim: `C_i = (P_i + K_i) mod 26`, per `i = 0..n-1`
- Dekriptim: `P_i = (C_i - K_i) mod 26`

### Si transformohet ne kod
- `text_to_numbers(...)`: kthen tekstin ne numra `0..25`
- Kontroll gjatesie:
  - `if len(plain) != len(key_nums): raise ValueError(...)`
- Iterim paralel me `zip(plain, key_nums)` dhe aplikim i formules.

### Kushtet per sigurine teorike te OTP
OTP eshte teorikisht i pathyeshem vetem nese:
1. Celesi eshte vertete rastesor.
2. Celesi ka gjatesi te njejte me plaintext-in.
3. Celesi perdoret vetem nje here.
4. Celesi mbahet sekret.

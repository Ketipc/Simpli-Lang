# SimpliLang Genişletme Rehberi

## 1. Yeni Fonksiyon Eklemek
- `core/stdlib.py` dosyasına yeni fonksiyon yaz.
- `AVAILABLE_FUNCTIONS` listesine ekle.

## 2. Yeni Kütüphane Eklemek
- `libs/` altına `.py` dosyası koy.
- `stdlib.py` dosyasından içe aktar.

## 3. Örnek
```python
def kare(args):
    return args[0] * args[0]
```

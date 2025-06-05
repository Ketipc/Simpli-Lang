from core.helpers import sayi_kontrol

def yaz(args):
    for arg in args:
        print(arg)
    return ""

def topla(args):
    return sum(args)

def carp(args):
    result = 1
    for a in args:
        result *= a
    return result

AVAILABLE_FUNCTIONS = {
    "yaz": yaz,
    "topla": topla,
    "carp": carp
}

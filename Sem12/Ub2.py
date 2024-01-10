def grossbuchstabe(s):
    if len(s) == 0:
        return None
    if s[-1].isupper() is True:
        return s[-1]
    else:
        return grossbuchstabe(s[:-1])


print(grossbuchstabe('MirUna'))
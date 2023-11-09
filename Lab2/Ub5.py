def filter(bez, l):
    new_l = []
    for nr in l:
        new_bez = bez.replace('x', str(nr//10)) #inlocuieste x cu prima cifra
        new_bez = new_bez.replace('y', str(nr%10)) #inlocuieste y cu a doua cifra
        k = new_bez.split('=') # sterge egal
        new_bez = k[0] + ' == ' + k[1] # pune dublu egal
        ok = eval(new_bez)
        if ok == True:
            new_l.append(nr) #daca beziehung e valabil adauga in lista noua
    return new_l


print(filter('x=y*3', [31, 93, 62, 39, 94]))

def main():

    d = {'c1': 'Vermelho', 'c2': None, 'c3': 'Verde'}

    print("Antes", d)

    lstkeys = list(d.keys())

    i = 0 
    while i < len(lstkeys): #não incrementa automaticamnte igual ao for
        chave = lstkeys[i]
        if d[chave] == None:
            del d[chave]
        i = i + 1 #no while, eu que tenho que fazer

    print("Depois", d)

main()

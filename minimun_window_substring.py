def minWindow(s, t):
    # Inicializo el diccionario con la frecuencia de cada letra de t, y otro diccionario en el que llevo la cuenta actual
    frec_letras_clave = dict()
    frec_letras_actual = dict()

    for letra in t:
        if letra in frec_letras_clave:
            frec_letras_clave[letra] += 1
        else:
            frec_letras_clave[letra] = 1
            frec_letras_actual[letra] = 0
    
    # Hago otro diccionario en el que llevo la cuenta de la frecuencia del substring actual
    res_len = float('inf')
    res_l, res_r = -1, -1


    l = 0
    for r in range(len(s)):
        if s[r] in frec_letras_clave:
            frec_letras_actual[s[r]] += 1
        
        while solucion_encontrada(frec_letras_actual, frec_letras_clave):
            if (r - l + 1) < res_len:
                res_len = r - l + 1
                res_l = l
                res_r = r

            if s[l] in frec_letras_clave:
                frec_letras_actual[s[l]] -= 1

            l += 1



        r += 1

    return s[res_l:res_r+1]


def solucion_encontrada(frec_letras_actual, frec_letras_clave):
    for l in frec_letras_clave:
        if frec_letras_actual[l] < frec_letras_clave[l]:
            return False
        
    return True
        




print(minWindow("ADOBECODEBANC", "ABC"))
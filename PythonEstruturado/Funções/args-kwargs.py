# O args vai permitir vc passar vários parametros sem dar nome para esses parametros.

def calcular_imposto(valor, *args):
    total_imposto = 0
    for item in args:
        total_imposto += valor * item
    
    return total_imposto

print(calcular_imposto(100, 200, 300, 10))

# O kwargs serve para vc passar quantos parametros vc quiser, sempre dando nome para esses parametros.

def calcular_imposto(**kwargs):
    total_imposto = 0
    print(kwargs)
    return total_imposto

#print(calcular_imposto(perc_ir=0.29, perc_iss=0.290, perc_csll=0.29, perc_is=0.207))

def calcular_imposto_trimestral(valor, **kwargs):
    total_imposto = 0
    print(kwargs)
    if "perc_ir" in kwargs:
        total_imposto += valor * kwargs["perc_ir"]
    if "perc_csll" in kwargs:
        total_imposto += valor * kwargs["perc_csll"]   
    return total_imposto

print(calcular_imposto_trimestral(1000, perc_ir=0.29, perc_pis=0.290, perc_csll=0.29, perc_is=0.207))


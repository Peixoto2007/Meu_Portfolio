# Crie uma função chamada verificar_aprovacao que receba uma média.
# A função deve retornar:
# - "Aprovado" se média >= 7
# - "Recuperação" se média >= 5 e < 7
# - "Reprovado" se média < 5

# Fora da função:
# - peça a média ao usuário
# - chame a função
# - mostre o resultado

# Regras:
# - usar if / elif / else
# - usar return
# - usar float no input

def verificar_aprovacao (nota1,nota2,nota3):
    total = nota1+nota2+nota3
    media  = total/3
    
    
    if media >7:
        return"aprovado"
    elif media <7 and media >5:
        return "recuperação"
    else: return"reprovado"

nota1 = float(input('qual foi sua nota'))
nota2 = float(input('qual foi sua nota'))
nota3 = float(input('qual foi sua nota'))
print(verificar_aprovacao(nota1,nota2,nota3))

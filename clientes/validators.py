import re
from validate_docbr import CPF

def cpf_valido(numerocpf):
    cpf = CPF()
    return cpf.validate(numerocpf)

def nome_valido(nome):
    return all(c.isalpha() or c.isspace() for c in nome)
        
def rg_valido(rg):
    return len(rg) == 9
        
def celular_valido(celular):
    """Verifica se o celular é válido (99 99999-9999) - utilizando expressão regular"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    # '[0-9]{2}' ... validação de 99 ( valor numérico de 0 à 9 - com 2 dígitos)
    # ' ' o espaço indicando o espaço do celular
    # '[0-9]{5}' ... validação de 99999 ( valor numérico de 0 à 9 - com 5 dígitos)
    # '-' indicando que deve ter um hífen
    # '[0-9]{4}' ... validação de 9999 ( valor numérico de 0 à 9 - com 4 dígitos)
    resposta = re.findall(modelo,celular)
    return resposta

       

import math


def byte_formatter(number:int, unit='si', decimal_digits=3, decimal:str=','):
    unidades = {'SI':1000, 'IEC':1024}
    prefix = ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']
    num_super = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
    
    base = unidades.get(unit, None)
    if not base:
        raise TypeError(f'Unidade `{unit}` não é válida!')

    deci = math.floor(math.log10(number))
    ordem = deci // 3
    div = base ** ordem

    try:
        pre = prefix[ordem]
    except IndexError:
        n = ''.join([num_super[int(i)] for i in str(ordem*3)])
        pre = f'10{n}'

    return str(round(number/div, decimal_digits)).replace('.', decimal) + f' {pre}B'


def byte_counter(chars:str,
                 word_length:int = 8,
                 length_char:int = 1,
                 break_line:bool = True):
    
    n_char = len(chars)
    b_value = 1 if break_line else 0

    return length_char * (n_char ** word_length) * (word_length + b_value)


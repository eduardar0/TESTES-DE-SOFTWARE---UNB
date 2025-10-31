def eh_operador(c):
    return c in ['+', '-', '*', '/']

def eh_digito(c):
    return c.isdigit()

def eh_expressao_valida(expressao):
    if expressao is None or expressao.strip() == "":
        return False
    
    expr = expressao.replace(" ", "")
    
    # Regra 3: Não pode começar ou terminar com operador
    if eh_operador(expr[0]) or eh_operador(expr[-1]):
        return False
    
    # Regra 2: Não pode haver dois operadores seguidos
    for i in range(len(expr) - 1):
        if eh_operador(expr[i]) and eh_operador(expr[i + 1]):
            return False
    
    # Regra 1: Parênteses balanceados
    balanceamento = 0
    for char in expr:
        if char == '(':
            balanceamento += 1
        elif char == ')':
            balanceamento -= 1
            if balanceamento < 0:
                return False
    
    if balanceamento != 0:
        return False
    
    # Regras 4 e 5: Transições válidas
    for i in range(len(expr) - 1):
        atual = expr[i]
        proximo = expr[i + 1]
        
        # Após número: operador ou ')'
        if eh_digito(atual):
            if not (eh_operador(proximo) or proximo == ')'):
                return False
        # Após operador: número ou '('
        elif eh_operador(atual):
            if not (eh_digito(proximo) or proximo == '('):
                return False
        # Após '(': número ou '('
        elif atual == '(':
            if not (eh_digito(proximo) or proximo == '('):
                return False
        # Após ')': operador ou ')'
        elif atual == ')':
            if not (eh_operador(proximo) or proximo == ')'):
                return False
    
    return True
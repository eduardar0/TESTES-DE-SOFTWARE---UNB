class ValidadorExpressao:
    
    @staticmethod
    def eh_expressao_valida(expressao):
        if expressao is None or expressao.strip() == "":
            return False
        
        expr = expressao.replace(" ", "")
        
        return (ValidadorExpressao._comeca_e_termina_corretamente(expr) and
                ValidadorExpressao._sem_operadores_consecutivos(expr) and
                ValidadorExpressao._parenteses_balanceados(expr) and
                ValidadorExpressao._transicoes_validas(expr))
    
    @staticmethod
    def _eh_operador(c):
        return c in ['+', '-', '*', '/']
    
    @staticmethod
    def _eh_digito(c):
        return c.isdigit()
    
    @staticmethod
    def _comeca_e_termina_corretamente(expr):
        return not (ValidadorExpressao._eh_operador(expr[0]) or 
                   ValidadorExpressao._eh_operador(expr[-1]))
    
    @staticmethod
    def _sem_operadores_consecutivos(expr):
        for i in range(len(expr) - 1):
            if (ValidadorExpressao._eh_operador(expr[i]) and 
                ValidadorExpressao._eh_operador(expr[i + 1])):
                return False
        return True
    
    @staticmethod
    def _parenteses_balanceados(expr):
        balanceamento = 0
        for char in expr:
            if char == '(':
                balanceamento += 1
            elif char == ')':
                balanceamento -= 1
                if balanceamento < 0:
                    return False
        return balanceamento == 0
    
    @staticmethod
    def _transicoes_validas(expr):
        for i in range(len(expr) - 1):
            atual = expr[i]
            proximo = expr[i + 1]
            
            if ValidadorExpressao._eh_digito(atual):
                if not (ValidadorExpressao._eh_operador(proximo) or proximo == ')'):
                    return False
            elif ValidadorExpressao._eh_operador(atual):
                if not (ValidadorExpressao._eh_digito(proximo) or proximo == '('):
                    return False
            elif atual == '(':
                if not (ValidadorExpressao._eh_digito(proximo) or proximo == '('):
                    return False
            elif atual == ')':
                if not (ValidadorExpressao._eh_operador(proximo) or proximo == ')'):
                    return False
        
        return True

def eh_expressao_valida(expressao):
    return ValidadorExpressao.eh_expressao_valida(expressao)
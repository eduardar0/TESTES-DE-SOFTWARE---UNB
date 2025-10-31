import unittest
import sys
import os

import unittest
from src.validador_expressao import eh_expressao_valida

class TestValidadorExpressao(unittest.TestCase):
    def test_expressao_vazia(self):
        self.assertFalse(eh_expressao_valida(""))

    def test_expressao_simples_valida(self):
        self.assertTrue(eh_expressao_valida("1+2"))

    def test_termina_com_operador(self):
        self.assertFalse(eh_expressao_valida("1+"))

    def test_comeca_com_operador(self):
        self.assertFalse(eh_expressao_valida("+1"))

    def test_operadores_consecutivos(self):
        self.assertFalse(eh_expressao_valida("1++2"))

    def test_parenteses_balanceados(self):
        self.assertTrue(eh_expressao_valida("(1+2)*3"))

    def test_parenteses_desbalanceados(self):
        self.assertFalse(eh_expressao_valida("(1+2"))

    def test_numero_apos_parentese_fechando(self):
        self.assertFalse(eh_expressao_valida("(1+2)3"))

    def test_operador_apos_parentese_abrindo(self):
        self.assertFalse(eh_expressao_valida("(+1)"))



if __name__ == '__main__':
    unittest.main()
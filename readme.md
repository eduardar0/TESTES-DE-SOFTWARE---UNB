##  Descrição
Implementação de um validador de expressões matemáticas usando **Test-Driven Development (TDD)** em Python. O validador verifica se expressões matemáticas seguem as regras sintáticas definidas.

## Estrutura do projeto 
```
aee_4/
├── src/
│   └── validador_expressao.py
├── tests/
│   └── test_validador_expressao.py
└── README.md
```

### Regras Implementadas

- Parênteses balanceados - ( ) devem fechar na ordem correta

- Sem operadores consecutivos - Não permite ++, --, +*, etc.

- Não começa/termina com operador - +1 ou 1+ são inválidos

- Transições válidas - Regras específicas após números, operadores e parênteses

- Ignora espaços - ( 1 + 2 ) é tratado como (1+2)

### Para executar os testes:

```
# Na pasta raiz do projeto (aee_4/)
python -m unittest discover tests -v
```


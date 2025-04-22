# Validadores-BR
 
Uma coleção de validadores em Python para dados comuns no Brasil. Esses validadores são utilizados em diversos aplicativos para garantir a integridade e consistência das informações.​

## ✨ Funcionalidades
- Validação de CPF e CNPJ: Verifica a validade de números de CPF e CNPJ.
- Validação de telefones celulares: Confirma se o número de telefone celular está no formato correto.
- Validação de datas e horas brasileiras: Garante que as datas e horas estejam no formato brasileiro adequado.
- Busca de CEPs: Permite a busca de endereços a partir do CEP informado.​

## 📁 Estrutura do Projeto
- `cpf_cnpj.py`: Validação de CPF e CNPJ.
- `telefone_celular.py`: Validação de números de telefone celular.
- `data_hora_br.py`: Validação de datas e horas no formato brasileiro.
- `busca_cep.py`: Função para busca de endereços a partir do CEP.
- `telefone_celular.py`: Validação de números de telefone celular.
- `data_hora_br.py`: Validação de datas e horas no formato brasileiro.
- `busca_cep.py`: Função para busca de endereços a partir do CEP.​

## 🚀 Como Utilizar
1. Clone o repositório:
```bash
git clone https://github.com/EdimarDeSa/Validadores-BR.git
```
2. Importe os módulos desejados em seu projeto Python:​
```python
from cpf_cnpj import validar_cpf, validar_cnpj
from telefone_celular import validar_telefone
from data_hora_br import validar_data, validar_hora
from busca_cep import buscar_endereco_por_cep
```
3. Utilize as funções conforme necessário:
```python
if validar_cpf("123.456.789-09"):
    print("CPF válido")
else:
    print("CPF inválido")
```

## 📄 Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](https://github.com/EdimarDeSa/Validadores-BR/blob/main/LICENSE) para mais informações.​

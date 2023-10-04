from acesso_cep import BuscaEndereco

# endereco = '88132600'
# resultado = BuscaEndereco(endereco)
# print(resultado)
# assert str(resultado) == 'CEP: 88132-600 - Cidade: Palhoça - Estado: SC'

# from cpf_cnpj import Documento
#
# cpf = '048.245.251-01'
# doc = Documento(cpf)
# print(doc)
# assert str(doc) == '04824525101'


from data_hora_br import DatasBr

hora_cadastro = DatasBr()
print(hora_cadastro)


from telefone_celular import TelefoneECelular

tel = '65999123899'
print(TelefoneECelular(tel))

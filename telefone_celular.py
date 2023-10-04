import re


class TelefoneECelular:
    def __init__(self, telefone):
        self._telefone = self._sanitiza_telefone(telefone)
        if self.valida_telefone(telefone):
            self.__numero = telefone
        else:
            raise ValueError("Número inválido, deve ser um celular ou fixo com DDD")

    @staticmethod
    def valida_telefone(telefone):
        return re.match(r'^(\+\d{1,3})?(\d{2})([6-9])?(\d{4})(\d{4})$', telefone)

    def _captura_numeros(self):
        telefone = re.search(r'([0-9]{2,3}?)?([1-9]{2})([6-9])?([0-9]{4})([0-9]{4}$)', self.__numero)
        return telefone.group  # Só para facilitar a vida e diminuir o tamanho a fstring

    def __str__(self):
        cod = self._captura_numeros
        if not cod(1) and not cod(3):
            return f"({cod(2)}) {cod(4)}-{cod(5)}"
        elif not cod(1):
            return f"({cod(2)}) {cod(3)}{cod(4)}-{cod(5)}"
        elif not cod(3):
            return f"+{cod(1)} ({cod(2)}) {cod(4)}-{cod(5)}"
        else:
            return f"+{cod(1)} ({cod(2)}) {cod(3)}{cod(4)}-{cod(5)}"

    def _sanitiza_telefone(self, telefone) -> str:
        return re.sub(r'\D', '', telefone)


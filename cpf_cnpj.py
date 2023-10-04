import re

from validate_docbr import CPF, CNPJ


class Documento:
    def __init__(self, doc_number: str):
        self._doc: str = self._sanitiza_doc(doc_number)
        self._validador_doc, self._doc_type= self._verifica_tipo()
        self._validade_do_doc: bool = self._validador_doc.validate(self._doc)
        self._doc_com_mascara: str = self._validador_doc.mask(self._doc)

    @property
    def mascara_doc(self) -> str:
        return self._doc_com_mascara

    @property
    def numero_doc(self) -> str:
        return self._doc

    @property
    def validade_doc(self) -> bool:
        return self._validade_do_doc

    def _sanitiza_doc(self, doc_number: str) -> str:
        return re.sub(r'\D', '', doc_number)

    def _verifica_tipo(self) -> tuple[[CPF, CNPJ], str]:
        total_de_digitos = len(self._doc)
        tipos_doc = {
            11: (CPF, 'CPF'),
            14: (CNPJ, CNPJ)
        }
        obj, tipo = tipos_doc[total_de_digitos]
        return obj(), tipo

    def __str__(self) -> str:
        return f'{self._doc}'

    def __repr__(self) -> repr:
        return f'<Tipo doc: {self._doc_type}>'

from validate_docbr import CPF, CNPJ


class Documento:
    def __init__(self, doc_number: str):
        self._doc = self._sanitiza_doc(doc_number)
        self._validador_doc = self._get_validator()
        self._validade_do_doc = self._validador_doc.validate(self._doc)

        if not self._validade_do_doc:
            raise ValueError(f'DocumentError: Invalid document `{doc_number}`')

        self._doc_com_mascara = self._validador_doc.mask(self._doc)

    def _get_validator(self):
        total_de_digitos = len(self._doc)
        tipos_doc = {
            11: CPF,
            14: CNPJ
        }
        return tipos_doc.get(total_de_digitos, None)()

    @property
    def mascara_doc(self) -> str:
        return self._doc_com_mascara

    @property
    def numero_doc(self) -> str:
        return self._doc

    @property
    def validade_doc(self) -> bool:
        return self._validade_do_doc

    def _sanitiza_doc(self, doc_number):
        return ''.join(filter(str.isdigit, doc_number))

    def __str__(self) -> str:
        return self._doc

    def __repr__(self) -> repr:
        return f'<Tipo doc: {self._validador_doc.__class__.__name__}>'


if __name__ == '__main__':
    print(repr(Documento('048.245.251-01')))
    # print(str(Documento('88.321.331/0001-01')))

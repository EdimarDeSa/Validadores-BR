from datetime import datetime, timedelta


class DatasBr:
    def __init__(self):
        self.__momento_cadastro = datetime.today()
        print(self.__momento_cadastro)

    def __mes_cadastro(self):
        meses_do_ano = ["Janeiro", "Fevereiro", "Março", "Abril",
                        "Maio", "Junho", "Julho", "Agosto",
                        "Setembro", "Outubro", "Novembro", "Dezembro"]
        indice = self.__momento_cadastro.month - 1
        return meses_do_ano[indice]

    def __dia_semana(self):
        dias_da_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sesxta-feira",
                          "Sábado", "Domingo"]
        indice = self.__momento_cadastro.weekday()
        return dias_da_semana[indice]

    @property
    def __format_data(self):
        data_formatada = self.__momento_cadastro.strftime("%d/%m/%y %H:%M:%S")
        return data_formatada

    def _tempo_cadastro(self):
        tempo_cadastro = datetime.today() + timedelta(days=360) - self.__momento_cadastro
        return tempo_cadastro

    def __str__(self):
        return self.__format_data

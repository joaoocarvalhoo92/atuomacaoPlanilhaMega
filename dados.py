from loteria_caixa import MegaSena
import datetime

concurso = MegaSena()

# Obtenha a data atual
data_atual = datetime.date.today()

# Suponha que data_apuracao é uma string no formato "DD/MM/YYYY"
data_apuracao_str = concurso.dataApuracao()
print(data_apuracao_str)

# Converta a string em um objeto datetime.date
data_apuracao = datetime.datetime.strptime(data_apuracao_str, "%d/%m/%Y").date()

# Verifique se a data de apuração é menor que a data atual
if data_apuracao < data_atual:
    # A data de apuração é anterior à data atual, o programa não continua
    print("A data de apuração é anterior à data atual. O programa não continua.")
else:
    # A data de apuração é igual ou posterior à data atual, o programa prossegue com o código
    print("A data de apuração é igual ou posterior à data atual. O programa prossegue com o código.")
    # Coloque o código que você deseja executar aqui



    
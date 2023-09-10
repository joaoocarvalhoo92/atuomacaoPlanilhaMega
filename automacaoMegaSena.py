
import xlwings as xw
import datetime
import pyperclip
from loteria_caixa import MegaSena
import pywhatkit
import sys


# Obtenha a data atual
data_atual = datetime.date.today()

# Função para executar a macro correspondente ao número sorteado
def executar_macro(numero, wb):
    try:
        macro_nome = f"BOLA{numero}"  # Nome da macro correspondente ao número sorteado
        wb.app.api.Run(macro_nome)  # Execute a macro
        print(f"A macro '{macro_nome}' foi executada com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao executar a macro: {e}")

# Caminho da planilha Excel
caminho_planilha = r"C:\Users\joao1\OneDrive\Documentos\AUTOMACAO_MEGASENA.xlsm"



# Criar uma instância do concurso da Mega Sena
concurso = MegaSena()


# Suponha que data_apuracao é uma string no formato "DD/MM/YYYY"
data_apuracao_str = concurso.dataApuracao()

# Converta a string em um objeto datetime.date
data_apuracao = datetime.datetime.strptime(data_apuracao_str, "%d/%m/%Y").date()



# Verifique se a data de apuração é menor que a data atual
if data_apuracao < data_atual:
    # A data de apuração é anterior à data atual, o programa não continua
    print("A data de apuração é anterior à data atual. O programa não continua.")
    sys.exit()
else:
    # A data de apuração é igual ou posterior à data atual, o programa prossegue com o código
    print("A data de apuração é igual ou posterior à data atual. O programa prossegue com o código.")
    # Coloque o código que você deseja executar aqui

    # Obter os números sorteados
    numeros_sorteados = concurso.listaDezenas()

    # Abra a planilha antes do loop
    wb = xw.Book(caminho_planilha)

    # Verificar os números sorteados e executar as macros correspondentes
    for numero in numeros_sorteados:
        executar_macro(numero, wb)


    # Execute a macro "RankingBJ" após o término do loop
    try:
        macro_nome_ranking = "RankingBJ"
        wb.app.api.Run(macro_nome_ranking)
        print(f"A macro '{macro_nome_ranking}' foi executada com sucesso após o loop.")
    except Exception as e:
        print(f"Ocorreu um erro ao executar a macro '{macro_nome_ranking}': {e}")

    # Execute a macro "historicoSorteiosMega"
    try:
        macro_nome_historico = "historicoSorteiosMega"
        wb.app.api.Run(macro_nome_historico)
        print(f"A macro '{macro_nome_historico}' foi executada com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao executar a macro '{macro_nome_historico}': {e}")
        
    # Execute a macro "CriarPDFComLimiteDeCelulas"
    try:
        macro_nome_pdf = "CriarPDFComLimiteDeCelulas"
        wb.app.api.Run(macro_nome_pdf)
        print(f"A macro '{macro_nome_pdf}' foi executada com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao executar a macro '{macro_nome_pdf}': {e}")

    # Obtenha a hora atual
    agora = datetime.datetime.now()
    # Pegue a hora atual e adicione 1 minuto ao minuto atual
    hora = agora.hour
    minuto = agora.minute + 1

    # Use as variáveis no lugar dos valores fixos
    pywhatkit.sendwhatmsg("+5511985386994", "*O SORTEIO DA MEGA DOS AMIGOS JA ESTA ATUALIZADO*", hora, minuto)
import pandas as pd
import pywhatkit as kit
import time
import os.path


class Automacao:

    def __init__(self):
        print("Iniciando Automação...")

        # Só tenta carregar o arquivo quando o objeto for criado
        self.diretorio = 'C:/DataFrame/Cadastramento_Odontológico_2.0.xlsx'
        self.data_frame = None  # Inicializa como None

        self.carregar_dataframe()  # Chama método para carregar dados

    def carregar_dataframe(self):
        """Método separado para carregar o DataFrame"""
        try:
            if os.path.exists(self.diretorio):
                print(f"Arquivo encontrado: {self.diretorio}")
                armazenador = pd.read_excel(self.diretorio)
                self.data_frame = pd.DataFrame(armazenador)
                print(f"DataFrame carregado com {len(self.data_frame)} registros")
                return True
            else:
                print(f"Arquivo NÃO encontrado: {self.diretorio}")
                self.data_frame = pd.DataFrame()  # DataFrame vazio
                return False
        except Exception as e:
            print(f"Erro ao carregar DataFrame: {e}")
            self.data_frame = pd.DataFrame()
            return False

    def enviar_mensagens_por_classificacao(self, classificacao_alvo):

        # Verifica se o dataframe foi carregado
        if self.data_frame is None:
            print("DataFrame não carregado. Tentando carregar...")
            if not self.carregar_dataframe():
                print("Não foi possível carregar o DataFrame")
                return

        if self.data_frame.empty:
            print("DataFrame vazio. Verifique o arquivo Excel.")
            return

        classificacao_Acionada = classificacao_alvo
        print('Classificação Alvo:', classificacao_Acionada)

        # Usa o tamanho real do dataframe
        for x in range(len(self.data_frame)):
            try:
                # Declaração das variáveis - Dados do Cliente
                nomeCompleto = self.data_frame.at[x, 'Nome']
                primeiroNome = nomeCompleto.split()[0]  # CORRIGIDO
                telefone = '+' + str(self.data_frame.at[x, 'Telefone'])
                classificacao = self.data_frame.at[x, 'Classificação']

                print(f"Telefone: {telefone} - Classificação: {classificacao}")

                # Só envia se a classificação do cliente corresponder à alvo
                if classificacao == classificacao_Acionada:

                    if classificacao_Acionada == 'A':
                        mensagem = f"Oi {primeiroNome}!\nÉ um prazer ter você conosco!\nEstamos entrando em contato para avisar que as radiografias odontológicas estão prestes a vencer.\nGostaria de agendar um retorno?"

                        print(f"Enviando mensagem para classificação A: {primeiroNome}")
                        kit.sendwhatmsg_instantly(telefone, mensagem)
                        time.sleep(20)

                    elif classificacao_Acionada == 'C':
                        mensagem = f"Oi {primeiroNome}!\nÉ um prazer ter você conosco!\nEstamos entrando em contato para avisar sobre os cuidados com os dentes provisórios, pois eles apresentam risco de soltar ou fraturar.\nGostaria de agendar um retorno?"

                        print(f"Enviando mensagem para classificação C1: {primeiroNome}")
                        kit.sendwhatmsg_instantly(telefone, mensagem)
                        time.sleep(20)
                        print("Processo finalizado!")
            except Exception as e:
                print(f"Erro ao processar linha {x}: {e}")
                continue
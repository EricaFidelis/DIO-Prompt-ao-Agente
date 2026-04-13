import os
import requests
from dotenv import load_dotenv

# 1. Carrega as variáveis do arquivo .env (Key, Token e ID da Lista)
load_dotenv()

class AgenteTrello:
    def __init__(self):
        # Busca as credenciais que você salvou no .env
        self.key = os.getenv("TRELLO_KEY")
        self.token = os.getenv("TRELLO_TOKEN")
        self.list_id = os.getenv("TRELLO_ID_LIST")
        self.base_url = "https://api.trello.com/1/cards"

    def criar_tarefa(self, nome, descricao):
        """Envia a tarefa diretamente para a coluna do seu Trello"""
        
        # Parâmetros exigidos pela API do Trello
        params = {
            'key': self.key,
            'token': self.token,
            'idList': self.list_id,
            'name': nome,
            'desc': descricao
        }
        
        try:
            # Faz a requisição para o Trello
            response = requests.post(self.base_url, params=params)
            
            if response.status_code == 200:
                print(f"\n✅ SUCESSO! O card '{nome}' foi criado no seu Trello.")
            else:
                print(f"\n❌ ERRO NA API: {response.status_code}")
                print(f"Detalhe: {response.text}")
                print("Dica: Verifique se o ID_LISTA no seu .env está correto.")
                
        except Exception as e:
            print(f"\n⚠️ Ocorreu um erro inesperado: {e}")

# --- BLOCO PRINCIPAL DE EXECUÇÃO ---
if __name__ == "__main__":
    agente = AgenteTrello()
    
    print("-" * 30)
    print("🤖 AGENTE DE AUTOMAÇÃO DIO")
    print("-" * 30)
    
    # Entradas do usuário via terminal
    titulo = input("Digite o NOME da tarefa: ")
    resumo = input("Digite a DESCRIÇÃO da tarefa: ")
    
    print("\n🚀 Enviando para o Trello...")
    agente.criar_tarefa(titulo, resumo)
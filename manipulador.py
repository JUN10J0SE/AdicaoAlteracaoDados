#importacao de biblioteca especifica json
import json

#classe ArquivoJason
class Manipulador:
    #metodo CRIAR ARQUIVO
    def criar_arquivo(self, nome_arquivo):
        try:
            #lista com discionario dentro
            usuarios = [
                {
                    'Codigo': 0,
                    'Nome': 'Admin',
                    'CPF': '000.000.000-00',
                    'E-mail': 'admin@admin.com.br',
                    'profissao': 'Admistrador'
                }
            ]
            #serializar objeto python como json
            json_dados = json.dumps(usuarios)
            with open(f'{nome_arquivo}.json', 'w', encoding='utf-8') as f:
                f.write(json_dados)
            return f'{nome_arquivo}.json Criado com sucesso.'
        except Exception as ex:
            return f"Nao foi possivel criar o arquivo. {ex}."
        
    #metodo ABRIR ARQUIVO 
    def abrir_arquivo(self, nome_arquivo):

        #desserializar objeto json em python
        with open(f'{nome_arquivo}.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
        return dados
    
    #metodo SALVAR DADOS
    def salvar_dados(self, usuarios, nome_arquivo):
        try:
            with open(f'{nome_arquivo}.json', 'w', encoding='utf-8') as f:
                json.dump(usuarios, f)#no caso se ja existisem dados o dump seria no plural e vazio
            return f'Dados gravados com sucesso.'
        except Exception as ex:
            return f'Nao foi possivel salvar os dados. {ex}'

    #destrutor
    def __del__(self):
        return "Manipulador destrutor"
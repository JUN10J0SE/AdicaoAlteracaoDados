#Este projeto cria um objeto tipo pessoa. E sera manupulado(inserindo e alterando dados)
#ao fina leste arquivo sera grava do no tipo json e o computador busca este arquivo

#importacao das classes e a biblioteca OS
import os
from pessoa import *
from manipulador import *

if __name__ == '__main__':
    #instaciar objetos
    p = Pessoa(0, '','','','')
    m = Manipulador()

    while True:
        #menu
        print('1 - Criar Novo Arquivo Json.')
        print('2 - Abrir Arquivo Json.')
        print('3 - Salvar Novo Usuario.')
        print('4 - Alterar Dados do Usuario')
        print('5 - Deletar Usuarios.')
        print('0 - Sair do Programa.')

        opcao = input('Informe a opcao desejada: ')
        #limpeza de tela
        os.system('cls')

        match opcao:
            case '0':
                break
            case '1':
                novo_arquivo = input('Informe o nome do arquivo que deseja criar: ')
                print(m.criar_arquivo(novo_arquivo))
                continue

            case '2':
                abrir_arquivo = input('Informe o nome do Arquivo que deseja Abrir: ')
                try:
                    os.system('cls')

                    usuarios = m.abrir_arquivo(abrir_arquivo)
                    print(f'Arquivo aberto: {abrir_arquivo}.json.\n')
                    for i in range(len(usuarios)):#um for para percorrer a lista e outro para percorrer o dicionario
                        for campo in usuarios[i]:
                            print(f'{campo.capitalize()}: {usuarios[i].get(campo)}.')
                        print(f'\n{'-'*30}\n')

                except Exception as ex:
                    print(f'Nao foi possivel  abrir o arquivo. {0}.')
                finally:#volta ao inicio do programa idependente do try ou do exceptions
                    continue

            case '3':
                try:
                   # usuario = {}#dicionario para armazenar os dados informados pelo usuario
                    #campos = ('Nome', 'CPF','E-mail','Profissao') #dupla para informar no for os imputs que se quer sem precisar informar um por um
                    #print(f'Arquivo aberto: {abrir_arquivo}.json\n')

                    #for campo in campos:
                        #usuario[campo] = input(f'Informe o campo {campo.capitalize()}:')

                    #usuario['Codigo'] = len(usuarios)#'usuarios' ja declarado no case 2. este comando é o que atribui os dados mas nao salva
                    #usuarios.append(usuario)
                    #print(m.salvar_dados(usuarios, abrir_arquivo))#este print e o que grava o usuario no arquivo
                    #______________________________________________________________________________________________________________________________________
                    #___________________________________________Forma baixo mais elegante___________________________________________________________________

                    print(f'Arquivo aberto: {abrir_arquivo}.json.\n')
                    p.codigo = len(usuarios)
                    p.nome = input('Informe o nome: ')
                    p.cpf = input('Informe o CPF: ')
                    p.email = input('Informe o e-mail: ')
                    p.profissao = input('Informe a profissão: ')
                    usuario = dict(codigo=p.codigo, nome=p.nome, cPF=p.cpf, email=p.email, profissao=p.profissao)#outra forma de fazer dicionario
                    usuarios.append(usuario)
                    print(m.salvar_dados(usuarios, abrir_arquivo))
                except Exception as e:
                    print(f'Nao foi possivel realizar a operacao. {e}')
                finally:
                    continue

            case '4':
                try:
                    print(f'Arquivo aberto: {abrir_arquivo}.json\n')
                    codigo = int(input('Infome o codigo do usuario que deseja alaterar os Dados: '))

                    for campo in usuarios[codigo]:#aqui mostra o campo que esta trabalhando( a posicao do ndice)
                        print(f'Valor atual do campo {campo}: {usuarios[codigo].get(campo)}')
                        novo_dado = input(f'Informe o novo dado do campo {campo} ou aperte ENTER caso deseje manter o mesmo valor: ')#aqui o uauario altera ou aperta enter para o prox
                        if novo_dado:
                            usuarios[codigo][campo] = novo_dado #aqui a alteracao e somente no dicionario e nao no json
                        else:
                            ...
                    print(m.salvar_dados(usuarios, abrir_arquivo))#aqui e onde a alteracao faz no json
                except Exception as e:
                    print(f'Não foi possivel alterar os dados. {e}.')
                finally:
                    continue
            
            case '5':
                try:
                    print(f'Arquivo aberto {abrir_arquivo}.json.\n')
                    codigo = int(input('Informe o codgo de usuario que deseja deletar: '))

                    nome_deletado = usuarios[codigo]['Nome']#aqui e para mostar o nome do usuario, no dicionario o atributo deve estar entre aspas2
                                                            #o atributo dentro do cochete debve estar escrito conforme no discionario e nao na CLASE!
                    confirmacao = input(f'Deseja deletar o usuario {nome_deletado}? Digite SIM para conforirmar').upper()# uperr para formatar para ver se realmente deseja ou na odeletar
                    if confirmacao == 'SIM':
                        del(usuarios[codigo])#aqui esta deletando so da lista
                        print(m.salvar_dados(usuarios, abrir_arquivo))#aqui que deleta no arquivo
                        print(f'Usuario {nome_deletado} deletado com sucesso')
                    else:
                        print(f'Usuario {nome_deletado} nao foi excluido.')

                except Exception as e:
                    print(f' Não foi possivel deletar o usuario {e}.')
                finally:
                    continue
            case _:
                print('Opcao Invalida.')
                continue




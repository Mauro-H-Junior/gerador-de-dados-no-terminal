import random
import os
import time


sistema = False
while sistema == False:

#LISTAS QUE SERÃO ITERADAS

    nome = ['Mauro', 'João', 'Lima', 'Duarte', 'Lucas', 'Lindalva', 'Rita']
    email = ['email@gmail.com', 'email@outlook.com']
    telefone = ['(34) 999999999', '(35)888888888', '(31)777777777' ]
    cidade = ['Uberaba', 'Santa Vitória']
    estado = ['MG', 'SP', 'GO']

        
    lista_de_dados = []
    lista_de_escolha = []
    lista_de_teclas_para_escolha_sorteio = ['1', '2', '3', '4', '5']
    lista_opcoes_de_texto = ['sim', 'y', 'Y', 's']
    # lista_opcoes_de_tela = ['tela', 'TELA', 'Tela']

#FUNÇÕES do APP

    def adiciona_nome_na_lista():
        nome_aleatorio = random.choice(nome)
        lista_de_dados.append(nome_aleatorio)

    def adiciona_email_na_lista():
        email_aleatorio = random.choice(email)
        lista_de_dados.append(email_aleatorio)

    def adiciona_telefone_na_lista():
        telefone_aleatorio = random.choice(telefone)
        lista_de_dados.append(telefone_aleatorio)

    def adiciona_cidade_na_lista():
        cidade_aleatorio = random.choice(cidade)
        lista_de_dados.append(cidade_aleatorio)

    def adiciona_estado_na_lista():
        estado_aleatorio = random.choice(estado)
        lista_de_dados.append(estado_aleatorio)

    def salvar_dados_no_txt():
        print('Exportando...')
        time.sleep(2)
        with open('DADOS.txt', 'a',  encoding='utf8', newline='') as arquivo:
            for item in lista_de_dados:
                arquivo.write(item + os.linesep)
        print('Exportação OK!')
        time.sleep(2)
    
    def imprimir_dados_na_tela():
        
        for i in lista_de_dados:
            print(f'{i}')
    

# MENU DO APP

    print('-'*70)
    print('SORTEAR VALORES ALEATÓRIOS EM LISTAS - Para fechar o sistema digite "parar"')
    print('-'*70)

    opcao_correta_para_sorteio = False
    while opcao_correta_para_sorteio == False:

        lista_de_escolha = input(
            '[1] - Sortear Nome \n[2] - Sortear Email \n[3] - Sortear Telefone \n[4] - Sortear Cidade \n[5] - Sortear Estado \n\nDigite a(s) opção(es) desejada(as):')
        print('-'*70)
            
# ITERA ITENS NA lista_de_escolhas PARA ADICIONAR NA lista_de_dados

        if lista_de_escolha == 'parar':
            sair = True
            sistema = True
            print('Finalizando o APP..')
            time.sleep(2)
            break
            

        for item in lista_de_escolha:  

            if item == '1':
                adiciona_nome_na_lista()
                opcao_correta_para_sorteio = True
                
            elif item == '2':
                adiciona_email_na_lista()
                opcao_correta_para_sorteio = True

            elif item == '3':
                adiciona_estado_na_lista()
                opcao_correta_para_sorteio = True

            elif item == '4':
                adiciona_cidade_na_lista()
                opcao_correta_para_sorteio = True

            elif item == '5':
                adiciona_estado_na_lista()
                opcao_correta_para_sorteio = True

            sair = False

        if item not in lista_de_teclas_para_escolha_sorteio:
            print('MENSAGEM: DIGITE SOMENTE OS NÚMEROS SOLICITADOS!')
            print('-'*70)
            opcao_correta_para_sorteio = False
                
        imprimir_dados_na_tela()

#VERIFICA SE IMPRIME NA TELA OU GRAVA NO TXT

    if sair is not True:
        opcao_correta_impressao = False
        while opcao_correta_impressao == False:

            print('-'*70)
            tela_ou_txt = input('Deseja exportar os dados no arquivo TXT? (Digite "y" ou "n")\n>')
            
            if tela_ou_txt in lista_opcoes_de_texto:
                salvar_dados_no_txt()
                opcao_correta_impressao = True

            elif tela_ou_txt in ('n', 'N', 'não'):
                opcao_correta_impressao = True

            else:
                print('Ops, DIGITE UMA OPÇÃO VÁLIDA!')
                opcao_correta_impressao = False




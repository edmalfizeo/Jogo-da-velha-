#declaração de valores (matriz, vetor e variaveis)
tabuleiro = [['_','_','_'],['_','_','_'],['_','_','_']]
ganhadores=[]
ganhar = False
jogador1 = "X"
jogador2 = "O"

#funções
def menu():
  while True: #irá sempre rodar o jogo, até o jogador decidir parar com a opção 3
    print('''1 - Iniciar Jogo
2 - Instruções
3 - Exit Game''')
    topcao = 0
    while topcao != 1:
      try:
        opcao = int(input('Digite uma opção:'))
        topcao =1
      except ValueError:
        print('Digite um numero não letras')
    #opções
    if opcao == 1:
      limpartTabuleiro()
      jogar()
    elif opcao == 2:
      instrucoes()
    elif opcao == 3:
      print('Foi um prazer ter você em nosso jogo, até breve!')
      break

def jogar():
  while True:
    mostrarTabuleiro()
    inserirLinhaColuna(jogador1)

    if checarSeGanhou(jogador1) == True:
      break
    mostrarTabuleiro()
    inserirLinhaColuna(jogador2)

    if checarSeGanhou(jogador2) == True:
      break

def mostrarTabuleiro():
  print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- JOGO DA VELHA -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
  for i in range(3):
    print()
    print('                  ',tabuleiro[i][0], '|', tabuleiro[i][1], '|', tabuleiro[i][2])
  print()
def inserirLinhaColuna(jogador):
  tlinha1 = False
  while tlinha1 != True:
    try:
      linha1 = int(input('Jogador'+jogador+'| Digite a Linha: '))
      break
    except ValueError:
      print('digite um numero')
  tcoluna1 = False
  while tcoluna1 !=True:
    try:
      coluna1 = int(input('Jogador'+jogador+'| Digite a Coluna: '))
      break
    except ValueError:
      print('digite um numero')
  if tabuleiro[linha1 - 1][coluna1 - 1] == '_':
    tabuleiro[linha1 - 1][coluna1 - 1] = jogador
  else:
    print('escolha um lugar vazio')
    mostrarTabuleiro()
    inserirLinhaColuna(jogador)
    
    
def limpartTabuleiro():
  for i in range(3):
    for j in range(3):
      tabuleiro[i][j] = '_'
def checarSeGanhou(jogador):
  if darVelha()==True or ganharEmLinha() == True or ganharEmColuna() == True or ganharEmDiagonal()== True:
    mostrarTabuleiro()
    return True
def ganharEmLinha():
  for i in range(3):
    if tabuleiro[i][0]=='X'and tabuleiro[i][1]== 'X'and tabuleiro[i][2] == 'X':
      print('Jogador 1 Venceu!')
      ganhadores.append('Jogador 1 Venceu!')
      return True
    elif tabuleiro[i][0]=='O'and tabuleiro[i][1]== 'O'and tabuleiro[i][2] == 'O':
      print('Jogador 2 Venceu!')
      ganhadores.append('Jogador 2 Venceu!')
      return True
  return False  
def ganharEmColuna():
  for i in range(3):
    if tabuleiro[0][i]=='X' and tabuleiro[1][i] == 'X'and tabuleiro[2][i]== 'X':
      print('Jogador 1 Venceu!')
      ganhadores.append('Jogador 1 Venceu!')
      return True
    elif tabuleiro[0][i]=='O' and tabuleiro[1][i] == 'O'and tabuleiro[2][i]== 'O':
      print('Jogador 2 Venceu!')
      ganhadores.append('Jogador 2 Venceu!')
      return True
  return False 
def ganharEmDiagonal():
  if tabuleiro[0][0]=='X'and tabuleiro[1][1]=='X'and tabuleiro[2][2]=='X':
    print('Jogador 1 Venceu!')
    ganhadores.append('Jogador 1 Venceu!')
    return True
  elif tabuleiro[0][2]=='X'and tabuleiro[1][1]=='X'and tabuleiro[2][0]=='X':
    print('Jogador 1 Venceu!')
    ganhadores.append('Jogador 1 Venceu!')
    return True
  if tabuleiro[0][0]=='O'and tabuleiro[1][1]=='O'and tabuleiro[2][2]=='O':
    print('Jogador 1 Venceu!')
    ganhadores.append('Jogador 1 Venceu!')
    return True
  elif tabuleiro[0][2]=='O'and tabuleiro[1][1]=='O'and tabuleiro[2][0]=='O':
    print('Jogador 2 Venceu!')
    ganhadores.append('Jogador 2 Venceu!')
    return True  
  return False
def darVelha():
  if tabuleiro[0][0] != '_' and tabuleiro[0][1]!='_'and tabuleiro[0][2] != '_':
    if tabuleiro[1][0] != '_' and tabuleiro[1][1]!='_'and tabuleiro[1][2] != '_':
      if tabuleiro[2][0] != '_' and tabuleiro[2][1]!='_'and tabuleiro[2][2] != '_':
        if ganharEmLinha()==False and ganharEmColuna()==False and ganharEmDiagonal()==False:
          print('# Deu Velha #')
          ganhadores.append('Velha')
          return True
  return False
def instrucoes():
  print('-='* 43)
  print('aqui esta o tabuleiro:')
  mostrarTabuleiro()
  print('O objeto do jogo é fazer com que o jogador consiga preencher uma linha ou uma coluna ou uma diagonal')
menu()

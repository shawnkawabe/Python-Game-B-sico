import os
#JOGO DA VELHA 5x5
print("x"*5,"o"*5,"JOGO DA VELHA (5x5)","o"*5,"x"*5)   
px = 0#Contador de pontos de x
po = 0#contador de pontos de o
pg1 = 0#pontuador que leva dados de pontos
pg2 = 0
def cr1(nomeg):#Função de Criação de arquivo de jogador - cr de Create, apenas para ajudar a organizar o codigo.
  global pg1#Variavel Global de pontos do jogador.
  pg1 = 0 #Pontos 0 já que o usuario nunca jogou.
  jogadorC = open(nomeg+".dat","w")#Cria um arquivo de acordo com nome do jogador, (nomeg e nomeh) servem para a mesma coisa, criar um arquivo com o nome do usuario.
  jogadorC.write("%s "%(0))#Escreve a atual pontuação do jogador novo.
  jogadorC.close()#Fecha a conexão com o arquivo do jogador.
  print("-Jogador Novo.")

def cr2(nomeh):
  global pg2
  pg2 = 0
  jogadorC = open(nomeh+".dat","w")
  jogadorC.write("%s "%(0))
  jogadorC.close()
  print("-Jogador Novo.")  
  

def re1(nomeg):#Função de Leitura (re1,re2) -  re de READ, melhor para organizar o codigo.
  global pg1 #Variavel Global de Pontos globais do jogador 1
  JogadorR = open(nomeg+".dat","r")#Abre coneção em forma de leitura com base no nome do jogador.
  print("Bem vindo "+nomeg)#Bem vindo ao suado jogo da velha.

  for ponto in JogadorR.readlines():#Lê quantos pontos o jogador possui.
    pg1 = int(ponto)#Salva os pontos na variavel global, que será chamada dentro do loop, para ser mostrada no placar do jogador.
  JogadorR.close()#Fecha  a conexão com o arquivo do jogador.
  
def re2(nomeh):
  global pg2
  JogadorR = open(nomeh+".dat","r")
  print("Bem vindo "+nomeh)

  for ponto in JogadorR.readlines():
    pg2 = int(ponto)
  JogadorR.close()


def vitoria(nomev):#Função de vitória(vitoria,vitoria1)
  JogadorV = open(nomev+".dat","r") #Abre em forma de leitura, o arquivo com o nome do jogador vitorioso.
  print("Parabéns "+nomev)
  for pontov in JogadorV.readlines():#Lê a quantidade de pontos(Na verdade lê qualquer valor né, recebe e salva tudo no parametro nomeado) que o jogador possui e salva na variavel.
    p = int(pontov)#Converte a pontuação do jogador e salva em p.
    p+=1#soma um ponto na pontuação total do jogador.
  JogadorV.close()#Fecha a conexão com o arquivo em forma de leitura.
  JogadorV = open(nomev+".dat","w")#Abre a conexão com o arquivo em forma de escrita, para adicionar dados.
  JogadorV.write("%d"%(p))#Sobrescreve a pontuação, com a pontuação atualizada, já com o ponto ganho da partida.
  JogadorV.close()#Fecha a conexão com o arquivo do jogar, e reiniciar o loop do jogo.

def vitoria1(nomey):
  JogadorV = open(nomey+".dat","r")
  print("Parabéns "+nomey)
  for pontoy in JogadorV.readlines():
    p = int(pontoy)
    p+=1
  JogadorV.close()
  JogadorV = open(nomey+".dat","w")
  JogadorV.write("%d"%(p))
  JogadorV.close()
  

def main():#Função main.
  c=0 #Contador de jogadas.
  nomeg=""
  nomev=""
  nomey=""
  global pg1#variável de pontuação global do jogador 1
  global pg2#variável de pontuação global do jogador 2
  global px#Chamada do contador de x na função
  global po#Chamada do contador de o na função
  while True:#Loop que recebe o nome do usuário 
    nome1 = input("Nome do 1º jogador:")#Recebe o nome do jogador
    ex=os.path.exists("%s.dat"%(nome1))#Verifica se o nome do jogador, possui um arquivo, se ele possuir o parametro retorna "True" se não "False"
    if ex == True: #Se retornar True
      nomeg = nome1 #A variavel nomeg recebe o conteúdo(nome do jogador) da variável nome1
      re1(nomeg)#Chama a função de leitura de dados, pois se retornou "True" o jogador já possui um arquivo, e envia o nome do jogador para a função ler seu arquivo com sua pontuação;
      px = pg1 #px (Variável que será exibida no placar), recebe o valor da pontuação do jogador.
      px=int(px)#conversão da variavel para inteiro. (os dados lidos no arquivo são em formato de "str" então é melhor converter)
      break#quebra do loop que recebe o nome do primeiro jogador.
    elif ex == False:#Se o parametro que retornar for "False" significa que o jogador não possui um arquivo, que é um "jogador novo".
      nomeg = nome1 #A variavel nomeg recebe o conteúdo(nome do jogador) da variável nome1
      px = pg1 #pg1(ou pg2) não troca de valor caso seja um jogador novo, pois a variavel se inicia com conteudo 0, e um jogador novo não possui pontuação anterior não é mesmo?
      cr1(nomeg)#Envia o nome do jogador, para a função criar um arquivo para o jogador novo.
      px=int(px)#Aqui é um "Previnir pra não dar erro". Mas não precisava disso aqui não, mas tbm não vou tirar.
      break#quebra do loop que recebe o nome do primeiro jogador.

  while True:
    nome2 = input("Nome do 2º jogador:")
    ex=os.path.exists(nome2+".dat")
    if ex == True:
      nomeh = nome2
      re2(nomeh)
      po = pg2
      po =int(po)
      break
    elif ex == False:
      nomeh = nome2
      po = pg2
      po = int(po)
      cr2(nomeh)
      break

  print("→Deseja começar a jogar?","\n1 - Jogar","\n2 - Sair")#Imprime as opções.
  i = int(input("→"))#Recebe a escolha do usuário.

  if i == 1:#Condição para início do jogo.
    m = [["-","-","-","-","-"],["-","-","-","-","-"],["-","-","-","-","-"],["-","-","-","-","-"],["-","-","-","-","-"]]#"Criação de uma matriz", minha desculpa aqui é que tentei economiza de linhas.
    print("="*10,"\n"*1)
    print("PLACAR - %s ( %d ) - %s ( %d )" % (nome1,px,nome2,po))#Imprimindo o placar dos jogadores.
    print("="*10)

    for linha in range(len(m)):#------------Imprime as linhas e colunas do jogo em forma de matriz.------------
        for coluna in range(len(m[linha])):
          print("%s"%m[linha][coluna],end=" ")
        print()
    while True:#---------------Loop de Jogadas-----------------------
      
      if c>=25:
        print("Deu velha!!!")
        break
      while True:#-----------------Loop jogador 'x'-----------------------
        x = int(input("→Quantas casas na horizontal você deseja jogar(→)?"))#Recebe a primeira cordenada
        if x == 1: #Condição para conversão de unidade, para tornar mais "prático" para o usuário;
          v = 0
        elif x == 2:
          v = 1
        elif x == 3:
          v = 2
        elif x == 4:
          v = 3
        elif x == 5:
          v = 4
        y = int(input("→Quantas casas na vertical você deseja jogar?(↓)"))#Recebe a segunda cordenada
        if y == 1:
          h = 0
        elif y == 2:
          h = 1
        elif y == 3:
          h = 2
        elif y == 4:
          h = 3
        elif y == 5:
          h = 4
        if m[h][v]!="-":#Verifica se já existe uma jogada naquela casa especifica em que o jogador tentou.
          print("→A casa já está preenchida, digite novamente.")
        else:  #Se a posição estiver "livre"(Nesse caso é se o indice especifico for "-")ele troca o conteudo por "x".
          m[h][v] = "x"
          
          break
      
      if c>=25:
        print("Deu velha!!!")
        break #Quebra de Loop (Jogadas)  (observação: fiquei tentnado dar velha, porém sempre dava alguma vitória, perdi a paciência mas se não funcionar acontece.)
        
      
      for linha in range(len(m)):#------------Imprime as linhas e colunas do jogo em forma de matriz.------------
        for coluna in range(len(m[linha])):
          print("%s"%m[linha][coluna],end=" ")
        print()

      c=c+1#------------Adiciona mais uma jogada ao contador.------------  
      
      if c>=7:#Minimo de jogadas possíveis para que alguem consiga ganhar.
          
        if m[0][0]=="x"  and m[0][1]=="x" and m[0][2]=="x" and m[0][3]=="x" :#----------- Verifica linha 1(1ªPossibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          nomev = nome1 
          vitoria(nomev)#Chamada Função de vitória  que enviará o nome do jogador vencedor (Nesse caso o jogador 1 mas poderia ser o 2, lá em baixo tem a do 2, fiz 2 funções gêmeas para que não ocorresse nenhum erro.(Essa explicação é precisa de comentar isso em todas as chamadas da função de vitória, tem uma em cada condição de vitória dos dois jogadores.))
          break#Quebra de loop(Jogadas)
        elif  m[0][1]=="x" and m[0][2]=="x" and m[0][3]=="x" and m[0][4]=="x":#----------- Verifica linha 1(2ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          nomev = nome1 
          vitoria(nomev)
          break#Quebra de loop(Jogadas)
        elif  m[1][0]=="x" and m[1][1]=="x" and m[1][2]=="x" and m[1][3]=="x" :#----------- Verifica linha 2(1ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          nomev = nome1 
          vitoria(nomev)
          break#Quebra de loop(Jogadas)
        elif  m[1][1]=="x" and m[1][2]=="x" and m[1][3]=="x" and m[1][4]=="x":#----------- Verifica linha 2(2ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          nomev = nome1 
          vitoria(nomev)
          break#Quebra de loop(Jogadas)
        elif  m[2][0]=="x" and m[2][1]=="x" and m[2][2]=="x" and m[2][3]=="x":#----------- Verifica linha 3(1ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          nomev = nome1 
          vitoria(nomev)
          break#Quebra de loop(Jogadas)  
        elif  m[2][1]=="x" and m[2][2]=="x" and m[2][3]=="x" and m[2][4]=="x":#----------- Verifica linha 3(2ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          nomev = nome1 
          vitoria(nomev)
          break #Quebra de loop(Jogadas) 
        elif m[3][0]=="x" and m[3][1]=="x" and m[3][2]=="x" and m[3][3]=="x" :#----------- Verifica linha 4(1ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          nomev = nome1 
          vitoria(nomev)
          break#Quebra de loop(Jogadas)
        elif m[3][1]=="x" and m[3][2]=="x" and m[3][3]=="x" and m[3][4]=="x":#----------- Verifica linha 4(2ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          nomev = nome1 
          vitoria(nomev)
          break#Quebra de loop(Jogadas) 
        elif m[4][0]=="x" and m[4][1]=="x" and m[4][2]=="x" and m[4][3]=="x":#----------- Verifica linha 5(1ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          nomev = nome1 
          vitoria(nomev)
          break#Quebra de loop(Jogadas)
        elif m[4][1]=="x" and m[4][2]=="x" and m[4][3]=="x" and m[4][4]=="x":#----------- Verifica linha 5(2ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          nomev = nome1 
          vitoria(nomev)
          break#Quebra de loop(Jogadas)  
        elif m[0][0]=="x" and m[1][0]=="x" and m[2][0]=="x" and m[3][0]=="x":#----------- Verifica coluna 1(1ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          nomev = nome1 
          vitoria(nomev)
          break#Quebra de loop(Jogadas)
        elif m[1][0]=="x" and m[2][0]=="x" and m[3][0]=="x" and m[4][0]=="x":#----------- Verifica coluna 1(2ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          nomev = nome1 
          vitoria(nomev)
          break#Quebra de loop(Jogadas)  
        elif m[0][1]=="x" and m[1][1]=="x" and m[2][1]=="x" and m[3][1]=="x":#----------- Verifica coluna 2(1ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          nomev = nome1 
          vitoria(nomev)
          break#Quebra de loop(Jogadas)
        elif m[1][1]=="x" and m[2][1]=="x" and m[3][1]=="x" and m[4][1]=="x":#----------- Verifica coluna 2(2ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          nomev = nome1 
          vitoria(nomev)
          break#Quebra de loop(Jogadas)
        elif m[0][2]=="x" and m[1][2]=="x" and m[2][2]=="x" and m[3][2]=="x":#----------- Verifica coluna 3(1ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          nomev = nome1 
          vitoria(nomev)
          break#Quebra de loop(Jogadas)
        elif m[1][2]=="x" and m[2][2]=="x" and m[3][2]=="x" and m[4][2]=="x":#----------- Verifica coluna 3(2ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          nomev = nome1 
          vitoria(nomev)
          print("O jogador 'x' ganhou!!!")
          break #Quebra de loop(Jogadas) 
        elif m[0][3]=="x" and m[1][3]=="x" and m[2][3]=="x" and m[3][3]=="x":#----------- Verifica coluna 4(1ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          nomev = nome1 
          vitoria(nomev)
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break#Quebra de loop(Jogadas)
        elif m[1][3]=="x" and m[2][3]=="x" and m[3][3]=="x" and m[4][3]=="x":#----------- Verifica coluna 4(2ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          nomev = nome1 
          vitoria(nomev)
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break#Quebra de loop(Jogadas)
        elif m[0][4]=="x" and m[1][4]=="x" and m[2][4]=="x" and m[3][4]=="x":#----------- Verifica coluna 5(1ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          nomev = nome1 
          vitoria(nomev)
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break#Quebra de loop(Jogadas)
        elif m[1][4]=="x" and m[2][4]=="x" and m[3][4]=="x" and m[4][4]=="x":#----------- Verifica coluna 5(2ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          nomev = nome1 
          vitoria(nomev)
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break#Quebra de loop(Jogadas)
        elif m[0][0]=="x" and m[1][1]=="x" and m[2][2]=="x" and m[3][3]=="x":#----------- Verifica diagonal principal(1ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          nomev = nome1 
          vitoria(nomev)
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break#Quebra de loop(Jogadas)
        elif m[1][1]=="x" and m[2][2]=="x" and m[3][3]=="x" and m[4][4]=="x":#----------- Verifica diagonal principal (invertida)(2ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          nomev = nome1 
          vitoria(nomev)
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break#Quebra de loop(Jogadas)
        elif m[0][1]=="x" and m[1][2]=="x" and m[2][3]=="x" and m[3][4]=="x":#----------- Verifica diagonal secundária (superior)(Apenas 1ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          nomev = nome1 
          vitoria(nomev)
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break#Quebra de loop(Jogadas)
        elif m[1][0]=="x" and m[2][1]=="x" and m[3][2]=="x" and m[4][3]=="x":#----------- Verifica diagonal secundária (inferior)(Apenas 1ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          nomev = nome1 
          vitoria(nomev)
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break#Quebra de loop(Jogadas)
        elif m[4][0]=="x" and m[3][1]=="x" and m[2][2]=="x" and m[1][3]=="x":#----------- Verifica diagonal principal (invertida)(1ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          nomev = nome1 
          vitoria(nomev)
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break#Quebra de loop(Jogadas)
        elif m[3][1]=="x" and m[2][2]=="x" and m[1][3]=="x" and m[0][4]=="x":#----------- Verifica diagonal principal (invertida)(2ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          nomev = nome1 
          vitoria(nomev)
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break#Quebra de loop(Jogadas)
        elif m[3][4]=="x" and m[2][3]=="x" and m[1][2]=="x" and m[0][1]=="x":#----------- Verifica diagonal secundária (invertida)(inferior)(Apenas 1ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          nomev = nome1 
          vitoria(nomev)
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break #Quebra de loop(Jogadas)
        elif m[4][3]=="x" and m[3][2]=="x" and m[2][1]=="x" and m[1][0]=="x":#----------- Verifica diagonal secundária (invertida)(superior)(Apenas 1ª Possibilidade) ----------------
          #px+=1 #Adiciona mais um ponto ao placar
          nomev = nome1 
          vitoria(nomev)
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break #Quebra de loop(Jogadas)
        elif m[3][0]=="x" and m[2][1]=="x" and m[1][2]=="x" and m[0][3]=="x":#----------- Verifica diagonal secundária (invertida)(superior)(Apenas 1ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomev = nome1 
          vitoria(nomev)
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break #Quebra de loop(Jogadas)
        elif m[0][1]=="x" and m[1][2]=="x" and m[2][3]=="x" and m[3][4]=="x":#----------- Verifica diagonal secundária (invertida)(superior)(Apenas 1ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomev = nome1 
          vitoria(nomev)
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break #Quebra de loop(Jogadas)
        elif m[0][3]=="x" and m[1][2]=="x" and m[2][1]=="x" and m[3][0]=="x":#----------- Verifica diagonal secundária (invertida)(superior)(Apenas 1ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomev = nome1 
          vitoria(nomev)
      
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break #Quebra de loop(Jogadas) 
        
        #*Aproveitei a lógica anterior de soma, e só adicionei condições nelas e dupliquei nas possibilidades(apenas uma observação.)*
      if c>=25:
        print("Deu velha!!!")
        break #Quebra de Loop (Jogadas)  (observação: fiquei tentnado dar velha, porém sempre dava alguma vitória, perdi a paciência mas se não funcionar acontece.)
      
         
      while True:#----------------Loop jogador 'o'------------------  
        x = int(input("Quantas casas na horizontal você deseja jogar(→)?"))#Entrada do primeiro indice.
        if x == 1:
          v = 0
        elif x == 2:
          v = 1
          
        elif x == 3:
          v = 2
        elif x == 4:
          v = 3
        elif x == 5:
          v = 4
        y = int(input("Quantas casas na vertical você deseja jogar(↓)?"))
        if y == 1:
          h = 0
        elif y == 2:
          h = 1
        elif y == 3:
          h = 2
        elif y == 4:
          h = 3
        elif y == 5:
          h = 4
        if m[h][v]!="-":
          print("→A casa já está preenchida, digite novamente.")
        else:
          m[h][v] = "o"
        
          break

      for linha in range(len(m)):
        for coluna in range(len(m[linha])):
          print("%s"%m[linha][coluna],end=" ")
        print()

      c= c+1

      if c>=1:

        if m[0][0]=="o"  and m[0][1]=="o" and m[0][2]=="o" and m[0][3]=="o" :#----------- Verifica linha 1(1ªPossibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2
          vitoria1(nomey) 
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break#Quebra de loop(Jogadas)
        elif  m[0][1]=="o" and m[0][2]=="o" and m[0][3]=="o" and m[0][4]=="o":#----------- Verifica linha 1(2ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          vitoria1(nomey)
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break#Quebra de loop(Jogadas)
        elif  m[1][0]=="o" and m[1][1]=="o" and m[1][2]=="o" and m[1][3]=="o" :#----------- Verifica linha 2(1ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          vitoria1(nomey)
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break#Quebra de loop(Jogadas)
        elif  m[1][1]=="o" and m[1][2]=="o" and m[1][3]=="o" and m[1][4]=="o":#----------- Verifica linha 2(2ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          vitoria1(nomey)
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break#Quebra de loop(Jogadas)
        elif  m[2][0]=="o" and m[2][1]=="o" and m[2][2]=="o" and m[2][3]=="o":#----------- Verifica linha 3(1ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao 
          nomey = nome2 
          vitoria1(nomey)
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break#Quebra de loop(Jogadas)  
        elif  m[2][1]=="o" and m[2][2]=="o" and m[2][3]=="o" and m[2][4]=="o":#----------- Verifica linha 3(2ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          vitoria1(nomey)
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break #Quebra de loop(Jogadas) 
        elif m[3][0]=="o" and m[3][1]=="o" and m[3][2]=="o" and m[3][3]=="o" :#----------- Verifica linha 4(1ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          vitoria1(nomey)
          break#Quebra de loop(Jogadas)
        elif m[3][1]=="o" and m[3][2]=="o" and m[3][3]=="o" and m[3][4]=="o":#----------- Verifica linha 4(2ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          vitoria1(nomey)
          break#Quebra de loop(Jogadas) 
        elif m[4][0]=="o" and m[4][1]=="o" and m[4][2]=="o" and m[4][3]=="o":#----------- Verifica linha 5(1ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          vitoria1(nomey)
          break#Quebra de loop(Jogadas)
        elif m[4][1]=="o" and m[4][2]=="o" and m[4][3]=="o" and m[4][4]=="o":#----------- Verifica linha 5(2ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          vitoria1(nomey)
          break#Quebra de loop(Jogadas)  
        elif m[0][0]=="o" and m[1][0]=="o" and m[2][0]=="o" and m[3][0]=="o":#----------- Verifica coluna 1(1ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          vitoria1(nomey)
          break#Quebra de loop(Jogadas)
        elif m[1][0]=="o" and m[2][0]=="o" and m[3][0]=="o" and m[4][0]=="o":#----------- Verifica coluna 1(2ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          vitoria1(nomey)
          break#Quebra de loop(Jogadas)  
        elif m[0][1]=="o" and m[1][1]=="o" and m[2][1]=="o" and m[3][1]=="o":#----------- Verifica coluna 2(1ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          vitoria1(nomey)
          break#Quebra de loop(Jogadas)
        elif m[1][1]=="o" and m[2][1]=="o" and m[3][1]=="o" and m[4][1]=="o":#----------- Verifica coluna 2(2ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          vitoria1(nomey)
          break#Quebra de loop(Jogadas)
        elif m[0][2]=="o" and m[1][2]=="o" and m[2][2]=="o" and m[3][2]=="o":#----------- Verifica coluna 3(1ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          vitoria1(nomey)
          break#Quebra de loop(Jogadas)
        elif m[1][2]=="o" and m[2][2]=="o" and m[3][2]=="o" and m[4][2]=="o":#----------- Verifica coluna 3(2ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          vitoria1(nomey)
          print("O jogador 'o' ganhou!!!")
          break #Quebra de loop(Jogadas) 
        elif m[0][3]=="o" and m[1][3]=="o" and m[2][3]=="o" and m[3][3]=="o":#----------- Verifica coluna 4(1ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          vitoria1(nomey)
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break#Quebra de loop(Jogadas)
        elif m[1][3]=="o" and m[2][3]=="o" and m[3][3]=="o" and m[4][3]=="o":#----------- Verifica coluna 4(2ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          vitoria1(nomey)
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break#Quebra de loop(Jogadas)
        elif m[0][4]=="o" and m[1][4]=="o" and m[2][4]=="o" and m[3][4]=="o":#----------- Verifica coluna 5(1ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          vitoria1(nomey)
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break#Quebra de loop(Jogadas)
        elif m[1][4]=="o" and m[2][4]=="o" and m[3][4]=="o" and m[4][4]=="o":#----------- Verifica coluna 5(2ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          vitoria1(nomey)
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break#Quebra de loop(Jogadas)
        elif m[0][0]=="o" and m[1][1]=="o" and m[2][2]=="o" and m[3][3]=="o":#----------- Verifica diagonal principal(1ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          vitoria1(nomey)
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break#Quebra de loop(Jogadas)
        elif m[1][1]=="o" and m[2][2]=="o" and m[3][3]=="o" and m[4][4]=="o":#----------- Verifica diagonal principal (invertida)(2ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          vitoria1(nomey)
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break#Quebra de loop(Jogadas)
        elif m[0][1]=="o" and m[1][2]=="o" and m[2][3]=="o" and m[3][4]=="o":#----------- Verifica diagonal secundária (superior)(Apenas 1ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          vitoria1(nomey)
          print("O jogador 'x' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break#Quebra de loop(Jogadas)
        elif m[1][0]=="o" and m[2][1]=="o" and m[3][2]=="o" and m[4][3]=="o":#----------- Verifica diagonal secundária (inferior)(Apenas 1ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          vitoria1(nomey)
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break#Quebra de loop(Jogadas)
        elif m[4][0]=="o" and m[3][1]=="o" and m[2][2]=="o" and m[1][3]=="o":#----------- Verifica diagonal principal (invertida)(1ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          vitoria1(nomey)
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break#Quebra de loop(Jogadas)
        elif m[3][1]=="o" and m[2][2]=="o" and m[1][3]=="o" and m[0][4]=="o":#----------- Verifica diagonal principal (invertida)(2ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          vitoria1(nomey)
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break#Quebra de loop(Jogadas)
        elif m[3][4]=="o" and m[2][3]=="o" and m[1][2]=="o" and m[0][1]=="o":#----------- Verifica diagonal secundária (invertida)(inferior)(Apenas 1ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          vitoria1(nomey)
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break #Quebra de loop(Jogadas)
        elif m[4][3]=="o" and m[3][2]=="o" and m[2][1]=="o" and m[1][0]=="o":#----------- Verifica diagonal secundária (invertida)(superior)(Apenas 1ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          vitoria1(nomey)
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break #Quebra de loop(Jogadas)
        elif m[3][0]=="o" and m[2][1]=="o" and m[1][2]=="o" and m[0][3]=="o":#----------- Verifica diagonal secundária (invertida)(superior)(Apenas 1ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          vitoria1(nomey)
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break #Quebra de loop(Jogadas)
        elif m[0][1]=="o" and m[1][2]=="o" and m[2][3]=="o" and m[3][4]=="o":#----------- Verifica diagonal secundária (invertida)(superior)(Apenas 1ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          vitoria1(nomey)
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break #Quebra de loop(Jogadas)
        elif m[0][3]=="o" and m[1][2]=="o" and m[2][1]=="o" and m[3][0]=="o":#----------- Verifica diagonal secundária (invertida)(superior)(Apenas 1ª Possibilidade) ----------------
          #po+=1 #Adiciona mais um ponto ao placar
          nomey = nome2 
          vitoria1(nomey)
          print("O jogador 'o' ganhou!!!")#Mensagem de retorno, da vitória do jogador x.
          break #Quebra de loop(Jogadas) 

      if c>=25:
        print("Deu velha!!!")
        break #Quebra de Loop (Jogadas)

  elif i == 2:#Fecha a aplicação.
    exit()
  
while True:#Loop da função main.
  main()


 

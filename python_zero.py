#!/usr/bin/env python
# coding: utf-8

# # Primeiros passos
# 
# O interpretador Python é um cara legal que gosta de conversar, mas ele é um pouco repetitivo..
# 
# Os notebooks Jupyter se comunicam com o interpretador, mandando suas mensagens e mostrando as resposta que ele dá. 
# 
# Clique no botão de Play para executar a célula abaixo (ou selecione a célula e aperte Shift+Enter).

# In[1]:


"Oi Python!"


# ## Melhorando a conversa com o interpretador
# 
# >Se o interpretador apenas repete o que eu falo, pra que ele serve? 🤔
# >*, perguntou um aluno apressado.*
# 
# O interpretador é mais sagaz do que parece. Teste as células abaixo:

# In[2]:


"Oi Python!".upper()


# In[3]:


"Oi Python!".lower()


# In[4]:


"Oi Python!" + " Tudo bom?"


# In[5]:


"Oi Python!".split()


# ### Exercícios de fixação

# EF1 - Peça pra o interpretador dizer **"Bom dia"** com letras minúsculas. 

# In[6]:


"Bom dia".lower()


# EF2 - Peça pra o interpretador dizer **"Boa tarde"** com letras maiúsculas. 

# In[8]:


"Boa tarde".upper()


# EF3 - Peça pra o interpretador dizer **"Bom dia ou Boa tarde?"**, sendo o **"Bom dia"** com letras maiúsculas e o **"boa tarde"** com letras minúsculas. 

# In[11]:


"Bom dia ".upper() + "ou " + "Boa tarde?".lower()


# ### Exercícios complementares

# EC1 - O que você acha que a opção `split()` significa para o interpretador? Dica -- pesquise no Google Translate.

# In[ ]:


Divida, separe, reparta.


# *Escreva sua resposta aqui*

# A gente vai estudar o `split` com mais calma depois, mas por enquanto vamos ver um pouco sobre números.

# ## Trabalhando com números
# 
# O interpretador Python também consegue lidar com números e operadores aritméticos, que podem ser usados para construir **expressões aritméticas**. 
# 
# As regras básicas sobre expressões aritméticas em Python são:
# 
# * Em geral, a precedência dos operadores em Python segue a precedência que conhecemos da matemática. 
# * Assim como na matemática, é possível usar parênteses para mudar a ordem de avaliação de uma expressão.
# * Caso reste apenas operações de mesma precedência, a expressão passa a ser avaliada da esquerda para a direita.
# 
# Alguns dos operadores aritméticos disponíveis em Python estão listados abaixo. 

# | Símbolo | Operação |
# |:----:|---|
# | +  | Adição |
# | -  | Subtração |
# | /  | Divisão |
# | // | Divisão inteira |
# | %  | Resto |
# | *  | Multiplicação |
# | **  | Exponenciação |

# Teste as células abaixo:

# In[12]:


1+2+5


# In[13]:


2-1


# In[14]:


1*2


# In[15]:


3/4


# In[16]:


2 ** 3


# No entanto, você não deve misturar textos e números:

# In[17]:


"Este é um texto" + 3


# ### Exercícios de fixação

# EF4 - Calcule o produto dos números 11 e 12.

# In[18]:


11 * 12


# EF5 - Calcule o quadrado do número 16.

# In[19]:


16 ** 2


# EF6 - Calcule a raiz quadrada de 1024.

# In[24]:


1024 ** (1/2)


# ### Exercícios complementares
# 
# Os operadores // e % trabalham com divisão inteira. Por exemplo, dividir 15 por 10 considerando apenas número inteiros é igual a 1. O resto da divisão é igual a 15 - (10*1), ou seja, 5.

# In[25]:


15//10


# In[26]:


15%10


# EC2 - Calcule o resto da divisão de 227 por 20.

# In[27]:


227%20


# # Valores, nomes e variáveis

# Em Python, tanto textos como números são chamados de *valores*. 
# 
# Podemos nos referir a valores usando *nomes*. 
# 
# >Em outras linguagens, usa-se o termo **variável** em vez de nome. Vamos adotar este termo aqui por ele ser mais universal.
# 
# Teste as células abaixo:

# In[28]:


x = 2          # qualquer coisa após o # é um comentário
y = 5
x + y


# Múltiplas variáveis podem estar associadas ao mesmo valor.

# In[29]:


x = y = 1
y


# In[30]:


texto = 'Este é um texto.' # textos podem ser escritos entre aspas simples
texto


# In[31]:


outro_texto = "Este é outro texto." # textos podem ser escritos entre aspas duplas
outro_texto


# ### Exercícios de fixação
# 
# Para verificar que seu código está correto, lembre-se de acrescentar uma linha contendo apenas o nome da variável para visualizar o valor associado a ela.

# EF7 - Associe uma variável `numero` ao número `10`.

# In[32]:


numero = 10
numero


# EF8 - Associe uma variável `nome` ao texto `Python`.

# In[33]:


nome = 'Python'
nome


# EF9 - Associe uma variável `resto` ao resultado do operação de resto entre `234` e `10`.

# In[34]:


resto = 230%10
resto


# EF10 - Associe uma variável `k` ao valor `8`. Associe uma variável `quadrado_k` ao quadrado do valor associado à variável `k`.

# In[40]:


k = 8
quadrado_k = k ** (1/2)
quadrado_k


# EF11 - Associe uma váriavel `z` ao valor `256`. Associe uma variável `divisao_zk` ao resultado da divisão entre os valores associados às variáveis `z` e `k`.

# In[42]:


z = 256
divisao_zk = z // k
divisao_zk


# ## Dados informados pelo usuário

# O procedimento `input()` solicita ao usuário dados que podem ser associados a variáveis. É possível personalizar a mensagem de solicitação, como mostrado abaixo.

# In[43]:


texto_usuario =  input("Diga um valor: ")
texto_usuario


# Por padrão, qualquer dado passada pelo usuário será tratado como texto. Para tratá-lo como um valor numérico, você deve usar os procedimentos `int()` ou `float()`, dependendo de serem números inteiros ou reais.

# In[44]:


inteiro = int(input("Diga um valor inteiro: "))
inteiro + 1


# In[46]:


real = float(input("Diga um valor real: "))
real + 1


# ### Exercícios de fixação

# EF12 - Solicite ao usuário *seu nome* e o associe a uma variavél chamada `nome`.

# In[47]:


nome = input('Digite seu nome: ')
nome


# EF13 - Solicite ao usuário *sua idade* e a associe a uma variável chamada `idade`.

# In[48]:


idade = int(input('Digite sua idade: '))
idade


# In[50]:


altura = float(input('Digite sua altura: '))
altura


# EF14 - Solicite ao usuário *sua altura* e a associe a uma variável chamada `altura`.

# In[ ]:





# ## Informando dados ao usuário

# Assim como é possível receber dados do usuário, também é possível informar dados ao usuário.
# 
# Para isto, usamos o procedimento `print()`.

# In[51]:


print(texto)


# É possível informar os valores associados a múltiplas variáveis com uma única chamada ao procedimento `print()`. 

# In[52]:


print(texto, x)


# Também é possível informar textos, valores e o resultado de expressões:

# In[53]:


print("Testando", 3, x + y)


# ### Exercícios de fixação

# EF15 - Informe ao usuário **seu nome**.

# In[54]:


print(nome)


# EF16 - Informe ao usuário **sua idade**.

# In[55]:


print(idade)


# EF17 - Informe ao usuário **seu índice de massa corporal (IMC)**. Para isso, solicite ao usuário seu peso.

# In[56]:


peso = float(input('Digite seu peso: '))
IMC = peso/(altura ** 2)
print('Seu índice de massa corporal (IMC) é ', IMC)


# ## Exercícios do URI

# O URI é um juiz online utilizado em treinamentos para competições de programação.
# 
# Nesta disciplina, utilizaremos exercícios inspirados na seção **Iniciante**, adaptados para o nosso contexto.
# 
# Para ver a descrição do exercício em sua versão original do URI, clique no seu número.

# [1008](https://www.urionlinejudge.com.br/judge/pt/problems/view/1008) - Um sistema do setor de recursos humanos de uma empresa deve calcular o salário a ser pago para cada funcionário da empresa em função de quantas horas o funcionário trabalhou no mês e de quanto ele recebe por hora trabalhada.
# 
# Escreva um código Python que leia o nome de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula seu salário. Em seguida, mostre o nome e o salário do funcionário.

# |.| Entrada | Saída |
# |-|----|---|
# | *Exemplo 1* | João 100 5.50  | João 550.00 | 
# | *Exemplo 2* | Maria 200 20.50 | Maria 4100.00 |
# | *Exemplo 3* | Facebookson 145 15.55 | Facebookson 2254.75 |

# In[60]:


nome = input('Digite o nome do funcionário: ')
hora_trab = float(input('Digite o número de horas trabalhadas: '))
sal_hora = float(input('Digite o valor que recebe por hora: '))
salario = hora_trab * sal_hora
print(nome, salario)


# [1009](https://www.urionlinejudge.com.br/judge/pt/problems/view/1009) - No caso de empresas do setor de comércio, a remuneração mensal de cada vendedor é composta por um salário fixo mais uma bonificação proporcional às vendas efetuadas pelo vendedor naquele mês.
# 
# Escreva um código Python que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informe o total que ele deverá receber no final do mês.

# |.| Entrada | Saída |
# |-|----|---|
# | *Exemplo 1* | João 500 1230.30  | João 684.54 | 
# | *Exemplo 2* | Pedro 700 0.00 | Pedro 700.00 |
# | *Exemplo 3* | Mangojata 1700 1230.50 | Mangojata 1884.58 |

# In[ ]:


nome = input('Digite o nome do vendedor: ')
sal_fixo = float(input('Digite o salario do vendedor: '))
total_vendas = float(input('Digite o tota de vendas efetuadas no mes (em dinheiro): '))
salario = sal_fixo + (sal_fixo * (total_vendas * 0,15))
print(nome, salario)


# [1010](https://www.urionlinejudge.com.br/judge/pt/problems/view/1010) - Outro tipo de sistema utilizado no setor de comércio é o sistema de frente de loja, que calcula o total de uma venda baseado nos itens adquiridos, suas quantidades e seus valores unitários.
# 
# Escreva um código Python que leia as informações de dois produtos adquiridos em uma compra e informe o valor a ser pago. Para cada produto, leia seu código, sua quantidade e seu valor unitário.

# |.| Entrada | Saída |
# |-|----|---|
# | *Exemplo 1* | 12 1 5.30 <br> 16 2 5.10 | VALOR A PAGAR: 15.50 |
# | *Exemplo 2* | 13 2 15.30 <br> 161 4 5.20 | VALOR A PAGAR: 51.40 |
# | *Exemplo 3* | 1 1 15.10 <br> 2 1 15.10 | VALOR A PAGAR: 30.20 |

# In[ ]:


cod1 = int(input('Digite o código do produto 1: '))
qtd1 = int(input('Digite a quantidade do produto 1: '))
vl_unitario1 = float(input('Digite o valor unitário do produto 1: '))
cod2 = int(input('Digite o código do produto 2: '))
qtd2 = int(input('Digite a quantidade do produto 2: '))
vl_unitario2 = float(input('Digite o valor unitário do produto 2: '))
valor_pagar = (vl_unitario1 * qtd1) + (vl_unitario2 * qtd2)
print('VALOR A PAGAR: ', valor_pagar)


# [1018](https://www.urionlinejudge.com.br/judge/pt/problems/view/1018) - Sistemas de frente de loja também devem auxiliar vendedores a dar trocos. Por simplicidade, vamos considerar primeiro apenas trocos inteiros, que podem ser dados usando apenas cédulas.
# 
# Escreva um código Python que leia um valor de troco e informe quantas cédulas de cada valor devem ser entregues pelo vendedor ao cliente.
# 
# **Obs.:** Considere que ainda existem notas de R$ 1,00.

# |.| Entrada | Saída |
# |-|----|---|
# | *Exemplo 1* | 576 | 5 nota(s) de 100,00 <br /> 1 nota(s) de 50,00 <br /> 1 nota(s) de 20,00 <br /> 0 nota(s) de 10,00 <br /> 1 nota(s) de 5,00  <br /> 0 nota(s) de 2,00  <br /> 1 nota(s) de 1,00 |
# | *Exemplo 2* | 11257 | 112 nota(s) de 100,00 <br /> 1 nota(s) de 50,00 <br /> 0 nota(s) de 20,00 <br /> 0 nota(s) de 10,00 <br /> 1 nota(s) de 5,00 <br /> 1 nota(s) de 2,00 <br /> 0 nota(s) de 1,00 |
# | *Exemplo 3* | 503 | 5 nota(s) de 100,00 <br /> 0 nota(s) de 50,00 <br /> 0 nota(s) de 20,00 <br /> 0 nota(s) de 10,00 <br /> 0 nota(s) de 5,00 <br /> 1 nota(s) de 2,00 <br /> 1 nota(s) de 1,00 |

# In[ ]:

troco = float(input("Digite o valor do troco: "))
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
nota1 = 0

while (troco >= 100):
    nota100 += 1;
    troco = troco - 100
while (troco >= 50):
    nota50 += 1;
    troco = troco - 50
while (troco >= 20):
    nota20 += 1;
    troco = troco - 20
while (troco >= 10):
    nota10 += 1;
    troco = troco - 10
while (troco >= 5):
    nota5 += 1;
    troco = troco - 5
while (troco >= 2):
    nota2 += 1;
    troco = troco - 2
while (troco >= 1):
    nota1 += 1;
    troco = troco - 1


print(nota100, " nota(s) de 100,00")
print(nota50, " nota(s) de 50,00")
print(nota20, " nota(s) de 20,00")
print(nota10, " nota(s) de 10,00")
print(nota5, " nota(s) de 5,00")
print(nota2, " nota(s) de 2,00")

    
# [1021](https://www.urionlinejudge.com.br/judge/pt/problems/view/1021) - Agora vamos voltar ao mundo real, onde trocos podem precisar utilizar cédulas e moedas.
# 
# Escreva um código Python que leia um valor de troco e informe quantas cédulas e moedas de cada valor devem ser entregues pelo vendedor ao cliente.
# 
# **Obs.:** Considere que ainda existem moedas de R$ 0,01.

# |.| Entrada | Saída |
# |-|----|---|
# | *Exemplo 1* | 576.73 | NOTAS: <br /> 5 nota(s) de 100,00 <br /> 1 nota(s) de 50,00 <br /> 1 nota(s) de 20,00 <br /> 0 nota(s) de 10,00 <br /> 1 nota(s) de 5,00  <br /> 0 nota(s) de 2,00  <br /> MOEDAS: <br /> 1 moeda(s) de 1,00 <br /> 1 moeda(s) de 0,50 <br /> 0 moeda(s) de 0,25 <br /> 2 moeda(s) de 0,10 <br /> 0 moeda(s) de 0,05 <br /> 3 moeda(s) de 0,01 |
# | *Exemplo 2* | 4.00 | NOTAS: <br /> 0 nota(s) de 100,00 <br /> 0 nota(s) de 50,00 <br /> 0 nota(s) de 20,00 <br /> 0 nota(s) de 10,00 <br /> 0 nota(s) de 5,00  <br /> 2 nota(s) de 2,00 <br /> MOEDAS: <br /> 0 moeda(s) de 1,00 <br /> 0 moeda(s) de 0,50 <br /> 0 moeda(s) de 0,25 <br /> 0 moeda(s) de 0,10 <br /> 0 moeda(s) de 0,05 <br /> 0 moeda(s) de 0,01 |
# | *Exemplo 3* | 91.01 | NOTAS: <br /> 0 nota(s) de 100,00 <br /> 1 nota(s) de 50,00 <br /> 2 nota(s) de 20,00 <br /> 0 nota(s) de 10,00 <br /> 0 nota(s) de 5,00  <br /> 0 nota(s) de 2,00 <br /> MOEDAS: <br /> 1 moeda(s) de 1,00 <br /> 0 moeda(s) de 0,50 <br /> 0 moeda(s) de 0,25 <br /> 0 moeda(s) de 0,10 <br /> 0 moeda(s) de 0,05 <br /> 1 moeda(s) de 0,01 |

# In[ ]:

troco = float(input("Digite o valor do troco: "))
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
moeda1real = 0
cent50 = 0
cent25 = 0
cent10 = 0
cent5 = 0
cent1 = 0

while (troco >= 100):
    nota100 += 1;
    troco = troco - 100
while (troco >= 50):
    nota50 += 1;
    troco = troco - 50
while (troco >= 20):
    nota20 += 1;
    troco = troco - 20
while (troco >= 10):
    nota10 += 1;
    troco = troco - 10
while (troco >= 5):
    nota5 += 1;
    troco = troco - 5
while (troco >= 2):
    nota2 += 1;
    troco = troco - 2
while (troco >= 1):
    moeda1real += 1;
    troco = troco - 1
while (troco >= 0.50):
    cent50 += 1
    troco = troco - 0.50
while (troco >= 0.25):
    cent25 += 1
    troco = troco - 0.25
while (troco >= 0.10):
    cent10 += 1
    troco = troco - 0.10
while (troco >= 0.05):
    cent5 += 1
    troco = troco - 0.05
while (troco >= 0.01):
    cent1 += 1
    troco = troco - 0.01

print('NOTAS: ')
print(nota100, " nota(s) de 100,00")
print(nota50, " nota(s) de 50,00")
print(nota20, " nota(s) de 20,00")
print(nota10, " nota(s) de 10,00")
print(nota5, " nota(s) de 5,00")
print(nota2, " nota(s) de 2,00")
print("MOEDAS: ")
print(moeda1real, " moedas(s) de 1,00")
print(cent50, " moedas(s) de 0,50")
print(cent25, " moedas(s) de 0,25")
print(cent10, " moedas(s) de 0,10")
print(cent5, " moedas(s) de 0,05")
print(cent1, " moedas(s) de 0,01")


# [1019](https://www.urionlinejudge.com.br/judge/pt/problems/view/1019) - Sistemas de frente de loja também precisam registrar a data e o horário das vendas. 
# 
# Computadores normalmente armazenam datas utilizando uma única unidade de tempo, convertendo para o formato de apresentação desejado quando necessário. Por simplicidade, considere neste exercício que o dado informado representa apenas o horário da venda.
# 
# Escreva um código Python que leia um valor em segundos e o converta para o formato *horas:minutos:segundos*.
# 
# **Dica 1 --** a opção sep do procedimento print() permite configurar o caracter de separação entre as diferentes partes de uma impressão, como no exemplo abaixo.

# In[ ]:


print(10,33,51,sep=":")


# **Dica 2 --** é possível utilizar o procedimento print para impressão formatada. Pesquise o funcionamento da máscara de formatação abaixo:

# In[ ]:


print("%02d:%02d:%02d" % (9,33,51))


# |.| Entrada | Saída |
# |-|----|---|
# | *Exemplo 1* | 556  | 00:09:16 | 
# | *Exemplo 2* | 1 | 00:00:01 |
# | *Exemplo 3* | 86153 | 23:55:53 |

tempo_total_segundos = int(input("Escreva o tempo total em segundos: "))
tempo_hora = tempo_total_segundos / 3600
tempo_total_segundos = tempo_total_segundos % 3600
tempo_minutos = tempo_total_segundos / 60
tempo_segundos = tempo_total_segundos = tempo_total_segundos % 60
print("%02d:%02d:%02d" % (tempo_hora, tempo_minutos, tempo_segundos))

#onion by PacMan v3.50 BETA
import os
import sys
import webbrowser as web
#База даних словники
base_program = {'wikioni': 'http://psychonaut3z5aoz.onion/wiki','wikioni2': 'http://rambleeeqrhty6s5jgefdfdtc6tfgg4jj6svr4jpgk4wjtg3qshwbaad.onion/wiki','wikioni3': 'http://kfj2am4ee2asdqflt4tuxxwbeuzmh6tv64ojbqscc4u55skrechsxzad.onion.ly', 'tgchannel': 'https://t.me/i2p_3218', 'search1': 'http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/', 'search2': 'http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/'}
def wikionilinks():
	print(base_program['wikioni'],"\n",base_program['wikioni2'],"\n",base_program['wikioni3'])
def onitxtopen():
	oniontxt = open("onion.txt")
	oniontxt2 = open("onion2.txt")
	print(oniontxt.read(),oniontxt2.read())
def i2ptxtopen():
	I2ptxtt = open("i2p.txt")
	print(I2ptxtt.read())
#START PROGRAM
def out_red(text):
    print("\033[34m{}".format(text))
out_red("Onion/I2p")
def out_red(text):
    print("\033[37m{}".format(text))
out_red("\tby")
def out_red(text):
    print("\033[33m{}".format(text))
out_red("PacMan")
print("\n")
def out_red(text):
    print("\033[37m{}".format(text))
out_red("v3.50 BETA")
print("\n\t#Ні_війні! ")
def out_red(text):
    print("\033[33m{}".format(text))
out_red("Що нового: Нові команди: /restart,/exit,/info,/wikionions, /i2p")
def out_red(text):
    print("\033[32m{}".format(text))
out_red("/a пошукові системи, /b  Сайти. Просто напишіть англійську а чи b.\nАбо введіть команди.")
what = input ("/")
if what == "a":
    print(base_program['search1'],"\n",base_program['search2'])
    del what 
    print("Телеграм канал?")
    what = input("yes/not: ")
    if what == "yes":
        web.open('https://t.me/i2p_3218', new=2)
        print("Заходьте в мій Telegram ^_^ ")
    elif what == "not":
    	print("Ok...\n\t Restart program,please...")
    else:
    	print("Errror!!")
elif what == "b":
	onitxtopen()
elif what == "wikionions":
  wikionilinks()
  exit()
elif what == "IDDQD":
  print("\tЧіт код запущений...")
  onitxtopen()
  wikionilinks()
  i2ptxtopen()
  exit()
elif what == "Слава Україні":
  print ("Героям слава ")
elif what == "restart":
  print("Перезагрузка...")
  os.execl(sys.executable, sys.executable, *sys.argv)
elif what == "info":
  def out_red(text):
    print("\033[32m{}".format(text))
  out_red("v3.50 BETA onionbypacman")
  def out_red(text):
    print("\033[33m{}".format(text))
  out_red("Команди: /a пошукові системи,/b сайти, /restart перезапуск, /exit вихід,/info,/wikionions")
  print("\nПапка з файлом:")
  print(os.getcwd())
  print ("\nМова програмування: Python")
  print("Мова програми: Українська,Україна \n\nGitHub: https://github.com/Aggggsu/onionbypac\n\n","telegram:", base_program['tgchannel'],"\n\n\n\tЯК ПРАЦЮЄ ПРОГРАМА:\n\nПрограма працює за командами, кожна команда має свою функцію та алгоритм. Посилання вона запозичує в словнику програми.\nАбо в текстових файлах.")
  exit()
elif what == "exit":
  exit()
elif what == "Ukraineflag":
  def out_red(text):
    print("\033[34m{}".format(text))
  out_red("СЛАВАУКРАЇНІСЛАВАУКРАЇНІСЛАВАУКРАЇНІСЛАВАУКРАЇНІСЛАВАУКРАЇНІСЛАВАУКРАЇНІСЛАВАУКРАЇНІСЛАВАУКРАЇНІСЛАВАУКРАЇНІСЛАВАУКРАЇНІСЛАВАУКРАЇНІСЛАВАУКРАЇНІСЛАВАУКРАЇНІСЛАВАУКРАЇНІ")
  def out_red(text):
    print("\033[33m{}".format(text))
  out_red("СЛАВАУКРАЇНІСЛАВАУКРАЇНІСЛАВАУКРАЇНІСЛАВАУКРАЇНІСЛАВАУКРАЇНІСЛАВАУКРАЇНІСЛАВАУКРАЇНІСЛАВАУКРАЇНІСЛАВАУКРАЇНІСЛАВАУКРАЇНІСЛАВАУКРАЇНІСЛАВАУКРАЇНІСЛАВАУКРАЇНІСЛАВАУКРАЇНІ")
elif what == "i2p":
	i2ptxtopen()
else:
  def out_red(text):
    print("\033[31m{}".format(text))
  out_red("Errrrrr :D [помилка] \n\nВи ввели неправильну команду,\nабо команда не існує...")
  exit()
input()

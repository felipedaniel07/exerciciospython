import urllib.request
import urllib
try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('O site não está acessivel no momento!')
else:
    print('O site está acessível no momento!')
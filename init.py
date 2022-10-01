import os
import sys
import subprocess

pathRelativofile ='cd lastProject;'

def logo():
    logo = '''
 _____                      _____                 
/  ___|                    /  ___|                
\ `--. _   _ _ __   ___ _ _\ `--.  ___ __ _ _ __  
 `--. | | | | '_ \ / _ | '__`--. \/ __/ _` | '_ \ 
/\__/ | |_| | |_) |  __| | /\__/ | (_| (_| | | | |
\____/ \__,_| .__/ \___|_| \____/ \___\__,_|_| |_|
            | |                                   
            |_|                                   
'''

    print(logo)

def clear():
    os.system('clear')

def default():
    print("------Ups, try Again------")
    input()
    clear()
    menu()

def ejecutarNmap(unaURL):
    
    print('Comenzando  Nmap---')
    urlNmap = unaURL.split('/', 1)[0]
    
    print('URL a analizar --> ' + urlNmap)
    toExecute = pathRelativofile + ' nmap -A -Pn -oN nmap_' + urlNmap + '.txt ' + urlNmap
    print(os.system(toExecute))
    print('Finalizando nmap---\n\n')
    
    print('Comenzando Nmap con ip -------------')
    toExecute = pathRelativofile + 'host ' + urlNmap + ' | grep "has address" | cut -d " " -f 4 | tee targetNmapIp.txt'
    print(os.system(toExecute))
    toExecute = pathRelativofile + 'nmap -A -Pn -iL targetNmapIp.txt -oN nmapIPs_' + urlNmap + '.txt '
    print(os.system(toExecute))
    print('Finalizando nmap con IP---\n\n')


def ejecutarSslScan(unaURL, protocolo):
    print('Comenzando  SSlScan---')
    urlSslScan = unaURL.split('/', 1)[0]
    print('URL a analizar --> ' + urlSslScan)
    toExecute = pathRelativofile + ' sslscan --no-failed ' + protocolo + urlSslScan +' | tee sslscan' + urlSslScan + '.txt  '
    print(os.system(toExecute))
    print('Finalizando SSlScan---\n\n')


def ejecutarTestSsl(unaURL, protocolo):
    print('Comenzando  TestSsl---')
    urlTestSsl = unaURL.split('/', 1)[0]
    print('URL a analizar -->' + unaURL)
    toExecute = pathRelativofile + ' /home/kali/Desktop/testssl.sh/testssl.sh -oH testSsl' + urlTestSsl + '.html ' + protocolo + unaURL 
    print(os.system(toExecute))
    print('Finalizando TestSsl---\n\n')
    
def ejecutarFFuF(unaURL, protocolo, cookie):
    print('Comenzando  FFuF---')
    print('Primer WordList common.txt---')
    urlSslScan = unaURL.split('/', 1)[0]
    print('URL a analizar -->' + urlSslScan)
    ComandoFfuf = 'ffuf -w /usr/share/seclists/Discovery/Web-Content/common.txt '
    ComandoFfuf += '-u ' + protocolo + unaURL +'/FUZZ '
    if cookie != '':
        ComandoFfuf += '-b  " ' + cookie + ' " '
    ComandoFfuf += '-s -c -mc 200 -of html -o ffuf_Common_'+ urlSslScan + '.html | tee -a ffuf200'
    toExecute = pathRelativofile + ComandoFfuf
    print(toExecute)
    print(os.system(toExecute))
    print('Finalizando Primer WordList---\n\n')

    print('URL a analizar -->' + urlSslScan)
    print('Segundo WordList big.txt---')
    ComandoFfuf = 'ffuf -w /usr/share/seclists/Discovery/Web-Content/big.txt '
    ComandoFfuf += '-u ' + protocolo + unaURL +'/FUZZ '
    if cookie != '':
        ComandoFfuf += '-b  " ' + cookie + ' " '
    ComandoFfuf += '-s -c -mc 200 -of html -o ffuf_Big_'+ urlSslScan + '.html | tee -a ffuf200'
    toExecute = pathRelativofile + ComandoFfuf
    print(toExecute)
    print(os.system(toExecute))
    print('Finalizando Segundo WordList---\n\n')

    print('URL a analizar -->' + urlSslScan)
    print('Tercer WordList juicy.txt---')
    ComandoFfuf = 'ffuf -w /media/sf_ShareKali/WordList/juicy.txt '
    ComandoFfuf += '-u ' + protocolo + unaURL +'/FUZZ '
    if cookie != '':
        ComandoFfuf += '-b  " ' + cookie + ' " '
    ComandoFfuf += '-s -c -mc 200 -of html -o ffuf_Juicy_'+ urlSslScan + '.html | tee -a ffuf200'
    toExecute = pathRelativofile + ComandoFfuf
    print(toExecute)
    print(os.system(toExecute))
    print('Finalizando Tercer WordList---\n\n')

    print('URL a analizar -->' + urlSslScan)
    print('Cuarto WordList fuzz-Bo0oM.txt---')
    ComandoFfuf = 'ffuf -w /usr/share/seclists/Fuzzing/fuzz-Bo0oM.txt '
    ComandoFfuf += '-u ' + protocolo + unaURL +'/FUZZ '
    if cookie != '':
        ComandoFfuf += '-b  " ' + cookie + ' " '
    ComandoFfuf += '-s -c -mc 200 -of html -o ffuf_Bo0oM_'+ urlSslScan + '.html | tee -a ffuf200'
    toExecute = pathRelativofile + ComandoFfuf
    print(toExecute)
    print(os.system(toExecute))
    print('Finalizando cuarto WordList---\n\n')

    print('Finalizando FFUF---')
    
def menu():
    print('\n-----Scan Management Pentesting Web-----\n ')
    logo()
    URL = input('Ingresa URL a analizar\n ')
    COOKIES = input('Ingresar Cookies\n ')

    URL = URL.strip()
    if COOKIES != '':
        COOKIES = COOKIES.strip()
    else:
        print('No hay Cookies')
        COOKIES = ''

    

    if URL.startswith('https://'):
        PORT = 443
        PROTOCOL = 'https://'
    elif URL.startswith('http://'):
        PORT = 80
        PROTOCOL = 'http://'
    else:
        print('http(s):// Falta esto....')
        sys.exit()

    URL = URL.replace(PROTOCOL, "")

    print('Creando carpeta lastProject.......')
    print(os.system('mkdir lastProject'))
    
    
    ejecutarFFuF(URL, PROTOCOL, COOKIES)
    logo()
    ejecutarNmap(URL)
    logo()
    ejecutarSslScan(URL, PROTOCOL)
    logo()
    ejecutarTestSsl(URL, PROTOCOL)
    logo()


    #print(URL)
    #print(COOKIES)




#inicio
menu()
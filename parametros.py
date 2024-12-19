import argparse

arg = argparse.ArgumentParser(
    description= 'herramienta de fuerza bruta: prueba contraseñas a partir de un usuario conocido o por medio de un diccionario proporcionado por el usuario'
)
arg.add_argument('-url',type=str,help='url de la web al ingresar datos incorrectos')
arg.add_argument('-c_u',type=str,help='casilla del html usuario')
arg.add_argument('-c_c',type=str,help='casilla del html contraseña')
arg.add_argument('-u','--usuario',type=str,help='si el usuario se conoce se ingresa aca')
arg.add_argument('-dic_c',type=str,help='diccionario de contraseñas')
arg.add_argument('-dic_u',type=str,help='diccionario de usuarios')
arg.add_argument('-n',type=int,help='numero de formulario en la pagina')
arg.add_argument('-hl','--hilos',type=int,help='numero de hilos')
arg.add_argument('-msg',type=str,help='mensaje que sale al ingresar credenciales incorrectas')
arg.add_argument('-d','--delay',type=float,help='delay: en ocasiones evita falsos positivos')
param= arg.parse_args()
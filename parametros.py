import argparse

arg = argparse.ArgumentParser(
    description= 'herramienta de fuerza bruta: prueba contraseñas a partir de un usuario conocido o por medio de un diccionario proporcionado por el usuario'
)
arg.add_argument('-url',type=str)
arg.add_argument('-c_u',type=str)
arg.add_argument('-c_c',type=str)
arg.add_argument('-u','--usuario',type=str)
arg.add_argument('-dic_c',type=str)
arg.add_argument('-dic_u',type=str)
arg.add_argument('-n',type=int)
arg.add_argument('-hl','--hilos',type=int)
arg.add_argument('-msg',type=str)

param= arg.parse_args()
import argparse

arg = argparse.ArgumentParser()
arg.add_argument('-url',type=str)
arg.add_argument('-c_u',type=str)
arg.add_argument('-c_p',type=str)
arg.add_argument('-u','--usuario',type=str)
arg.add_argument('-dic_p',type=str)
arg.add_argument('-dic_u',type=str)
arg.add_argument('-n',type=int)

param= arg.parse_args()
from main import *

main = Mixed(__file__)

with open("code.mixed", "r") as pf:
    print(eval("main." + pf.read()))
from fileinput import filename
import os
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument("--name",action="store",required=True)
my_parser.add_argument("--entity",action="store",required=True)
my_parser.add_argument("--attribute",action="store",required=True)
my_parser.add_argument("--type",action="store",required=True)
init = my_parser.parse_args()
path = os.path.join(os.getcwd(),init.name)
filename = os.path.join(os.getcwd(),init.name,"src","main","java","com","example","{}".format(init.name),"entities","{}.java".format(init.entity))


#transiet function
def make_transiet(name):
    transiet = "@Transient"
    #with open(filename, 'r+b') as f:

if __name__ == "__main__":
    if (init.type=="transiet"):
        make_transiet(init.attribute)
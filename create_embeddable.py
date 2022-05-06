#!/usr/bin/env python3
import os
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument("--name",action="store",required=True)
my_parser.add_argument("--embeddable",action="store",required=True)
my_parser.add_argument("--attributes",action="store",required=True)
init = my_parser.parse_args()
filename = os.path.join(os.getcwd(),init.name,"src","main","java","com","example","{}".format(init.name),"entities","{}.java".format(init.enum))
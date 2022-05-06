#!/usr/bin/env python3
import os
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument("--name",action="store",required=True)
my_parser.add_argument("--enum",action="store",required=True)
my_parser.add_argument("--attributes",action="store",required=True)
init = my_parser.parse_args()
filename = os.path.join(os.getcwd(),init.name,"src","main","java","com","example","{}".format(init.name),"entities","{}.java".format(init.enum))
package = "package com.example.{}.entities;\n".format(init.name);

def create():
    with open(filename,"w") as f:
        f.write(package)
        f.write("public enum {} {}\n".format(init.enum.lower().capitalize(),"{"))
        f.write("    {}\n".format(init.attributes))
        f.write("}")
    print("enum {} was created".format(init.enum))

if __name__ == "__main__":
    create()
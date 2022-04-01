#!/usr/bin/env python3
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
transient = "@Transient\n"
json_ignore="@JsonProperty(access = JsonProperty.Access.WRITE_ONLY)\n"
def find_index_attribute(name):
    i = 0
    with open(filename, 'r') as f:
        for line in f:
            i = i+1
            if ("private" in line and name in line):
                return i-1

def write_type_in_index(index,type):
    i = 0
    with open(filename, 'r') as f:
        lines = f.readlines()
        before = lines[:index]
        after = lines[index:]
        new_file = before + [type] + after
        return new_file

def write_transient(file):
    os.remove(filename)
    with open(filename,"w") as f:
        for line in file:
            f.write(line)

def new_type(type):
    index = find_index_attribute(init.attribute)
    new_file = write_type_in_index(index,type)
    write_transient(new_file)

if __name__ == "__main__":
    if (init.type=="transient"):
        new_type(transient)
    elif (init.type=="json_ignore"):
        new_type(json_ignore)
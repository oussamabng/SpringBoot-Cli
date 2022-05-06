#!/usr/bin/env python3
import os
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument("--name",action="store",required=True)
my_parser.add_argument("--many",action="store",required=True)
my_parser.add_argument("--one",action="store",required=True)
my_parser.add_argument("--type",action="store",required=True)
init = my_parser.parse_args()

filename_many = os.path.join(os.getcwd(),init.name,"src","main","java","com","example","{}".format(init.name),"entities","{}.java".format(init.many))
filename_one = os.path.join(os.getcwd(),init.name,"src","main","java","com","example","{}".format(init.name),"entities","{}.java".format(init.one))

many = "@ManyToOne\nprivate {} {};\n".format(init.one,init.one.lower())
one = '@OneToMany(mappedBy = "{}",cascade = CascadeType.ALL,fetch = FetchType.{})\nCollection<{}> {}s;\n'.format(init.one.lower(),init.type.upper(),init.many,init.many.lower())


def read(filename,type):
    with open(filename,"r") as f:
        lines = f.readlines()
        new_file = lines[:-1] + [type] + lines[-1:]
        return (new_file)

def write(file,filename):
    with open(filename,"w") as f:
        for line in file:
            f.write(line)

if __name__ == "__main__":
    
    new_many = read(filename_many,many)
    write(new_many,filename_many)
    
    new_one = read(filename_one,one)
    write(new_one,filename_one)

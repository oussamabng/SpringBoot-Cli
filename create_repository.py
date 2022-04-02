#!/usr/bin/env python3
import os
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument("--name",action="store",required=True)
my_parser.add_argument("--entity",action="store",required=True)
init = my_parser.parse_args()

package = "package com.example.{}.repositories;\n".format(init.name);
entity = "import com.example.{}.entities.{};\n".format(init.name,init.entity)
repository = "import org.springframework.data.jpa.repository.JpaRepository;\nimport org.springframework.data.rest.core.annotation.RepositoryRestResource;\n"
filename = os.path.join(os.getcwd(),init.name,"src","main","java","com","example","{}".format(init.name),"repositories","{}Repository.java".format(init.entity.lower().capitalize()))

def create():
    with open(filename,"w") as f:
        f.write(package)
        f.write(entity)
        f.write(repository)
        f.write("\n@RepositoryRestResource\n")
        f.write("public interface {}Repository extends JpaRepository<{},Long> ".format(init.entity.lower().capitalize(),init.entity.lower().capitalize()))
        f.write("{\n")
        f.write("}\n")

if __name__ == "__main__":
    create()
    print("{}Repository created".format(init.entity.lower().capitalize()) )

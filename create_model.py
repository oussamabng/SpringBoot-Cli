#!/usr/bin/env python3
import os
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument("--name",action="store",required=True)
my_parser.add_argument("--model",action="store",required=True)
my_parser.add_argument("--attributes",action="store",required=True)
init = my_parser.parse_args()

data_types = ["String","Boolean","int","Long","double","Date","Integer"]
attributes = init.attributes.split(",")
filename = os.path.join(os.getcwd(),init.name,"src","main","java","com","example","{}".format(init.name),"models","{}.java".format(init.model))
package = "package com.example.{}.models;\n".format(init.name);
lombok = "import lombok.*;\n"
util = "import java.util.*;\n"


def create():
    with open(filename, 'w') as f:
      f.write(package)
      f.write(lombok)
      f.write(util)
      f.write("@Data @AllArgsConstructor @NoArgsConstructor\n")
      f.write("public class {}".format(init.model.lower().capitalize()))
      f.write("{\n")
      for attribute in attributes:
        name,type = attribute.split(":")
        name,type = attribute.split(":")
        f.write("private {} {};\n".format(type,name))
      f.write("}")

if __name__ == "__main__":

  for attribute in attributes:
        name,type = attribute.split(":")
        if (type not in data_types):
          print("this type: {} don't exist in JAVA".format(type))
          exit(0)
  create()
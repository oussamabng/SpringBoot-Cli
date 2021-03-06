#!/usr/bin/env python3
import os
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument("--name",action="store",required=True)
my_parser.add_argument("--entity",action="store",required=True)
my_parser.add_argument("--embeddable",action="store")
my_parser.add_argument("--attributes",action="store",required=True)
init = my_parser.parse_args()

data_types = ["String","Boolean","int","Long","double","Date","Integer"]
attributes = init.attributes.split(",")
filename = os.path.join(os.getcwd(),init.name,"src","main","java","com","example","{}".format(init.name),"entities","{}.java".format(init.entity))
package = "package com.example.{}.entities;\n".format(init.name);
persistence = "import javax.persistence.*;\n"
util = "import java.util.*;\n"
lombok = "import lombok.*;\n"
json = "import com.fasterxml.jackson.annotation.JsonProperty;\n"
emb = "import javax.persistence.Embeddable;\nimport java.io.Serializable;\n"

def create(embeddable):
    with open(filename, 'w') as f:
      f.write(package)
      f.write(persistence)
      f.write(util)
      f.write(lombok)
      f.write(json)
      if (embeddable):
            f.write(emb)
      if (init.embeddable!="true"):
            f.write("@Entity\n")
      else:
            f.write("@Embeddable\n")
      f.write(" @Data @AllArgsConstructor @NoArgsConstructor\n")
      
      if (embeddable):
            f.write("public class {} implements Serializable".format(init.entity.lower().capitalize()))
      else:
            f.write("public class {}".format(init.entity.lower().capitalize()))
      f.write("{\n")
      
      for attribute in attributes:
            name,type = attribute.split(":")
            if (name == "id"):
                  f.write("@Id\n")
                  f.write("@GeneratedValue(strategy = GenerationType.IDENTITY)\n")
            if (len(type.split("-")) == 2):
                  if (type.split("-")[1] == "enum"):
                        f.write("@Enumerated(EnumType.STRING)\n")
                        f.write("private {} {};\n".format(type.split("-")[0],name))   
                  if (type.split("-")[1] == "embeddable"):
                        f.write("@ElementCollection(fetch = FetchType.LAZY)\n")
                        f.write("private Collection<{}> {};\n".format(type.split("-")[0],name)) 
            else:
                  f.write("private {} {};\n".format(type,name))
      
      f.write("}")
      if (init.embeddable == "true"):
            print("embeddable {} created successfully".format(init.entity))
      else:
            print("entity {} created successfully".format(init.entity))
if __name__ == "__main__":

  for attribute in attributes:
        name,type = attribute.split(":")
        if (type not in data_types):
              if (len(type.split("-")) == 2):
                  if (type.split("-")[1] != "enum" and type.split("-")[1] != "embeddable"):
                        print("this type: {} don't exist in JAVA".format(type))
                        exit(0)
  if (init.embeddable and init.embeddable == "true"):
        create(embeddable=True)
  else:
    create(embeddable=False)
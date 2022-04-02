import os
import argparse

my_parser = argparse.ArgumentParser()

my_parser.add_argument("--port",action="store",required=True)
my_parser.add_argument("--name",action="store",required=True)
my_parser.add_argument("--dbName",action="store",required=True)

init = my_parser.parse_args()

filename = os.path.join(os.getcwd(),init.name,"src","main","resources","application.properties")

lines = ["server.port = {}".format(init.port),"spring.application.name={}".format(init.name),"spring.datasource.url=jdbc:h2:mem:{}".format(init.dbName),"spring.h2.console.enabled=true","spring.jpa.show-sql=true"]

folders = ["entities","repositories","models","proxies","controllers"]


def config_project():
  with open(filename, 'w') as f:
    for line in lines:
      f.write(line)
      f.write("\n")

def create_architecture():
  dir = os.path.join(os.getcwd(),init.name,"src","main","java","com","example","{}".format(init.name))
  if not os.path.isdir(dir):
    print("Folder {} do not exist".format(init.name))
    exit(0)
  for folder in folders:
    path = os.path.join(dir, folder)
    os.mkdir(path)

    
if __name__ == "__main__":
  config_project()
  create_architecture()


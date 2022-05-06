import os
import argparse

my_parser = argparse.ArgumentParser()

my_parser.add_argument("--port",action="store",required=True)
my_parser.add_argument("--name",action="store",required=True)
my_parser.add_argument("--dbName",action="store",required=True)
my_parser.add_argument("--type_bdd",action="store",required=True)
my_parser.add_argument("--eureka",action="store")

init = my_parser.parse_args()

eureka = ""

if (init.eureka and init.eureka == "true"):
      eureka = "eureka.client.register-with-eureka =true\neureka.client.fetch-registry=true\neureka.client.service-url.defaultZone=http://localhost:8888/eureka\n"


filename = os.path.join(os.getcwd(),init.name,"src","main","resources","application.properties")

lines = ["server.port = {}\n".format(init.port),"spring.application.name={}\n".format(init.name),"spring.datasource.url=jdbc:h2:mem:{}\n".format(init.dbName),"spring.h2.console.enabled=true\n","spring.jpa.show-sql=true\n{}".format(eureka)]

mysql = ["server.port = {}\n".format(init.port),"spring.application.name={}".format(init.name),"spring.datasource.url=jdbc:mysql://localhost:3306/{}\n".format(init.dbName),"spring.datasource.username=root\nspring.datasource.password=\n","spring.jpa.show-sql=true\n","spring.jpa.hibernate.ddl-auto=create-drop\n","spring.main.allow-bean-definition-overriding=true\n"]

folders = ["entities","repositories","models","proxies","controllers"]


def config_project():
  with open(filename, 'w') as f:
    if (init.type_bdd == "h2"):
      for line in lines:
        f.write(line)
        f.write("\n")
    else:
      for line in mysql:
        f.write(line)
        f.write("\n")

def create_architecture():
  dir = os.path.join(os.getcwd(),init.name,"src","main","java","com","example","{}".format(init.name))
  print(dir)
  if not os.path.isdir(dir):
    print("Folder {} do not exist".format(init.name))
    exit(0)
  for folder in folders:
    path = os.path.join(dir, folder)
    os.mkdir(path)

    
if __name__ == "__main__":
  config_project()
  create_architecture()


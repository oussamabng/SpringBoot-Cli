import os
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument("--name",action="store",required=True)
init = my_parser.parse_args()



if __name__ == "__main__":
  os.system("cd {} && mvn spring-boot:run".format(os.path.join(os.getcwd(),init.name)))
 

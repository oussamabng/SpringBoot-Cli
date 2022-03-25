import argparse
import os
import zipfile

def unzip(name):
  with zipfile.ZipFile(os.path.join(os.getcwd(),"{}.zip".format(name)), 'r') as zip_ref:
    directory = name
    path = os.path.join(os.getcwd(), directory)
    os.mkdir(path)
    zip_ref.extractall(path)

def delete_zip(name):
  os.system("rm -rf {}.zip".format(name))


def spring_init():
  my_parser = argparse.ArgumentParser()

  my_parser.add_argument("--name",action="store",required=True)
  my_parser.add_argument("--javaVersion",action="store",required=True)
  my_parser.add_argument("--dependencies",action="store",required=True)

  init = my_parser.parse_args()

  os.system("spring init --name={} --javaVersion={} --dependencies={} --artifactId={} --packageName=com.example.{}".format(init.name,init.javaVersion,init.dependencies,init.name,init.name))

  unzip(init.name)
  delete_zip(init.name)

  return(1)




if __name__ == "__main__":
  print("spring initiated")
  


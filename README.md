
# Spring Boot CLI

a small spring boot cli with h2 database for windows



## Installation

Clone the project

```bash
  https://github.com/oussamabng/SpringBoot-Cli
  cd SpringBoot-Cli

```
make sure u have spring installed in ur PC.

to install it

```bash
  scoop bucket add extras
```
```bash
  scoop install springboot
```

if you dont have scoop open powershell as administrator and install it
```bash
  Set-ExecutionPolicy RemoteSigned -scope CurrentUser
```
```bash
  iwr -useb get.scoop.sh | iex
```
Make sure to install mvn and openjdk too with choco
```bash
  choco install openjdk
```
```bash
  choco install maven
```

to check everything is okay
```bash
  spring --version
  mvn --version
```
## Python Installation
install python requirements 
```bash
  pip install -r requirements.txt
```

## Creation of the project

execute the file index.py with the different arguments for the project

```bash
python index.py --name=name_of_the_project --javaVersion=17 --dependencies=data-rest,web,lombok,data-jpa,h2

```

you can see the list of dependencies by executing

```bash
spring init --list
```

check your project

```bash
ls name_of_the_project
```

## Config of the project
execute the file config.py with the different arguments for the configuration

```bash
python config.py --port=8080 --name=name_of_the_project --dbName=testdb

```
to add eureka seetings add --eureka=true

```bash
python config.py --port=8080 --name=name_of_the_project --dbName=testdb --eureka=true

```

to specify the db type add (type_bdd)  :
h2,mysql

```bash
python config.py --type_bdd=h2

```

check if the folders (entities , repository, models... ect) were created inside your projec

## Create Entity

exec the create_entity.py script with different arguments

```bash
python create_entity.py --name=name_of_the_project --entity=User 
--attributes=id:Long,name:String
```

for created an attribute of type enum add (-enum) after type Enum :
```bash
python create_entity.py --attributes:genre:Gender-enum
```

for created an attribute of type embeddable add (-embeddable) after type of the class embeddable :
```bash
python create_entity.py --attributes:genre:Adresse-embeddable
```


data types disponible are:
```bash
["String","Boolean","int","Long","double","Date","Integer"]
```

## Create Embeddable
exec the same create_entity.py script with one more argument
```bash
python create_entity.py --name=name_of_the_project --entity=User 
--attributes=id:Long,name:String --embeddable=true
```

## Create Enum
exec the create_enum.py script with different arguments
```bash
python create_enum.py --name=name_of_the_project --enum=Gender 
--attributes=Male,Female
```

## Create Model
exec the create_model.py script with different arguments
```bash
python create_enum.py --name=name_of_the_project --model=Formation 
--attributes=name:String
```
## Create Repository
exec the create_repository.py script with different arguments
```bash
python create_repository.py --name=name_of_the_project --entity=User
```
## Adding Transient or JsonIgnore
exec the manage_entity.py script with different arguments
```bash
python manage_entity.py --name=name_of_the_project --entity=User 
--attribute=name --type=transient
```
```bash
python manage_entity.py --name=name_of_the_project --entity=User 
--attribute=name --type=json_ignore
```
## Adding Relation ManyToOne OneToMany
exec the many_to_one.py script with different arguments
```bash
python many_to_one.py --name=name_of_the_project --many=Project --one=User --type=LAZY
```

## Execution of the project
execute the file exec.py with the name argument

```bash
python exec.py --name=name_of_the_project
```

check your api

```url
localhost:8080
```

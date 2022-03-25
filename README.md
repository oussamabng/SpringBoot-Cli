
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


check if the folders (entities , repository, models... ect) were created inside your project

## Execution of the project
execute the file exec.py with the name argument

```bash
python exec.py --name=name_of_the_project
```

check your api

```url
localhost:8080
```

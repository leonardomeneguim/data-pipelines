# data_pipeline

Data pipeline usando Airflow, Bash, Python e utilitários

# Desenvolvimento

**Definição de objetivo:**

O objetivo deste projeto é analisar o arquivo california_housing e exemplificar alguns processos de engenharia de dados, além de realizar a predição dos valores através de regressão. Este projeto visa mostrar como um pipeline simples pode ser criado com ferramentas como Spark, Airflow, bash e Python;

Esta é uma versão de amostra, sem considerar parâmetros de performance, qualidade da persistência, integridade dos tipos de dados, paths relativos, etc.;
Mais detalhes sobre cada ferramenta, e em como transformar este scratch em “hero” será feito posteriormente!

# Definição de workflow:

1. Realizar a conversão do bunch california_housing do scikit para csv;
2. Selecionar os dados que serão usados através de utilitário bash (csvkit);
3. Usar o PySpark para realizar a análise do arquivo;
4. Realizar load em MySQL:
  Obs.: pode-se criar uma prévia do schema da tabela utilizando o comando abaixo do csvkit:
  csvsql -i mysql california_housing_cleaned.csv > california_housing_ddl.sql
5. Realizar a regressão do alvo através do scikit;
6. Orquestrar o fluxo através do Airflow.

# Instalação e Setup

**Opcional: instalar WSL no Windows:**

Estou utilizando uma máquina Windows, e se este for seu caso, você deve instalar o subsistema Linux do Windows para este tutorial. Você pode ver as informações para esta instalação através do link abaixo:

  - https://docs.microsoft.com/pt-br/windows/wsl/install
  
Obs.: lembre de sempre realizar o restart da máquina para que a instalação funcione corretamente.
Realize a atualização dos pacotes através do comando abaixo:

  - sudo apt-get update
  
  Use sudo para as instalações!

**Java:**

  - apt-get install openjdk-8-jdk-headless -qq > /dev/null

**Apache Spark:**

Executar os seguintes comandos na sequência:

  - wget -q https://archive.apache.org/dist/spark/spark-2.4.4/spark-2.4.4-bin-hadoop2.7.tgz
  
  - tar xf spark-2.4.4-bin-hadoop2.7.tgz

**PySpark:**

Instalar através do pip:

  - pip install pyspark
  
Checar se a instação está OK:

Execute o script Python abaixo para verificar se tudo está OK (se aparecer a versão do Spark, tudo certo):

  - from pyspark.sql import SparkSession
  - sc = SparkSession.builder.master('local[*]').getOrCreate()
  - print("Apache Spark version: ", sc.version)

**Apache Airflow:** 

Instalar o Airflow via pip:

  - pip install apache-airflow
  
Defina a home do Airflow:

  - export AIRFLOW_HOME=~/airflow
  
Crie uma subpasta na home do Airflow, onde você criará os DAGs (definição do fluxo a ser orquestrado pelo Airflow).
Execute os seguintes comandos (importante os 2 últimos serem em background, usando o operador &):

  - airflow db init
  
  - airflow users create \
    --username admin \
    --firstname <seu nome>\
    --lastname <seu sobrenome> \
    --role Admin \
    --email <seu email>
  
  - airflow webserver --port 8080 &
  
  - airflow scheduler &
  
Obs.: verifique o quickstart no link abaixo:
  
  - https://airflow.apache.org/docs/apache-airflow/stable/start/local.html 
  
Acesse localhost:8080 e se tudo deu certo, após o login com Admin será apresentada a tela inicial.

**MySQL:**
  
Rodar os seguintes comandos:
  
  - apt-get install mysql-server
  
  - service mysql start
  
  - mysql (este último abrirá o prompt do mysql). Nele vamos criar um novo database:
  
    - create database pipelines;
  
Habilite o uso de arquivos para Load:
  
  - SET GLOBAL local_infile = true;
  
Mova os arquivos que serão utilizados para o Load para a pasta /var/lib/mysql-files/
Com isso temos um database para realizarmos o nosso trabalho.
Obs.: aqui é a instalação básica, com o usuário root sem password. Sugiro alterar a senha do root.

**Pacotes para interação do Python com MySQL:**
  
Execute os seguintes comandos:
  
  - apt-get install libmysqlclient-dev
  
  - pip install mysqlclient
  
  - pip install mysql-connector-python
  
**Outros:**
Sugiro instalar o Jupyter para criação dos scripts Python, mas você pode usar o bom e velho editor de texto (p. ex.: Nano).

#!/usr/bin/bash
echo ">>> Loading california_housing in MySQL"
echo "Drop Table"
mysql --user="root" --password="<your password>" -D pipelines -e "drop table if exists california_housing_cleaned"
echo "Create Table"
mysql --user="root" --password="<your password>" -D pipelines < /home/superuser/data/ddl/california_housing_ddl.sql
echo "Load Table"
cp /home/superuser/data/california_housing_cleaned.csv /var/lib/mysql-files/
mysql --user="root" --password="<your password>" -D pipelines -e "load data infile '/var/lib/mysql-files/california_housing_cleaned.csv' into table california_housing_cleaned fields terminated by ',' IGNORE 1 LINES"

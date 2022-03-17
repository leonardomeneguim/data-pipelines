#!/usr/bin/bash
echo ">>> Columns of california_housing"
csvcut -n /home/superuser/data/california_housing.csv
echo ">>> First 5 rows of california_housing"
csvlook /home/superuser/data/california_housing.csv | head -5
csvcut --not-columns 1 /home/superuser/data/california_housing.csv > /home/superuser/data/california_housing_filtered.csv
echo ">>> First 5 rows of california_housing filtered"
csvlook /home/superuser/data/california_housing_filtered.csv | head -5
# local session
from pyspark.sql import SparkSession
sc = SparkSession.builder.master('local[*]').getOrCreate()
print("Apache Spark version: ", sc.version)

# create a dataframe from csv
df = (sc.read.format('csv')
           .option('header', 'True')
           .option("inferSchema", "true")
           .load('/home/superuser/data/california_housing_filtered.csv'))

# create a table in spark
df.write.mode("overwrite").saveAsTable("california_housing")

# print the tables in the catalog
print(sc.catalog.listTables())

# perform a query
from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)
df_select = sqlContext.sql("SELECT * FROM california_housing")
df_select.show()

# create dataframe
df_california_housing = sc.table("california_housing")

# head
df_california_housing.show()

# count
df_california_housing.groupBy().count().show()

# EDA

# imports
import matplotlib.pyplot as plt
import seaborn as sns

# convert spark to pandas
pandas_california_housing = df_california_housing.toPandas()

# basic plots

# distribution
sns.distplot(pandas_california_housing.AveRooms)
plt.title('Distribution of AveRooms')
plt.show()

# scatter plot
plt.title('Scatterplot of MedHouseVal')
sns.scatterplot(pandas_california_housing.MedInc, pandas_california_housing.MedHouseVal)
plt.show()

# linear
sns.lmplot(x='AveRooms', y='MedHouseVal', data=pandas_california_housing)
plt.show()

# filter Population
filter_Population = df_california_housing.Population >= 200.0

# filter HouseAge
filter_houseAge = df_california_housing.HouseAge >= 2.0

# Filter the data, first by filterA then by filterB
filtered_df_california_housing = df_california_housing.filter(filter_Population).filter(filter_houseAge)
filtered_df_california_housing.show()

# count
filtered_df_california_housing.groupBy().count().show()

# write csv

# vars
path_to_file = '/home/superuser/data/'

# create csv
filtered_df_california_housing.toPandas().to_csv(path_to_file +'california_housing_cleaned.csv')


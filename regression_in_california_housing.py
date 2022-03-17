# imports
import pandas as pd
import sqlalchemy

# functions
def query(db_connect, sql_statement):
    df = pd.read_sql(sql_statement, db_connect)
    print("Result of SQL (first 10 rows): \n", sql_statement, "\n")
    print(df.head(10))

# connect
engine = sqlalchemy.create_engine('mysql://root:<your password>@localhost')

# inspect engine
inspect_engine = sqlalchemy.inspect(engine)
list_of_schemas = inspect_engine.get_schema_names()
print("List of Schemas: \n", list_of_schemas)

# show tables
connection = engine.connect()
connection.execute("USE pipelines")

# show tables
query(connection, "SHOW TABLES")

# select created table
query(connection, "SELECT count(*) FROM california_housing_cleaned")

# read to dataframe
df = pd.read_sql("SELECT * FROM california_housing_cleaned", connection)
print(df)

# regression

# imports
import matplotlib.pyplot as plt
import seaborn as sns

# define data and target
california_housing_data = df.drop(['a','MedHouseVal'], axis=1)
california_housing_target = df['MedHouseVal']

# import algorithm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

# split dataset
X_train, X_test, y_train, y_test = train_test_split(california_housing_data, california_housing_target, test_size=0.2, random_state=123)
X_test, X_holdout, y_test, y_holdout = train_test_split(X_test, y_test, test_size=0.2, random_state=123)

# create a model
model = LinearRegression()

# fit
model.fit(X_train, y_train)
print("R2 of Train: ", model.score(X_train, y_train), "\n") # R2, varying between -1 (worst) and 1 (best)

# predict
predictions = model.predict(X_test)

# show results

# MSE
mse_test=mean_squared_error(y_test, predictions)
print("MSE for predictions: ", str(mse_test.round(2))), "\n"

# MAE
mae_test=mean_absolute_error(y_test, predictions)
print("MAE for predictions: ", str(mae_test.round(2)), "\n")

# Coefficients and Intercept
print("Coefficients: ", model.coef_, "\n")
print("Intercept: ", model.intercept_, "\n")

# create a dataframe and plot results
for index, column in enumerate(df.drop(['a','MedHouseVal'], axis=1).columns):
    # construct dataframe
    df = pd.DataFrame()
    df[column] = X_test.iloc[:, index]
    df['actual'] = y_test
    df['predicted'] = predictions
    df['coeff'] = model.coef_[index]
    df['intercept'] = model.intercept_ 
    print("Dataframe: \n", df.sort_values([column]))
    df = df.sort_values([column])

    # plot
    plt.figure(figsize=(20,6))
    plt.scatter(df[column], df['actual'], color='green')
    plt.scatter(df[column], df['predicted'], color='red')
    plt.plot(df[column], df['coeff'] * df[column] - df['intercept'], color='blue')
    plt.xlabel(column)
    plt.show()

# predict a one sample
other_prediciton = model.predict(X_holdout[:10]) 
print("y_holdout: \n", y_holdout[:10])
print("other_prediciton: \n", other_prediciton[:10])


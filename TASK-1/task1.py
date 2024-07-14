import pandas as pd

pd.set_option('display.max_columns', None)
df = pd.read_csv("../dataset/sample.csv", sep=",")
print("Print the first row")
print(df.head(1))

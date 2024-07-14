print("------------------------  TASK 1 ------------------------------------")
import pandas as pd
pd.set_option('display.max_columns', None)
df = pd.read_csv("../dataset/sample.csv", sep=",")
print("Print the first row")
print(df.head(1))


print("------------------------ TASK 2 -------------------------------------------")
df= df.rename(columns={"VendorID":"vendor_id","RatecodeID":"ratecode_id",
              "PULocationID":"pu_location_id","DOLocationID":"do_location_id"})
print(df.dtypes)


print("------------------------- TASK 3 ------------------------------------------")
df_multiple_cols = df[["vendor_id", "passenger_count", "trip_distance", "payment_type", "fare_amount", "extra", "mta_tax", "tip_amount", 
                       "tolls_amount", "improvement_surcharge", "total_amount", "congestion_surcharge"]]
print("Selecting multiple columns")
print(df_multiple_cols.sort_values(by= "passenger_count", ascending=False).head(10))

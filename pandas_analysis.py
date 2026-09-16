import pandas as pd 

df = pd.read_csv("data/sales_data.csv")

print("Sales Data: ")
print(df)

print("\nFirst 5 rows: ")
print(df.head())

print("\nLast 5 rows: ")
print(df.tail())

print("\nData types: ")
print(df.dtypes)

print("\nData information: ")
print(df.info())

print("Statistical Analysis:")

print("Mean: ")
print(df[["Quantity","Price","Revenue"]].mean())

print("\nMedian: ")
print(df[["Quantity","Price","Revenue"]].median())

print("\nMinimum: ")
print(df[["Quantity","Price","Revenue"]].min())

print("\nMaximum: ")
print(df[["Quantity","Price","Revenue"]].max())

print("\nCount: ")
print(df[["Quantity","Price","Revenue"]].count())

electronics_df = df[df["Category"] == "Electronics"]
print("\nElectronics Products: ")
print(electronics_df) 

selected_columns = df[["Product","Quantity","Revenue"]]
print("\nSelected Columns: ")
print(selected_columns)

subset_df = df.iloc[0:5]
print("\nSubset of first 5 rows: ")
print(subset_df)

# 5. Save filtered results

electronics_df.to_csv("output/filtered_sales.csv",index=False)

electronics_df.to_excel("output/filtered_sales.xlsx",index=False)

print("\nFiltered data saved successfully")
# 5 Functions to implement:
import pandas as pd
import openpyxl as px

"""
Function 1. 
Load the Dataset from an Excel file and return a DataFrame
Parameters: `filename`: The filename of the dataset (string).
Returns a pandas dataframe with the dataset
"""
def load_data(filename):
  # read excel file:
  df = pd.read_excel(filename)
  return df

# run the function:
df = load_data('Online Retail.xlsx')
# checking:
print(df.head())
print(df.shape)


"""
Function 2. 
Clean the dataset by removing rows with missing `CustomerID` values and any negative quantities or unit prices.
Parameters: `df`: The raw dataset DataFrame.
Returns: A cleaned DataFrame.
"""
def clean_data(df):
  #make a list of the columns to pass neatly into the cleaned dataframe:
  all_cols_list = df.columns.tolist()
  # print(all_cols_list)
  # filtering OUT the null Customer Ids, NEGATIVE quantity values and NEGATIVE unit prices:
  df = df[all_cols_list][(df['CustomerID'].notnull()) & (df['Quantity'] >= 0) & (df['UnitPrice'] >= 0)]
  # checking:
  # df = df[df['Quantity'] < 0]
  # df = df[df['UnitPrice'] < 0]
  return df
# checking:
print(clean_data(df))

#make sure my df is the clean df!
df = (clean_data(df))
"""
Function 3. 
Identify the top `n` customers by total spending.
Parameters: `df`: The cleaned DataFrame, `n`: Number of top customers to return.
Returns: A DataFrame with the top `n` customers and their total spending.
"""
# checking - out of curiosity:
unique_customers = df['CustomerID'].nunique()
print(unique_customers) # returns 4372 unique customers!

def top_customers(df, n):
  # the line below does NOT multiply quantity by unit price!:
  # customer_spend = df.groupby('CustomerID')['UnitPrice'].sum()

  # I'm fairly certain I need this:
  df['spend_per_order'] = df['Quantity'] * df['UnitPrice']
  # ok this works:
  # print(df['spend_per_order'])

  # totalling the order spends for each customer:
  total_spend = df.groupby('CustomerID')['spend_per_order'].sum()
  # print(total_spend)

  # ordering total_spend:
  total_spend_sorted = total_spend.sort_values(ascending=False)
  # print(total_spend)

  #pass in n to get specified length of rows: 
  top_customers = total_spend_sorted.iloc[:n] 
  return top_customers

#checking: 
print(top_customers(df, 4))

"""
Function 4. 
Calculate total monthly sales.
Parameters: `df`: The cleaned DataFrame
Returns: A DataFrame with two columns: `month` and `total_sales`.
"""
def monthly_sales(df):
  filtered = df.




# Function 5. 
# Find the top `n` most popular products by quantity sold.
# Parameters: `df`: The cleaned DataFrame, `n`: Number of top products to return.
# Returns: A DataFrame with the top `n` products by quantity sold.
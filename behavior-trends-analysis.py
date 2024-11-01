# 5 Functions to implement:
import pandas as pd
import openpyxl as px

def import_data(filename):
    # read excel file:
    df = pd.read_excel(filename)
    # df = pd.read_csv(filename)
    return df

# run the function:
df = import_data('Online Retail.xlsx')
# checking:
print(df.head())
print(df.shape)

def filter_data(df):

    #make a list of the columns to pass into the cleaned dataframe:
    all_cols_list = df.columns.tolist()
    # print(all_cols_list)
    # filtering OUT the null Customer Ids, NEGATIVE quantity values and NEGATIVE unit prices:
    df = df[all_cols_list][(df['CustomerID'].notnull()) & (df['Quantity'] >= 0) & (df['UnitPrice'] >= 0)]
    # checking:
    # df = df[df['Quantity'] < 0]
    # df = df[df['UnitPrice'] < 0]
    return df
    # checking:
print(filter_data(df))

#make sure my df is the clean df!
df = (filter_data(df))

def loyalty_customers(df):
    #min_purchases
    orders_per_customer = df.groupby('CustomerID')['InvoiceNo'].count()
    print(orders_per_customer)

    df['purchases_number'] = df['Quantity'] * orders_per_customer

    print(df['purchases_number'])

    # orders_sorted = orders_per_customer.sort_values(ascending=False)

print(loyalty_customers(df))

def answer_conceptual_questions() -> dict:
    answers = {
        "Q1": {"A"},
        "Q2": {"B"},
        "Q3": {"C"},
        "Q4": {"C"},
        "Q5": {"B"},
    }
    return answers
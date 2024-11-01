# 5 Functions to implement:
import pandas as pd
import openpyxl as px

#Function 1.
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


# Function 2. All by myself!
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


# Function 3.  With some help from chatgpt:
def loyalty_customers(df, min_purchases):
    # I did this by myself:
    orders_per_customer = df.groupby('CustomerID')['InvoiceNo'].count()
    print(orders_per_customer)
    
    # then I got stuck here...
    # number_of_purchases = df['Quantity'] * orders_per_customer
    # ...then Chatgpt suggested I do it like this, after quite a bit of prompting..just by summing the actual quantity per customer!:
    total_quantity_per_customer = df.groupby('CustomerID')['Quantity'].sum()

    #and make them into a dataframe:
    loyalty_df = pd.DataFrame({
        'NumOrders': orders_per_customer,
        'TotalQuantity': total_quantity_per_customer
    })

    # Filter for customers with at least the minimum number of purchases - chapgpt suggested using the NumOrders but I think it needs to be this.. the total quantity per customer.
    loyal_customers = loyalty_df[loyalty_df['TotalQuantity'] >= min_purchases]

    return loyal_customers.reset_index()

print(loyalty_customers(df, 5000))

# Function 4.
def quarterly_revenue(df):
    #chat gpt suggested converting to datetime, which is good as I would otherwise have done it very long-windedly using the strings!!
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    # first need the revenue total for each row:
    df['total_revenue'] = df['Quantity'] * df['UnitPrice']

    #From Chatgpt:
    df['year'] = df['InvoiceDate'].dt.year
    df['quarter'] = df['InvoiceDate'].dt.quarter

    # use groupby to get the revenue by year and quarter, and reset the index because is is shorter:
    quarterly_revenue = df.groupby(['year', 'quarter'])['total_revenue'].sum().reset_index()

    # combining the year and quarter into one:
    quarterly_revenue['quarter'] = quarterly_revenue['year'].astype(str) + ' Q' + quarterly_revenue['quarter'].astype(str)

    # do the same thing but without the year column (gpt but I think this could be more efficient?)
    quarterly_revenue = quarterly_revenue.groupby('quarter')['total_revenue'].sum().reset_index()

    return quarterly_revenue

print(quarterly_revenue(df))

# Function 5. 
def high_demand_products(df, top_n):
    # this is actually my own code - I already wrote something very similar practising yesterday (on group 1 questions that you released yesterday) - before I ran out of steam last night! 

    # totalling the quantities for each Stock Item (product):
    product_quantities = df.groupby('StockCode')['Quantity'].sum().reset_index()
    # 
    product_quantities_sorted = product_quantities.sort_values(by='Quantity', ascending=False)

    #the number of rows are determined by 'top_n'
    top_products = product_quantities_sorted.iloc[:top_n]
    return top_products

print(high_demand_products(df, 10))


# Function 6.
def answer_conceptual_questions():
    answers = {
        "Q1": {"A"},
        "Q2": {"B"},
        "Q3": {"C"},
        "Q4": {"A"},
        "Q5": {"A"},
    }
    return answers

print(answer_conceptual_questions())

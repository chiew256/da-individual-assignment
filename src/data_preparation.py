import pandas as pd

def create_dataframes():
    customers_df = pd.DataFrame({
        'CustomerID': [101, 102, 103],
        'Name': ['John Doe', 'Jane Smith', 'Mike Jordan'],
        'Email': ['john.doe@example.com', 'jane.smith@example.com', 'mike.jordan@example.com'],
        'SignupDate': pd.to_datetime(['2023-01-10', '2023-01-15', '2023-01-20']),
        'Address': ['New York, NY, 10001, USA', 'Los Angeles, CA, 90001, USA', 'Chicago, IL, 60601, USA']
    })

    products_df = pd.DataFrame({
        'ProductID': [201, 202, 203],
        'Name': ['Laptop', 'Tablet', 'Smartphone'],
        'Category': ['Electronics', 'Electronics', 'Electronics'],
        'Price': [1000, 500, 800]
    })

    orders_df = pd.DataFrame({
        'OrderID': [301, 302, 303],
        'CustomerID': [101, 102, 103],
        'OrderDate': pd.to_datetime(['2023-02-01', '2023-02-05', '2023-02-10']),
        'ShipDate': pd.to_datetime(['2023-02-03', '2023-02-07', '2023-02-12']),
        'ShipLocation': ['New York, NY, 10001, USA', 'Los Angeles, CA, 90001, USA', 'Chicago, IL, 60601, USA']
    })

    order_details_df = pd.DataFrame({
        'OrderID': [301, 302, 303],
        'ProductID': [201, 202, 203],
        'Quantity': [1, 2, 1],
        'Discount': [0, 0.1, 0]
    })

    return customers_df, products_df, orders_df, order_details_df
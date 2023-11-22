from data_preparation import create_dataframes
from entity_creation import create_entityset
from feature_engineering import perform_feature_engineering

import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

def main():
    customers_df, products_df, orders_df, order_details_df = create_dataframes()
    print(type(customers_df), type(products_df), type(orders_df), type(order_details_df))

    es = create_entityset(customers_df, products_df, orders_df, order_details_df)
    features, feature_defs = perform_feature_engineering(es)

    # Ensure the directory exists
    os.makedirs('../outputs', exist_ok=True)
    features.to_csv('../outputs/features.csv')

if __name__ == "__main__":
    main()
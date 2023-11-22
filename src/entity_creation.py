import featuretools as ft

def create_entityset(customers_df, products_df, orders_df, order_details_df):
    # Create a new entityset to hold our entities
    es = ft.EntitySet(id='ecommerce')

    # Add entities to our entityset
    es = es.add_dataframe(customers_df, 'Customers', index='CustomerID')
    es = es.add_dataframe(products_df, 'Products', index='ProductID')
    es = es.add_dataframe(orders_df, 'Orders', index='OrderID')
    es = es.add_dataframe(order_details_df, 'OrderDetails', make_index=True, index='OrderDetailsID')

    # Define relationships between entities
    relationship_customer_order = ft.Relationship(es, 'Customers', 'CustomerID', 'Orders', 'CustomerID')
    relationship_order_orderdetails = ft.Relationship(es, 'Orders', 'OrderID', 'OrderDetails', 'OrderID')
    relationship_product_orderdetails = ft.Relationship(es, 'Products', 'ProductID', 'OrderDetails', 'ProductID')

    # # Add relationships to the entityset
    es = es.add_relationships([relationship_customer_order, relationship_order_orderdetails, relationship_product_orderdetails])

    return es
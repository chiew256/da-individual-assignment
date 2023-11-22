import featuretools as ft

def perform_feature_engineering(es):
    # Use Deep Feature Synthesis (DFS) to perform automated feature engineering
    features, feature_defs = ft.dfs(entityset=es, target_dataframe_name='Customers')

    return features, feature_defs
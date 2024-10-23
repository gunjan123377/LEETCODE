import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    data_filter = (products["low_fats"] == "Y") & (products["recyclable"] == "Y")
    return products.loc[data_filter]["product_id"].to_frame()
import pandas as pd
from products.models import ProductModel

data_file = r'C:\\Users\\TRUST\\Desktop\\CustomDataSet.xlsx'
data = pd.read_excel(data_file)

# Read rows and create productmodel objects
for index, row in data.iterrows():
    try:
        product = ProductModel(
            name=row['product_name'],
            price=row['price'],
            desc=row['description'],
            details=row['details'],
            cat=row['category'],
            image1=row['image1'],
            image2=row['image2'],
            image3=row['image3'],
            image4=row['image4']
        )
        product.save()
    except Exception as e:
        print(f"Error importing row {index}: {e}")

print("Data imported successfully!")

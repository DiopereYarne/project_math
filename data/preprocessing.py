import pandas as pd

data = pd.read_csv('dataset/dataset.csv')

# data = pd.DataFrame({
#     'name': ['John', 'Jane', 'Jack', 'John', None],
#     'age': [28, 34, None, 28, 22],
#     'purchase_amount': [100.5, None, 85.3, 100.5, 50.0],
#     'date_of_purchase': ['2023/12/01', '2023/12/02', '2023/12/01', '2023/12/01', '2023/12/03']
# 	})

#preprocessing step 1

data = data.dropna()

#preprocessing step 2
columns = ['Arrest Date', 'Booking Date']

for col in columns:
    if col in data.columns:
        data[col] = pd.to_datetime(data[col], errors='coerce')


#preprocessing step 3
columns = ['Arrest Date', 'Booking Date']


#preprocessing step 4


print(data)
data.to_csv('dataset/cleaned_dataset.csv', index=False)



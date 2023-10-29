import pandas as pd
import matplotlib.pyplot as plt
import chardet
from pandas import DataFrame

# 1. Pandas ბიბლიოთეკის საშუალებით სასურველი სვეტებისა და სტრიქონების გამოტანა
with open('spotify-2023.csv', 'rb') as f:
    result = chardet.detect(f.read())
dataFrame = pd.read_csv('spotify-2023.csv', encoding=result['encoding'])
selected_columns = dataFrame[['track_name', 'artist(s)_name']][:10]
# print(selected_columns)

# 2. ინდექსირება კონკრეტული სვეტის მიმართ
#df.set_index('track_name', inplace=False)
# print(df)

# 3. ფილტრაცია 2 პარამეტრით
count_filter = (dataFrame['artist_count'] == 2)
date_filter = (dataFrame['released_year'] == 2023)
filtered_df = dataFrame[count_filter & date_filter]
# print(filtered_df)

# 4. სორტირება 2 პარამეტრით
sorted_df = dataFrame.sort_values(by=['artist_count', 'released_year'])
# print(sorted_df[['artist_count', 'released_year']][:20])

# 5. სტატიკური ფუნქციები
number_of_days_column = dataFrame['released_day']
mean = number_of_days_column.mean()
std_dev = number_of_days_column.std()
median = number_of_days_column.median()
min = number_of_days_column.min()
# max = number_of_days_column.max()
# print(f"Mean: {mean}")
# print(f"Standard Deviation: {std_dev}")
# print(f"Median: {median}")
# print(f"Minimum: {min}")
# print(f"Maximum : {max}")

# 6. გრაფები

plt.bar(dataFrame['artist(s)_name'][:5], dataFrame['streams'][:5])
plt.xlabel('Name of Artist(s)')
plt.ylabel('Streams')
plt.title('Bar Chart of Artists')
plt.show()

plt.plot(dataFrame['artist(s)_name'][:5], dataFrame['streams'][:5], marker='o', linestyle='-')
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Line Chart of Age Over Time')
plt.grid(True)
plt.show()
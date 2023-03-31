import pandas as pd
from sklearn.linear_model import LinearRegression

# Read the data from the file
data = pd.read_csv('Model/data.txt', header=None, names=['Produced Energy', 'Consumed Energy', 'Temperature', 'Humidity', 'Date', 'Time', 'Day of Week', 'Adverse Weather', 'Special Events', 'Construction Work'])

# Convert the date and time columns to datetime format
data['Timestamp'] = pd.to_datetime(data['Date'] + ' ' + data['Time'])

# Drop the Date and Time columns
data.drop(['Date', 'Time'], axis=1, inplace=True)

# Extract some insights from the data
print('Descriptive Statistics:')
print(data.describe())

print('Correlation Matrix:')
print(data.corr())

# Split the data into training and testing sets
train_data = data[data['Timestamp'] < '2021-12-01']
test_data = data[data['Timestamp'] >= '2021-12-01']

# Train a linear regression model on the training set
X_train = train_data.drop(['Produced Energy', 'Consumed Energy', 'Timestamp'], axis=1)
y_train_consumed = train_data['Consumed Energy']
y_train_produced = train_data['Produced Energy']

lr_consumed = LinearRegression()
lr_consumed.fit(X_train, y_train_consumed)

lr_produced = LinearRegression()
lr_produced.fit(X_train, y_train_produced)

# Test the linear regression model on the testing set
X_test = test_data.drop(['Produced Energy', 'Consumed Energy', 'Timestamp'], axis=1)
y_test_consumed = test_data['Consumed Energy']
y_test_produced = test_data['Produced Energy']

y_pred_consumed = lr_consumed.predict(X_test)
y_pred_produced = lr_produced.predict(X_test)

# Calculate the mean absolute error (MAE) of the predictions
mae_consumed = abs(y_pred_consumed - y_test_consumed).mean()
mae_produced = abs(y_pred_produced - y_test_produced).mean()

print('MAE Consumed Energy:', mae_consumed)
print('MAE Produced Energy:', mae_produced)

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("Test_new.xlsx")

print(data)

data_t = data.filter(["T"])

print(data_t)
plt.title("Температа Перми с 01.01.2023 по 29.01.2023")
plt.plot(data_t)

plt.xlabel("Дата")
plt.ylabel("градусов, С")
plt.savefig("Test_new.png")

plt.show()



import pandas as pd
from geopy.geocoders import Nominatim
import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import tensorflow as tf
from tensorflow import keras


param_size = data_t
print(data.shape)
print(data.shape)

def pogoda():
        data_filter = data.filter(["T"])
        dataset = data_filter.values
        print(dataset)
        training_data_len = math.ceil(len(dataset) * .8)
        print(training_data_len)
        scaler = MinMaxScaler(feature_range=(0,1))
        print(scaler)
        scaled_data = scaler.fit_transform(dataset)
        print(scaled_data)
        train_data = scaled_data[0:training_data_len , :]
        x_train = []
        y_train = []
        for i in range(80, len(train_data)):
                x_train.append(train_data[i-80:i, 0])
                y_train.append(train_data[i, 0])
                if i <= 81:
                        #print(x_train)
                        #print(y_train)
                        print()
        x_train, y_train = np.array(x_train),np.array(y_train)
        x_train = np.reshape(x_train, (x_train.shape[0],x_train.shape[1],1))
        print(x_train.shape)
        model = Sequential()
        model.add(LSTM(50, return_sequences=True, input_shape = (x_train.shape[1],1)))
        model.add(LSTM(101, return_sequences=False))
        model.add(Dense(50))
        model.add(Dense(25))
        model.add(Dense(1))

        model.compile(optimizer='adam',loss='mean_squared_error')
        model.fit(x_train, y_train, batch_size=1,epochs=100)
        model.save("test.h5")
        test_data = scaled_data[training_data_len - 80:, :]
        x_test = []
        y_test = dataset[training_data_len:, :]
        for i in range(80, len(test_data)):
              x_test.append(test_data[i - 80:i, 0])
        x_test = np.array(x_test)
        X_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
        predictions = model.predict(X_test)
        predictions = scaler.inverse_transform(predictions)
        rmse = np.sqrt(np.mean(predictions - y_test) ** 2)
        print(rmse)
        btc_quote = data_filter
        new_df = data_filter
        last_60_days = new_df[-1:].values
        last_60_days_scaled = scaler.transform(last_60_days)
        X_test = []
        X_test.append(last_60_days_scaled)
        X_test = np.array(X_test)
        X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
        pred_price = model.predict(X_test)
        pred_price = scaler.inverse_transform(pred_price)
        print(pred_price)
        pred_price = np.array(pred_price)
        pred_price = pred_price[0]
        pred_price = pred_price[0]
        print(pred_price)
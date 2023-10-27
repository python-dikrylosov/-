import pandas as pd
from geopy.geocoders import Nominatim
import time


data1 = "Данные по метеостанциям. Соответствие МО.csv"

data2 = "Данные по метеостанциям.csv"
data3 = "ДТП.csv"
data4 = "Износ сетей по МО ПК.csv"
data5 = "ОЯ и НЯ.csv"
data6 = "Пожары.csv"
data7 = "Происшествия.csv"
data8 = "Температурная статистика.csv"

data_read_1 = pd.read_csv(data1)
data_read_mo = data_read_1["Муниципальное образование"]
data_read_ms = data_read_1["Метеорологическая станция"]

def get_address_from_coordinates(latitude, longitude):
    geolocator = Nominatim(user_agent='my-app')
    location = geolocator.reverse(f"{latitude}, {longitude}", language='ru')
    return location.address

# Создание экземпляра геокодера
geolocator = Nominatim(user_agent="my_app")

for i in range(data_read_mo.shape[0]):
    print([i,data_read_mo[i]])

    print([i,data_read_ms[i]])
    location_x = geolocator.geocode(data_read_mo[i] + ",Россия")
    print(location_x)

    location_y = geolocator.geocode(data_read_ms[i] + ",Россия")
    print(location_y)

    # Пример использования
    latitude = location_y.latitude

    longitude = location_y.longitude

    address = get_address_from_coordinates(latitude, longitude)
    print([latitude, longitude], address)

    data_read_2 = pd.read_csv(data2)
    data_read_time = data_read_2["Местное время"]
    print(data_read_time[i])
    data_read_T = data_read_2["T"]
    print(data_read_T[i])
    data_read_Po = data_read_2["Po"]
    print(data_read_Po[i])
    # data_read_tp = data_read_2["P"]
    print(data_read_T[i])
    # data_read_tp = data_read_2["P"]
    print(data_read_T[i])
    # data_read_tp = data_read_2["P"]
    print(data_read_T[i])
    # data_read_tp = data_read_2["P"]
    print(data_read_T[i])
    # data_read_tp = data_read_2["P"]
    # data_read_tp = data_read_2["P"]
    # data_read_tp = data_read_2["P"]
    # data_read_tp = data_read_2["P"]
    # data_read_tp = data_read_2["P"]
    # data_read_tp = data_read_2["P"]
    # data_read_tp = data_read_2["P"]
    # data_read_tp = data_read_2["P"]
    # data_read_tp = data_read_2["P"]
    # data_read_tp = data_read_2["P"]
    # data_read_tp = data_read_2["P"]
    # data_read_tp = data_read_2["P"]
    # data_read_tp = data_read_2["P"]
    # data_read_tp = data_read_2["P"]
    # data_read_tp = data_read_2["P"]
    # data_read_tp = data_read_2["P"]
    # data_read_tp = data_read_2["P"]
    # data_read_tp = data_read_2["P"]
    # data_read_tp = data_read_2["P"]
    # data_read_tp = data_read_2["P"]
    # data_read_tp = data_read_2["P"]
    # data_read_tp = data_read_2["P"]
    # data_read_tp = data_read_2["P"]
    # data_read_tp = data_read_2["P"]


    print(data_read_2)

    for i in range(30):
        time.sleep(1)
        print(30 - i)


data_read_2 = pd.read_csv(data2)
data_read_3 = pd.read_csv(data3)
data_read_4 = pd.read_csv(data4)
data_read_5 = pd.read_csv(data5)
data_read_6 = pd.read_csv(data6)
data_read_7 = pd.read_csv(data7)
data_read_8 = pd.read_csv(data8)

print(data_read_1.shape)
print(data_read_2.shape)
print(data_read_3.shape)
print(data_read_4.shape)
print(data_read_5.shape)
print(data_read_6.shape)
print(data_read_7.shape)
print(data_read_8.shape)



print(data_read_1)
print(data_read_2)
print(data_read_3)
print(data_read_4)
print(data_read_5)
print(data_read_6)
print(data_read_7)
print(data_read_8)


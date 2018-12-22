import serial
from filter import Filter
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

model = LinearRegression()
f = Filter(3)
l = []
threshold = 60
# reading data from Arduino
arduino = serial.Serial("COM11", 9600)
print("serial communication established")
list = []
plt.figure(1)
for i in range(50):
    a = arduino.readline()
    a = str(a)
    a = a[2:4]
    predictions = []
    indicces = []
    list = np.append(list, int(a))
    l = np.append(l, int(a))
    list = f.real_time(list)
    print(a)
    if len(list) > 10:
        x = list[i-10:i]
        y = np.arange(i - 10, i)
        model.fit(y.reshape((-1, 1)), x)
    predictions = list
    if len(list) > 10:
        for j in range(i, i + 10):
            predictions = np.append(predictions, model.predict(j))

    p3 = plt.plot(predictions)
    p1 = plt.plot(l)
    p2 = plt.plot(list)
    plt.draw()
    plt.pause(0.01)
    plt.clf()
    time=0
    if len(list)>10:
        for j in range(i+10, i+50):
            predictions = np.append(predictions, model.predict(j))
    for k,p in enumerate(predictions):
        if (p < threshold):
            time = 1.2*(k-i)
            break
    arduino.write(str(time).encode('utf-8')+b'\r\n')
    print(time)
arduino.close()

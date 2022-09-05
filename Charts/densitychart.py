import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('gyrodata.xlsx', 'Taul1')
plt.plot(df['time'], df['gyro'])


plt.xlabel("Time")
plt.ylabel("Gyro")
plt.title("Gyro data from phone")
plt.legend()
plt.show()

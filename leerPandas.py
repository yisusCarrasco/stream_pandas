import pandas as pd
import matplotlib.pyplot as plt


variable = "dataset/traj_UNI_CORR_500_01.txt"
df = pd.read_csv(variable, 
                 skiprows=4, 
                 sep="\t", 
                 names=["ID", "frames", "X", "Y", "Z"])

print(df.head())

plt.hist(df["X"], bins=40)
plt.show()
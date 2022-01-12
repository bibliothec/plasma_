import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np

#ファイルの読み込み
input_file1="2pa.csv"
input_file2="1pa.csv"
input_file3="0.5pa.csv"
encoding_type="utf-8" #file encode
try:                #get csv file
    df1 = pd.read_csv(input_file1,encoding=encoding_type)
    df2 = pd.read_csv(input_file2,encoding=encoding_type)
    df3 = pd.read_csv(input_file3,encoding=encoding_type)
except UnicodeDecodeError:
    print("encode error")
    sys.exit()

plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.direction'] = 'in'

df1*=-1
df2*=-1
df3*=-1

plt.scatter(x=df1.iloc[:,0],y=df1.iloc[:,1]/3,label="2[Pa]")
plt.scatter(x=df2.iloc[:,0],y=df2.iloc[:,1]/3,label="1[Pa]")
plt.scatter(x=df3.iloc[:,0],y=df3.iloc[:,1]/3,label="0.5[Pa]")
plt.title("Magnetron discharge",fontsize=15)
plt.xlabel("V[V]",fontsize=13)
plt.ylabel("I[A]",fontsize=13)
plt.legend()
plt.savefig("image.png")
plt.show()

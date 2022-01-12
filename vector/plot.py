import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable 
#インポート

#ファイルの読み込み
input_file="a.csv"
encoding_type="utf-8" #file encode
try:                #get csv file
    df = pd.read_csv(input_file,encoding=encoding_type)
except UnicodeDecodeError:
    print("encode error")
    sys.exit()

#データの取り出し
X = df.iloc[:,0]
Y = df.iloc[:,1]
U = df.iloc[:,3]
V = df.iloc[:,2]

#大きさを1にする
C = np.sqrt(U* U + V * V)
U=U/C
V=V/C

plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.direction'] = 'in'


#グラフの描写領域の作成
fig, ax = plt.subplots(figsize=(10, 10))

#ベクトル図の作成　
ratio=0.002
q = ax.quiver(X, Y, U*ratio, V*ratio, C , cmap="jet", angles='xy', scale_units='xy', scale=0.01,label="vector[mT]")

#設定とプロット
ax.set_xlabel('x[cm]', fontsize=10)
ax.set_ylabel('y[cm]', rotation=90, fontsize=10)
ax.set_xticks(ticks=np.arange(0,9,1))
ax.set_yticks(ticks=np.arange(0,2.5,1))
ax.set_aspect(aspect="equal")
plt.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=1, fontsize=10)
plt.title("magnetic field")
divider = make_axes_locatable(ax)
cax = divider.append_axes("right",size="5%",pad=0.1)
plt.colorbar(q,cax=cax)
plt.savefig("imgpy.png")
plt.show()

# 3D 球体绘制（Python + matplotlib）
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建3D画布
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')

# 生成球体数据
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u) * np.sin(v)
y = np.sin(u) * np.sin(v)
z = np.cos(v)

# 画球体
ax.plot_surface(x, y, z, color='lightblue')

# 显示
plt.show()
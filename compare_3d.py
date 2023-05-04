import numpy as np
import matplotlib.pyplot as plt

# 读取第一个points3D文件
with open('points3D_1.txt', 'r') as f:
    lines = f.readlines()[3:] # 跳过前三行注释
    points1 = []
    for line in lines:
        elements = line.strip().split()
        points1.append([float(e) for e in elements[1:4]])
    points1 = np.array(points1)

# 读取第二个points3D文件
with open('points3D_2.txt', 'r') as f:
    lines = f.readlines()[3:] # 跳过前三行注释
    points2 = []
    for line in lines:
        elements = line.strip().split()
        points2.append([float(e) for e in elements[1:4]])
    points2 = np.array(points2)

# 计算距离差
dist_diff = np.linalg.norm(points1 - points2, ord=2, axis=1)

# 生成x坐标
x = np.arange(1, len(points1)+1)

# 绘制图像
plt.plot(x, dist_diff)
plt.xlabel('Point ID')
plt.ylabel('Distance Difference')
plt.title('Distance Difference between Two Points3D Files')
plt.show()

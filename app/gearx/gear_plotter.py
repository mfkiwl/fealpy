import numpy as np
from fealpy.experimental.backend import backend_manager as bm
import matplotlib.pyplot as plt

# 定义渐开线的函数，增加旋转方向的控制参数 direction
def involute_curve(phi, r_b, theta_offset, direction=1):
    x = r_b * (bm.cos(direction * phi + theta_offset) + direction * phi * bm.sin(direction * phi + theta_offset))
    y = r_b * (bm.sin(direction * phi + theta_offset) - direction * phi * bm.cos(direction * phi + theta_offset))
    return x, y

def inv(alpha):
    return bm.tan(alpha)-alpha

# 参数
x = 0  # 变位系数
m = 5  # 模数
z = 22  # 齿数
alpha = 20  # 压力角
alpha = alpha/180*bm.pi

r_p = m*z  # 分度圆半径
r_b = r_p*bm.cos(alpha)  # 基圆半径
r_a = r_p + m  # 齿顶圆半径
r_f = r_p - 1.25*m  # 齿根圆半径

# 齿厚计算公式 1
# 分度圆齿厚
s = 0.5*m*bm.pi+2*m*x*bm.tan(alpha)
# 基圆齿厚
s_b = bm.cos(s+2*m*x*bm.tan(alpha)+m*z*inv(alpha))

# 齿厚计算公式 2
# 分度圆齿厚
s = 0.5*m*bm.pi+2*x*bm.tan(alpha)
# 基圆齿厚
s_b = bm.cos(s+2*m*x*bm.tan(alpha)+m*z*inv(alpha))

phi_range = bm.linspace(0, bm.pi/4, 100)  # 参数范围
theta_offsets = bm.linspace(0, 2*bm.pi, z)  # 四条渐开线的起始角度
delta_theta = s_b/np.pi/2

# 选择旋转方向: 1 为逆时针，-1 为顺时针
direction = -1  # 修改为 -1 可以得到顺时针旋转的渐开线

# 绘图
plt.figure(figsize=(8, 8))
for theta_offset in theta_offsets:
    x, y = involute_curve(phi_range, r_b, theta_offset+delta_theta, direction)
    plt.plot(x, y)


direction = 1  # 修改为 -1 可以得到顺时针旋转的渐开线

for theta_offset in theta_offsets:
    x, y = involute_curve(phi_range, r_b, theta_offset-delta_theta, direction)
    plt.plot(x, y)

# 绘制基圆
theta = bm.linspace(0, 2*bm.pi, 300)
x_circle = r_b * bm.cos(theta)
y_circle = r_b * bm.sin(theta)
plt.plot(x_circle, y_circle)

# 绘制分度圆
theta = bm.linspace(0, 2*bm.pi, 300)
x_circle = r_p * bm.cos(theta)
y_circle = r_p * bm.sin(theta)
plt.plot(x_circle, y_circle)

# 绘制齿顶圆
theta = bm.linspace(0, 2*bm.pi, 300)
x_circle = r_a * bm.cos(theta)
y_circle = r_a * bm.sin(theta)
plt.plot(x_circle, y_circle)

# 绘制齿根圆
theta = bm.linspace(0, 2*bm.pi, 300)
x_circle = r_f * bm.cos(theta)
y_circle = r_f * bm.sin(theta)
plt.plot(x_circle, y_circle)

# 图形设置
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

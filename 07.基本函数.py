import numpy as np
#计算平方根 
print(np.sqrt([1,4,9,25]))

#计算指数 e^X
print(np.exp([0,1]))

#计算自然对数 lnX
print(np.log(2))

#计算正弦值、余弦值
print(np.sin(np.pi/2))
print(np.cos(np.pi/2))

#计算绝对值
print(np.abs([-1,-2,-3]))

#计算a的b次幂
print(np.power([2,3,4,5],2))

#四舍五入round(数字，保留位数)
print(np.round([3.2,4.5,6.7]))

#向下取整(砍掉小数)
print(np.floor(4.6))

#向上取整(进一位)
print(np.ceil(5.5))

#检测缺失值NaN
print(np.isnan([1,2,3,5,np.nan]))
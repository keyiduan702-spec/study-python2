import numpy as np
#是否大于
print(np.greater([1,2,3,4,5],3))
#是否小于
print(np.less([1,2,3,4,5],3))
#是否等于
print(np.equal([1,2,3,4,5],3))
print(np.equal([1,2,3],[3,3,3]))

#逻辑与
print(np.logical_and([1,0],[1,1]))
#逻辑或
print(np.logical_or([1,0],[1,1]))
#逻辑非
print(np.logical_not([1,0]))

#检查元素是否至少有一个元素为True
print(np.any([1,0,0,0]))
#检查元素是否全为True
print(np.all([1,0,0,0]))

#自定义条件
#np.where(条件，符合条件的，不符合条件的)
#np.select(条件，返回的结果)
scores=np.array([3,6,7,8,10,1,0])
print(np.select(
    [scores<6, (scores>=6)&(scores<=8), scores>8],  # 条件列表
    ['不及格','良好','优秀'], # 结果列表
    default='未知'                       
))


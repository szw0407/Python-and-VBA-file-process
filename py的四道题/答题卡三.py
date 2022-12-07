import pandas as pd
# 从线性模型包中导入逻辑回归
from sklearn.linear_model import *

# 读取数据集，编码方式gbk
df = pd.read_csv("数据集.csv", encoding='gbk')

# y是目标数组/目标向量，是训练集的真实值
y = df["可用"]

# X是特征矩阵，这是一个二维数组
X = df[["稳定指数","成本指数"]].values

# 建立模型，训练模型
model = LogisticRegression()
model.fit(X, y)

# 进行预测，并输出预测结果
a = model.predict([[3,5]])
print(a)

# 输出模型拟合直线的一些参数
print(model.coef_,model.intercept_)


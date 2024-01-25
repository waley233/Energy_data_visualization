import pandas as pd

# 读取CSV文件
df = pd.read_csv('2021_1da.csv')

# 确保'DateTime'列是datetime类型
df['DateTime'] = pd.to_datetime(df['Date'])

# 将'DateTime'设置为索引
df.set_index('DateTime', inplace=True)

# 按月份分组并求和
monthly_sum = df.resample('M').sum()

# 重置索引，这样'DateTime'就会成为一列
monthly_sum.reset_index(inplace=True)

# 输出到新的CSV文件
monthly_sum.to_csv('2021_1_monthly_sum.csv', index=False)

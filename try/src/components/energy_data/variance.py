import pandas as pd

# 步骤1：从CSV文件读取数据
df = pd.read_csv('2021_3.csv')

# 步骤2：将DateTime列转换为pandas的datetime类型
df['Time'] = pd.to_datetime(df['Time'],format='%d/%m/%Y %H:%M')

# 步骤3：将DateTime设置为索引
df.set_index('Time', inplace=True)

# 步骤4：按月对数据进行重采样，并计算方差
monthly_variance = df.resample('M').var()

# 步骤5：将结果输出到新的CSV文件
monthly_variance.to_csv('2021_3mv.csv')

print('Monthly variance has been calculated and saved to monthly_variance.csv.')

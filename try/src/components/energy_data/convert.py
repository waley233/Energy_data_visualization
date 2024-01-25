import pandas as pd

# 读取CSV文件
df = pd.read_csv('2021_3.csv')  # 替换为你的文件名

# 检查表头，这里假设第一行是表头
header = df.columns.tolist()

# 假设第一列是日期时间信息，将其解析为日期时间对象，并只保留日期部分
df['Date'] = pd.to_datetime(df[header[0]], format='%d/%m/%Y %H:%M').dt.date

# 确保第二列和第三列是数值类型
for col in header[1:3]:  # 假设数据在第二列和第三列
    df[col] = pd.to_numeric(df[col], errors='coerce')

# 根据日期对数值数据进行分组，并计算每组的平均值
daily_average = df.groupby('Date').agg({header[1]: 'mean', header[2]: 'mean'})

# 重置索引，这样日期就回到了DataFrame的一列
daily_average.reset_index(inplace=True)

# 使用原始的列名（除了第一列，它现在是'Date'）
new_header = ['Date'] + header[1:3]

# 修改列名，以匹配原始的表头
daily_average.columns = new_header

# 将结果保存到新的CSV文件中，并保留表头
daily_average.to_csv('2021_3da.csv', index=False)

import pandas as pd

# 替换为你的 CSV 文件路径
file_path = '20162017_3.csv'

# 读取 CSV 文件，假设第一列是日期时间信息，并没有列名
df = pd.read_csv(file_path, header=0)
# 假设第一列包含日期时间信息，我们给它命名为 'DateTime'
df.rename(columns={df.columns[0]: 'DateTime'}, inplace=True)

# 将 'DateTime' 列转换为 datetime 类型
# 注意，这里的 format 参数必须与你的数据中的日期时间格式匹配
df['DateTime'] = pd.to_datetime(df['DateTime'], format='%d/%m/%Y %H:%M')

# 现在我们使用 'DateTime' 列来分割文件
years = df['DateTime'].dt.year.unique()
for year in years:
    # 筛选该年份的数据
    df_year = df[df['DateTime'].dt.year == year]
    # 保存到新的 CSV 文件中，文件名包含年份
    df_year.to_csv(f'{year}_3.csv', index=False)

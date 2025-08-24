import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv(r"D:\sql-projects\hr-analytics-project\HR-Employee-Attrition.csv", encoding='latin1')

# Ensure all numeric types are compatible with MySQL
for col in df.select_dtypes(include=['uint64']).columns:
    df[col] = df[col].astype('int64')

engine = create_engine("mysql+mysqlconnector://root:28012002@localhost:3306/real_work")

# Export
df.to_sql(name='hr-analytics', con=engine, index=False, if_exists='replace', method='multi')
print("Data successfully exported to MySQL!")

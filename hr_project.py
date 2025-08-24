import pandas as pd
from sqlalchemy import create_engine

username = 'root'
password = '28012002'
host = 'localhost'
database = 'real_work'

engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@{host}/{database}")

query_avg_salary = """
SELECT Department, ROUND(AVG(MonthlyIncome), 2) AS avg_salary
FROM hr_analytics
GROUP BY Department;    """

df_avg_salary = pd.read_sql(query_avg_salary, engine)
print(df_avg_salary)
df_avg_salary.to_csv("D:/sql-projects/hr-analytics-project/avg_salary_by_department.csv", index=False)

query_attrition_rate = """
SELECT 
ROUND((SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)/COUNT(*))*100, 2) AS attrition_rate
FROM hr_analytics
;    """

df_attrition_rate = pd.read_sql(query_attrition_rate, engine)
print(df_attrition_rate)
df_attrition_rate.to_csv("D:/sql-projects/hr-analytics-project/attrition_rate.csv", index=False)

query_gender_ratio = """
SELECT Department, 
    SUM(CASE WHEN Gender = 'Male' THEN 1 ELSE 0 END) AS male_count,
    SUM(CASE WHEN Gender = 'Female' THEN 1 ELSE 0 END) AS female_count
FROM hr_analytics
GROUP BY Department;    """

df_gender_ratio = pd.read_sql(query_gender_ratio, engine)
print(df_gender_ratio)
df_gender_ratio.to_csv("D:/sql-projects/hr-analytics-project/gender_ratio.csv", index=False)

query_avg_years = """
SELECT Department, ROUND(AVG(YearsAtCompany),2) AS avg_years
FROM hr_analytics
GROUP BY Department;    """

df_avg_years = pd.read_sql(query_avg_years, engine)
print(df_avg_years)
df_avg_years.to_csv("D:/sql-projects/hr-analytics-project/gender_ratio.csv", index=False)
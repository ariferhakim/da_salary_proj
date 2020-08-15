import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

# salary parsing


# salary parsing
df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

df['min_salary'] = minus_Kd.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_Kd.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

# Company name text only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)

# state field
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[-1])
df['job_state'] = df['job_state'].apply(lambda x: x.replace('California',' CA').replace('Illinois',' IL').replace('New York State',' NY').replace('New Jersey',' NJ').replace('Utah',' UT').replace('United States',' DC').replace('Remote',' RT'))
df['job_state'] = df['job_state'].apply(lambda x: x.replace(' ',''))
# df.sql.value_counts()

# age of company
df['age'] = df.Founded.apply(lambda x: x if x <1 else 2020 - x)

# parsing of job desc (python, etc.)
df['Job Description'][0]

# python
df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
# r studio
df['r'] = df['Job Description'].apply(lambda x: 1 if 'r studo' in x.lower() or 'r-studio' in x.lower() else 0)
# spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
# aws
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
# excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
# sql
df['sql'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)

df_out = df.drop('Headquarters', axis = 1)
df_out = df_out.drop('Competitors', axis = 1)

df_out.to_csv('salary_data_cleaned.csv', index = False)

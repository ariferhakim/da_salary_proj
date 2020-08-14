import glassdoor_scraper as gs 
import pandas as pd 

path = "C:/Users/arifi/Documents/da_salary_proj/chromedriver"

df = gs.get_jobs('data analyst',70, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)
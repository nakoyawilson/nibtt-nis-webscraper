import requests
import pandas as pd

url = "https://www.nibtt.net/Contribution_Rates/cont_Sept05_2016.htm"
data = requests.get(url)

# This parses all the tables in webpages to a list
df_list = pd.read_html(data.text) 
df = df_list[0]

# Save as csv file
df.to_csv("data.csv")

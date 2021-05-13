import pandas as pd

##  website to scrapping    ##
url = 'https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US%3Aen'

##  "read_html" method of the Pandas library to read the HTML tables    ##
df_list = pd.read_html(url)

##  output number of tables on webpage  ##
# print(len(df_list))

##  in case there are multiples tables, we can select table with [table_number]  ##
# print(df_list)

##  creating a .txt file with table data scrapped from website    ##
with open('data_scrapped.txt', 'a') as file:
    file.write(str(df_list))
    file_save = df_list.append(file)

from bs4 import BeautifulSoup
import pandas as pd

with open('Top 250 Movies - IMDb.html') as file:
    soup = BeautifulSoup(file)

df_list = list()
for i in range(0,250):
    rank = soup.find_all('td',class_="titleColumn")[i].contents[0].strip()[0]
    title = soup.find_all('td',class_='titleColumn')[i].contents[1].contents[0]
    rating = soup.find_all('td',class_='ratingColumn imdbRating')[i].contents[1].contents[0]
    count_of_ratings = str(soup.find_all('td',class_='ratingColumn imdbRating')[i].contents[1])[28:37].replace(",","")
    df_list.append({'Rank': rank,'Title':title,'Rating':rating,'Count of Ratings':count_of_ratings})

df = pd.DataFrame(df_list, columns=("Rank","Title","Rating","Count of Ratings"))
df.head()

df.to_csv('IMDB_TOP_250.csv',index=False)

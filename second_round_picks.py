from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# url that we are scraping
base_url = "http://www.basketball-reference.com/draft/NBA_{year}.html"

draft_df = pd.DataFrame()

second_round_numbers = list(range(31,61))
second_round_numbers = [str(x) for x in second_round_numbers]

for year in range(2004, 2015):  # for each year
    url = base_url.format(year=year)  # get the url
    
    html = urlopen(url)  # get the html
    soup = BeautifulSoup(html, 'html5lib') # create our BS object
    
    column_headers = [th.getText() for th in soup.findAll('tr', limit=2)[1].findAll('th')]
    column_headers.remove('Rk') # Rk does not get caught by player data
    
    # get our player data
    data_rows = soup.findAll('tr')[2:] 
    player_data = [[td.getText() for td in data_rows[i].findAll('td')] for i in range(len(data_rows))]
    
    # replace '' with 0
    for i in player_data:
        i[:] = [0 if x=='' else x for x in i]
    
    # remove empty data
    counter = 0
    length = len(player_data)
    while counter < length:
        if player_data[counter] == []:
            player_data.remove(player_data[counter])
            # as an element is removed
            # so decrease the length by 1
            length = length - 1  
            # run loop again to check element
            # at same index, when item removed 
            # next item will shift to the left 
            continue
        counter = counter + 1
    
    # only access 2nd rounders
    player_data = [x for x in player_data if x[0] in second_round_numbers]
        
    # Turn yearly data into a DataFrame
    year_df = pd.DataFrame(player_data, columns=column_headers)
    # create and insert the Draft_Yr column
    year_df.insert(0, 'Draft Year', year)
    
    # Append to the big DataFrame
    draft_df = draft_df.append(year_df, ignore_index=True)


# Convert data to proper data types
draft_df = draft_df.infer_objects()

# Get rid of the rows full of null values
draft_df = draft_df[draft_df.Player.notnull()]

# Replace NaNs with 0s
draft_df = draft_df.fillna(0)

# Rename Columns
draft_df.rename(columns={'WS/48':'WS_per_48'}, inplace=True)

# Change % symbol
draft_df.columns = draft_df.columns.str.replace('%', '_Perc')

# Add per_G to per game stats
draft_df.columns.values[15:19] = [draft_df.columns.values[15:19][col] + 
                                  "_per_G" for col in range(4)]

draft_df.infer_objects()
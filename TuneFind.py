from bs4 import BeautifulSoup as bs
import requests

season_num  = 'season-3'
series_name = '/show/entourage'

tune_url = 'http://www.tunefind.com'

complete_url = tune_url + series_name + '/' + season_num

rseries = requests.get(complete_url)

soup_series = bs(rseries.content, 'lxml')

for link in soup_series.findAll('a', {'class': 'EpisodeListItem__songCount___geE8l'}): 
    episodes = link['href']
    print episodes
		
    episode_link = tune_url + episodes
    repisodes    = requests.get(episode_link)
    soup_episodes = bs(repisodes.content, 'lxml')
        
    for (songs_link, artist_link) in zip(soup_episodes.findAll('a', {'class': 'SongTitle__link___2OQHD'}), soup_episodes.findAll('div', attrs={'class': 'SongRow__subtitle___2q0h5'})):
        songs  = songs_link['title'].encode('utf-8')
        artist = artist_link.text.encode('utf-8')

        ysearch = songs + ' ' + artist
        print ysearch
        
        with open("test.txt", "a") as myfile:
            myfile.write(ysearch)
            myfile.write("\n")
            


        

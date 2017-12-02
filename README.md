# Canadian News Twitter Scraper
### SYDE 212 Project
#### Dominic Dotzert, Hanna Kyowski, Tara Yuen, Sam Yuyitung


On November 9th 2017, Twitter doubled their character limit to 280 characters

Did Canadian news outlets take advantage of this?


### Prereq

Built with python 2.7.x (probs wont work on python 3.6)

### Usage of script

1. __dependancies__  
This uses the tweepy python library. This can be downloaded through pip with
```
pip install -r requirements.txt
```

2. __Twitter auth__  
This relies on the twitter api, create then enter your twitter consumer keys in the `auth.py.example` file then rename it to just `auth.py`

3. __accounts__  
Input all desired accounts into the `all_accounts` array within the accounts.py file

4. __run__  
Run the main file tweets.py

### Outputs

All tweets will be stored in a csv file called `<account>_tweets.csv` with the following information

```
date,text
```


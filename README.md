# wordcloud
Wordcloud for kakaotalk chat log

## Requirements
* Python >= 3.6.0

## Run
Before running, you should export the kakaotalk chat log and put it in `log/` directory.
It will find the latest log file and make wordcloud for that

```shell
pip install -r requirements.txt
python3 make_wordcloud.py
```

## Todo
* [X] Provides simple log handlers for reading the chat log  from csv format
* [ ] We have to preprocess the chat log data for removing the useless words
* [ ] Render the wordcloud on web page using D3 like library instead of manual rendering on local environment
* [ ] Supports the chat log caching for reusing
* [ ] Provides time series weekly/montly hot keywords wordclouds
* [ ] Provides public github pages for viewing the wordcloud easily on web
* [ ] Supports auto updating the entire wordcloud when log file be updated
* [ ] We will make this as a tiny framework for drawing the wordcloud for kakaotalk chats
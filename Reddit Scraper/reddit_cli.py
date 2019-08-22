import requests,praw,time,os
from IPython.display import clear_output

reddit=praw.Reddit(client_id='yourid',client_secret='yoursecret',user_agent='yourusername')

while True:
	i=1
	try:
		sub=reddit.subreddit('News').hot(limit=None)
		for post in sub:
			#print('#',post.title.upper(),'\n>',post.comments[0].body,sep=' ')
			print('#',post.title.upper(),sep=' ')
			i+=1
			time.sleep(10)
			clear_output(wait=True)
			os.system('cls')
	except (IndexError,EOFError):
		continue
	except KeyboardInterrupt:
		break
	

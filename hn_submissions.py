import requests
from operator import itemgetter
from plotly.graph_objs import Bar
from plotly import offline

#Make API call and store the reponse
url ='https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

#Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    #Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
    
    #Build a dictionary for each articule
    #Some posts haven't key "descendants"
    try:        
        submission_dict = {
                'title': response_dict['title'],
                'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
                'comments': response_dict['descendants'],
                'missing_comments': False,
                'author': response_dict['by']
            }
    except KeyError:        
        submission_dict['comments'] = 0
        submission_dict['missing_comments'] = True
    
    submission_dicts.append(submission_dict)
    
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

titles, n_comments, labels = [], [], []
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Dicussion link: {submission_dict['hn_link']}")
    
    #Display number of comments if there have some of them
    if submission_dict['missing_comments'] == False:
        msg_comments = submission_dict['comments']
    else:
        msg_comments = "Missing info"        
    
    print(f"Comments: {msg_comments}")
    
    #Get info of posts.
    label = f"By: {submission_dict['author']}"
    labels.append(label)
    
    title =  f"<a href='{submission_dict['hn_link']}'>{submission_dict['title']}</a>"
    
    titles.append(title)
    n_comments.append(submission_dict['comments'])
    


#Make visualization.
data =[{
    'type': 'bar',
    'x': titles,
    'y': n_comments,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        },
    'opacity': 0.6,
    }]

my_layout = {
    'title': 'Most commented post on Hacker News',
    'titlefont': {'size': 28},
    'xaxis':{
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
    'yaxis':{
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
    }

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hacker_news_homepage.html')




# coding: utf-8
import pandas  as pd
uname = ['user_id','gender','age','occupation','zip']
users = pd.read_table('pydata-book/ch02/movielens/users.dat',sep='::',header=None,names=unames)
uname
unames = ['user_id','gender','age','occupation','zip']
users = pd.read_table('pydata-book/ch02/movielens/users.dat',sep='::',header=None,names=unames)
users = pd.read_table('pydata-book/ch02/movielens/users.dat',sep='::',header=None,engine='python',names=unames)
rnames = ['user_id','movie_id','rating','timestamp']
mnames=['movie_id','title
mnames=['movie_id','title','genres']
ratings = pd.read_table('pydata-book/ch02/movielens/ratings.dat',sep='::',header=None,engine='python',names=unames)
movies = pd.read_table('pydata-book/ch02/movielens/movies.dat',sep='::',header=None,engine='python',names=unames)
users[:5]
ratins[:5]
ratings[:5]
ratings = pd.read_table('pydata-book/ch02/movielens/ratings.dat',sep='::',header=None,engine='python',names=rnames)
movies = pd.read_table('pydata-book/ch02/movielens/movies.dat',sep='::',header=None,engine='python',names=mnames)
ratins[:5]
ratings[:5]
movies[:5]
ratings
data = pd.merge(pd.merge(ratings,users),movies)
data
data.ix[0]
mean_ratings = data.pivot_table('rating',rows='title',cols='gender',aggfunc='mean')
mean_ratings = data.pivot_table('rating',row='title',cols='gender',aggfunc='mean')
mean_ratings = data.pivot_table('rating',rows='title',cols='gender',aggfunc='mean')
mean_ratings = data.pivot_table('rating',index='title',columns='gender',aggfunc='mean')
mean_ratings[:5]
rating_by_title = data.groupby('title').size()
rating_by_title
active_titles=rating_by_title.index[rating_by_title >= 250]
active_title
active_titles
mean_ratings = mean_ratings.ix[active_titles]
mean_ratings
top_female_ratings = mean_ratings.sort_index(by='F',ascending=False)
top_female_ratings = mean_ratings.sort_value(by='F',ascending=False)
top_female_ratings = mean_ratings.sort_values(by='F',ascending=False)
top_female_ratings
top_female_ratings[:10]
top_male_ratings = mean_ratings.sort_values(by='M',ascending=False)
top_male_ratings[:10]
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F]
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_values(by='diff')
sorted_by_diff[:15]
sorted_by_diff[::-1][:15]
rating_std_by_title = data.groupby('title')['rating'].std()
rating_std_by_title = rating_std_by_title.ix[active_titles]
rating_std_by_title.order(ascending=False)[:10]
get_ipython().magic(u'save -a MoviveRating 1-52')

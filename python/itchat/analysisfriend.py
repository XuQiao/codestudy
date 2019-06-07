#coding=utf-8
import itchat, json, pandas, os
from geopy.geocoders import Nominatim
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

itchat.auto_login(enableCmdQR=2, hotReload=True)
def get_users(chatroomUserName=''):
#    chatroom = itchat.update_chatroom(chatroom['UserName'])
#    itchat.get_chatrooms(update=True)
    chatrooms = itchat.search_chatrooms(chatroomUserName);
    if chatrooms and chatroomUserName:
        return chatrooms[0]['MemberList']
#        for friend in chatroom['MemberList']:
#            yield friend
    else:
        friend = itchat.get_friends(update=True)
        return friend

def save_json(friends, filename):
    with open(filename, 'w') as f:
        json.dump(friends,f)

def convertgeo(city):
    geolocator = Nominatim()
    location = geolocator.geocode(city)
    if location:
        return list(location.latitude, location.longitude)
    else:
        return None

def analysis(filename):
    with open(filename, 'r') as f:
        friends = json.load(f)
        df = pandas.DataFrame(friends)
        df.to_csv(filename.replace('json','csv'),sep='\t',encoding='utf-8')
#        print(df.groupby(['City','Sex']).value_counts())
        print(df['City'].value_counts()[:30])
#        print df
#        for friend in friends:
#            print("%s: %s" % (friend.get('NickName'),friend.get('Sex')))

# Create a map on which to draw.  We're using a mercator projection, and showing the whole world.
	m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')
# Draw coastlines, and the edges of the map.
	m.drawcoastlines()
	m.drawmapboundary()
# Convert latitude and longitude to x and y coordinates
	x, y = m(covertgeo(df[0]['City']))
#                list(airports["longitude"].astype(float)), list(airports["latitude"].astype(float)))
# Use matplotlib to draw the points onto the map.
	m.scatter(x,y,1,marker='o',color='red')
# Show the plot.
	plt.show()

def main():
#    chatroomUserName = 'USTC-AAGNY-Summit'
    chatroomUserName = 'ridge'
    filename = 'friendlist_%s.json' % chatroomUserName
    if not (os.path.isfile(filename) and os.stat(filename).st_size):
        friends = get_users(chatroomUserName)
        print('Total %s friends' % len(friends))
        save_json(friends, filename)
    analysis(filename)

if __name__ == "__main__": main()

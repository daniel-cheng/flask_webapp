import os, json, urllib2
from flask import Flask, render_template, request
from forms import ChannelForm
 
 # Create Flask instance using current shell name (this allows running on both your computer and on a server)
app = Flask(__name__)
YOUR_API_KEY = "AIzaSyCvmUuH7_MNaGQG5Sxbb6jhyVTa_5aLCA8"
# .route Decorator function creates the actual URL structure of the site - see example below for adding additional pages

@app.route('/', methods=['GET','POST'])
def CostlyBanana():
    form = ChannelForm(request.form)
    data = ""
    data2= ""
    if request.method == 'POST':
        #get channel, channel url
        channelname = form.channelname.data
        url = "https://www.googleapis.com/youtube/v3/search?part=snippet&q={channelname}&type=channel&key={api_key}".format(channelname=channelname,api_key=YOUR_API_KEY)
        data = json.load(urllib2.urlopen(url))

        #gets channel id, and channel title/video url
        channelId = data['items'][0]['snippet']['channelId']
        channel = "https://www.googleapis.com/youtube/v3/activities?part=snippet&channelId={channelId}&key=AIzaSyCvmUuH7_MNaGQG5Sxbb6jhyVTa_5aLCA8".format(channelId=channelId)
        data2 = json.load(urllib2.urlopen(channel))

        #



    #channelName = data['items'][0]['statistics']['viewCount']
    #thumbnail = data['items'][0]['snippet']['thumbnails']['medium']['url']
    return render_template('home.html', data=data, form=form,data2=data2)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

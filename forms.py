from wtforms import Form, TextField

class ChannelForm(Form):
    channelname = TextField('Channel name')

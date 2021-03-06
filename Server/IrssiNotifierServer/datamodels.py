import json
from google.appengine.ext import db

class IrssiUser(db.Model):
    user_name = db.StringProperty()
    email = db.StringProperty()
    user_id = db.StringProperty()
    api_token = db.StringProperty()
    registration_date = db.IntegerProperty()
    notification_count = db.IntegerProperty()
    last_notification_time = db.IntegerProperty()
    irssi_script_version = db.IntegerProperty()


class GcmToken(db.Model):
    gcm_token = db.StringProperty()
    enabled = db.BooleanProperty()
    name = db.StringProperty()
    registration_date = db.IntegerProperty()


class Message(db.Model):
    server_timestamp = db.IntegerProperty(indexed=True)
    message = db.TextProperty()
    channel = db.StringProperty()
    nick = db.StringProperty()
    def ToJson(self):
        return json.dumps({'server_timestamp': '%f' % self.server_timestamp, 'message': self.message, 'channel': self.channel, 'nick': self.nick, 'id': self.key().id()})
    def ToGcmJson(self):
        m = json.dumps({'server_timestamp': '%f' % self.server_timestamp, 'message': self.message, 'channel': self.channel, 'nick': self.nick, 'id': self.key().id()})
        if len(m) < 3072:
            return m
        return json.dumps({'server_timestamp': '%f' % self.server_timestamp, 'message': 'toolong', 'channel': self.channel, 'nick': self.nick, 'id': self.key().id()})


class AuthKey(db.Model):
    gcm_authkey = db.StringProperty()

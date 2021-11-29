from hashlib import sha1
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
from requests import request
import hmac, time, base64, json, os

class Auth():
    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    def get_auth_header(self):
        xdate = format_date_time(mktime(datetime.now().timetuple()))
        hashed = hmac.new(self.app_key.encode('utf8'), ('x-date: ' + xdate).encode('utf8'), sha1)
        signature = base64.b64encode(hashed.digest()).decode()

        authorization = 'hmac username="' + self.app_id + '", ' + \
                        'algorithm="hmac-sha1", ' + \
                        'headers="x-date", ' + \
                        'signature="' + signature + '"'
        return {
            'Authorization': authorization,
            'x-date': format_date_time(mktime(datetime.now().timetuple())),
            'Accept - Encoding': 'gzip'
        }


def get_last(data, keys):
    tmp = data
    try:
        for index in keys:
            tmp = tmp[index]
        return tmp
    except Exception:
        return 0


class Bus(Auth):
    def __init__(self, app_id, app_key, routeID):
        super().__init__(app_id, app_key)
        self.app_id = app_id
        self.app_key = app_key
        self.routeID = routeID

    def url_req(self, url):
        response = request('get', url, headers = self.get_auth_header())
        stopData = response.json()
        self.stopData = stopData
        return stopData

    def busDict(self, dicts, setting):
        return {
                get_last(row, dicts): get_last(row, setting)
                for row in self.stopData
                if row['RouteID'] == self.routeID
               }
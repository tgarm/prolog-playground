from pydantic import BaseModel

import redis
import json
import base64

class Prog(BaseModel):
    name = 'unnamed'
    rules = 'none'
    query = 'none'
    def save():
        key = name2Key(self.name)
        rd.set(key,self.json())

rd = redis.Redis(host='localhost', port=6379, db=0)

key_prefix = 'pl-'

def name2Key(name):
    b = base64.b64encode(name.encode('utf-8')).decode('utf-8')
    return "pl-{}".format(b)

def key2Name(key):
    kd = key.decode('utf-8')
    plen = len(key_prefix)
    if(kd.startswith(key_prefix)):
        n = kd[plen:]
        name = base64.b64decode(n).decode('utf-8')
        return name
    return None


def load(name):
    key = name2Key(name)
    val = rd.get(key)
    return json.loads(val)

def removePrefix(lst):
    new_list = []
    for key in lst:
        name = key2Name(key)
        if name!=None:
            new_list.append(name)
    return new_list

def list():
    ls = rd.keys("pl-*")
    nls = removePrefix(ls)
    return nls

def listAll():
    ls = rd.keys("pl-*")
    ps = []
    for key in ls:
        p = json.loads(rd.get(key))
        ps.append(p)
    return ps

from fastapi import FastAPI
import prog
import json

app = FastAPI()

def removePrefix(lst):
    new_list = []
    for key in lst:
        name = key2Name(key)
        if name!=None:
            new_list.append(name)
    return new_list

@app.get('/list')
async def list():
    ls = prog.list()
    res = {'list':ls,'res':'ok'}
    return res

@app.get('/list-all')
async def listAll():
    return prog.listAll()

@app.post('/prog')
async def new_prog(p: prog.Prog):
    p.save()
    return {'res':'ok'}

@app.get('/prog/{prog_name}')
async def read_prog(prog_name):
    p = prog.load(prog_name)
    return {'res':'ok','prog':p}

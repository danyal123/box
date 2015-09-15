# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:25:11 2015
@author: dhussai
"""
#curl "https://api.box.com/2.0/folders/folder_id/items?limit=100&offset=0" -H "Authorization: Bearer access token" -i -s
# the line above when used in curl will give folder ids and file ids that can be used in the functions defined 
from __future__ import print_function, unicode_literals
from boxsdk import Client, OAuth2
from boxsdk.network.default_network import DefaultNetwork
from boxsdk.exception import BoxAPIException
from boxsdk.object.collaboration import CollaborationRole
from boxsdk.object import file,metadata
from boxsdk.object.folder import Folder
from boxsdk.session.box_session import BoxSession
from boxsdk.object.events import Events
from boxsdk.object.item import Item
import pycurl,re,os,sys,json
import boto,unittest,StringIO

class Test:
    def __init__(self):
        self.contents = ''
    def body_callback(self, buf):
        self.contents = self.contents + buf
sys.stderr.write("Testing %sn" % pycurl.version)

#User variables
client_id= "client_id"
client_secret= "client_secret"
parent_folder= "4308645477"
def create_subfolders(folder_ID):
    client.folder(folder_id=folder_ID).create_subfolder("Incoming")
    client.folder(folder_id=folder_ID).create_subfolder("Rejected")
def create_branch(seed_branch):
    client.folder(folder_id=seed_branch).create_subfolder("Test")
    client.folder(folder_id=seed_branch).create_subfolder("QA")
    client.folder(folder_id=seed_branch).create_subfolder("Production")
    client.folder(folder_id=seed_branch).create_subfolder("Development")
def create_parentfolders(folder_name_parent):
    list_of_vendors=client.folder(folder_id='4308645477').create_subfolder(folder_name_parent)
    return list_of_vendors
def movefile(file_ID,folder_ID):
    client.file(file_id=file_ID).move(client.folder(folder_id=folder_ID))
def rename(file_ID,new_name):
    client.file(file_id=file_ID).rename(new_name)
def delete(folder_ID):
    client.folder(folder_id=folder_ID).delete()
##the regex can be changed prn user requirments i used commas just as an example the regex module can also be used  
def ids(folder_id):
    t = Test()
    c = pycurl.Curl()
    c.setopt(c.URL, (str("https://api.box.com/2.0/folders/%s")%(folder_id)))
    c.setopt(pycurl.HTTPHEADER, ['Authorization: Bearer QU37ay7GmyMFKnZuBgJWvWkIcpWii0BP'])
    c.setopt(c.WRITEFUNCTION, t.body_callback)
    c.perform()
    c.close()
    contents=(t.contents)
    #print(contents)
    jsondict=(json.JSONDecoder().decode(contents))
    collect=(jsondict['item_collection'])
    ids= (collect['entries'])
    dicts={}
    vendor_ids=[]
    for k in ids[0]: 
        if k == None :
            break 
        dicts[k]=[d[k]for d in ids]
    name=dicts["name"]
    vendor_ids=dicts["id"]
    return vendor_ids,name
def info(file_id):
    info=client.file(file_id=file_id).content()
    return (info)
#create metadata 
def metatcreate(file_id,key,value):
    client.file(file_id=file_id).metadata().create({key: value})
#get metadata 
def meta(file_id):
    meta_data=client.file(file_id=file_id).metadata().get()
    return meta_data
#   print (meta_data)
#updata meta data 
def up_meta(file_id):
    metadata = client.file(file_id=file_id).metadata()
    update = metadata.start_update()
    update.add('/key', 'new_value')
    metadata.update(update)
    return metadata
def whatis_infolder(folder_id):
    folder = client.folder(folder_id= folder_id).get()
    ('folder name: ' + folder['name'])
    #the limit can be set according to requirements 
    items = folder.get_items(limit=100, offset=0)
    for item in items:
       print("   " + item.name)
    return folder
def download(file_id):
    with open('C:\\Users\\dhussai\\Desktop\\down_box\\read.txt','wb') as open_file:
        client.file(file_id).download_to(open_file)
def event():
    t = Test()
    c = pycurl.Curl()
    c.setopt(c.URL,"https://api.box.com/2.0/events?stream_position=1442347448411")
    c.setopt(pycurl.HTTPHEADER, ['Authorization: Bearer QU37ay7GmyMFKnZuBgJWvWkIcpWii0BP'])
    c.setopt(c.WRITEFUNCTION, t.body_callback)
    c.perform()
    c.close()
    events=(t.contents)
    jsond=(json.JSONDecoder().decode(events))
    return jsond
oauth2 = OAuth2("68akmqusbktx65oelq9n6e166rmqw8el", "iE96DxCTUfw6USg3GsU7opw5hWArXtam", access_token="QU37ay7GmyMFKnZuBgJWvWkIcpWii0BP")
client = Client(oauth2)
my_jnj_box = client.user(user_id='me').get()
print('user_login: ' + my_jnj_box['login'])
vendor_ids,name=ids("4308645477")
#print(vendor_ids)
def tree():
    create_parentfolders("vendor")
    vendor_ids,name=ids(parent_folder)
    seed=vendor_ids[-1]
    create_subfolders(seed)
    seed_branch,names= ids(seed)
    ID_incoming= seed_branch[0]
    create_branch(ID_incoming)
tree()

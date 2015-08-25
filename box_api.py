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
# User variables
client_id= "client_id"
client_secret= "client_secret"

def create_subfolders(folder_ID,folder_name):
    client.folder(folder_id=folder_ID).create_subfolder(folder_name)
    
def create_parentfolders(folder_name_parent):
    client.folder(folder_id='0').create_subfolder(folder_name_parent)
    
def movefile(file_ID,folder_ID):
    client.file(file_id=file_ID).move(client.folder(folder_id=folder_ID))
    
def rename(file_ID,new_name):
    client.file(file_id=file_ID).rename(new_name)
    
def delete(folder_ID):
    client.folder(folder_id=folder_ID).delete()
##the regex can be changed prn user requirments i used commas just as an example the regex module can also be used  
def info(file_id):
    info=client.file(file_id=file_id).content()
    for i in info :
        if i == ",":
            print ('\n')
        elif i==i:
            print(i, end="")
def metatcreate(file_id,key,value):
    client.file(file_id=file_id).metadata().create({key: value})

def meta(file_id):
    meta_data=client.file(file_id=file_id).metadata().get()
    print (meta_data)

def up_meta():
    metadata = client.file(file_id='file_id').metadata()
    update = metadata.start_update()
    update.add('/key', 'new_value')
    metadata.update(update)
##user will have to look up access token
oauth2 = OAuth2("client_id", "client_secret", access_token="access_token")
#client = Client(oauth2)
my_jnj_box = client.user(user_id='me').get()
print('user_login: ' + my_jnj_box['login'])

root_folder = client.folder(folder_id= '0').get()
print ('folder name: ' + root_folder['name'])
## the limit can be set according to requirements 
items = root_folder.get_items(limit=10, offset=0)
print('This is up to the first 10 items in the root folder in JNJ Box:')
for item in items:
    print("   " + item.name)




    

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:25:11 2015

@author: dhussai
"""
##https://app.box.com/api/oauth2/authorize?response_type=code&client_id=68akmqusbktx65oelq9n6e166rmqw8el&redirect_uri=YOUR_REDIRECT_URI&state=security_token%q8oO4z6sdkoG3wuoVS65QXxb5QpPHyFe


#curl "https://api.box.com/2.0/folders/4248601869/items?limit=100&offset=0" -H "Authorization: Bearer LPTtWkOd1Pl9Yr3Rhv6XV5ytYZVnMG4S" -i -s

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
    metadata = client.file(file_id='35169481403').metadata()
    update = metadata.start_update()
    update.add('/key', 'new_value')
    metadata.update(update)
oauth2 = OAuth2("68akmqusbktx65oelq9n6e166rmqw8el", "iE96DxCTUfw6USg3GsU7opw5hWArXtam", access_token="nVB4iG6xIiRfrBNmJ8cSNERchjDNB9Q2")
#client = Client(oauth2)
my_jnj_box = client.user(user_id='me').get()
print('user_login: ' + my_jnj_box['login'])

root_folder = client.folder(folder_id= '0').get()
print ('folder name: ' + root_folder['name'])
 
items = root_folder.get_items(limit=10, offset=0)
print('This is up to the first 10 items in the root folder in JNJ Box:')
for item in items:
    print("   " + item.name)




    
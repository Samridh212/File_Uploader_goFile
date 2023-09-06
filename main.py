from gofile2 import Gofile
import os
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)



root_folder = config["root_folder"]
folder_output_name = input("Please enter the name of the Output Folder: ")
g_a = Gofile(token=config["api_key"])
upload_folder_id=g_a.create_folder(parentFolderId=config["parent_folder_id"], folderName=folder_output_name)['id']

for foldername, subfolders, filenames in os.walk(root_folder):
    print(f"Uploading from the Folder: {foldername}")

    for filename in filenames:
        file_path = os.path.join(foldername, filename)
        upload_file_data = g_a.upload(file=file_path,folderId=upload_folder_id)
        print(f"'{upload_file_data['fileName']}' was Uploaded Successfully:\n Link:{upload_file_data['downloadPage']} \n")









#g_a.upload_folder(path="D:\pythonProject\goFileUploader\Test")




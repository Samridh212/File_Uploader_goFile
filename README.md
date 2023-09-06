Gofile File Uploader:

The Gofile File Uploader is a Python program that allows you to easily upload files to Gofile servers, which offer unlimited fast server storage. This program simplifies the process of uploading files by providing a user-friendly interface where you can set your API token, parent folder ID, and root folder path.

Prerequisites
Before you can use this program, make sure you have the following prerequisites installed:

Python 3.x: You can download and install Python from the official website python.org.
Installation
Clone this repository to your local machine:
bash
Copy code:
  git clone https://github.com/Samridh212/File_Uploader_goFile.git
Change the directory to the project folder
Install the required dependencies:
  pip install gofile

Configuration
Before using the program, you need to configure your API token, parent folder ID, and root folder path. Here's how to obtain these values:

Obtaining the API Token
To obtain your Gofile API token, follow these steps:

Visit the Gofile website: (https://gofile.io/myProfile)

Sign in to your Gofile account or create a new account if you don't have one.

Now you should be able to see your api token at the botton

Open the config.json file in a text editor and replace "your_api_token_here" with your Gofile API token.

Obtaining the Parent Folder ID
To obtain the parent folder ID, you'll need to create a folder on Gofile. Here's how:

Visit the Gofile website: https://gofile.io/.

Sign in to your Gofile account or create a new account if you don't have one.

Once you're logged in, click on your profile icon in the top-right corner.

Select "Files" from the dropdown menu.

Click on the "New Folder" button to create a new folder.

Give the folder a name and click "Create Folder."

Click on the newly created folder to open it.

click on 3 dots menu iicon near the folder name and click on 'infos' , there you will see a 'content_id' , that will be your parent folder id you can paste it in your config

Open the config.json file in a text editor and replace "your_parent_folder_id_here" with your parent folder ID.

Now create/open a folder in  your desktop of which you will upload the files , copy the folder's path and paste it in the config

Save the changes to the config.json file.

Usage
Run the program:
bash
Copy code
 python main.py
The program will prompt you to enter an output folder name. This is the name of the folder that will be created on Gofile to store your uploaded files.

The program will upload all files from the specified root folder path to the Gofile server.

Once the upload is complete, the program will display the file links. You can access these links to share your files.

Contributing
If you would like to contribute to this project, please open an issue or submit a pull request on GitHub.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to customize this README file further if needed, and make sure to replace "yourusername" with your actual GitHub username in the repository URL.





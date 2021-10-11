# Dropbox program to upload a whole folder to Dropbox\
import dropbox
import os

class DropboxUploader:
    def __init__(self, access_token):
        self.access_token = access_token
        self.dbx = dropbox.Dropbox(self.access_token)
        print(f'Created DropBox Client: {self.dbx}')

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """

        with open(file_from, 'rb') as f:
           self.dbx.files_upload(f.read(), file_to)

    def upload_folder(self, folder_from, folder_to):
        """upload a whole folder to Dropbox using API v2
        """

        for item in os.listdir(folder_from):
            src = os.path.join(folder_from, item)
            if os.path.isfile(src):
                dst = os.path.join(folder_to, item)
                self.upload_file(src, dst)
            elif os.path.isdir(src):
                dst = os.path.join(folder_to, item)
                self.upload_folder(src, dst)

def main():
    access_token = '<YOUR API KEY>'
    uploader = DropboxUploader(access_token)
    n = input('Path of the folder to upload: ')
    uploader.upload_folder(n,'/'+os.path.basename(n)+'/')

if __name__ == '__main__':
    main()

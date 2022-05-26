import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BIV_41d6kzW9gK1zKR5_4XYWEKkx413XkehHEgcbjY61KXKVJ11xP7J9hxO9UHOawXAgBo5WEXaDl5OD1U34uSP_qC7qNkAtbermnsePNcPK0oyjWihra1kxC0wf12bPaiVAq-BFFYux'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/test/test.txt'
    # API v2
    transferData.upload_file(file_from, file_to)

main()

import subprocess
import shutil


class AttachmentManagerService:
    def __init__(self):
        pass

    def attach_to_contract(self, path, id):
        destination = f'{id}.pdf'
        shutil.copy(path, destination)

    def get_attachment(self, id):
        subprocess.Popen(f'{id}.pdf', shell=True)

import subprocess
import shutil
import os
from PyPDF2 import PdfFileReader, PdfFileMerger


class AttachmentManagerService:
    def __init__(self):
        pass

    def attach_to_contract(self, path, id):
        destination = f'contracts\\{id}.pdf'
        shutil.copy(path, destination)

    def get_attachment(self, id):
        subprocess.Popen(f'contracts\\{id}.pdf', shell=True)

    def merge_to_attachment(self, id, path):
        old_file = f'contracts\\{id}.pdf'
        os.rename(old_file, 'contracts\\temporary.pdf')
        old_file_renamed = f'contracts\\temporary.pdf'
        new_file = path
        files = [old_file_renamed, new_file]
        merger = PdfFileMerger()
        for file in files:
            merger.append(open(file, 'rb'))
        merger.write(old_file)
        merger.close()
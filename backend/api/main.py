from ninja import NinjaAPI, File
from ninja.files import UploadedFile


api = NinjaAPI()

@api.post("/upload")
def upload(request, file: UploadedFile = File(...)):
    data = file.read()
    return {'name': file.name, 'len': len(data)}

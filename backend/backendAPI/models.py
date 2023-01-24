from django.db import models
import uuid
import os
# Create your models here.

class Folder (models.Model) :
    uid =models.UUIDField(primary_key=True , editable=False , default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)


def getpath(ins , filename) :
    return os.path.join(str(ins.folder.uid) , filename)


class Files (models.Model) :
    folder = models.ForeignKey(Folder , on_delete=models.CASCADE)
    file =models.FileField(upload_to=getpath , max_length=10000)
    created_at = models.DateTimeField(auto_now=True)
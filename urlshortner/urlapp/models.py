from pyexpat import model
import uuid
from django.db import models

# Create your models here.
class URLS(models.Model):
    id = models.CharField(primary_key=True,
                            max_length=12,
                            unique=True,
                            blank=False,
                            default=uuid.uuid4,
                            editable=False)
    short_url = models.CharField(max_length=10,blank=False)
    long_url = models.CharField(max_length=256,blank=False)
    counter = models.IntegerField(default=1)

    def __str__(self) -> str:
        return super().__str__()

import uuid
from django.db import models
from django.forms import CharField, UUIDField
from django.core.validators import validate_comma_separated_integer_list
from uuid import uuid4

class model_User(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True)
    name = models.CharField(max_length=32, default='', blank=False)
    present = models.BooleanField(default=True)
    entry_year = models.DateField()
    pin_hash = models.CharField(max_length=256, default='', blank=False)


class model_SmallTask(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True)
    priority = models.IntegerField(default=0)
    description = models.CharField(max_length=512, default='', blank=False)
    complete = models.BooleanField(default=False)
    assigned_user = models.UUIDField(blank=True)
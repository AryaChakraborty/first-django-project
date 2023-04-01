from django.db import models

# Create your models here.
# makemigrations means store changes in a file, migrate means apply the changes made by makemigrations
class Contact(models.Model) :
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        # this function shows the name of the user in the admin database
        return self.name

class Blogs(models.Model) :
    username = models.CharField(max_length=122)
    title = models.CharField(max_length=122)
    blog = models.TextField()
    date = models.DateField()

    def __str__(self) :
        return self.title

'''then move to the admin.py in the same directory and do this(for this specific example)

from django.contrib import admin
from home.models import Contact

admin.site.register(Contact)

in the same directory move to app.py and copy the classname(usually 'HomeConfig')
then move to the __projectname__ directory and add the __appname__.apps.classname to the list INSTALLED_APPS.'''
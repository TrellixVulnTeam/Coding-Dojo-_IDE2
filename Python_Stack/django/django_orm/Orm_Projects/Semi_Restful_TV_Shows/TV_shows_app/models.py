from django.db import models

class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['title'])<2:
            errors["title"] = "Title should be more than 2 characters."
        if len(postData['network']) < 3:
            errors["network"] = "Network should be more than 3 characters."
        if len(postData['descript']) <10:
            errors["descript"] = "Description should be more than 10 characters."
        return errors
        

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    descript = models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = ShowManager()
    def __repr__(self):
        return f"({self.id}){self.title}{self.network}{self.release_date}{self.descript} "

# Create your models here.

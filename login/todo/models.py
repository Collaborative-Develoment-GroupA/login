from django.db import models

class Todo(models.Model):
   title = models.CharField(max_length=100)
   description = models.TextField()
   completed = models.BooleanField(default=False)

   def __str__(self):
     return self.title

class Login(models.Model):
   email = models.CharField(max_length=50)
   password = models.CharField(max_length=50)
   username = models.CharField(max_length=100)

   def __str__(self):
      return self.email


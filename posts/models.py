from django.db import models
from catagories.models import Catagory
from author.models import Author
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    catagory = models.ManyToManyField(Catagory)
    # ekta post multiple catagory'r under e thakte pare
    # abar multiple post ekta catagory'r under e thakte pare
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    natinolity = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)    
    author = models.ForeignKey(Author, related_name= "book", on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

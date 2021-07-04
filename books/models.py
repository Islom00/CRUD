from django.db import models


class AuthorModel(models.Model):
    name = models.CharField(max_length=60)
    birth_date = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class GenreModel(models.Model):
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BookModel(models.Model):
    title = models.CharField(max_length=1280)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    genres = models.ManyToManyField(GenreModel)
    cover = models.ImageField(upload_to="media", null=True)
    isbn = models.CharField(max_length=13, unique=True)
    page_count = models.IntegerField(null=True)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

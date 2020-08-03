from django.db import models
import os

class series(models.Model):
    name = models.CharField(max_length=30)
    bio = models.TextField()
    link = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class soulsearchingmodel(models.Model):
    name = models.CharField(max_length=100)
    series = models.ForeignKey(series, on_delete=models.CASCADE)
    medium = models.CharField(max_length=100)
    about = models.TextField()
    date = models.CharField(max_length=100)
    image = models.FileField(upload_to="portfolio/static/images/uploaded/")

    def filename(self):
        return os.path.basename(self.image.name)

    def __str__(self):
        return self.name

class thirtyonedaysofmemodel(models.Model):
    name = models.CharField(max_length=100)
    series = models.ForeignKey(series, on_delete=models.CASCADE)
    medium = models.CharField(max_length=100)
    about = models.TextField()
    date = models.CharField(max_length=100)
    image = models.FileField(upload_to="portfolio/static/images/uploaded/")

    def filename(self):
        return os.path.basename(self.image.name)

    def __str__(self):
        return self.name

class wanderlustmodel(models.Model):
    name = models.CharField(max_length=100)
    series = models.ForeignKey(series, on_delete=models.CASCADE)
    medium = models.CharField(max_length=100)
    about = models.TextField()
    date = models.CharField(max_length=100)
    image = models.FileField(upload_to="portfolio/static/images/uploaded/")

    def filename(self):
        return os.path.basename(self.image.name)

    def __str__(self):
        return self.name

class innerconsciencemodel(models.Model):
    name = models.CharField(max_length=100)
    series = models.ForeignKey(series, on_delete=models.CASCADE)
    medium = models.CharField(max_length=100)
    about = models.TextField()
    date = models.CharField(max_length=100)
    image = models.FileField(upload_to="portfolio/static/images/uploaded/")

    def filename(self):
        return os.path.basename(self.image.name)

    def __str__(self):
        return self.name

class regenerationmodel(models.Model):
    name = models.CharField(max_length=100)
    series = models.ForeignKey(series, on_delete=models.CASCADE)
    medium = models.CharField(max_length=100)
    about = models.TextField()
    date = models.CharField(max_length=100)
    image = models.FileField(upload_to="portfolio/static/images/uploaded/")

    def filename(self):
        return os.path.basename(self.image.name)

    def __str__(self):
        return self.name

class theuntoldtruthmodel(models.Model):
    name = models.CharField(max_length=100)
    series = models.ForeignKey(series, on_delete=models.CASCADE)
    medium = models.CharField(max_length=100)
    about = models.TextField()
    date = models.CharField(max_length=100)
    image = models.FileField(upload_to="portfolio/static/images/uploaded/")

    def filename(self):
        return os.path.basename(self.image.name)

    def __str__(self):
        return self.name

class thehumantrapmodel(models.Model):
    name = models.CharField(max_length=100)
    series = models.ForeignKey(series, on_delete=models.CASCADE)
    medium = models.CharField(max_length=100)
    about = models.TextField()
    date = models.CharField(max_length=100)
    image = models.FileField(upload_to="portfolio/static/images/uploaded/")

    def filename(self):
        return os.path.basename(self.image.name)

    def __str__(self):
        return self.name
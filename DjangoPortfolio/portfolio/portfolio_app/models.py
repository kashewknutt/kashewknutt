from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    # Add more fields as needed

    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    # Add more fields as needed

    def __str__(self):
        return self.title

class Certification(models.Model):
    title = models.CharField(max_length=100)
    issuer = models.CharField(max_length=100)
    description = models.TextField()
    date_earned = models.DateField()
    # Add more fields as needed

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateField()
    # Add more fields as needed

    def __str__(self):
        return self.title
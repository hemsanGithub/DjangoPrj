from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class chaiVariety(models.Model):
    CHAI_TYPES = [
        ('Black Tea', 'Black Tea'), 
        ('Green Tea', 'Green Tea'), 
        ('Herbal Tea', 'Herbal Tea'), 
        ('Oolong Tea', 'Oolong Tea'), 
        ('White Tea', 'White Tea'), 
        ('Chai Latte', 'Chai Latte'),
    ]   
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chai_images/')
    date_added = models.DateTimeField(default=timezone.now)
    chai_type = models.CharField(max_length=10, choices=CHAI_TYPES)
    description = models.TextField(default='Delicious chai variety.')

    def __str__(self):
        return self.name
    

# Relationship Model (if needed in future)
# one-to-many relationship example

class ChaiReview(models.Model):
    chai = models.ForeignKey(chaiVariety, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.PositiveIntegerField(default=5)  # Rating out of 5
    date_reviewed = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Review for {self.chai.name} by {self.reviewer.username}'
    
# Many-to-many relationship example (if needed in future)

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chais_available = models.ManyToManyField(chaiVariety, related_name='stores')

    def __str__(self):
        return self.name
    
# One-to-one relationship example (if needed in future)

class chaicertificate(models.Model):
    chai = models.OneToOneField(chaiVariety, on_delete=models.CASCADE, primary_key=True,related_name='certificate')
    certificate_number = models.CharField(max_length=50)
    issue_date = models.DateTimeField(default=timezone.now)
    expiry_date = models.DateTimeField()
    
    def __str__(self):
        return f'Certificate for {self.chai.name}'


from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=120)
    ingredients = models.TextField()
    cooking_time = models.IntegerField()
    pic = models.ImageField(upload_to='recipes', default='/media/no_picture.jpg')

    def __str__(self):
        return str(self.name)
    
    def calc_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients.split(", ")) < 4:
            difficulty = "Easy"
        if self.cooking_time < 10 and len(self.ingredients.split(", ")) >= 4:
            difficulty = "Medium"
        if self.cooking_time >= 10 and len(self.ingredients.split(", ")) < 4:
            difficulty = "Intermediate"
        if self.cooking_time >= 10 and len(self.ingredients.split(", ")) >= 4:
            difficulty = "Hard"
        return difficulty
    
    def get_absolute_url(self):
       return reverse ('recipes:detail', kwargs={'pk': self.pk})
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def __iter__(self):
        # Повертає ітератор по всіх рецептах, що належать до цієї категорії
        return iter(self.recipes.all())


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructions = models.TextField()
    ingredients = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='recipes'
    )

    def __str__(self):
        return self.title
from django.test import TestCase
from .models import Category, Recipe

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Випічка")

    def test_category_creation(self):
        # Перевірка створення категорії
        self.assertEqual(self.category.name, "Випічка")

    def test_category_iter_method(self):
        # Перевірка роботи магічного методу __iter__
        recipe1 = Recipe.objects.create(
            title="Торт",
            description="Смачний торт",
            instructions="Запікати 40 хв",
            ingredients="Борошно, яйця",
            category=self.category
        )
        recipe2 = Recipe.objects.create(
            title="Пиріг",
            description="Яблучний пиріг",
            instructions="Запікати 30 хв",
            ingredients="Борошно, яблука",
            category=self.category
        )
        
        # Використовуємо ітерацію по об'єкту категорії
        recipes_list = list(self.category)
        
        self.assertEqual(len(recipes_list), 2)
        self.assertIn(recipe1, recipes_list)
        self.assertIn(recipe2, recipes_list)


class RecipeModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Напої")
        self.recipe = Recipe.objects.create(
            title="Кава",
            description="Чорна кава",
            instructions="Залити окропом",
            ingredients="Кава, вода",
            category=self.category
        )

    def test_recipe_creation(self):
        # Перевірка створення рецепту та зв'язку з категорією
        self.assertEqual(self.recipe.title, "Кава")
        self.assertEqual(self.recipe.category.name, "Напої")
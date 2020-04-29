from django.test import Client, TestCase
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

from .forms import *   # import all forms
from .models import *
from .views import *

# Test forms
class GameFormTest(TestCase):

    # Valid Form Data
    def test_gameform_valid(self):
        valid_data = {
          "price": "29.90",
          "homepage_display": False,
          }
        form = GameForm(data=valid_data)
        # print(form.is_valid())
        # print(form['price'])
        # print(form['homepage_display'])
        self.assertTrue(isinstance(form, GameForm))
        # self.assertTrue(form.is_valid())

class GameSearchFormTest(TestCase):

    def test_gamesearch_form(self):
            form = GameSearchForm(data={'search_terms': "Monopoly Deal"})

            self.assertTrue(isinstance(form, GameSearchForm))
            self.assertTrue(form.is_valid())

# Test Models
class GameTest(TestCase):

    def setUp(self):

            self.category = Category.objects.create(name="Board Games")
            self.game = Game.objects.create(
              name="Catan",
              category=self.category,
              description="This is a very long description about this game",
              inside_box="There could be many things. \b Many things could be there",
              price=29.90,
              # image="image.jpg",
              homepage_display=False
              )

    def test_game_name(self):
            game = Game.objects.get(name='Catan')
            name = game.name
            category = game.category
            max_length = game._meta.get_field('name').max_length
            blank = game._meta.get_field('name').blank

            self.assertTrue(isinstance(game, Game))
            self.assertEqual(type(name), str)
            self.assertEqual(game.__str__(), f'{game.name} ({game.category})')
            self.assertEquals(max_length, 21)
            self.assertEquals(blank, False)

    def test_game_category(self):
            game = Game.objects.get(name='Catan')
            category = game.category

            self.assertTrue(isinstance(category, Category))
            self.assertEqual(game.category_id, self.category.id)
            self.assertEqual(game.category, self.category)

    def test_game_description(self):
            game = Game.objects.get(name='Catan')
            description = game.description
            blank = game._meta.get_field('name').blank

            self.assertEqual(type(description), str)
            self.assertEquals(blank, False)

    def test_game_inside_box(self):
            game = Game.objects.get(name='Catan')
            inside_box = game.inside_box
            blank = game._meta.get_field('name').blank

            self.assertEqual(type(inside_box), str)
            self.assertEquals(blank, False)

    def test_game_price(self):
            game = Game.objects.get(name='Catan')
            price = game.price
            max_digits = game._meta.get_field('price').max_digits
            decimal_places = game._meta.get_field('price').decimal_places
            blank = game._meta.get_field('price').blank

            self.assertLess(float(price), 100000)
            self.assertEquals(max_digits, 5)
            self.assertEquals(decimal_places, 2)
            self.assertEquals(blank, False)

    def test_game_homepage_display(self):
            game = Game.objects.get(name='Catan')
            homepage_display = game.homepage_display
            default = game._meta.get_field('homepage_display').default

            self.assertEquals(type(default), bool)
            self.assertEquals(default, False)

class CategoryTest(TestCase):

    def create_category(self, name="Card Game"):
            return Category.objects.create(name=name)

    def test_category_creation(self):
            category = self.create_category()
            max_length = category._meta.get_field('name').max_length
            blank = category._meta.get_field('name').blank

            self.assertTrue(isinstance(category, Category))
            self.assertEqual(category.__str__(), category.name)
            self.assertEquals(max_length, 50)
            self.assertEquals(blank, False)

# Test Views
class ShowGamesTest(TestCase):

    def test_show_games(self):
            url = reverse('show_games')
            response = self.client.get(url)
            context = response.context

            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'catalogue/games.template.html')
            self.assertTrue('all_games' in context)
            self.assertTrue('search_terms' in context)
            self.assertTrue('party_games' in context)
            self.assertTrue('card_games' in context)
            self.assertTrue('board_games' in context)
            self.assertTrue('filtering' in context)
            self.assertTrue('results' in context)
            self.assertContains(response, 'Party Games')

class CreateGameTest(TestCase):

    def test_create_game_not_superuser(self):
            url = reverse('create_game')
            response = self.client.get(url)
            # context = response.context

            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, "/user/login/?next=/catalogue/create")

#     def test_create_game_as_superuser(self):

#             def setUp(self):
#                   self.client = Client()
#                   superuser = User(username='testing123', is_staff=True)
#                   superuser.set_password('user123!')
#                   superuser.save() # needed to save to temporary test db
#                   response = self.client.get('/admin/', follow=True)
#                   self.client.force_login(superuser)
#                   self.superuser.force_login(username='testing123',password='user123!')

#             url = reverse('create_game')
#             response = self.client.get(url)
#             print(response)

#             self.assertEqual(response.status_code, 200)
#             self.assertEqual(response.url, "/catalogue/create")


# class GameInfoTest(TestCase):

#     def test_game_info(self):
#             url = reverse('game_info')
#             response = self.client.get(url)
#             response = self.client.get(reverse('game_info',
#                                            kwargs={'game_id': 2}))
#             context = response.context
#             print(response)
#             print(response)
#             print(context)
#             self.assertEqual(response.status_code, 200)
#             self.assertEqual(response.url, "/catalogue/game_info/pk")

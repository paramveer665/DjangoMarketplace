from django.test import TestCase
from django.urls import reverse
from products.models import Products
from django.contrib.auth.models import User

class TestingTest(TestCase):
    def test_login_page_loads(self):
        response=self.client.get(reverse('login'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'login.html')

    def setUp(self):
        self.test_add_product=Products.objects.create(title="title",price=3000,desc="desc",active=True,featured=True)
        User.objects.create_user(username='walter', password='white')

    def test_user_login_failed(self):
        response=self.client.post(reverse('login'),{'username':'heisenberg','password':'heisenberg'})
        
        self.assertContains(response,"Please enter a correct username and password.")
       

    def test_login_success(self):
        response=self.client.post(reverse('login'),{'username':'walter','password':'white'})
        self.assertRedirects(response,reverse('home'))
        
    def test_homepage_loads(self):
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    def test_add_product(self):
        response=self.client.post(reverse('login'),{'username':'heisenberg','password':'heisenberg'})
        form_data={'title':'title','price':2000,'desc':'desc','active':True,'featured':False}
        response=self.client.post(reverse('create'),form_data)
        self.assertEqual(response.status_code,302)
       





    
    
from django.test import TestCase, LiveServerTestCase, Client
from blog.models import BlogPost
from django.contrib.auth.models import User

#Create your tests here.
class PostTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='AAA', email='A@A.com', password='pwd')
        user.save()

    def tearDown(self):
        user = User.objects.get(username='AAA')

        if user:
            user.delete()

    def test_create_post(self):
        user = User.objects.get(username='AAA')
        post = BlogPost(user=user)

        post.title = "My test post"
        post.content = "This is a test post"

        post.save()

        all_posts = BlogPost.objects.all()
        self.assertEquals(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEquals(only_post, post)

        self.assertEquals(only_post.title, "My test post")

class AdminTest(LiveServerTestCase):
    def setUp(self):
        user = User.objects.create_superuser(username='AAA', email='A@A.com', password='pwd')
        user.save()
        self.client = Client()

    def tearDown(self):
        user = User.objects.get(username='AAA')

        if user:
            user.delete()

    def test_login(self):
        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 200)
        self.assertTrue('Log in' in response.content)

        self.client.login(username='AAA', password='pwd')

        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 200)
        self.assertTrue('Log out' in response.content)
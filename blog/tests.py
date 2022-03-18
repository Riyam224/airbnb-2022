
from django.test import TestCase

# Create your tests here.
from .models import Post , Category
from django.contrib.auth.models import User
from django.urls import reverse


class BlogModelTest(TestCase):
    


    def post_create(self):
        author = User.objects.create(username='yonna' , password='ilovemoney1')
        category = Category.objects.create(name='text category')
        
        return Post.objects.create(
            author=author,
            title='food vegan',
            tags='food',
            description='vegan is cool and modern',
            category=category

        )


    def test_model_str(self):
        post = self.post_create()
        self.assertEqual(post.__str__(),post.title)



# todo 

class BlogViewTest(TestCase):

    def test_blog_url(self):

        response = self.client.get('/blog/')
        self.assertEqual(response.status_code,200)


    def test_view_uses_correct_template(self):

        response = self.client.get(reverse('blog/post_list.html'))
        self.assertTemplateUsed(response, 'blog/post_list.html')


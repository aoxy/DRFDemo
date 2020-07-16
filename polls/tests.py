import datetime

from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from polls import views
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        如果问题在未来被发布，则was_published_recently()返回False
        """
        time = timezone.now()+datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        如果问题在1天以前被发布，则was_published_recently()返回False
        """
        time = timezone.now()-datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        如果问题在最近1天内被发布，则was_published_recently()返回True
        """
        time = timezone.now()-datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


class TestQuestion(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.view = views.QuestionViewSet.as_view({'get': 'list'})
        # self.uri = '/questions/'
        self.uri = '/polls/questions/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user('test', email='testuser@test.com', password='test')

    def test_list(self):
        request = self.factory.get(
            self.uri, HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         '期望Code 200, 然而收到 {0} .'.format(response.status_code))

    def test_list2(self):
        self.client.login(username="test", password="test")
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         '期望Code 200, 然而收到 {0} .'.format(response.status_code))

    def test_create(self):
        self.client.login(username='test', password='test')
        params = {
            "question_text": "测试test_create()生成的问题1",
            "created_by": 1
        }
        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code, 201,
                         '期望Code 201, 然而收到 {0} .'.format(response.status_code))

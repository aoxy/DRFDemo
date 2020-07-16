import datetime

from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APITestCase, APIRequestFactory
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
        self.factory = APIRequestFactory()
        self.view = views.QuestionViewSet.as_view({'get': 'list'})
        self.uri = '/questions/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         '期望Code 200, 然而收到 {0} .'.format(response.status_code))
        return super().setUp()

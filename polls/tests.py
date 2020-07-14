import datetime

from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        如果问题在未来被发布，则was_published_recently()返回False
        """
        time=timezone.now()+datetime.timedelta(days=30)
        future_question=Question(pub_date=time)
        self.assertIs(future_question.was_publisted_recently,False)

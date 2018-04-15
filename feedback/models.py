from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Survey(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=400)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return 'Survey for {}'.format(self.title)


class Question(models.Model):
    question = models.CharField(max_length=250)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    #answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Answer(models.Model):
    STRONGLY_AGREE = 'SR'
    AGREE = 'AG'
    NEITHER = 'NR'
    DISAGREE = 'DA'
    STRONGLY_DISAGREE = 'SD'
    ANSWER_OPTIONS = (
        (STRONGLY_AGREE, 'Strongly Agree'),
        (AGREE, 'Agree'),
        (NEITHER, 'Neither agree nor disagree'),
        (DISAGREE, 'Disagree'),
        (STRONGLY_DISAGREE, 'Strongly Disagree'),
    )
    answer = models.CharField(
        max_length=2,
        choices=ANSWER_OPTIONS,
        default=AGREE,
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.get_answer_display()


class Response(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    #question = models.ManyToManyField(Question)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    answer = models.ManyToManyField(Answer)

    def __str__(self):
        return 'response {0} for {1} is added'.format(self.id, self.survey)
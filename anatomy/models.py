from django.db import models
from ckeditor.fields import RichTextField
from django.utils import translation

# Create your models here.
class Course_List(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Course_Summary(models.Model):
    chapter = models.ForeignKey(Course_List, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    body = RichTextField()
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.chapter.name

class Ana_Quiz(models.Model):
    chapter = models.ForeignKey(Course_List, on_delete=models.CASCADE, related_name='quiz')
    title = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'Anatomy Quiz'
        verbose_name_plural = 'Anatomy Quizzes'

    def __str__(self):
        return self.title

class Ana_Question(models.Model):
    chapter = models.ForeignKey(Course_List, on_delete=models.CASCADE, related_name='chapter')
    quiz = models.ForeignKey(Ana_Quiz, related_name='question', on_delete=models.CASCADE)
    question = models.TextField()

    class Meta:
        verbose_name = 'Anatomy Question'
        verbose_name_plural = 'Anatomy Questions'

    def __str__(self):
        return self.quiz.title

class Ana_Answer(models.Model):
    question = models.ForeignKey(Ana_Question, related_name='answer', on_delete=models.CASCADE)
    choice = models.CharField(max_length=20)
    correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Anatomy Answer'
        verbose_name_plural = 'Anatomy Answers'

    def __str__(self):
        return self.choice
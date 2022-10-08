from rest_framework import serializers
from .models import Course_List, Course_Summary, Ana_Answer, Ana_Question, Ana_Quiz

#anatomy home page serializer to show all the courses with links to the summary and quiz for each course
class HomePageSerializer(serializers.ModelSerializer):
    summary = serializers.HyperlinkedIdentityField(
        view_name='summary',
        lookup_field = 'pk',
    )
    class Meta:
        model = Course_List
        fields = [
            'id',
            'name',
            'summary',
        ]

class ChapterSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)

#this serializer shows thw chapter name, date created and the summary of the chapter after it has been verified
class SummaryPageSerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer(read_only=True)
    class Meta:
        model = Course_Summary
        fields = [
            'id',
            'chapter',
            'date_created',
            'body',
        ]

#this serializer controls all the summary data verified or not
class SummaryOverviewSerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer(read_only=True)
    class Meta:
        model = Course_Summary
        fields = [
            'id',
            'chapter',
            'date_created',
            'body',
            'verified',
        ]

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ana_Answer
        fields = [
            'choice',
            'correct',
        ]

class QuizSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Ana_Question
        fields = [
            'id',
            'question',
            'answer',
        ]
from rest_framework import serializers
from .models import Test, Question, Answer, Student, StudentAnswer, AudioAnswer #, AnswerVV

class TestListSerializer(serializers.ModelSerializer):
    questions_count = serializers.SerializerMethodField()
    class Meta:
        model = Test
        fields = ["id", "name", "desc", "slug", "questions_count"]
        read_only = ["questions_count"]
        
    def get_questions_count(self,obj):
        return obj.question_set.all().count()

'''class AnswerVVSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AnswerVV
        fields = ["id", "question", "label", "audio"]'''
        
class AnswerSerializer(serializers.ModelSerializer):
    #answer_vv_set = AnswerVVSerializer(many=True)
    class Meta:
        model = Answer
        fields = ["id", "question", "label", "audio"]
        
class QuestionSerializer(serializers.ModelSerializer):
    answer_set = AnswerSerializer(many=True)
    
    class Meta:
        model = Question
        fields = "__all__"

class StudentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAnswer
        fields = "__all__"
        
class AudioAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioAnswer
        fields = "__all__"

class MyTestListSerializer(serializers.ModelSerializer):
    questions_count = serializers.SerializerMethodField()
    score = serializers.SerializerMethodField()
    completed = serializers.SerializerMethodField()
    progress = serializers.SerializerMethodField()
    
    class Meta:
        model = Test
        fields = ["id", "name", "desc", "slug", "questions_count", "completed", "score", "progress"]
        read_only_fields = ["questions_count", "completed", "progress"]

    def get_questions_count(self,obj):
        return obj.question_set.all().count()
        
    def get_completed(self, obj):
        try:
            student = Student.objects.get(user=self.context['request'].user, test=obj)
            return student.completed
        except Student.DoesNotExist:
            return None
    
    def get_progress(self, obj):
        try:
            student = Student.objects.get(user=self.context['request'].user, test=obj)
            if student.completed == False:
                questions_answered = StudentAnswer.objects.filter(student=student, answer__isnull=False).count()
                total_questions = obj.question_set.all().count()
                return int(questions_answered / total_questions)
            return None
        except Student.DoesNotExist:
            return None
            
    def get_score(self, obj):
        try:
            student = Student.objects.get(user=self.context['request'].user, test=obj)
            if student.completed == True:
                return student.score
            return None
        except Student.DoesNotExist:
            return None

class StudentSerializer(serializers.ModelSerializer):
    studentanswer_set = StudentAnswerSerializer(many=True)
    
    class Meta:
        model = Student
        fields = "__all__"
        
class TestDetailSerializer(serializers.ModelSerializer):
    students_set = serializers.SerializerMethodField()
    question_set = QuestionSerializer(many=True)
    
    class Meta:
        model = Test
        fields = "__all__"
        
    def get_students_set(self,obj):
        try:
            student = Student.objects.get(user=self.context['request'].user, test=obj)
            serializer = StudentSerializer(student)
            return serializer.data
        except Student.DoesNotExist:
            return None
            
class TestResultSerializer(serializers.ModelSerializer):
    student_set = serializers.SerializerMethodField()
    question_set = QuestionSerializer(many=True)
    
    class Meta:
        model = Test
        fields = "__all__"
    
    def get_student_set(self, obj):
        try:
            student = Student.objects.get(user=self.context['request'].user, test = obj)
            serializer = StudentSerializer(student)
            return serializer.data
        except Student.DoesNotExist:
            return None
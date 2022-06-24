from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status, routers, views
from rest_framework.response import Response
from .models import Test, Student, Question, Answer, StudentAnswer, AudioAnswer
from .serializers import MyTestListSerializer, TestListSerializer, TestDetailSerializer, StudentAnswerSerializer, TestResultSerializer, AudioAnswerSerializer

class MyTestListAPI(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = MyTestListSerializer
    
    def get_queryset(self, *args, **kwargs):
        queryset = Test.objects.filter(student__user=self.request.user)
        query = self.request.GET.get("q")
        
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(desc__icontains=query)
            ).distinct()
        
        return queryset
        
class TestListAPI(generics.ListAPIView):
    serializer_class = TestListSerializer
    
    def get_queryset(self, *args, **kwargs):
        #queryset = Test.objects.all()
        queryset = Test.objects.all().exclude(student__user=self.request.user)
        query = self.request.GET.get("q")
        
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(desc__icontains=query)
            ).distinct()
        
        return queryset

class TestDetailAPI(generics.RetrieveAPIView):
    serializer_class = TestDetailSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def get(self, *args, **kwargs):
        slug = self.kwargs["slug"]
        test = get_object_or_404(Test, slug=slug)
        last_question = None #Последний вопрос, на который ответил пользователь
        obj, created = Student.objects.get_or_create(user=self.request.user, test=test)
        if created:
            for question in Question.objects.filter(test=test):
                StudentAnswer.objects.create(student=obj,question=question)
        else:
            last_question = StudentAnswer.objects.filter(student=obj,answer__isnull=False)
            if last_question.count() > 0:
                last_question = last_question.last().question.id
            else:
                last_question = None
                
        return Response({'test': self.get_serializer(test, context={'request' : self.request}).data, 'last_question_id' : last_question})
        
class SaveUsersAnswer(generics.UpdateAPIView):
    serializer_class = StudentAnswerSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    
    def patch(self, request, *args, **kwargs):
        student_id = request.data['student']
        question_id = request.data['question']
        answer_id = request.data['answer']
        #audio_id = request.data['audio']
        
        student = get_object_or_404(Student, id=student_id)
        question = get_object_or_404(Question, id=question_id)
        answer = get_object_or_404(Answer, id=answer_id)
        #audio = get_object_or_404(AudioAnswer, id=audio_id)
            
        
        if student.completed:
            return Response({
                "message" : "Данный тест был пройден. Вы не можете изменить свои ответы."}, 
                status=status.HTTP_412_PRECONDITION_FAILED
            )
        
        obj = get_object_or_404(StudentAnswer, student = student, question = question)
        obj.answer = answer
        #obj.audio = audio
        obj.save()
        return Response(self.get_serializer(obj).data)

from rest_framework.parsers import MultiPartParser, FormParser
        
class UploadAudioFileAPI(views.APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    parser_classes = [MultiPartParser, FormParser,]
    
    def post(self, request, *args, **kwargs):
        audio_serializer = AudioAnswerSerializer(data=request.data)
        if audio_serializer.is_valid():
            audio_serializer.save()
            return Response(audio_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(audio_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class SubmitTestAPI(generics.GenericAPIView):
    serializer_class = TestResultSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    
    def post(self, request, *args, **kwargs):
        student_id = request.data['student']
        question_id = request.data['question']
        answer_id = request.data['answer']
        
        student_obj = get_object_or_404(Student, id=student_id)
        question = get_object_or_404(Question, id=question_id)
        #answer = get_object_or_404(Answer, id=answer_id)
        
        test = Test.objects.get(slug=self.kwargs['slug'])
        
        if student_obj.completed:
            return Response({
                "message" : "Данный тест был пройден. Вы не можете пройти его снова."}, 
                status=status.HTTP_412_PRECONDITION_FAILED
            )
        
        if answer_id is not None:
            answer = get_object_or_404(Answer, id=answer_id)
            obj = get_object_or_404(StudentAnswer, student = student_obj, question = question)
            obj.answer = answer
            obj.save() 
        
        student_obj.completed = True
        
        correct_answers = 0
        
        for studentanswer in StudentAnswer.objects.filter(student = student_obj):
            #pass
            answer = Answer.objects.filter(question=studentanswer.question, is_correct=True)
            if studentanswer.answer == answer:
                correct_answers +=1
            
        student_obj.score = int(correct_answers / student_obj.test.question_set.count() * 100)
        student_obj.save()
        
        return Response(self.get_serializer(test).data)
        

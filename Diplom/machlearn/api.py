from .preprocess import *
from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializer import StudentAudioAnswerSerializer
from django.apps import apps
StudentAnswer = apps.get_model('quiz', 'StudentAnswer')
AudioAnswer = apps.get_model('quiz', 'AudioAnswer')

import os
import keras
from keras.models import model_from_json

# Second dimension of the feature is dim2
feature_dim_2 = 11

# # Feature dimension
feature_dim_1 = 20
channel = 1
epochs = 50
batch_size = 100
verbose = 1
num_classes = 3

def load_model_from_disk(file_name_without_extention):
    # load json and create model
    json_file = open(os.path.join(settings.STATIC_ROOT,file_name_without_extention + '.json'), 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(os.path.join(settings.STATIC_ROOT,file_name_without_extention + ".h5"))
    return loaded_model
     

def predict(filepath, model):
    sample = wav2mfcc(filepath)
    sample_reshaped = sample.reshape(1, feature_dim_1, feature_dim_2, channel)
    return get_labels()[0][
            np.argmax(model.predict(sample_reshaped))
    ]
    
def status_test(audio):
    model = load_model_from_disk('test')
    print(predict(audio, model=model))
    return predict(audio, model=model)
        
class PredictAnswerAPI(generics.GenericAPIView):
    serializer_class = StudentAudioAnswerSerializer
    
    def post(self, request, *args, **kwargs):
        audio_id = request.data['audio']
        
        audio_obj = get_object_or_404(AudioAnswer, id=audio_id)
        
        audio = audio_obj.audiofile.path
        
        return Response({
            'result': status_test(audio)
        })
        
    
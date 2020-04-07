from django.shortcuts import render, redirect
from .models import Question
from sys import stderr
from collections import OrderedDict 

def open_landing_page(request):
    lang_code_translator = OrderedDict({"English": "en", "Hindi": "hi", "Bengali": "bn", "Telugu": "te", "Marathi": "mr", "Tamil": "ta",  "Kannada": "kn", "Gujarati": "gu"})
    lang_translator = OrderedDict({"English": "English", "Hindi": "हिन्दी", "Bengali": "বাংলা", "Telugu": "తెలుగు", "Marathi": "मराठी", "Tamil": "தமிழ்",  "Kannada": "ಕನ್ನಡ", "Gujarati": "ગુજરાતી"})

    language = request.GET.get('l')

    for key in lang_code_translator.keys():
        if language == lang_code_translator[key]:
            question_objects = Question.objects.filter(language = key).order_by('created_at')
            active_lang = key

    if language == None:
        question_objects = Question.objects.filter(language = "Hindi").order_by('created_at')
        active_lang = "Hindi"

    
    language_data = []

    for key in lang_code_translator.keys():
        active_status = False
        if key == active_lang:
            active_status = True
        language_data.append({"active": str(active_status), "head":lang_translator[key], "url" : "/?l=" + lang_code_translator[key]})


    # print (language_data, file = stderr)



    return render(request, 'landing.html', {"questions": question_objects, "language_data": language_data})


    
def open_about_page(request):

    return render(request, 'about.html')


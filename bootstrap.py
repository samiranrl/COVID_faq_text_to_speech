import django
import os
import pandas as pd
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")
django.setup()

from corona_core.navigation.models import Question

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

TAG_RE = re.compile(r'<[^>]+>')
def remove_tags(text):
    return TAG_RE.sub('', text)


from gtts import gTTS



Question.objects.all().delete()

from googletrans import Translator
translator = Translator()

lang_code_translator = {"English": "en", "Hindi": "hi", "Bengali": "bn", "Marathi": "mr", "Tamil": "ta", "Telugu": "te", "Kannada": "kn", "Gujarati":"gu", "Malayalam":"ml"}


english_questions = pd.read_excel("questions/questions.xlsx", sheet_name = "English")
for i, row in english_questions.iterrows():
#     print(row['question'], row['answer'])
    question = Question.objects.create(question_text = row['question'], answer_text = row['answer'], language = "English")
    tts = gTTS(remove_tags(row['answer']), lang='en')
    tts.save('corona_core/static/sounds/' + str(question.id) + '_' + 'answer.mp3')
    tts = gTTS(remove_tags(row['question']), lang='en')
    tts.save('corona_core/static/sounds/' + str(question.id) + '_' + 'question.mp3')
    print("done", row['question'])


hindi_questions = pd.read_excel("questions/questions.xlsx", sheet_name = "Hindi")
for i, row in hindi_questions.iterrows():
#     print(row['question'], row['answer'])
    question = Question.objects.create(question_text = row['question'], answer_text = row['answer'], language = "Hindi")
    tts = gTTS(remove_tags(row['answer']), lang='hi')
    tts.save('corona_core/static/sounds/' + str(question.id) + '_' + 'answer.mp3')
    tts = gTTS(remove_tags(row['question']), lang='hi')
    tts.save('corona_core/static/sounds/' + str(question.id) + '_' + 'question.mp3')
    print("done", row['question'])


for i, row in hindi_questions.iterrows():
    for key in lang_code_translator.keys():
        if key not in ["English", "Hindi"]:
            print(key)
            question_translated = translator.translate(row['question'], src="hi", dest=lang_code_translator[key]).text
            answer_translated = translator.translate(row['answer'], src="hi", dest=lang_code_translator[key]).text
            question = Question.objects.create(question_text = question_translated, answer_text = answer_translated, language = key)
            tts = gTTS(remove_tags(answer_translated), lang=lang_code_translator[key])
            tts.save('corona_core/static/sounds/' + str(question.id) + '_' + 'answer.mp3')
            tts = gTTS(remove_tags(question_translated), lang=lang_code_translator[key])
            tts.save('corona_core/static/sounds/' + str(question.id) + '_' + 'question.mp3')
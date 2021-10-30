from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# import requests for api request &
# json to create a dictionary
import requests
import json

# import cognate database
from word_cognate.models import Cognates

# import nltk for nlp
import nltk
# verify ssl certificate by handling attribute error to install punkt
# from: @ishwardgret on stackoverflow.com/questions/
# 38916452/nltk-download-ssl-certificate-verify-failed
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# import stopwords & punkt & word_tokenize
# to create lists excluding english stopwords
# from: stackabuse.com/removing-stop-words-from-strings-in-python
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words('english'))

# index method sets default page to index.html
def index(request):
    return render(request, 'word_cognate/index.html')

# output method takes user input, replaces words
# with cognate synonyms & sends new text to output.html
def output(request):

    # create a string for user input
    original_text = ''

    # if the request is a post request,
    # create a list of words from user input
    # & create a copy of the original text string
    # from: stackabuse.com/removing-stop-words-from-strings-in-python
    if request.method == 'POST':
        original_text = request.POST
        new_text = dict(original_text).get('original_text')[0]
        original_text = word_tokenize(dict(original_text).get('original_text')[0])
        original_text = [word for word in original_text if not word in stopwords.words()]

    # exception handling for GET request
    else:
        new_text = ''

    try:
        # api request to wordsapi from: rapidapi.com/dpventures/api/wordsapi/
        # for each alphabetical word in list, check for synonyms & store
        # this information in response variable
        for original_word in original_text:
            if original_word.isalpha():
                url = "https://wordsapiv1.p.rapidapi.com/words/" + original_word + "/synonyms"
                headers = {
                    'x-rapidapi-key': "e261835ec8mshfa2de210c84a33fp10edcdjsn1c3712b6ca51",
                    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
                }
                response = requests.request("GET", url, headers=headers)
                # convert each response to a dictionary using json
                # & access the values with the 'synonyms' key
                # if a synonym is found in the Cognates model,
                # replace the word with its synonym in the new text
                for synonym in response:
                    synonym_dict = (response.json())
                    for y in synonym_dict['synonyms']:
                        if Cognates.objects.filter(english_word=y).exists():
                            new_word = '<b>' + y + '</b>'
                            new_text = (new_text.replace(synonym_dict.get('word'), new_word))


    # use try & except to deal with jsondecode error
    except json.decoder.JSONDecodeError:
         new_text = "json decode error"
    # use try & except to deal with spelling errors
    except KeyError:
        new_text = "You misspelled a word!"

    #return a render request of the new text to output.html
    return render(request, 'word_cognate/output.html', {'output': new_text})
# wordCognateReplace
this app replaces words with their cognate synonyms. it can help make material understandable for Spanish-speaking ELL speakers while avoiding direct translation. using cognates in this way helps facilitate language development.

contact me @ ajk2256@barnard.edu if you want to use this code in a project or if you have any questions/suggestions!

**table of contents:**

templates/word_cognate/

this HTML & CSS template allows users to input & submit text. the output page returns text with all words that have cognate synonyms replaced with those cognates. 

/word_cognate/views.py 

this python code uses nltk library tools to filter stop words from the user’s text. it then requests the words synonyms from the Words API. next, if a synonym matches a word in the cognate database, then the cognate synonym replaces the original word in the output text. more detailed comments and citations are written in the code. 

/word_cognate/models.py

this python code creates two Django models: one to store Cognates and one to store FalseCognates. The Cognates model has the fields english_word and language_word. The FalseCognates model has the fields english_word, language_word, and language_defintion. 

**credits:**

database of English-Spanish cognate words provided by:
    colorincolorado word cognate list: www.colorincolorado.org/guide/cognate-list-english-and-spanish
    Adapted from: Calderón, M., August, D., Durán, D., Madden, N., R. Slavin & M. Gil (2003). Spanish to English Transitional Reading: Teacher's Manual. Baltimore, MD: The Success for All Foundation.

Words API thesaurus API provided by:
    Words API from Rapid API: rapidapi.com/dpventures/api/wordsapi

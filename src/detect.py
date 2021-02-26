#from guesslang import Guess

LangGuess = Guess()

def _gl_detect(filename):
    with open(filename, 'r') as f:
        text = f.readlines()
        text = ''.join(text)
    lang = LangGuess.language_name(text)
    return lang
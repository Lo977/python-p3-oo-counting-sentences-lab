

class MyString:
    def __init__(self,value=""):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        if '.' in self._value:
            return True
        else:
            return False

    def is_question(self):
        if '?' in self._value:
            return True
        else:
            return False

    def is_exclamation(self):
        if '!' in self._value:
            return True
        else:
            return False

    def count_sentences(self):
       
        value = self.value
        for punc in ['!', '?']:
            value = value.replace(punc,'.')
        sentences = [s for s in value.split('.') if s]
        return len(sentences)
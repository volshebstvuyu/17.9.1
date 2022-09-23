class ElementNotInList(Exception):
    def __init__(self, text, previousInt):
        self.text = text
        self.previousInt = previousInt

    def __call__(self):
        return f'{self.text}', self.previousInt
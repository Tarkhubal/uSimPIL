class Text:
    def __init__(self, text: str):
        self.text = text
        
        self.align = TextAlign(self)
        self.font = TextFont(self)
        
        self.position = None
    

class TextAlign:
    def __init__(self, text: Text):
        self.text = text
        
    @property
    def justify(self):
        self.text.align = "justify"
    
    @property
    def left(self):
        self.text.align = "left"
    
    @property
    def right(self):
        self.text.align = "right"
    
    @property
    def center(self):
        self.text.align = "center"


class TextFont:
    def __init__(self, text: Text):
        self.text = text
    
    def from_file(self, path: str):
        ...
    
    def from_os(self, name: str):
        ...
    
    
    @property
    def times_new_roman(self):
        self.text.font = "Times New Roman"
    # Repeat some basic fonts like this


class TextPosition:
    center = -5
    top = -1
    right = -2
    bottom = -3
    left = -4
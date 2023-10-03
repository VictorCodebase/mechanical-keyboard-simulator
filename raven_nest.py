
class raven:
    def __init__(self, contents, keyword):
        self.contents = contents
        self.keyword = keyword
        self.send()
    
    def send(self):
        #future easter-egg
        print(f"Context: {self.keyword} \nthe information before: {self.contents}")
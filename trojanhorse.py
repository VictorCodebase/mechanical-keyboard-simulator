
class raven:
    def __init__(self, contents, keyword):
        self.contents = contents
        self.keyword = keyword
        self.send()
    
    def send(self):
        print(f"the raven successfully sent the contents: {self.contents} with hopes its about: {self.keyword}")
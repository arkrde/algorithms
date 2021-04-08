class BoyerMoore:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.table = self.preprocess()
    
    def preprocess(self):
        pattern_length = len(self.pattern)
        table = {
            self.pattern[i]: (pattern_length - 1 - i) 
            for i in range(pattern_length - 1)
        }
        return table
    
    @staticmethod
    def same(str1, str2, len):
        for i in reversed(range(len)):
            if str1[i] != str2[i]: 
                return False
        return True
    
    def search(self):
        skip = 0
        text_length = len(self.text)
        pattern_length = len(self.pattern)
        while True:
            print(skip)
            if (text_length - skip) < pattern_length:
                return -1
            if self.same(self.text[skip:], self.pattern, pattern_length):
                return skip
            marker = self.text[skip + pattern_length - 1]
            step = self.table[marker] if marker in self.table else pattern_length
            skip += step

"""
 This is a python-based implementation of the Bayer-Moore-Horespool
 Algorithm for substring search
 
 Copyright (C) 2021  Arnab De <arkrde@gmail.com>
 
 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
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

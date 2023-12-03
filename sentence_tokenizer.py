import string, sys
import re


class DummySentencizer:
    """
    The DummySentencizer is a simple way of sentencizing. It is based on default punctuation characters and uses a special token for splitting.

    Attributes
    ----------
    raw : str
        The raw text string passed as input to be sentencized.
    sentences : list of str
        The list of sentences after sentencizing.

    """

    def __init__(self, input_text, split_characters=['.','?','!',':'], delimiter_token='<SPLIT>'):
        """
        Parameters
        ----------
        input_text : str
            Text to be sentencized. Initialization immediately sentencizes the input text based on the input parameters.
        split_characters : list of str, optional
            List of characters to use as sentence splitter. Default to dot, question mark, exclamation mark and colon.
        delimiter_token : str, optional
            Token to be used to split text. Defaults to '<SPLIT>'. Can be changed if the token word is reserved.

        """

        self.sentences = []
        self.raw = str(input_text)
        self._split_characters=split_characters
        self._delimiter_token=delimiter_token
        self._index=0
        self._sentencize()

    def _sentencize(self):
        work_sentence = self.raw
        for character in self._split_characters:
            work_sentence = work_sentence.replace(character, character+""+self._delimiter_token)
        self.sentences = [x.strip() for x in work_sentence.split(self._delimiter_token) if x !='']

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self.sentences):
            result = self.sentences[self._index]
            self._index+=1
            return result
        raise StopIteration
        
        
        
if __name__ == "__main__":
    ds = DummySentencizer("All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.")
    print(ds.sentences
    
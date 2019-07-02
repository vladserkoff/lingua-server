# pylint: disable = too-few-public-methods
"""
Identify language of a text
"""

from fasttext import load_model
from gensim.parsing.preprocessing import preprocess_string


class Lingua:
    """
    Identify language of a text. Uses facebooks's pretrained
    model, see https://fasttext.cc/blog/2017/10/02/blog-post.html
    """

    def __init__(self, model_path: str) -> None:
        """
        Identify language using fasttext model.

        Parameters
        ----------
        model_path : str
            Path to the trained model.
        """
        self.model = load_model(model_path)

    def identify_language(self, text: str) -> str:
        """
        Identify language of the text.

        Parameters
        ----------
        text : str

        Returns
        -------
        language_code : str
            Language code in lowercase.
        """

        text_processed = preprocess(text)
        language, _ = self.model.predict(text_processed)
        return language[0].replace('__label__', '')


def preprocess(text: str) -> str:
    """
    Preprocess text with standard techniques:
        - remove stopwords
        - remove punctuation
        - lowercase all letters
        - strip whitespaces
        - etc.

    Parameters
    ----------
    text : str
        Unprocessed text.

    Returns
    -------
    text_processed : str
        Precessed text.
    """
    tokens = preprocess_string(text)
    return ' '.join(tokens)

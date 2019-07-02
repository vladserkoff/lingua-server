# pylint: disable = too-few-public-methods, missing-docstring, invalid-name
"""
Know your language.
"""
import falcon

from lingua import Lingua


class IdentifyLanguageResource:
    def __init__(self):
        self.lingua = Lingua(model_path='models/lid.176.ftz')

    def on_get(self, req, resp):
        if req.content_length:
            text = req.stream.read()
        else:
            raise falcon.errors.HTTPBadRequest('Empty request')
        language_code = self.lingua.identify_language(text)
        resp.body = language_code


app = falcon.API()

identify_language = IdentifyLanguageResource()

app.add_route('/identify-language', identify_language)

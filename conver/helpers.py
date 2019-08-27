import requests

class ImportUSDFromExternalAPI:

    url = 'https://api.exchangeratesapi.io/latest'
    #'https://api.exchangeratesapi.io/latest?symbols=BRL&base=USD'
    #'https://api.exchangeratesapi.io/latest?base=USD'


    def import_one(self,currency):
        response = requests.get(self.url + F'?symbols={currency}&base=USD')

        if response.status_code is not 200:
            return False

        resp = response.json()
        return {
            'name': currency,
            'coverage' : resp['rates'][currency],
            'date' : resp['date']
            }

    def import_all(self):
        resp = []
        response = requests.get(self.url + '?base=USD')

        if response.status_code is not 200:
            return False

        text = response.json()
        for key , val in text['rates'].items():
            resp.append({ 'name': key, 'coverage': val})
        return resp

#ImportUSDFromExternalAPI().import_one('BRL')
#ImportUSDFromExternalAPI().import_all()
import requests

def handler(pd: "pipedream"):
    r = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/<word>')
    # Export the data for use in future steps
    return r.json()

result = handler("request")
print(result)
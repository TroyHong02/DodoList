import requests

port = 5000
newlist_url = f'https://localhost{port}/newlist'
getlists_url = f'https://localhost{port}/newlist'

def test_newlist(self):
    # TODO login, json payload
    resp = requests.post(newlist_url)
    print(resp.text)
    
    try:
        json = resp.json()
        assert json.get('status', '') == 'success'
    except:
        self.fail('new list response not json')

    resp = requests.get(getlists_url)
    print(resp.text)
    # hardcoded list name TODO
    assert 'xxx' in resp.text 

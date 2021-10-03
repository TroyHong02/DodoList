import requests

port = 5000
newlist_url = f'http://localhost:{port}/newlist'
getlists_url = f'http://localhost:{port}/getlists'

def test_newlist():
    # TODO login, json payload
    resp = requests.post(newlist_url, json={
        'title': 'blue',
    })
    print(resp.text)
    
    try:
        json = resp.json()
        assert json.get('success', '') == True
    except:
        print('new list response not json')
        return

    resp = requests.get(getlists_url)
    print(resp.text)

if __name__ == '__main__':
    test_newlist()
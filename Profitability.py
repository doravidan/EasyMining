import json
import requests

def check_proditability():
    urlSoa = "http://whattomine.com/coins.json"
    result = requests.get(urlSoa, verify=False)
    coins = json.loads(result.text)
    coins = coins['coins']
    results = []
    for coin in coins:
        if coin == 'Pascalcoin' or coin == 'Decred' or coin == 'Sia' or coin == 'LBRY':
            score = coins[coin]['btc_revenue']
            result = {'coin': coin, 'score': score}
            results.append(result)

    print (results)
    profitable = max(results, key=lambda x:x['score'])
    print("most profitable: " + str(profitable))

    return profitable['coin']



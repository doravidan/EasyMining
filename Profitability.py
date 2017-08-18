import json
import requests
import wmi


def check_proditability(gpu):
    get_user_gpu(gpu)
    url = "http://whattomine.com/coins.json"
    result = requests.get(url, verify=False)
    coins = json.loads(result.text)
    coins = coins['coins']
    results = []
    for coin in coins:
        if coin == 'Pascalcoin' or coin == 'Decred' or coin == 'Sia' or coin == 'LBRY':
            score = coins[coin]['btc_revenue']
            result = {'coin': coin, 'score': score}
            results.append(result)

    print(results)
    profitable = max(results, key=lambda x: x['score'])
    print("most profitable: " + str(profitable))

    return profitable['coin']


def system_prop():
    computer = wmi.WMI()
    gpu_info = computer.Win32_VideoController()[0]
    gpus = ('Graphics Card: {0}'.format(gpu_info.Name))

def get_user_gpu(gpu):
    if gpu == "1060":
        url1060 = "https://whattomine.com/coins?utf8=%E2%9C%93&eth=true&factor%5Beth_hr%5D=21.3&factor%5Beth_p%5D=90.0&grof=true&factor%5Bgro_hr%5D=20.5&factor%5Bgro_p%5D=90.0&x11gf=true&factor%5Bx11g_hr%5D=7.2&factor%5Bx11g_p%5D=90.0&cn=true&factor%5Bcn_hr%5D=430.0&factor%5Bcn_p%5D=70.0&eq=true&factor%5Beq_hr%5D=270.0&factor%5Beq_p%5D=90.0&lre=true&factor%5Blrev2_hr%5D=20300.0&factor%5Blrev2_p%5D=90.0&ns=true&factor%5Bns_hr%5D=500.0&factor%5Bns_p%5D=90.0&lbry=true&factor%5Blbry_hr%5D=170.0&factor%5Blbry_p%5D=90.0&bk2bf=true&factor%5Bbk2b_hr%5D=990.0&factor%5Bbk2b_p%5D=80.0&bk14=true&factor%5Bbk14_hr%5D=1550.0&factor%5Bbk14_p%5D=90.0&pas=true&factor%5Bpas_hr%5D=580.0&factor%5Bpas_p%5D=90.0&bkv=true&factor%5Bbkv_hr%5D=NaN&factor%5Bbkv_p%5D=NaN&factor%5Bcost%5D=0.1&sort=Profitability24&volume=0&revenue=24h&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=bleutrade&factor%5Bexchanges%5D%5B%5D=btc_e&factor%5Bexchanges%5D%5B%5D=bter&factor%5Bexchanges%5D%5B%5D=c_cex&factor%5Bexchanges%5D%5B%5D=cryptopia&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=yobit&dataset=Main&commit=Calculate&adapt_q_280x=1&adapt_q_380=1&adapt_q_fury=1&adapt_q_470=1&adapt_q_480=1&adapt_q_750Ti=1&adapt_q_10606=1&adapt_10606=true&adapt_q_1070=1&adapt_q_1080=1&adapt_q_1080Ti=1"
        requests.get(url1060, verify=False)
    elif gpu == "1070":
        url1070 = "https://whattomine.com/coins?utf8=%E2%9C%93&eth=true&factor%5Beth_hr%5D=171.0&factor%5Beth_p%5D=630.0&grof=true&factor%5Bgro_hr%5D=213.0&factor%5Bgro_p%5D=780.0&x11gf=true&factor%5Bx11g_hr%5D=69.0&factor%5Bx11g_p%5D=720.0&cn=true&factor%5Bcn_hr%5D=3000.0&factor%5Bcn_p%5D=600.0&eq=true&factor%5Beq_hr%5D=2520.0&factor%5Beq_p%5D=720.0&lre=true&factor%5Blrev2_hr%5D=213000.0&factor%5Blrev2_p%5D=780.0&ns=true&factor%5Bns_hr%5D=6300.0&factor%5Bns_p%5D=930.0&lbry=true&factor%5Blbry_hr%5D=1650.0&factor%5Blbry_p%5D=720.0&bk2bf=true&factor%5Bbk2b_hr%5D=9600.0&factor%5Bbk2b_p%5D=720.0&bk14=true&factor%5Bbk14_hr%5D=15000.0&factor%5Bbk14_p%5D=750.0&pas=true&factor%5Bpas_hr%5D=5640.0&factor%5Bpas_p%5D=720.0&bkv=true&factor%5Bbkv_hr%5D=0.0&factor%5Bbkv_p%5D=0.0&factor%5Bcost%5D=0.1&sort=Profitability24&volume=0&revenue=24h&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=bleutrade&factor%5Bexchanges%5D%5B%5D=btc_e&factor%5Bexchanges%5D%5B%5D=bter&factor%5Bexchanges%5D%5B%5D=c_cex&factor%5Bexchanges%5D%5B%5D=cryptopia&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=yobit&dataset=Main&commit=Calculate&adapt_q_280x=0&adapt_q_380=0&adapt_q_fury=0&adapt_q_470=0&adapt_q_480=0&adapt_q_750Ti=0&adapt_q_10606=0&adapt_q_1070=1&adapt_1070=true&adapt_q_1080=0&adapt_q_1080Ti=0"
        requests.get(url1070, verify=False)
    elif gpu == "1080":
        url1080 = "https://whattomine.com/coins?utf8=%E2%9C%93&eth=true&factor%5Beth_hr%5D=23.3&factor%5Beth_p%5D=140.0&grof=true&factor%5Bgro_hr%5D=44.5&factor%5Bgro_p%5D=150.0&x11gf=true&factor%5Bx11g_hr%5D=13.5&factor%5Bx11g_p%5D=145.0&cn=true&factor%5Bcn_hr%5D=580.0&factor%5Bcn_p%5D=100.0&eq=true&factor%5Beq_hr%5D=450.0&factor%5Beq_p%5D=130.0&lre=true&factor%5Blrev2_hr%5D=46500.0&factor%5Blrev2_p%5D=150.0&ns=true&factor%5Bns_hr%5D=1050.0&factor%5Bns_p%5D=150.0&lbry=true&factor%5Blbry_hr%5D=360.0&factor%5Blbry_p%5D=150.0&bk2bf=true&factor%5Bbk2b_hr%5D=2050.0&factor%5Bbk2b_p%5D=150.0&bk14=true&factor%5Bbk14_hr%5D=3300.0&factor%5Bbk14_p%5D=150.0&pas=true&factor%5Bpas_hr%5D=1250.0&factor%5Bpas_p%5D=150.0&bkv=true&factor%5Bbkv_hr%5D=NaN&factor%5Bbkv_p%5D=NaN&factor%5Bcost%5D=0.1&sort=Profitability24&volume=0&revenue=24h&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=bleutrade&factor%5Bexchanges%5D%5B%5D=btc_e&factor%5Bexchanges%5D%5B%5D=bter&factor%5Bexchanges%5D%5B%5D=c_cex&factor%5Bexchanges%5D%5B%5D=cryptopia&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=yobit&dataset=Main&commit=Calculate&adapt_q_280x=1&adapt_q_380=1&adapt_q_fury=1&adapt_q_470=1&adapt_q_480=1&adapt_q_750Ti=1&adapt_q_10606=1&adapt_q_1070=1&adapt_q_1080=1&adapt_1080=true&adapt_q_1080Ti=1"
        requests.get(url1080, verify=False)
    elif gpu == "1080ti":
        url1080ti = "https://whattomine.com/coins?utf8=%E2%9C%93&eth=true&factor%5Beth_hr%5D=35.0&factor%5Beth_p%5D=140.0&grof=true&factor%5Bgro_hr%5D=58.0&factor%5Bgro_p%5D=210.0&x11gf=true&factor%5Bx11g_hr%5D=19.5&factor%5Bx11g_p%5D=170.0&cn=true&factor%5Bcn_hr%5D=830.0&factor%5Bcn_p%5D=140.0&eq=true&factor%5Beq_hr%5D=635.0&factor%5Beq_p%5D=190.0&lre=true&factor%5Blrev2_hr%5D=64000.0&factor%5Blrev2_p%5D=190.0&ns=true&factor%5Bns_hr%5D=1400.0&factor%5Bns_p%5D=190.0&lbry=true&factor%5Blbry_hr%5D=460.0&factor%5Blbry_p%5D=190.0&bk2bf=true&factor%5Bbk2b_hr%5D=2750.0&factor%5Bbk2b_p%5D=190.0&bk14=true&factor%5Bbk14_hr%5D=4350.0&factor%5Bbk14_p%5D=210.0&pas=true&factor%5Bpas_hr%5D=1700.0&factor%5Bpas_p%5D=210.0&bkv=true&factor%5Bbkv_hr%5D=NaN&factor%5Bbkv_p%5D=NaN&factor%5Bcost%5D=0.1&sort=Profitability24&volume=0&revenue=24h&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=bleutrade&factor%5Bexchanges%5D%5B%5D=btc_e&factor%5Bexchanges%5D%5B%5D=bter&factor%5Bexchanges%5D%5B%5D=c_cex&factor%5Bexchanges%5D%5B%5D=cryptopia&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=yobit&dataset=Main&commit=Calculate&adapt_q_280x=1&adapt_q_380=1&adapt_q_fury=1&adapt_q_470=1&adapt_q_480=1&adapt_q_750Ti=1&adapt_q_10606=1&adapt_q_1070=1&adapt_q_1080=1&adapt_q_1080Ti=1&adapt_1080Ti=true"
        requests.get(url1080ti, verify=False)
    elif gpu == "480":
        url480 = "https://whattomine.com/coins?utf8=%E2%9C%93&eth=true&factor%5Beth_hr%5D=28.0&factor%5Beth_p%5D=135.0&grof=true&factor%5Bgro_hr%5D=21.3&factor%5Bgro_p%5D=150.0&x11gf=true&factor%5Bx11g_hr%5D=6.7&factor%5Bx11g_p%5D=140.0&cn=true&factor%5Bcn_hr%5D=730.0&factor%5Bcn_p%5D=110.0&eq=true&factor%5Beq_hr%5D=290.0&factor%5Beq_p%5D=120.0&lre=true&factor%5Blrev2_hr%5D=4900.0&factor%5Blrev2_p%5D=130.0&ns=true&factor%5Bns_hr%5D=650.0&factor%5Bns_p%5D=150.0&lbry=true&factor%5Blbry_hr%5D=105.0&factor%5Blbry_p%5D=175.0&bk2bf=true&factor%5Bbk2b_hr%5D=1150.0&factor%5Bbk2b_p%5D=210.0&bk14=true&factor%5Bbk14_hr%5D=1970.0&factor%5Bbk14_p%5D=190.0&pas=true&factor%5Bpas_hr%5D=700.0&factor%5Bpas_p%5D=135.0&bkv=true&factor%5Bbkv_hr%5D=NaN&factor%5Bbkv_p%5D=NaN&factor%5Bcost%5D=0.1&sort=Profitability24&volume=0&revenue=24h&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=bleutrade&factor%5Bexchanges%5D%5B%5D=btc_e&factor%5Bexchanges%5D%5B%5D=bter&factor%5Bexchanges%5D%5B%5D=c_cex&factor%5Bexchanges%5D%5B%5D=cryptopia&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=yobit&dataset=Main&commit=Calculate&adapt_q_280x=0&adapt_q_380=0&adapt_q_fury=0&adapt_q_470=0&adapt_q_480=1&adapt_480=true&adapt_q_750Ti=0&adapt_q_10606=0&adapt_q_1070=6&adapt_q_1080=0&adapt_q_1080Ti=0"
        requests.get(url480, verify=False)
    elif gpu == "470":
        url470 = "https://whattomine.com/coins?utf8=%E2%9C%93&eth=true&factor%5Beth_hr%5D=24.5&factor%5Beth_p%5D=120.0&grof=true&factor%5Bgro_hr%5D=17.0&factor%5Bgro_p%5D=125.0&x11gf=true&factor%5Bx11g_hr%5D=5.3&factor%5Bx11g_p%5D=125.0&cn=true&factor%5Bcn_hr%5D=660.0&factor%5Bcn_p%5D=100.0&eq=true&factor%5Beq_hr%5D=260.0&factor%5Beq_p%5D=110.0&lre=true&factor%5Blrev2_hr%5D=4400.0&factor%5Blrev2_p%5D=120.0&ns=true&factor%5Bns_hr%5D=600.0&factor%5Bns_p%5D=140.0&lbry=true&factor%5Blbry_hr%5D=80.0&factor%5Blbry_p%5D=140.0&bk2bf=true&factor%5Bbk2b_hr%5D=940.0&factor%5Bbk2b_p%5D=165.0&bk14=true&factor%5Bbk14_hr%5D=1600.0&factor%5Bbk14_p%5D=165.0&pas=true&factor%5Bpas_hr%5D=560.0&factor%5Bpas_p%5D=120.0&bkv=true&factor%5Bbkv_hr%5D=NaN&factor%5Bbkv_p%5D=NaN&factor%5Bcost%5D=0.1&sort=Profitability24&volume=0&revenue=24h&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=bleutrade&factor%5Bexchanges%5D%5B%5D=btc_e&factor%5Bexchanges%5D%5B%5D=bter&factor%5Bexchanges%5D%5B%5D=c_cex&factor%5Bexchanges%5D%5B%5D=cryptopia&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=yobit&dataset=Main&commit=Calculate&adapt_q_280x=1&adapt_q_380=1&adapt_q_fury=1&adapt_q_470=1&adapt_470=true&adapt_q_480=1&adapt_q_750Ti=1&adapt_q_10606=1&adapt_q_1070=1&adapt_q_1080=1&adapt_q_1080Ti=1"
        requests.get(url470, verify=False)




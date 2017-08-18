import subprocess
import time
from Profitability import check_proditability



def init_miner(config):
    first_result = check_proditability(config.gpu)

    #print("start")
    #print("wallet_address: " + config.wallet_address)
    #print("currency: " + config.currency)
    #print("miner: " + config.miner)
    #print("pool: " + config.pool)

    if config.pool == "ethermine":
        config.pool = "eu1.ethermine.org:4444"

    cmd = command(config, first_result)

    # p = subprocess.call(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p = subprocess.Popen(cmd)  # something long running
    run_miner_prof_check(cmd, first_result, config, p)


def run_miner_prof_check(cmd, first_result, config, p):

    result = check_proditability(config.gpu)

    #result = check_proditability(config.gpu)

    time.sleep(3600)
    if result != first_result:
        p.terminate()
        cmd = command(config, result)
        p = subprocess.Popen(cmd)
    run_miner_prof_check(cmd, first_result, config, p)


def command(config, result):
    cmd = ['Claymore\\ethdcrminer64.exe', '-epool', 'eth-eu1.nanopool.org:9999', '-ewal', config.wallet_address_ETH, '-epsw', 'x']

    if result == "Pascalcoin":
        cmd = ['Claymore\\ethdcrminer64.exe', '-epool', 'eu1.ethermine.org:4444', '-ewal', config.wallet_address_ETH, '-epsw', 'x', '-dpool', 'stratum+tcp://pasc-eu1.nanopool.org:15555', '-dwal', config.wallet_address_Pascalcoin, '-dpsw', 'x', '-dcoin', 'pasc']
    elif result == "Decred":
        cmd = ['Claymore\\ethdcrminer64.exe', '-epool', 'eu1.ethermine.org:4444', '-ewal', config.wallet_address_ETH, '-epsw', 'x', '-dpool', 'stratum+tcp://yiimp.ccminer.org:3252', '-dwal', config.wallet_address_Decred, '-dpsw', 'x']
    elif result == "LBRY":
        cmd = ['Claymore\\ethdcrminer64.exe', '-epool', 'eu1.ethermine.org:4444', '-ewal', config.wallet_address_ETH, '-epsw', 'x', '-dpool', 'stratum+tcp://lbry.suprnova.cc:6256', '-dwal', config.suprnova_login_worker, '-dpsw', 'x', '-dcoin', 'lbc']
    elif result == "Sia":
        cmd = ['Claymore\\ethdcrminer64.exe', '-epool', 'eu1.ethermine.org:4444', '-ewal', config.wallet_address_ETH, '-epsw', 'x', '-dpool', 'stratum+tcp://stratum+tcp://eu.siamining.com:7777', '-dwal', config.wallet_address_Sia, '-dpsw', 'x', '-dcoin', 'sia']

    return cmd
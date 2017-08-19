import subprocess
import time
from Profitability import check_proditability


def init_miner(config):
    old_result = check_proditability(config.gpu)
    cmd = command(config, old_result)
    p = subprocess.Popen(cmd)  # something long running
    run_miner_prof_check(cmd, old_result, config, p)


def run_miner_prof_check(cmd, old_result, config, p):
    time.sleep(config.profitability_time_check)
    result = check_proditability(config.gpu)
    if result != old_result:
        p.terminate()
        cmd = command(config, result)
        p = subprocess.Popen(cmd)
        old_result = result
    run_miner_prof_check(cmd, old_result, config, p)


def command(config, result):
    cmd = ['Claymore\\ethdcrminer64.exe', '-epool', 'eth-eu1.nanopool.org:9999', '-ewal', config.wallet_address_ETH, '-epsw', 'x']

    if result == "Pascalcoin":
        cmd = ['Claymore\\ethdcrminer64.exe', '-epool', 'eth-eu1.nanopool.org:9999', '-ewal', config.wallet_address_ETH, '-epsw', 'x', '-dpool', 'stratum+tcp://pasc-eu1.nanopool.org:15555', '-dwal', config.wallet_address_Pascalcoin, '-dpsw', 'x', '-dcoin', 'pasc']
    elif result == "Decred":
        cmd = ['Claymore\\ethdcrminer64.exe', '-epool', 'eth-eu1.nanopool.org:9999', '-ewal', config.wallet_address_ETH, '-epsw', 'x', '-dpool', 'stratum+tcp://yiimp.ccminer.org:4252', '-dwal', config.wallet_address_Decred, '-dpsw', 'x']
    elif result == "LBRY":
        cmd = ['Claymore\\ethdcrminer64.exe', '-epool', 'eth-eu1.nanopool.org:9999', '-ewal', config.wallet_address_ETH, '-epsw', 'x', '-dpool', 'stratum+tcp://lbry.suprnova.cc:6256', '-dwal', config.suprnova_login_worker, '-dpsw', 'x', '-dcoin', 'lbc']
    elif result == "Sia":
        cmd = ['Claymore\\ethdcrminer64.exe', '-epool', 'eth-eu1.nanopool.org:9999', '-ewal', config.wallet_address_ETH, '-epsw', 'x', '-dpool', 'stratum+tcp://sia-eu1.nanopool.org:7777', '-dwal', config.wallet_address_Sia, '-dpsw', 'x', '-dcoin', 'sia']

    return cmd
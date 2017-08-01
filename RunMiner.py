__author__ = 'dor.av'
import os

def init_docker(wallet_address, currency, miner, pool):

    print("start")
    print("wallet_address: " + wallet_address)
    print("currency: " + currency)
    print("miner: " + miner)
    print("pool: " + pool)

    if pool == "ethermine":
        pool = "eu1.ethermine.org:4444"

    command = "start Claymore/ethdcrminer64.exe -epool "+pool+" -ewal "+wallet_address+" -epsw x"
    print(command)
    os.system(command)
    
    
subprocess.call("for i in {1..5}; do echo 1 && sleep 1; done", shell=True)

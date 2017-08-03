import subprocess
import time

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

    cmd = ['Claymore\\ethdcrminer64.exe', '-epool', 'eu1.ethermine.org:4444', '-ewal', '0x89e566af36e7274f0ddd84ba87184e6f3aa2e82f.dor', '-epsw', 'x']
    cmd = ['Claymore\\ethdcrminer64.exe', '-epool']

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    while(not p.poll()):
        time.sleep(1)
        line = p.stdout.readline().rstrip()
        if line != '':
            print(line)
        else:
            break


'''
    cmd = ['Claymore/ethdcrminer64.exe', '-epool', 'eu1.ethermine.org:4444', '-ewal', '0x89e566af36e7274f0ddd84ba87184e6f3aa2e82f.dor', '-epsw', 'x']
    p = subprocess.call(cmd, stdout=subprocess.PIPE, bufsize=1)
    for line in iter(p.stdout.readline, b''):
        print (line),
    p.stdout.close()
    p.wait()
'''



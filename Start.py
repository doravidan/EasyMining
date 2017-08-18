import threading
import Configuration
from RunMiner import init_miner


def start():
    init_miner(Configuration)


def run_start():
    t = threading.Thread(target=start)
    t.daemon = True
    t.start()
    return t

start()
import threading
import Configuration
from RunMiner import init_miner


def start():
    init_miner(Configuration)

start()
from RunMiner import init_docker
from tkinter import *
import threading
from tkinter import ttk
from logs import Std_redirector



def start():
    init_docker(wallet_address.get(), currency.get(), miner.get(), pool.get())

def run_start():
    t = threading.Thread(target=start)
    t.daemon = True
    t.start()
    return t



root = Tk()
root.title("Mining tool")
mainframe = ttk.Frame(root, padding="4 4 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

wallet_address = StringVar()
currency = StringVar()
miner = StringVar()
pool = StringVar()

wallet_address = ttk.Entry(mainframe, width=50, textvariable=wallet_address)
wallet_address.grid(column=1, row=2, sticky=(W, E))

Label(mainframe, text="wallet_address").grid(column=1, row=1, sticky=W)
Label(mainframe, text="what to mine").grid(column=1, row=3, sticky=W)
Label(mainframe, text="choose miner").grid(column=1, row=5, sticky=W)
Label(mainframe, text="choose pool").grid(column=1, row=7, sticky=W)

what_to_mine = ttk.Combobox(mainframe, textvariable=currency)
what_to_mine.grid(column=1, row=4, sticky=(W, E))
what_to_mine['values'] = "ETH"

choose_miner = ttk.Combobox(mainframe, textvariable=miner)
choose_miner.grid(column=1, row=6, sticky=(W, E))
choose_miner['values'] = "claymore"

choose_pool = ttk.Combobox(mainframe, textvariable=pool)
choose_pool.grid(column=1, row=8, sticky=(W, E))
choose_pool['values'] = "ethermine"


Button(mainframe, text="Start", command=run_start).grid(column=2, row=9, sticky=W)


#wallet_address.set('3_nq_8Mq2zwLXS2bcluAyTsPd5AZv1Jtb57ix_T-hV5bGUDUx4AQSflNl8l8Iv0uUJ')

text_area = Text(mainframe, height=22, width=70, bg='light cyan')
text_area.grid(row=10, column=1)
sys.stdout = Std_redirector(text_area)

root.mainloop()
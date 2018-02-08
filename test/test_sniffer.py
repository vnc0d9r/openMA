from core.sniffer import *

def test_sniffer():
    sniffer=Sniffer("data")
    #sniffer.start(interface="wlp3s0", guest_mac="e8:b1:fc:82:b0:c2")
    sniffer.stop()
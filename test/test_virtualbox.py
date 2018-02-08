from core.virtualbox import *

def test_virtualbox():
    virtualbox=VirtualMachine("openma1")
    if virtualbox.check():
        virtualbox.infos()
        virtualbox.start()
        virtualbox.stop()
        virtualbox.restore()
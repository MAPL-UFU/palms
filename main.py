from palms.pnml import parse_pnml_file,write_pnml_file
import numpy as np
from palms.Pnrd import Pnrd

def main():
    pnrd = Pnrd()

    _,ok = pnrd.set_pnml("exemplo1.pnml")
    if ok:
        _,created = pnrd.create_net()
        if created:
            print(pnrd)
            msg, sended = pnrd.update_pnml([1,0,0,0,0,0,0,0])
            print(msg)
            print(pnrd)

if __name__ == "__main__":
    main()
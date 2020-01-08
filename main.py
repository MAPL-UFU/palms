

from pnml.pnml import parse_pnml_file,write_pnml_file


def main():
    nets = parse_pnml_file("exemplo1.pnml")
        
    for net in nets:
        print(net)





if __name__ == "__main__":
    main()
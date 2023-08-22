from PalmsGui import PalmsGui

# pyinstaller --specpath palms.spec -F main.py


def main():
    palms = PalmsGui()
    palms.run()


if __name__ == "__main__":
    main()

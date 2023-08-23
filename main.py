from PalmsGui import PalmsGui

# pyinstaller --specpath palms.spec -F main.py


def main():
    broker = "mqtteste.cloud.shiftr.io"
    port = 1883
    palms = PalmsGui(mqtt_broker=broker, mqtt_port=port)
    print(palms)


if __name__ == "__main__":
    main()

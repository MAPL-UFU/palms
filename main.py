from PalmsGui import PalmsGui

# pyinstaller --specpath palms.spec -F main.py

WIFI_SSID = "PNRD"
WIFI_PASSWORD = "pnrd1234"
BROKER = "pnrd-mqtt.cloud.shiftr.io"
PORT = 1883
USERNAME = "pnrd-mqtt"
PASSWORD = "y05CGL0lcWqciz8N"


def main():
    palms = PalmsGui(
        wifi_ssid=WIFI_SSID,
        wifi_password=WIFI_PASSWORD,
        mqtt_broker=BROKER,
        mqtt_port=PORT,
        mqtt_username=USERNAME,
        mqtt_password=PASSWORD,
    )
    print(palms)


if __name__ == "__main__":
    main()

import nest_asyncio
from PyQt5.QtCore import QThread, pyqtSignal
import paho.mqtt.client as mqtt
import tracemalloc

nest_asyncio.apply()


class MqttThreadQt(QThread):
    msg_status = pyqtSignal(str, dict, name="msg_status")  # define new Signal

    def __init__(
        self, mqtt_broker, mqtt_port, mqtt_username, mqtt_password, readers, parent=None
    ):
        super(MqttThreadQt, self).__init__(parent)
        self.mqtt_broker = mqtt_broker
        self.mqtt_port = mqtt_port
        self.mqtt_username = mqtt_username
        self.mqtt_password = mqtt_password
        self.readers = readers  # Store the readers array
        self.is_running = True
        self.client = mqtt.Client("PALMS")

    def on_connect(client, userdata, flags, rc, properties=None):
        if rc == 0:
            print("Conectado ao MQTT Broker!")
        else:
            print("Falha na conexão, return code %d\n", rc)

    def on_message(self, client, userdata, message):
        payload = message.payload.decode()
        self.msg_status.emit(
            "Receiving data", {"topic": message.topic, "payload": payload}
        )
        print(f"Received message '{payload}' on topic '{message.topic}'")

    def run(self):
        tracemalloc.start()
        if self.mqtt_username != "" and self.mqtt_password != "":
            self.client.username_pw_set(self.mqtt_username, self.mqtt_password)

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.mqtt_broker, self.mqtt_port)

        self.client.subscribe("initTag")  # Subscribe to initTag topic

        # Subscribe to each readerName in the readers list
        for reader in self.readers:
            self.client.subscribe(reader["readerName"])
        if not self.is_running:
            self.client.loop_stop()
            self.client.disconnect()

        self.client.loop_start()

    def stop(self):
        self.is_running = False
        tracemalloc.stop()
        print("Stopping MQTT thread...")
        self.is_running = False
        print("stopping thread...")
        self.client.loop_stop()
        self.client.disconnect()
        self.terminate()
        print("Thread dead")

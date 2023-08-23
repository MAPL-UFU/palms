import nest_asyncio
from PyQt5.QtCore import QThread, pyqtSignal
import asyncio
import paho.mqtt.client as mqtt

nest_asyncio.apply()


class MqttThreadQt(QThread):
    msg_status = pyqtSignal(str, dict, name="msg_status")  # define new Signal

    def __init__(self, mqtt_broker, topic, parent=None):
        super(MqttThreadQt, self).__init__(parent)
        self.mqtt_broker = mqtt_broker
        self.topic = topic
        self.is_running = True

    def on_message(self, client, userdata, message):
        payload = message.payload.decode()
        self.msg_status.emit("Receiving data", {"topic": message.topic, "payload": payload})
        print(f"Received message '{payload}' on topic '{message.topic}'")

    def run(self):
        client = mqtt.Client()
        client.on_message = self.on_message
        client.connect(self.mqtt_broker)
        client.subscribe(self.topic)
        client.loop_start()

        while self.is_running:
            asyncio.sleep(1)  # Just to keep the thread running

        client.loop_stop()
        client.disconnect()

    def stop(self):
        self.is_running = False
        print("Stopping MQTT thread...")

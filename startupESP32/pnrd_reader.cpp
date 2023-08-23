#include <SPI.h>
#include <PN532.h>
#include <PN532_HSU.h>
#include <Pn532NfcReader.h>
#include <NfcAdapter.h>
#include "SPIFFS.h"
#include <WiFi.h>
#include <PubSubClient.h>

const char *FILE_NAME = "/pnrd_initData.txt";
const char *SSID = "YOUR_SSID";
const char *PASSWORD = "YOUR_PASSWORD";
const char *MQTT_SERVER = "YOUR_MQTT_SERVER";
const int MQTT_PORT = YOUR_MQTT_PORT;
const char *MQTT_USER = "YOUR_MQTT_USER";
const char *MQTT_PASSWORD = "YOUR_MQTT_PASSWORD";
const char *MQTT_TOPIC = "YOUR_MQTT_TOPIC";

uint32_t tagId1 = 0xFF;

uint16_t *tokenVector;

uint8_t fire;          // Dynamically loaded from file
uint8_t n_places;      // Dynamically loaded from file
uint8_t n_transitions; // Dynamically loaded from file

bool tagReadyToContinue = false;

String stringToken;

String readerId = MQTT_TOPIC;
PN532_HSU pn532hsu1(Serial1);
NfcAdapter nfc1 = NfcAdapter(pn532hsu1);
Pn532NfcReader *reader1 = new Pn532NfcReader(&nfc1);
Pnrd pnrd1;

WiFiClient espClient;
PubSubClient client(espClient);

void setup_wifi()
{
    delay(10);
    Serial.println();
    Serial.print("Connecting to ");
    Serial.println(SSID);

    WiFi.begin(SSID, PASSWORD);

    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }

    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
}

void callback(char *topic, byte *message, unsigned int length)
{
    Serial.print("Message arrived on topic: ");
    Serial.print(topic);
    Serial.print(". Message: ");
    String messageTemp;

    for (int i = 0; i < length; i++)
    {
        Serial.print((char)message[i]);
        messageTemp += (char)message[i];
    }
    Serial.println();
}

void connect_mqtt()
{
    while (!client.connected())
    {
        String clientId = "client_";
        clientId += MQTT_TOPIC;

        Serial.print("Attempting MQTT connection...");
        Serial.print("Client ID: ");

        Serial.println(clientId);
        if (client.connect(clientId, MQTT_USER, MQTT_PASSWORD))
        {
            Serial.println("connected");
        }
        else
        {
            Serial.print("failed, rc=");
            Serial.print(client.state());
            Serial.println(" try again in 5 seconds");
            delay(5000);
        }
    }
}

void setup()
{
    Serial.begin(9600);

    if (!SPIFFS.begin(true))
    {
        Serial.println("An error has occurred while mounting SPIFFS");
        return;
    }

    File file = SPIFFS.open(FILE_NAME);
    if (!file)
    {
        Serial.println("Failed to open file for reading");
        return;
    }

    String line = file.readStringUntil('\n'); // Read the first line (int_places)
    n_places = line.toInt();
    line = file.readStringUntil('\n'); // Read the second line (int_transitions)
    n_transitions = line.toInt();
    line = file.readStringUntil('\n'); // Read the third line (fire)
    fire = line.toInt();
    file.close();

    pnrd1 = Pnrd(reader1, n_places, n_transitions, false, false, false);

    reader1->initialize();
    pnrd1.setAsTagInformation(PetriNetInformation::TOKEN_VECTOR);
    pnrd1.setAsTagInformation(PetriNetInformation::ADJACENCY_LIST);

    setup_wifi();
    client.setServer(MQTT_SERVER, MQTT_PORT);
    client.setCallback(callback);
}
void palms_comm(
    uint32_t tagId,
    String readerId,
    int antena,
    char ErrorType[100],
    String tokenVector,
    int fireVector)
{
    String mqtt_message = String("I") + String(tagId, HEX) + String("-A") + String(1) + String("-R") + String(readerId) + String("-P") + String(ErrorType) + String("-T[") + String(tokenVector) + String("]") + String("-F") + String(fireVector) + String("-EE");
    client.publish(MQTT_TOPIC, mqtt_message.c_str());
}

void loop()
{
    delay(50);
    if (!client.connected())
    {
        connect_mqtt();
    }
    client.loop();

    ReadError readError1 = pnrd1.getData();
    delay(50);
    if (readError1 == ReadError::NO_ERROR)
    {
        FireError fireError1;
        if (tagId1 != pnrd1.getTagId())
        {
            tagId1 = pnrd1.getTagId();
            FireError fireError1 = pnrd1.fire(fire);
            pnrd1.getTokenVector(tokenVector);
            stringToken = " ";
            for (int32_t place = 0; place < n_places; place++)
            {
                if ((n_places - 1) == place)
                {
                    stringToken += String(tokenVector[place]);
                }
                else
                {
                    stringToken += String(tokenVector[place]);
                    stringToken += ",";
                }
            }
            //------------------------------------
            switch (fireError1)
            {
            case FireError::NO_ERROR:
                if (pnrd1.saveData() == WriteError::NO_ERROR)
                {
                    serial_com(tagId1, readerId, 0, "NO_ERROR", stringToken, 0);
                    return;
                }
                else
                {
                    serial_com(tagId1, readerId, 0, "ERROR_TAG_UPDATE", stringToken, 0);
                    return;
                }

            case FireError::PRODUCE_EXCEPTION:
                serial_com(tagId1, readerId, 0, "PRODUCE_EXCEPTION", stringToken, 0);
                return;

            case FireError::CONDITIONS_ARE_NOT_APPLIED:
                serial_com(tagId1, readerId, 0, "CONDITIONS_ARE_NOT_APPLIED", stringToken, 0);
                break;

            case FireError::NOT_KNOWN:
                serial_com(tagId1, readerId, 0, "NOT_KNOWN", stringToken, 0);
                break;
            }
        }
    }

    Serial.flush();
}
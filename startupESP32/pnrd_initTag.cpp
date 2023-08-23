#include <Pn532NfcReader.h>
#include <SPI.h>
#include <PN532_SPI.h>
#include <PN532.h>
#include <NfcAdapter.h>
#include <WiFi.h>
#include "SPIFFS.h"
#include "FS.h"

#define SSID "your_wifi_ssid"
#define PASSWORD "your_wifi_password"
#define FILE_NAME "/pnrd_reader.txt"

PN532_SPI pn532spi(SPI, 10);
NfcAdapter nfc = NfcAdapter(pn532spi);
Pn532NfcReader *reader = new Pn532NfcReader(&nfc);
Pnrd *pnrd;

void connectToWiFi()
{
    WiFi.begin(SSID, PASSWORD);
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }
    Serial.println("Connected to WiFi");
}

void setup()
{
    Serial.begin(9600);

    connectToWiFi();

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

    int int_places = file.parseInt();
    int int_transitions = file.parseInt();
    int size_mIncidenceMatrix = file.parseInt();
    int size_mStartingTokenVector = file.parseInt();

    int8_t *mIncidenceMatrix = new int8_t[size_mIncidenceMatrix];
    uint16_t *mStartingTokenVector = new uint16_t[size_mStartingTokenVector];

    for (int i = 0; i < size_mIncidenceMatrix; i++)
    {
        mIncidenceMatrix[i] = file.parseInt();
    }

    for (int i = 0; i < size_mStartingTokenVector; i++)
    {
        mStartingTokenVector[i] = file.parseInt();
    }

    file.close();

    reader->initialize();

    // pnrd.setGoalToken(goalToken);
    pnrd = new Pnrd(reader, int_places, int_transitions, false, false, false);

    pnrd->setIncidenceMatrix(mIncidenceMatrix);
    pnrd->setTokenVector(mStartingTokenVector);
    pnrd->setAsTagInformation(PetriNetInformation::TOKEN_VECTOR);
    pnrd->setAsTagInformation(PetriNetInformation::ADJACENCY_LIST);

    Serial.print("\n\nInitial recording of PNRD tags.");
}

void loop()
{
    if (Serial.available() > 0)
    {
        int incomingByte = Serial.read();

        Serial.print("I received: ");
        Serial.println(incomingByte, DEC);
    }

    delay(1000);
    Serial.println("Place a tag near the reader.");

    if (pnrd->saveData() == WriteError::NO_ERROR)
    {
        Serial.println("Tag configurated successfully.");
    }

    Serial.print("\n\n");
    delay(1000);
}

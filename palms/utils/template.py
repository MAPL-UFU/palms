


def init_template(n_places,n_transitions,IncidenceMatrix,StartingTokenVector):
    return f'\n\
        #include <Pn532NfcReader.h>                                     \n\
        #include <SPI.h>                                                \n\
        #include <PN532_SPI.h>                                          \n\
        #include <PN532.h>                                              \n\
        #include <NfcAdapter.h>                                         \n\
                                                                        \n\
        int8_t mIncidenceMatrix[] = {{{IncidenceMatrix}}};              \n\
        uint16_t mStartingTokenVector[] = {{{StartingTokenVector}}};    \n\
                                                                        \n\
        int incomingByte = 0;                                           \n\
                                                                        \n\
        PN532_SPI pn532spi(SPI, 10);                                    \n\
        NfcAdapter nfc = NfcAdapter(pn532spi);                          \n\
                                                                        \n\
        Pn532NfcReader* reader = new Pn532NfcReader(&nfc);              \n\
        Pnrd pnrd = Pnrd(reader,{n_places},{n_transitions}, false, false, false);            \n\
                                                                        \n\
                                                                        \n\
        void setup() {{                                                 \n\
//Initialization of the communication with the reader and with the computer Serial bus\n\
        Serial.begin(9600);                                             \n\
        reader->initialize();                                           \n\
                                                                        \n\
        // pnrd.setGoalToken(tokenDesejado);                            \n\
        pnrd.setIncidenceMatrix(mIncidenceMatrix);                      \n\
        pnrd.setTokenVector(mStartingTokenVector);                      \n\
                                                                        \n\
        // pnrd.setAsTagInformation(PetriNetInformation::GOAL_TOKEN);   \n\
        pnrd.setAsTagInformation(PetriNetInformation::TOKEN_VECTOR);    \n\
        pnrd.setAsTagInformation(PetriNetInformation::ADJACENCY_LIST);  \n\
                                                                        \n\
        Serial.print("\\n\\nInitial recording of PNRD tags.");          \n\
                                                                        \n\
        }}                                                              \n\
                                                                        \n\
        void loop() {{                                                  \n\
        if (Serial.available() > 0) {{                                  \n\
            incomingByte = Serial.read();                               \n\
                                                                        \n\
            Serial.print("I received: ");                               \n\
            Serial.println(incomingByte, DEC);                          \n\
    }}                                                                  \n\
        delay(1000);                                                    \n\
        Serial.println("Place a tag near the reader.");                 \n\
                                                                        \n\
        if(pnrd.saveData() == WriteError::NO_ERROR){{                   \n\
                Serial.println("Tag configurated successfully.");       \n\
                                                                        \n\
        }};                                                             \n\
                                                                        \n\
        Serial.print("\\n\\n");                                         \n\
        delay(1000);                                                    \n\
                                                                        \n\
        }}                                                              \n\
        '



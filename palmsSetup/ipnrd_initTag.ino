
        #include <Pn532NfcReader.h>         
        #include <PN532_HSU.h>              
        #include <PN532.h>              
        #include <SPI.h>                
        #include <PN532_SPI.h>              
        #include <NfcAdapter.h>    
            
        uint16_t mFireVector[] = {1,0,0,0,0,0,0,0};
        uint8_t n_places = 7;
        uint8_t n_transitions = 8;
        //Rotines related with the configuration of the RFID reader PN532      
        PN532_SPI pn532spi(SPI, 10);                
        NfcAdapter nfc = NfcAdapter(pn532spi); 
        
        //Creation of the reader and PNRD objects
        Pn532NfcReader* reader = new Pn532NfcReader(&nfc);
        Pnrd pnrd = Pnrd(reader,n_places,n_transitions, false, false,false);
        
        void setup() {  
        //Initialization of the communication with the reader and with the computer Serial bus
        Serial.begin(9600); 
        reader->initialize();      
        
        //Defining the fire vector to be recorded
        pnrd.setFireVector(mFireVector);
        
        //Setting of the classic iPNRD approach 
        pnrd.setAsTagInformation(PetriNetInformation::FIRE_VECTOR);
        Serial.print("\nInitial recording of iPNRD tags.");
        }
        
        void loop() {
        
        Serial.println("Place a tag near the reader.");
        
        if(pnrd.saveData() == WriteError::NO_ERROR){
                Serial.println("Tag configurated successfully.");
        };
        
        Serial.print("
"); 
        delay(1000); 
        
        }

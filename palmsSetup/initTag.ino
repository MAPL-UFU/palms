
        #include <Pn532NfcReader.h>                                     
        #include <SPI.h>                                                
        #include <PN532_SPI.h>                                          
        #include <PN532.h>                                              
        #include <NfcAdapter.h>                                         
                                                                        
        int8_t mIncidenceMatrix[] = {-1,0,0,0,1,-1,0,0,1,-1,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,1,-1,0,0,1,-1,-1,0,0,1,0,0,0,1,0,0,0,0};              
        uint16_t mStartingTokenVector[] = {0,5,1,0,0,0,6};    
                                                                        
        int incomingByte = 0;                                           
                                                                        
        PN532_SPI pn532spi(SPI, 10);                                    
        NfcAdapter nfc = NfcAdapter(pn532spi);                          
                                                                        
        Pn532NfcReader* reader = new Pn532NfcReader(&nfc);              
        Pnrd pnrd = Pnrd(reader,7,8, false, false, false);            
                                                                        
                                                                        
        void setup() {                                                 
//Initialization of the communication with the reader and with the computer Serial bus
        Serial.begin(9600);                                             
        reader->initialize();                                           
                                                                        
        // pnrd.setGoalToken(tokenDesejado);                            
        pnrd.setIncidenceMatrix(mIncidenceMatrix);                      
        pnrd.setTokenVector(mStartingTokenVector);                      
                                                                        
        // pnrd.setAsTagInformation(PetriNetInformation::GOAL_TOKEN);   
        pnrd.setAsTagInformation(PetriNetInformation::TOKEN_VECTOR);    
        pnrd.setAsTagInformation(PetriNetInformation::ADJACENCY_LIST);  
                                                                        
        Serial.print("\n\nInitial recording of PNRD tags.");          
                                                                        
        }                                                              
                                                                        
        void loop() {                                                  
        if (Serial.available() > 0) {                                  
            incomingByte = Serial.read();                               
                                                                        
            Serial.print("I received: ");                               
            Serial.println(incomingByte, DEC);                          
    }                                                                  
        delay(1000);                                                    
        Serial.println("Place a tag near the reader.");                 
                                                                        
        if(pnrd.saveData() == WriteError::NO_ERROR){                   
                Serial.println("Tag configurated successfully.");       
                                                                        
        };                                                             
                                                                        
        Serial.print("\n\n");                                         
        delay(1000);                                                    
                                                                        
        }                                                              
        
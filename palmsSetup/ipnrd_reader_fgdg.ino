        #include <Pn532NfcReader.h>         
        #include <PN532_HSU.h>              
        #include <PN532.h>              
        #include <SPI.h>                
        #include <PN532_SPI.h>              
        #include <NfcAdapter.h>             
                        
        int8_t mIncidenceMatrix[] = {-1,0,0,0,1,-1,0,0,1,-1,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,1,-1,0,0,1,-1,-1,0,0,1,0,0,0,1,0,0,0,0};              
        uint16_t mStartingTokenVector[] = {1,0,0,0,0,0,0};    
                        
        uint32_t tagId = 0xFF;             
        String readerId = "fgdg";               
        uint16_t * tokenVector;             
        uint16_t * fireVector;             
        uint8_t n_places = 7;      
        uint8_t n_transitions = 8;               
        uint8_t position_fire;             
        int antenna = 1;                                                   
        bool tagReadyToContinue = false;                
        String stringToken;             
                        
        //Rotines related with the configuration of the RFID reader PN532               
        PN532_SPI pn532spi(SPI, 10);                
        NfcAdapter nfc = NfcAdapter(pn532spi);                     
        //Creation of the reader and PNRD objects               
        Pn532NfcReader* reader = new Pn532NfcReader(&nfc);                
        Pnrd pnrd = Pnrd(reader,n_places,n_transitions,false,false,false);                
        // -----------------------------------------------------------------------              
                        
        void setup() {                 
        //Initialization of the communication with the reader and with the computer Serial bus                
        Serial.begin(9600);                   
        reader->initialize();                    
        pnrd.setTokenVector(mStartingTokenVector);
        pnrd.setIncidenceMatrix(mIncidenceMatrix);

        //Setting of the classic iPNRD approach 
        pnrd.setAsTagInformation(PetriNetInformation::FIRE_VECTOR);

        pnrd.setDeviceId(1);
                        
        }               
        void serial_com(                
            uint32_t tagId,               
            String readerId,                
            int antenna,              
            char ErrorType[100],              
            String tokenVector,               
            int fireVector=position_fire              
            ){             
        Serial.println(String("I") + String(tagId,HEX) + String("-A") + String(antenna) + String("-R") + String(readerId) + String("-P")+ String(ErrorType)+ String("-T[") + String(tokenVector)+ String("]")+ String("-F")+ String(fireVector)+String("-EE"));               
        }               
                        
        void loop() {              
        delay(50);               
                        
        ReadError readError = pnrd.getData();               
        delay(50);               
        if(readError == ReadError::NO_ERROR){               
            FireError fireError;               
            // pnrd.printTokenVector();                
                        
            //verifica se é uma nova tag                
            if(tagId != pnrd.getTagId()){              
                tagId = pnrd.getTagId();                
                FireError fireError = pnrd.fire();             
                        
                //get token Vector                
                pnrd.getTokenVector(tokenVector);                
                stringToken = " ";                
                for (int32_t place = 0; place < n_places; place++) {             
                    if ((n_places -1) == place){             
                        stringToken += String(tokenVector[place]);              
                    }             
                    else{            
                        stringToken += String(tokenVector[place]);              
                        stringToken += ",";             
                    }             
                }             
                //------------------------------------                
                pnrd.getFireVector(fireVector);                     
                for (uint32_t  transition = 0; transition < n_transitions; transition++) {
                    if(fireVector[transition]==1){
                        position_fire = transition;
                        break;
                    };	        
                }
                        
                switch (fireError){             
                    case FireError::NO_ERROR :                
                        //Atualizando a tag             
                        if(pnrd.saveData() == WriteError::NO_ERROR){              
                            // pnrd.printGoalToken();                
                            serial_com(tagId,readerId,antenna,"NO_ERROR",stringToken);             
                            return;               
                        }else{             
                            serial_com(tagId,readerId,antenna,"ERROR_TAG_UPDATE",stringToken);             
                            return;               
                        }               
                        
                    case FireError::PRODUCE_EXCEPTION :               
                        serial_com(tagId,readerId,antenna,"PRODUCE_EXCEPTION",stringToken);                
                    return;               
                        
                    case FireError::CONDITIONS_ARE_NOT_APPLIED :              
                        serial_com(tagId,readerId,antenna,"CONDITIONS_ARE_NOT_APPLIED",stringToken);               
                    break;                
                        
                    case FireError::NOT_KNOWN:                
                        serial_com(tagId,readerId,antenna,"NOT_KNOWN",stringToken);              
                    break;                
                }                 
            }             
        }             
        Serial.flush();
        }
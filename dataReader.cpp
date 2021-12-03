#include "dataStorage.hpp"
#include <fstream>
#include <string.h>

int main() {
    ifstream dataFile;
    DataStorage dataStorage[20];
    string buffer; 
    string buffCh, nameBuffer;
    
    strcpy((char*)nameBuffer.c_str(), "");
    dataFile.open("akiyo.txt");

    for (int i = 0; i < 5; i ++)
        getline(dataFile, buffer);
        
    
    for (int i = 0; i < 20; i ++){
        strcpy((char*)nameBuffer.c_str(), "");
        strcpy((char*)buffCh.c_str(), "");
        
        getline(dataFile, buffer);
        
        
        dataStorage[i].insertPercentageTime(atof(strtok((char*)buffer.c_str(), " \t")));
        dataStorage[i].insertCumulativeTime(atof(strtok(NULL, " \t")));
        dataStorage[i].insertSelfTime(atof(strtok(NULL, " \t")));
        dataStorage[i].insertCalls(atoi(strtok(NULL, " \t")));
        dataStorage[i].insertSelfSCall(atof(strtok(NULL, " \t")));
        dataStorage[i].insertTotalSCall(atof(strtok(NULL, " \t")));
        
        do{
            buffCh = strtok(NULL, " \t\n");
            
        
            if((char*)buffCh.c_str() != NULL){
                strcat((char*)nameBuffer.c_str(), (char*)buffCh.c_str());
                cout << "hello" << endl;
            }
        } while ((char*)buffCh.c_str() != NULL);strcpy((char*)nameBuffer.c_str(), "");
        cout << nameBuffer << endl;
        dataStorage[i].insertName(nameBuffer);

        

        dataStorage[i].showData();
    }
    


    dataFile.close();
    return 0;
}
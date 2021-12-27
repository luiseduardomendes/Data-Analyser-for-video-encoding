#include "dataStorage.hpp"
#include <fstream>
#include <string>
#include <cstring>

int main() {
    ifstream dataFile;
    DataStorage dataStorage[20];
    string buffer; 
    char *buffCh, *nameBuffer;
    
    strcpy(nameBuffer, "");
    dataFile.open("akiyo.txt");

    for (int i = 0; i < 5; i ++)
        getline(dataFile, buffer);
        
    
    for (int i = 0; i < 20; i ++){
        strcpy(nameBuffer, "");
        strcpy(buffCh, "");
        
        getline(dataFile, buffer);
        
        
        dataStorage[i].insertPercentageTime(atof(strtok((char*)buffer.c_str(), " \t")));
        dataStorage[i].insertCumulativeTime(atof(strtok(NULL, " \t")));
        dataStorage[i].insertSelfTime(atof(strtok(NULL, " \t")));
        dataStorage[i].insertCalls(atoi(strtok(NULL, " \t")));
        dataStorage[i].insertSelfSCall(atof(strtok(NULL, " \t")));
        dataStorage[i].insertTotalSCall(atof(strtok(NULL, " \t")));
        
        do{
            buffCh = strtok(NULL, " \t\n");
        
            if(buffCh != NULL){
                strcat(nameBuffer, buffCh);
                cout << "hello" << endl;
            }
        } while (buffCh != NULL);strcpy(nameBuffer, "");
        cout << nameBuffer << endl;
        dataStorage[i].insertName(nameBuffer);

        dataStorage[i].showData();
    }
    


    dataFile.close();
    return 0;
}
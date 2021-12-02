#include <iostream>
#include <vector>
#include <cstdlib>
#include "dataStorage.hpp"

using namespace std;

int main(){
    DataStorage *dataStorage = new DataStorage[20];

    for (int i = 0; i < 4; i ++){
        dataStorage[i].insertName("Function");     
        dataStorage[i].insertPercentageTime(rand());
        dataStorage[i].insertCumulativeTime(rand());
        dataStorage[i].insertSelfTime(rand());
        dataStorage[i].insertCalls(rand());
        dataStorage[i].insertSelfSCall(rand());
        dataStorage[i].insertTotalSCall(rand());
    }

    for (int i = 0; i < 4; i ++){
        dataStorage[i].showData();
    }



    return 0;
}  
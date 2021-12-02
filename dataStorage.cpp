#include "dataStorage.hpp"

void DataStorage::insertName(string name_){
    dataStruct.name = name_;
}

void DataStorage::insertPercentageTime(float percentageTime_) {
    dataStruct.funcInfo.percentageTime = percentageTime_;
}
        
void DataStorage::insertCumulativeTime(float cumulativeTime_) {
    dataStruct.funcInfo.cumulativeTime = cumulativeTime_;
}

void DataStorage::insertSelfTime(float selfTime_){
    dataStruct.funcInfo.selfTime = selfTime_;
}

void DataStorage::insertCalls(int calls_) {
    dataStruct.funcInfo.calls = calls_;
}

void DataStorage::insertSelfSCall(float selfSCall_) {
    dataStruct.funcInfo.selfSCall = selfSCall_;
}

void DataStorage::insertTotalSCall(float totalSCall_) {
    dataStruct.funcInfo.totalSCall = totalSCall_;
}

void DataStorage::showData() {
    cout << dataStruct.name << endl;
    cout << dataStruct.funcInfo.percentageTime << endl;
    cout << dataStruct.funcInfo.cumulativeTime << endl;
    cout << dataStruct.funcInfo.selfSCall << endl;
    cout << dataStruct.funcInfo.calls << endl;
    cout << dataStruct.funcInfo.selfTime << endl;
    cout << dataStruct.funcInfo.totalSCall << endl << endl;
}
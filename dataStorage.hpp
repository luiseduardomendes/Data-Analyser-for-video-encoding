#pragma once
#include <iostream>
#include <vector>
using namespace std;

typedef struct {
    float percentageTime;
    float cumulativeTime;
    float selfTime;
    int calls;
    float selfSCall;
    float totalSCall;
} t_functionInfo;

typedef struct {
    t_functionInfo funcInfo;
    string name;
} t_dataStruct;



class DataStorage{
private:
    t_dataStruct dataStruct;

public:
    void insertName(string name_);
    void insertPercentageTime(float percentageTime_);
    void insertCumulativeTime(float cumulativeTime_);
    void insertSelfTime(float selfTime_);
    void insertCalls(int calls_);
    void insertSelfSCall(float selfSCall_);
    void insertTotalSCall(float totalSCall_);
    void showData();


};

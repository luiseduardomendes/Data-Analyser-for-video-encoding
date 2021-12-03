#include "dataStorage.hpp"
#include <fstream>

int jumpLines(int n, ifstream f){
    string buffer;
    int flag;
    for (int i = 0; i < n; i ++){
        getline(f, buffer);
        if (f.eof()){
            flag = 0;
        }
    }
    return flag;
}


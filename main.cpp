#include <iostream>
#include <fstream>
#include <string>

void readLogFile(const std::string &filePath) {
    std::ifstream logFile(filePath);
    std::string line;

    if (logFile.is_open()) {
        while (std::getline(logFile, line)) {
            std::cout << "Log Entry: " << line << std::endl;
        }
        logFile.close();
    } else {
        std::cerr << "Unable to open file" << std::endl;
    }
}

int main() {
    readLogFile("logs/sample_log.txt");
    return 0;
}
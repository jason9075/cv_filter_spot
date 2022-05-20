// Your First C++ Program
#include <opencv2/opencv.hpp>
#include <iostream>
#include "Math.h"

int main(int argc, char** argv ) {
    int result = Multiply(3,2);
    std::cout << result; 
    cv::Mat image;
    image = cv::imread( argv[1], 1 );
    return 0;
}


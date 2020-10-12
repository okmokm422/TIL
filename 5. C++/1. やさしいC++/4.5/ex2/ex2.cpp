#include <iostream>
using namespace std;

int main()
{
    double h = 1;
    double w = 5;

    cout << "三角形の高さを入力してください。\n";
    cin >> h;
    cout << "三角形の底辺を入力してください。\n";
    cin >> w;
    cout << "三角形の面積は" << h * w / 2 << "です。\n";

    return 0;
}
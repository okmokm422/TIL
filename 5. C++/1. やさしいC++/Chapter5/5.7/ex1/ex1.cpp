#include <iostream>
using namespace std;

int main()
{
    int num;

    cout << "整数を入力してください。\n";

    cin >> num;

    if (num % 2)
        cout << num << "は奇数です\n";
    else
        cout << num << "は偶数です。\n";

    return 0;
}
#include <iostream>
using namespace std;

int main()
{
    cout << "1〜10までの偶数を出力します。\n";

    for (int i = 1; i <= 10; i++)
    {
        if ((i % 2) == 0)
            cout << i << "\n";
    }
    return 0;
}
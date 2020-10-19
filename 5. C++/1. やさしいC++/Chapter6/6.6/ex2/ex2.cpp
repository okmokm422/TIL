#include <iostream>
using namespace std;

int main()
{

    int score, sum = 0;

    cout << "テストの点数を入力してください。（0で終了）\n";
    do
    {
        cin >> score;
        sum += score;
    } while (score);

    cout << "テストの合計点は" << sum << "点です。\n";

    return 0;
}
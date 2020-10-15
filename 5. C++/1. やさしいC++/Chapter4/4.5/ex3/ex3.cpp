#include <iostream>
using namespace std;

int main()
{
    int sum = 0, num = 0;
    cout << "科目１の点数を入力してください。\n";
    cin >> num;
    sum += num;
    cout << "科目２の点数を入力してください。\n";
    cin >> num;
    sum += num;
    cout << "科目３の点数を入力してください。\n";
    cin >> num;
    sum += num;
    cout << "科目４の点数を入力してください。\n";
    cin >> num;
    sum += num;
    cout << "科目５の点数を入力してください。\n";
    cin >> num;
    sum += num;

    cout << "５科目の合計点は" << sum << "です。\n";
    cout << "５科目の平均点は" << (double)sum / 5 << "です。\n";

    return 0;
}
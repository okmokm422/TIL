#include <iostream>
using namespace std;

// max関数の定義
inline int max(int x, int y)
{
    if (x > y)
        return x;
    else
        return y;
}

int main()
{
    int num1, num2, ans;

    cout << "1番目の整数を入力してください。\n";
    cin >> num1;

    cout << "2番目の整数を入力してください。\n";
    cin >> num2;

    ans = max(num1, num2); // インライン関数として埋め込み

    cout << "最大値は" << ans << "です。\n";

    return 0;
}
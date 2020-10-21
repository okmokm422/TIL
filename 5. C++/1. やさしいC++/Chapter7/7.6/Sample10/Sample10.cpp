// 関数プロトタイプ宣言を使う
// 関数の定義を関数の呼び出しより後に記述してみる

#include <iostream>
using namespace std;

// max関数の宣言
int max(int x, int y);

// max関数の呼び出し
int main()
{
    int num1, num2, ans;

    cout << "1番目の整数を入力してください。\n";
    cin >> num1;

    cout << "2番目の整数を入力してください。\n";
    cin >> num2;

    ans = max(num1, num2);

    cout << "最大値は" << ans << "です。\n";

    return 0;
}

// max関数の定義
int max(int x, int y)
{
    if (x > y)
        return x;
    else
        return y;
}
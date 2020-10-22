#include <iostream>
using namespace std;

// 関数の宣言
int square(int x);

// 関数の呼び出し
int main()
{

    int num, ans;

    cout << "整数を入力してください。\n";
    cin >> num;

    ans = square(num);

    cout << num << "の2乗は" << ans << "です。\n";
}

// 関数の定義
int square(int x)
{
    return x * x;
}
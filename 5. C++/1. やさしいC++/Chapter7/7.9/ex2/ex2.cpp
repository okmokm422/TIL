#include <iostream>
using namespace std;

// 関数の宣言
int square(int x);
double square(double x);

// 関数の呼び出し
int main()
{

    int num1, ans1;
    double num2, ans2;

    cout << "整数を入力してください。\n";
    cin >> num1;
    ans1 = square(num1);
    cout << num1 << "の2乗は" << ans1 << "です。\n";

    cout << "小数を入力してください。\n";
    cin >> num2;
    ans2 = square(num2);
    cout << num2 << "の2乗は" << ans2 << "です。\n";
}

// 関数の定義
int square(int x)
{
    return x * x;
}

double square(double x)
{
    return x * x;
}
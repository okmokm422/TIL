// 関数のオーバーロード
// 引数の型や数が異なり、同じ名前を持つ関数を複数定義する

#include <iostream>
using namespace std;

int main()
{
    int a, b;
    double da, db;

    cout << "2つの整数を入力してください。\n";
    cin >> a >> b;

    cout << "2つの小数を入力してください。\n";
    cin >> da >> db;

    int ans1 = max(a, b);
    double ans2 = max(da, db);

    cout << "整数値の最大値は" << ans1 << "です。\n";
    cout << "小数値の最大値は" << ans2 << "です。\n";

    return 0;
}

// max(int型)関数の定義
int max(int x, int y)
{

    if (x > y)
        return x;
    else
        return y;
}

double max(double x, double y)
{

    if (x > y)
        return x;
    else
        return y;
}
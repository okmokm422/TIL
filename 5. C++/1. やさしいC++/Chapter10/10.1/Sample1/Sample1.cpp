#include <iostream>
using namespace std;

// func関数の宣言
void func();

int a = 0;

// main関数
int main() {
    int b = 1;
    cout << "main関数では変数aとbが使えます。\n";
    cout << "グローバル変数aの値は" << a << "です。\n";
    cout << "ローカル変数bの値は" << b << "です。\n";

    func();

    return 0;
}

// func関数の定義
void func() {
    int c = 2;

    cout << "func関数ではaとcが使えます。\n";
    cout << "グローバル変数aの値は" << a << "です。\n";
    cout << "ローカル変数cの値は" << c << "です。\n";
}
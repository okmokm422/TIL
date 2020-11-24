#include <iostream>
using namespace std;

// fun関数の宣言
void func();

int a = 0;

// main関数
int main() {
    for (int i = 0; i < 5; i++) func();
    return 0;
}

// func関数の定義
void func() {
    int b = 0;
    static int c = 0;

    cout << "grobal変数aは" << a << "local変数bは" << b << "static変数cは" << c
         << "です。\n";
    a++;
    b++;
    c++;
}
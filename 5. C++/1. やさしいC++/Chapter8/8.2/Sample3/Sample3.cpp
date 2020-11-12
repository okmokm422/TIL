// ポインタにアドレスを格納する
#include <iostream>
using namespace std;

int main() {
    int a;
    int* pA;  // ポインタの宣言

    a = 5;
    pA = &a;  // ポインタにアドレスを格納する

    cout << "変数aの値は" << a << "です。\n";
    cout << "変数aのアドレス（&a）は" << &a << "です。\n";
    cout << "ポインタpAの値は" << pA << "です。\n";

    return 0;
}
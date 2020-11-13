// 誤った関数

#include <iostream>
using namespace std;

// swap関数の宣言
void swap(int* pX, int* pY);

int main() {
    int num1 = 5;
    int num2 = 10;

    cout << "変数num1の値は" << num1 << "です。\n";
    cout << "変数num2の値は" << num2 << "です。\n";
    cout << "変数num1とnum2の値を交換します。\n";

    swap(&num1, &num2);
    // 変数を参照渡し

    cout << "変数num1の値は" << num1 << "です。\n";
    cout << "変数num2の値は" << num2 << "です。\n";

    return 0;
}

// swap関数の定義
// 仮引数をポインタとして定義する
void swap(int* pX, int* pY) {
    int tmp;

    tmp = *pX;
    *pX = *pY;
    *pY = tmp;
}
// 誤った関数

#include <iostream>
using namespace std;

// 誤ったswap関数の宣言
void swap(int x, int y);

int main() {
    int num1 = 5;
    int num2 = 10;

    cout << "変数num1の値は" << num1 << "です。\n";
    cout << "変数num2の値は" << num2 << "です。\n";
    cout << "変数num1とnum2の値を交換します。\n";

    swap(num1, num2);
    // 変数の中身5と10が渡される（値渡し）
    // swap()関数内で値を交換しても、呼び出し元の変数num1とnum2には影響がない

    cout << "変数num1の値は" << num1 << "です。\n";
    cout << "変数num2の値は" << num2 << "です。\n";

    return 0;
}

// 誤ったswap関数の定義
void swap(int x, int y) {
    int tmp;

    tmp = x;
    x = y;
    y = tmp;
}
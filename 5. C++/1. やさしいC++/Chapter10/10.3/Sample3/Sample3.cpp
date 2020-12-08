// 動的にメモリを確保する

#include <iostream>
using namespace std;

int main() {
    int* pA;  // ポインタを用意
    pA = new int;  // new演算子で動的にメモリを確保, アドレスを代入

    cout << "動的にメモリを確保しました\n";

    *pA = 10;

    cout << "動的に確保したメモリを使って" << *pA << "を出力しています。\n";

    delete pA;  // メモリを解放

    cout << "確保したメモリを開放しました。\n";

    return 0;
}
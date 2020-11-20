// 文字列が配列であることを利用して操作
#include <iostream>
using namespace std;

int main() {
    char str[] = "Hello";
    cout << "Hello\n";

    // 文字列が\0（終わり）でない限り繰り返す
    for (int i = 0; str[i] != '\0'; i++) {
        cout << str[i] << '*';
    }
    cout << '\n';

    return 0;
}
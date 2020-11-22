#include <iostream>
using namespace std;

// length関数の宣言
int length(char* str);

// 処理実行
int main() {
    char str[100];
    cout << "文字列を入力してください。\n";
    cin >> str;
    int ln = length(str);
    cout << "文字列の長さは" << ln << "です。\n";

    return 0;
}

// lenght関数の定義
int length(char* str) {
    int i = 0;
    while (str[i]) {
        i++;
    }
    return i;
}
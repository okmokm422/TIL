// 配列の要素をソートする
#include <iostream>
using namespace std;

int main() {
    const int num = 5;
    int test[num];

    cout << num << "人の点数を入力してください。\n";
    for (int i = 0; i < num; i++) {
        cin >> test[i];
    }

    // s=0,1,2,3 t=1,2,3,4
    for (int s = 0; s < num - 1; s++) {
        for (int t = s + 1; t < num; t++) {
            // test[1] > test[0]スタートでインクリメント
            if (test[t] > test[s]) {
                // 入れ替え
                int tmp = test[t];
                test[t] = test[s];
                test[s] = tmp;
            }
        }
    }
    for (int j = 0; j < num; j++) {
        cout << j + 1 << "番目の人の点数は" << test[j] << "です。\n";
    }
    return 0;
}
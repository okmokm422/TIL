#include <iostream>
using namespace std;

int main()
{
    int grade;

    cout << "成績を入力してください。\n";
    cin >> grade;
    cout << "成績は" << grade << "です。\n";

    switch (grade)
    {
    case 1:
        cout << "成績は1です。もっと頑張りましょう。\n";
        break;
    case 2:
        cout << "成績は2です。もう少し頑張りましょう。\n";
        break;
    case 3:
        cout << "成績は3です。さらに上を目指しましょう。\n";
        break;
    case 4:
        cout << "成績は4です。たいへんよくできました。\n";
        break;
    case 5:
        cout << "成績は5です。たいへん優秀です。\n";
        break;
    }

    return 0;
}
#include <iostream>
using namespace std;

int main()
{
    int grade;

    cout << "成績を入力してください。\n";
    cin >> grade;

    if (grade == 1)
    {
        cout << "成績は1です。もっと頑張りましょう。\n";
    }
    else if (grade == 2)
    {
        cout << "成績は2です。もう少し頑張りましょう。\n";
    }
    else if (grade == 3)
    {
        cout << "成績は3です。さらに上を目指しましょう。\n";
    }
    else if (grade == 4)
    {
        cout << "成績は4です。たいへんよくできました。\n";
    }
    else if (grade == 5)
    {
        cout << "成績は5です。たいへん優秀です。\n";
    }

    return 0;
}
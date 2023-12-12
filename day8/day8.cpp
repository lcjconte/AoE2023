#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;

void solve() {
    string inst;
    cin >> inst;
    map<string, vector<string>> mp;
    std::string line;
    vector<string> nodes;
    while (std::getline(std::cin, line))
    {
        if (line == " ") {
            break;
        }
        if (line == "") {
            continue;
        }
        auto a = line.substr(0, 3);
        auto b = line.substr(7, 3);
        auto c = line.substr(12, 3);
        nodes.push_back(a);
        mp[a] = {b, c};
    }
    cout << "Read" << endl;
    vector<string> current;
    for (auto i : nodes) {
        if (i[2] == 'A') {
            current.push_back(i);
        }
    }
    int i = 0;
    while (true)
    {
        vector<string> ncur;
        for (auto cn : current) {
            ncur.push_back(mp[cn][inst[i % inst.size()]=='L' ? 0 : 1]);
        }
        current = ncur;
        i++;   
        bool val = 1;
        for (auto c : current) {
            if (c[2] != 'Z') {
                val = 0;
            }
        }
        if (val) {
            cout << i << endl;
            break;
        }
    }
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(0);
    solve();
    return 0;
}
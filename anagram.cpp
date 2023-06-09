#include <iostream>
#include <vector>
using namespace std;
#include<algorithm>

class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        return s == t;
    }
};

main() {
    string s = "anagram";
    string t = "nagaram";

    Solution sol;
    bool sul;
    sul = sol.isAnagram(s, t);
    cout << sul;

}
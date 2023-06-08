#include <iostream>
#include <vector>
#include <set>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        return nums.size() > set<int>(nums.begin(),nums.end()).size();
    }
};
main() {
    vector<int> num {1, 2, 3, 4, 5};
    Solution sol;
    bool s;
    s = sol.containsDuplicate(num);
    cout << s;
}
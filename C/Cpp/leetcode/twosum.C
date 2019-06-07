class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> map;
        vector<int> result;
        for(int i = 0; i < nums.size(); i++){
            int res = target - nums[i];
            if(map.find(res) != map.end() && map[res] != i){
                result.push_back(map[res]);
                result.push_back(i);
                return result;
            }
            map[nums[i]] = i;
        }
    }
};

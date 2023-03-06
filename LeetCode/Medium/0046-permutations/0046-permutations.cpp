class Solution {
public:

    vector<vector <int>> results;
    vector<int> prev_elements;

    void dfs(vector<int>& elements){
        if (elements.size() == 0){
            results.push_back(prev_elements);
        }

        for(int i = 0; i<elements.size(); i++){
            vector<int> next_elements = elements;
            next_elements.erase(next_elements.begin()+ i);

            
            prev_elements.push_back(elements[i]);
            dfs(next_elements);
            prev_elements.pop_back();
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
    dfs(nums);

    return results;    
    }
};
#include <iostream>
#include <map>
#include <unordered_set>
#include <string>

int longest_charin(vector<string> w){
    map <string, int> m();
    unorder_set dict();

    for(int i = 0; i< w.length(); i ++){
        m.add(w[i]);
    }

    int longest = 0;
    for(int i = 1; i< w.length(); i++){
        int len = helper(w, dict, map) + 1;
        map.add(w, len);
        longest = max(longest, len);
}

int hepler(string word, dict, map<string, int> m){
    for(int i = 0;i < word.length(); i++){
        string s(word);
        s.remove(i);
        if(dict.contains(s)){
            if(map.containkey(s)){
            return map.get(s);
            }
            return helper(s, dict, map) + 1:
        }
        }
    }


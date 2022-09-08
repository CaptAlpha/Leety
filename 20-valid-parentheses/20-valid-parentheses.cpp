class Solution {
public:
    bool isValid(string s) {
        if (s.size() == 0)
            return true;
        if (s.size() % 2)
            return false;

        stack<char> st;
        string str = "";
        for(int i = 0; i < s.size(); i++){
            if(s[i]=='(' || s[i]=='{' || s[i]=='['){
                st.push(s[i]);
            }
            else{
            if(st.empty())
                return false;
            else{
                char c = st.top();
                st.pop();
                if(c=='(' && s[i]==')'){
                    continue;
                }else if(c=='{' && s[i]=='}'){
                    continue;
                }else if(c=='[' && s[i]==']'){
                    continue;
                }else{
                    return false;
                }
            }
        }
        }
        if(st.empty())
            return true;
        else
            return false;
        return true;
        
    }
};
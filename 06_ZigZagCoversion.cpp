class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1 || numRows >= s.size())
            return s;

        vector<string> rows(numRows);
        int currRow = 0;
        int direction = 1;

        for (char c : s) {
            rows[currRow] += c;

            if (currRow == 0)
                direction = 1;
            else if (currRow == numRows - 1)
                direction = -1;

            currRow += direction;
        }

        string ans;
        for (string row : rows)
            ans += row;

        return ans;
    }
};

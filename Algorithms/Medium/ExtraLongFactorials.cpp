#include <bits/stdc++.h>

using namespace std;

// Complete the extraLongFactorials function below.
void extraLongFactorials(int n) {
    vector<int> factorial;
    factorial.push_back(1);
    int length = 1;
    for(int i = n; i > 0; i--){
        int carry = 0;
        for(int j = 0; j < length; j++){
            int tempSum = factorial[j] * i + carry;
            factorial[j] = tempSum % 10;
            carry = tempSum/ 10;
        }
        while(carry){
            factorial.push_back(carry%10);
            carry = carry/10;
            length++;
        }
    }
    for(int i = length-1; i>=0;i--){
        cout<<factorial[i];
    }

}

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    extraLongFactorials(n);

    return 0;
}

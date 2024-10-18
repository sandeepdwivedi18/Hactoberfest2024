#include <bits/stdc++.h>
using namespace std;

// Function to check whether any pair exists
// whose sum is equal to the given target value
bool twoSum(vector<int> &arr, int target){
  
    // Create an unordered_set to store the elements
    unordered_set<int> s;

    // Iterate through each element in the vector
    for (int i = 0; i < arr.size(); i++){

        // Calculate the complement that added to
        // arr[i], equals the target
        int complement = target - arr[i];

        // Check if the complement exists in the set
        if (s.find(complement) != s.end())
            return true;

        // Add the current element to the set
        s.insert(arr[i]);
    }
    // If no pair is found
    return false;
}

int main(){
    vector<int> arr = {0, -1, 2, -3, 1};
    int target = -2;

    // Call the twoSum function and print the result
    if (twoSum(arr, target))
        cout << "true";
    else
        cout << "false";

    return 0;
}

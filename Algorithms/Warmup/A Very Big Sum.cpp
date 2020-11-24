#include <bits/stdc++.h>
#include<iostream>
using namespace std;
int main()
{
    int n;
    long int result=0;
    cin>>n;
    int a[n];
    for(int j=0;j<n;j++)
    {
        cin>>a[j];
        result=result+a[j];
    }
    cout<<result;
    return 0;
}
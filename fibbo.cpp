#include<iostream>
using namespace std;
int main()
{
    int i,j,k=1,nt=0,l=0;
    cout<<"Enter the number of terms ";
    cin>>j;
    for(i=1;i<=j;i++){
        if(i==1){
            cout<<l<<" ";
            continue;
        }
        if(i==2){
            cout<<k<<" ";
            continue;
        }
        nt=l+k;
        l=k;
        k=nt;

        cout<<nt<<" ";
        
    }
    return 0;
}
// time complexity in avg case:O(nlogn)
					// worst case:O(n^2)	

#include<iostream>
using namespace std;
//it is also a divide& conquor algorithm
//chose the pivot element means the rightmost element
int partition(int *arr,int s,int e) {
	int pivot=arr[e];

	//make the pointer1 points to s-1 and pointer2 to s
	int i=s-1;//
	int j=s;
	for(;j<=e-1;j++){//run the loop from j=s to elment before the pivot elemnt
		if(arr[j]<=pivot) {
			//merge the smaller element in region-1
			i=i+1;
			swap(arr[i],arr[j]);
		}
	}
	swap(arr[e],arr[i+1]);
	return i+1;
}

void quickSort(int *arr,int s,int e) {
	//base case
	if(s>=e) {//s: starting point   e:ending point
		return;
	}
	//recursive case
	//the postion of partition about which the array to be broken
	int p=partition(arr,s,e);
	//left part sort
	quickSort(arr,s,p-1);
	//right part sort
	quickSort(arr,p+1,e);

}

int main() {
	int arr[]={2,7,8,6,1,5,4};
	int n=7;//length of the array
	quickSort(arr,0,n-1);

	for(int i=0;i<n;i++) {
		cout<<arr[i]<<",";
	}
	return 0;
}
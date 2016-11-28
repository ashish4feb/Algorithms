#include<stdio.h>
#include<conio.h>

using namespace std;

void quicksort(int ar[], int l, int h);
int partition(int ar[], int l, int h);

void quicksort(int ar[], int l, int h)
{
	int p;
	if(l<h)
	{
		p=partition(ar, l, h);
		quicksort(ar,l,p-1);
		quicksort(ar,p+1,h);
	}
}

int partition(int ar[], int l, int h)
{
	int pivot=0;
	int temp=0;
	int i,j;
	pivot=ar[h];
	i=l-1;
	for(j=l; j<h;j++)
	{
		if(ar[j] <= pivot)
			{
				i=i+1;
				temp=ar[i];
				ar[i]=ar[j];
				ar[j]=temp;
			}
		
	}
	temp=ar[i+1];
	ar[i+1]=ar[h];
	ar[h]=temp;
	return i+1;
}

int main()
{
	int i=0;
	int arr[]= {3,5,8,2,9,4,7,10};
	quicksort(arr,0,7);
	for(i=0; i<8;i++)
	{
		printf("Sorted Array : %d\n", arr[i]);
	}
	getch();
	return 0;
}

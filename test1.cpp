#include<stdio.h>
#define N 10     //定义元素个数；
int a[N]={1,2,3,4,5,6,7,8,9,10};    //定义查找数组；
int half(int low,int high,int key)  //low表示起点  high表示终点；
{
	if(low<high)
	{	
		int mid=(low+high)/2;     //设置中间值，用中间值与key比较；
		if(a[mid]==key)       //等于的话，说明找到了这个元素；
			return mid;
		else if(a[mid]>key)     //要找的值在mid的左边；
			return half(low,mid-1,key);   //重新定义区间长度，调用half函数；
		else                            //要找的值在mid的右边；
			return half(mid+1,high,key);   //重新定义区间长度，调用half函数；
	}
	return -1;  
}
int main(void)
{
	int key;
	printf("输入要查找的关键字: ");
	scanf("%d",&key);
	int pos=half(0,N-1,key);
	printf("原数据表:  ");
	for(int i=0;i<N;i++)
		printf("%d ",a[i]);
	printf("\n\n");
	if(pos>=0)
		printf("查找成功,该关键字位于数组的第%d个元素!\n",pos+1);
	else
		printf("查找失败!!!\n");
	return 0;
}

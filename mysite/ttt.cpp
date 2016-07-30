#include<iostream>
#include<malloc.h>
#include<string>
using namespace std;

class Point
{
	public:
	float x;
	float y;
	
	~Point()
	{
	 cout<<"dosome thing "<<x<<y<<endl;
	}
};

void process(Point * p,int index)
{
	float step = 50.0;
	int k = 3.14*(p->x * p->x + p->y * p->y)/step/2;
	cout<<"Property "<<index+1<<": This property will begin eroding in year "<<k+1<<".\n";
	
}


int main()
{
	int number;
	cin >> number;
	//Point * points = (Point * ) malloc(sizeof(Point)*number);
	Point* points = new Point[number];
	Point * temp = points;
	for (int i=0; i<number; i++)
	{
		cin>>temp[i].x;
		cin>>temp[i].y;
	}
	for (int i=0; i<number; i++)
	{
		process(&points[i],i);
	}
	cout<<"END OF OUTPUT.\n";
	//free(points);
	delete [] points;
	return 0;


}

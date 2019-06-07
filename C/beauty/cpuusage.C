#include <windows.h>
#include <stdint.h>
#include <iostream>
#include <math.h>

using namespace std;

//int getCurrentCpuUsage();

int main(){
	int Num = 200;
	int busytime = 10;
	int idletime = busytime;
	float PI = 3.1415926;
	float busytimearray[Num];
	float idletimearray[Num];
	int Max = 50;
	int Min = 0;
	int half = (Max - Min) / 2;
	for(int i = 0;i < Num; i++){
		busytimearray[i] = half + half * sin(2 * PI / Num * i);
		idletimearray[i] = 2 * half - busytimearray[i];
	}	
	
	
	while(true){
//busy loop
	//	for(int i = 0; i< 32e6; i++){
	//		;
	//	}
		for(int i = 0;i < Num; i++){
			int64_t starttime = GetTickCount();
			while((GetTickCount() - starttime) < busytimearray[i])
				;
//idle loop
			Sleep(idletimearray[i]);
		}	
	}
}

/*
int getCurrentCpuUsage(){
	PerformanceCounter cpuCounter;
	//PerformanceCounter ramCounter;

	cpuCounter = new PerformanceCounter();

	cpuCounter.CategoryName = "Processor";
	cpuCounter.CounterName = "% Processor Time";
	cpuCounter.InstanceName = "_Total";

	//ramCounter = new PerformanceCounter("Memory", "Available MBytes");
	return cpuCount.NextValue();

} 
*/

#include <stdio.h>
#include <pthread.h>	//thread function header file

void func(int x);
void func2(int x);

int main(){
	pthread_t t1;		//t1 data necessary for thread
	pthread_t t2;		//t2 data necessary for thread
	pthread_create(&t1, NULL, (void*)func, (void*)1); //activate thread 1
	pthread_create(&t2, NULL, (void*)func2, (void*)2); //activate thread 2
	printf("main()\n");	//show begin main
	pthread_join(t1, NULL); 	//wait until thread 1 finish
	pthread_join(t2, NULL);		//wait until thread 2 finish
	return 0;
}

void func(int x){		//function that process thread
	int i;
	for(i=0; i<10; i++){
		printf("func(%d): %d\n", x, i);	//show thread process
		usleep(100000);		//100000us(=0.1s)
	}						//normally nothing happens but for multithread switch to other thread
}

void func2(int x){
	int i;
	for(i=0; i<10; i++){
		printf("func(%d): %d\n", x, i);
		usleep(200000);
	}
}

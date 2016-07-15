#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <pthread.h>
#include <string.h>

void recv_thread();
int sock;

//recv block (wait until input), if different thread is not used, keyboard input cannot be accepted
void recv_thread(){
	char recv_buf[2048];
	while(1){
		int num =recv(sock, recv_buf, sizeof(recv_buf), 0);	//wait until receive
		recv_buf[num] = 0;
		printf("%s\n", recv_buf);
	}
}

int main(int argc, char *argv[]){
	pthread_t t1;
	struct sockaddr_in addr;
	char send_buf[2048];
	sock = socket(AF_INET, SOCK_DGRAM, 0);			//construct UDP/IP socket

	addr.sin_family = AF_INET; 		
	addr.sin_port = htons(atoi(argv[1]));			//assign receive port
	addr.sin_addr.s_addr = INADDR_ANY;
	bind(sock, (struct sockaddr *)&addr, sizeof(addr));
	pthread_create(&t1, NULL, (void *)recv_thread, (void *)NULL);	//begin receive thread

	addr.sin_port = htons(atoi(argv[2]));	//assign transmit port
	if(argc == 4) addr.sin_addr.s_addr = inet_addr(argv[3]);	//assing IP address

	while(1){
		scanf("%s", send_buf);
		if (!strcmp(send_buf, "quit")) break;	//finish when enter "quit"
		sendto(sock, send_buf, strlen(send_buf), 0, (struct sockaddr *)&addr, sizeof(addr));
	}
	close(sock);
	return 0;
}

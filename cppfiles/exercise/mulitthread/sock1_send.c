#include <stdio.h>
#include <string.h>
#include <sys/types.h>	//necessary header for connection between socket
#include <sys/socket.h>
#include <netinet/in.h>

int main(){
	int sock;					//socket number
	struct sockaddr_in addr;	//data struct for connection between socket
	char test[50] = "Hello from SOCKET!\n";

	sock = socket(AF_INET, SOCK_DGRAM, 0); 	//construct socket
	addr.sin_family = AF_INET;				//assign communication protocol
	addr.sin_port = htons(8000);			//assign port
	addr.sin_addr.s_addr = inet_addr("127.0.0.1");	//IP address 127.0.0.1

	sendto(sock, test, strlen(test), 0, (struct sockaddr *)&addr, sizeof(addr));	//send data
	close(sock);	//deallocate socket
	return 0;
}

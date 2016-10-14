#include <iostream>
using namespace std;
int main(){
	unsigned char TxData[10]; //transmit byte data
	unsigned char CheckSum = 0; //checksum calculation
	int angle = 9000;

	TxData[0] = 0x09; //All byte
	TxData[1] = 0x04; //Command
	TxData[2] = 0x00; //Option/Status
	TxData[3] = 0x00; //ID
	TxData[4] = (unsigned char) 0x00FF & angle; //mode
	TxData[5] = (unsigned char) 0x00FF & (angle >> 8); //address
	TxData[6] = 0x2A; //device number
	TxData[7] = 0x01; //count

	int i;
	//checksum calculation
	for(i=0; i<7; i++){
		CheckSum = CheckSum + TxData[i];
	}
	CheckSum = (unsigned char) 0x0FF & CheckSum;
	TxData[8] = CheckSum;

	//Send Packet
	for(i=0; i<=8; i++){
		cout<< hex << TxData[i];
	}
	cout << endl;
}

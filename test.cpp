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
	cout << (int)TxData[6] << endl;

	int i;
	//checksum calculation
	for(i=0; i<7; i++){
		CheckSum = CheckSum + TxData[i];
	}
	cout << (unsigned)CheckSum << endl;
	CheckSum = (unsigned char) 0x0FF & CheckSum;
	TxData[8] = CheckSum;

	//Send Packet
	for(i=0; i<=8; i++){
		cout << unsigned(TxData[i]);
	}
	TxData[0] = 0x08;
	TxData[1] = 0x04;
	TxData[2] = 0x00;
	TxData[3] = 0x00;
	TxData[4] = 0x01;
	TxData[5] = 0x29;
	TxData[6] = 0x01;
	CheckSum = 0;
	for(i=0; i<7; i++){
		CheckSum = CheckSum + TxData[i];
	}
	cout << endl;
	cout << hex << (unsigned)CheckSum << endl;
	CheckSum = (unsigned char) 0x0FF & CheckSum;
	cout << hex << (unsigned)CheckSum << endl;
}

#pragma once
#include <string>
#include "Treehopper.h"

using namespace std;

class TREEHOPPER_API UsbConnection
{
public:
	virtual ~UsbConnection() 
	{ 
	
	}
	virtual bool open() = 0;
	virtual void close() = 0;
	wstring getSerialNumber();
	wstring getName();
	wstring getDevicePath();
	virtual void sendDataPinConfigChannel(uint8_t* data, int len) = 0;
	virtual void sendDataPeripheralChannel(uint8_t* data, int len) = 0;
	//virtual unique_ptr<
	
protected:
	wstring serialNumber;
	wstring name;
	wstring devicePath;
	uint8_t pinReportEndpoint = 0x81;
	uint8_t peripheralResponseEndpoint = 0x82;
	uint8_t pinConfigEndpoint = 0x01;
	uint8_t peripheralConfigEndpoint = 0x02;
};
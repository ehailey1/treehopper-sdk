#pragma once
#include "Treehopper.h"
#include <stdint.h>

using namespace std;
namespace Treehopper 
{
	class TREEHOPPER_API I2c
	{
	public:
		~I2c() { }
		virtual void setSpeed(double value) = 0;
		virtual double getSpeed() = 0;

		virtual void setEnabled(bool value) = 0;
		virtual bool getEnabled() = 0;

		virtual void sendReceive(uint8_t address, uint8_t* writeBuffer, size_t numBytesToWrite,
			uint8_t* readBuffer = NULL, size_t numBytesToRead = 0) = 0;
	};
}
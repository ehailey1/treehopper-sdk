/*
 * treehopper.h
 *
 *  Created on: Jul 19, 2015
 *      Author: jay
 */

#ifndef TREEHOPPER_H_
#define TREEHOPPER_H_

#include "efm8_usb.h"
#include <stdint.h>

// enable this for verbose logging of all packets sent
// and received (not implemented yet -- sorry!)
// #define ENABLE_UART_DEBGUGGING

// Timing debugging lets you check how long
// it's taking to process packets. The high
// time tells you how long it's taking to process
// the task, and the low time is telling you
// how long USB traffic is taking. The debug
// pin is set as P1_B2 (which is Pin 10)
// #define	ENABLE_TIMING_DEBUGGING

#ifdef ENABLE_TIMING_DEBUGGING
	#define DEBUG_HIGH();	P1_B2 = true;
	#define DEBUG_LOW();		P1_B2 = false;
#else
	#define DEBUG_HIGH() { }
	#define DEBUG_LOW() { }
#endif

typedef enum GlobalCommands {
	GlobalCommandsReserved = 0,
	ConfigureDevice,
	PWMConfig,
	UARTConfig,
	I2CConfig,
	SPIConfig,
	I2CTransaction,
	SPITransaction,
	UARTTransaction,
	SoftPwmConfig,
	FirmwareUpdateSerial,
	FirmwareUpdateName,
	Reboot,
	EnterBootloader,
	LedConfig,
    ParallelConfig,
    ParallelTransaction

} GlobalCommands_t;

typedef enum PinConfigCommands {
	PinConfig_Reserved = 0,
	PinConfig_MakeDigitalInput,
	PinConfig_MakePushPullOutput,
	PinConfig_MakeOpenDrainOutput,
	PinConfig_MakeAnalogInput,
	PinConfig_SetDigitalValue,
} PinConfigCommands_t;

typedef enum DeviceResponse {
	DeviceResponseReserved = 0,
	DeviceResponse_DeviceInfo,
	DeviceResponse_CurrentReadings,
	DeviceResponse_UARTDataReceived,
	DeviceResponse_I2CDataReceived,
	DeviceResponse_SPIDataReceived
} DeviceResponse_t;

typedef struct pinConfigPacket {
	uint8_t PinNumber;
	PinConfigCommands_t PinCommand;
	uint8_t PinConfigData[4];
} pinConfigPacket_t;

typedef enum AppState {
	AppState_Normal,
	AppState_Spi1,
	AppState_Spi2,
	AppState_Spi3,
	AppState_Spi4,
	AppState_Spi5,
} AppState_t;

typedef enum BurstMode {
	Burst_None, Burst_Tx, Burst_Rx
} BurstMode_t;

#define TREEHOPPER_NUM_PINS		20

//extern SI_SEGMENT_VARIABLE(Treehopper_TxBuffer[255], uint8_t, SI_SEG_XDATA);
extern SI_SEGMENT_VARIABLE(Treehopper_RxBuffer[255], uint8_t, SI_SEG_XDATA);
extern SI_SEGMENT_VARIABLE(pins[TREEHOPPER_NUM_PINS], uint8_t, SI_SEG_XDATA);
extern SI_SEGMENT_VARIABLE(Treehopper_ReportData[TREEHOPPER_NUM_PINS*2+1], uint8_t, SI_SEG_XDATA);
extern SI_SEGMENT_VARIABLE(Treehopper_PinConfig, pinConfigPacket_t, SI_SEG_XDATA);
extern SI_SEGMENT_VARIABLE(Treehopper_PeripheralConfig[262], uint8_t, SI_SEG_XDATA);
extern SI_SEGMENT_VARIABLE(Treehopper_PeripheralResponse[64], uint8_t, SI_SEG_XDATA);

#define PIN0	P0_B0
#define PIN1	P0_B1
#define PIN2	P0_B2
#define PIN3	P0_B3
#define PIN4	P0_B6
#define PIN5	P0_B4
#define PIN6	P0_B5
#define PIN7	P0_B7
#define PIN8	P1_B0
#define PIN9	P1_B1
#define PIN10	P1_B2
#define PIN11	P1_B3
#define PIN12	P1_B4
#define PIN13	P1_B5
#define PIN14	P1_B6
#define PIN15	P1_B7
#define PIN16	P2_B0
#define PIN17	P2_B1
#define PIN18	P2_B2
#define PIN19	P2_B3


#define EP_PinStatus           EP1IN
#define EP_PinConfig           EP1OUT
#define EP_PeripheralResponse  EP2IN
#define EP_PeripheralConfig    EP2OUT


void Treehopper_Init();
void Treehopper_Task();

#endif /* TREEHOPPER_H_ */

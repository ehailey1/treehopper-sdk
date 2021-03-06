/// This file was auto-generated by RegisterGenerator. Any changes to it will be overwritten!
#pragma once
#include "SMBusDevice.h"
#include "Libraries/Treehopper.Libraries.h"
#include "Libraries/RegisterManager.h"
#include "Libraries/Register.h"

using namespace Treehopper::Libraries;

namespace Treehopper { namespace Libraries { namespace Sensors { namespace Magnetic { 

    enum class MagDataRates
    {
        Hz_0_75 = 0,
        Hz_1_5 = 1,
        Hz_3_0 = 2,
        Hz_7_5 = 3,
        Hz_15 = 4,
        Hz_30 = 5,
        Hz_75 = 6,
        Hz_100 = 7
	};

    enum class GainConfigurations
    {
        gauss_1_3 = 1,
        gauss_1_9 = 2,
        gauss_2_5 = 3,
        gauss_4_0 = 4,
        gauss_4_7 = 5,
        gauss_5_6 = 6,
        gauss_8_1 = 7
	};

    enum class MagSensorModes
    {
        ContinuousConversion = 0,
        SingleConversion = 1,
        PowerDown = 2
	};


    class Lsm303dlhcMagRegisters : public RegisterManager
    {
    public:
        class TempOutRegister : public Register
        {
        public:
			TempOutRegister(RegisterManager& regManager) : Register(regManager,0x05, 2, false) { }
            int value;

            long getValue() { return ((value & 0xFFF) << 4); }
            void setValue(long val)
            {
                value = (int)(((val >> 4) & 0xFFF) << (32 - 12)) >> (32 - 12);
            }
        };

        class SrRegister : public Register
        {
        public:
			SrRegister(RegisterManager& regManager) : Register(regManager,0x09, 1, false) { }
            int drdy;
            int registerLock;

            long getValue() { return ((drdy & 0x1) << 0) | ((registerLock & 0x1) << 1); }
            void setValue(long val)
            {
                drdy = (int)((val >> 0) & 0x1);
                registerLock = (int)((val >> 1) & 0x1);
            }
        };

        class CraRegister : public Register
        {
        public:
			CraRegister(RegisterManager& regManager) : Register(regManager,0x80, 1, false) { }
            int magDataRate;
            int tempEnable;
            MagDataRates getMagDataRate() { return (MagDataRates)magDataRate; }
            void setMagDataRate(MagDataRates enumVal) { magDataRate = (int)enumVal; }

            long getValue() { return ((magDataRate & 0x7) << 2) | ((tempEnable & 0x1) << 7); }
            void setValue(long val)
            {
                magDataRate = (int)((val >> 2) & 0x7);
                tempEnable = (int)((val >> 7) & 0x1);
            }
        };

        class CrbRegister : public Register
        {
        public:
			CrbRegister(RegisterManager& regManager) : Register(regManager,0x81, 1, false) { }
            int gainConfiguration;
            GainConfigurations getGainConfiguration() { return (GainConfigurations)gainConfiguration; }
            void setGainConfiguration(GainConfigurations enumVal) { gainConfiguration = (int)enumVal; }

            long getValue() { return ((gainConfiguration & 0x7) << 5); }
            void setValue(long val)
            {
                gainConfiguration = (int)((val >> 5) & 0x7);
            }
        };

        class MrRegister : public Register
        {
        public:
			MrRegister(RegisterManager& regManager) : Register(regManager,0x82, 1, false) { }
            int magSensorMode;
            MagSensorModes getMagSensorMode() { return (MagSensorModes)magSensorMode; }
            void setMagSensorMode(MagSensorModes enumVal) { magSensorMode = (int)enumVal; }

            long getValue() { return ((magSensorMode & 0x3) << 0); }
            void setValue(long val)
            {
                magSensorMode = (int)((val >> 0) & 0x3);
            }
        };

        class OutXRegister : public Register
        {
        public:
			OutXRegister(RegisterManager& regManager) : Register(regManager,0x83, 2, false) { }
            int value;

            long getValue() { return ((value & 0xFFFF) << 0); }
            void setValue(long val)
            {
                value = (int)(((val >> 0) & 0xFFFF) << (32 - 16)) >> (32 - 16);
            }
        };

        class OutYRegister : public Register
        {
        public:
			OutYRegister(RegisterManager& regManager) : Register(regManager,0x85, 2, false) { }
            int value;

            long getValue() { return ((value & 0xFFFF) << 0); }
            void setValue(long val)
            {
                value = (int)(((val >> 0) & 0xFFFF) << (32 - 16)) >> (32 - 16);
            }
        };

        class OutZRegister : public Register
        {
        public:
			OutZRegister(RegisterManager& regManager) : Register(regManager,0x87, 2, false) { }
            int value;

            long getValue() { return ((value & 0xFFFF) << 0); }
            void setValue(long val)
            {
                value = (int)(((val >> 0) & 0xFFFF) << (32 - 16)) >> (32 - 16);
            }
        };

            TempOutRegister tempOut;
            SrRegister sr;
            CraRegister cra;
            CrbRegister crb;
            MrRegister mr;
            OutXRegister outX;
            OutYRegister outY;
            OutZRegister outZ;

		Lsm303dlhcMagRegisters(SMBusDevice& device) : RegisterManager(device, true), tempOut(*this), sr(*this), cra(*this), crb(*this), mr(*this), outX(*this), outY(*this), outZ(*this)
		{ 
			registers.push_back(&tempOut);
			registers.push_back(&sr);
			registers.push_back(&cra);
			registers.push_back(&crb);
			registers.push_back(&mr);
			registers.push_back(&outX);
			registers.push_back(&outY);
			registers.push_back(&outZ);
		}
    };
 }  }  } }
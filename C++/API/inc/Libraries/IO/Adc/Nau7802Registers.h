/// This file was auto-generated by RegisterGenerator. Any changes to it will be overwritten!
#pragma once
#include "SMBusDevice.h"
#include "Libraries/Treehopper.Libraries.h"
#include "Libraries/RegisterManager.h"
#include "Libraries/Register.h"

using namespace Treehopper::Libraries;

namespace Treehopper { namespace Libraries { namespace IO { namespace Adc { 

    enum class Gains
    {
        x1 = 0,
        x4 = 1,
        x2 = 2,
        x8 = 3,
        x16 = 4,
        x32 = 5,
        x64 = 6,
        x128 = 7
	};

    enum class Vldoes
    {
        mV_4500 = 0,
        mV_4200 = 1,
        mV_3900 = 2,
        mV_3600 = 3,
        mV_3300 = 4,
        mV_3000 = 5,
        mV_2700 = 6,
        mV_2400 = 7
	};

    enum class CalMods
    {
        OffsetCalibrationInternal = 0,
        Reserved = 1,
        OffsetCalibrationSystem = 2,
        GainCalibrationSystem = 3
	};

    enum class ConversionRates
    {
        Sps_10 = 0,
        Sps_20 = 1,
        Sps_40 = 2,
        Sps_80 = 3,
        Sps_320 = 7
	};

    enum class AdcVcms
    {
        ExtendedCommonModeRefp = 3,
        ExtendedCommonModeRefn = 2,
        disable = 0
	};

    enum class RegChpFreqs
    {
        off = 3
	};


    class Nau7802Registers : public RegisterManager
    {
    public:
        class PuCtrlRegister : public Register
        {
        public:
			PuCtrlRegister(RegisterManager& regManager) : Register(regManager,0x00, 1, false) { }
            int registerReset;
            int powerUpDigital;
            int powerUpAnalog;
            int powerUpReady;
            int cycleStart;
            int cycleReady;
            int useExternalCrystal;
            int useInternalLdo;

            long getValue() { return ((registerReset & 0x1) << 0) | ((powerUpDigital & 0x1) << 1) | ((powerUpAnalog & 0x1) << 2) | ((powerUpReady & 0x1) << 3) | ((cycleStart & 0x1) << 4) | ((cycleReady & 0x1) << 5) | ((useExternalCrystal & 0x1) << 6) | ((useInternalLdo & 0x1) << 7); }
            void setValue(long val)
            {
                registerReset = (int)((val >> 0) & 0x1);
                powerUpDigital = (int)((val >> 1) & 0x1);
                powerUpAnalog = (int)((val >> 2) & 0x1);
                powerUpReady = (int)((val >> 3) & 0x1);
                cycleStart = (int)((val >> 4) & 0x1);
                cycleReady = (int)((val >> 5) & 0x1);
                useExternalCrystal = (int)((val >> 6) & 0x1);
                useInternalLdo = (int)((val >> 7) & 0x1);
            }
        };

        class Ctrl1Register : public Register
        {
        public:
			Ctrl1Register(RegisterManager& regManager) : Register(regManager,0x01, 1, false) { }
            int gain;
            int vldo;
            int drdySelect;
            int conversionReadyPinPolarity;
            Gains getGain() { return (Gains)gain; }
            void setGain(Gains enumVal) { gain = (int)enumVal; }
            Vldoes getVldo() { return (Vldoes)vldo; }
            void setVldo(Vldoes enumVal) { vldo = (int)enumVal; }

            long getValue() { return ((gain & 0x7) << 0) | ((vldo & 0x7) << 3) | ((drdySelect & 0x1) << 6) | ((conversionReadyPinPolarity & 0x1) << 7); }
            void setValue(long val)
            {
                gain = (int)((val >> 0) & 0x7);
                vldo = (int)((val >> 3) & 0x7);
                drdySelect = (int)((val >> 6) & 0x1);
                conversionReadyPinPolarity = (int)((val >> 7) & 0x1);
            }
        };

        class Ctrl2Register : public Register
        {
        public:
			Ctrl2Register(RegisterManager& regManager) : Register(regManager,0x02, 1, false) { }
            int calMod;
            int calStart;
            int calError;
            int conversionRate;
            int channelSelect;
            CalMods getCalMod() { return (CalMods)calMod; }
            void setCalMod(CalMods enumVal) { calMod = (int)enumVal; }
            ConversionRates getConversionRate() { return (ConversionRates)conversionRate; }
            void setConversionRate(ConversionRates enumVal) { conversionRate = (int)enumVal; }

            long getValue() { return ((calMod & 0x3) << 0) | ((calStart & 0x1) << 2) | ((calError & 0x1) << 3) | ((conversionRate & 0x7) << 4) | ((channelSelect & 0x1) << 7); }
            void setValue(long val)
            {
                calMod = (int)((val >> 0) & 0x3);
                calStart = (int)((val >> 2) & 0x1);
                calError = (int)((val >> 3) & 0x1);
                conversionRate = (int)((val >> 4) & 0x7);
                channelSelect = (int)((val >> 7) & 0x1);
            }
        };

        class I2cCtrlRegister : public Register
        {
        public:
			I2cCtrlRegister(RegisterManager& regManager) : Register(regManager,0x11, 1, false) { }
            int bgpCp;
            int ts;
            int boPga;
            int si;
            int wpd;
            int spe;
            int frd;
            int crsd;

            long getValue() { return ((bgpCp & 0x1) << 0) | ((ts & 0x1) << 1) | ((boPga & 0x1) << 2) | ((si & 0x1) << 3) | ((wpd & 0x1) << 4) | ((spe & 0x1) << 5) | ((frd & 0x1) << 6) | ((crsd & 0x1) << 7); }
            void setValue(long val)
            {
                bgpCp = (int)((val >> 0) & 0x1);
                ts = (int)((val >> 1) & 0x1);
                boPga = (int)((val >> 2) & 0x1);
                si = (int)((val >> 3) & 0x1);
                wpd = (int)((val >> 4) & 0x1);
                spe = (int)((val >> 5) & 0x1);
                frd = (int)((val >> 6) & 0x1);
                crsd = (int)((val >> 7) & 0x1);
            }
        };

        class AdcResultRegister : public Register
        {
        public:
			AdcResultRegister(RegisterManager& regManager) : Register(regManager,0x12, 3, true) { }
            int value;

            long getValue() { return ((value & 0xFFFFFF) << 0); }
            void setValue(long val)
            {
                value = (int)(((val >> 0) & 0xFFFFFF) << (32 - 24)) >> (32 - 24);
            }
        };

        class AdcRegister : public Register
        {
        public:
			AdcRegister(RegisterManager& regManager) : Register(regManager,0x15, 1, false) { }
            int regChp;
            int adcVcm;
            int regChpFreq;
            AdcVcms getAdcVcm() { return (AdcVcms)adcVcm; }
            void setAdcVcm(AdcVcms enumVal) { adcVcm = (int)enumVal; }
            RegChpFreqs getRegChpFreq() { return (RegChpFreqs)regChpFreq; }
            void setRegChpFreq(RegChpFreqs enumVal) { regChpFreq = (int)enumVal; }

            long getValue() { return ((regChp & 0x3) << 0) | ((adcVcm & 0x3) << 2) | ((regChpFreq & 0x3) << 4); }
            void setValue(long val)
            {
                regChp = (int)((val >> 0) & 0x3);
                adcVcm = (int)((val >> 2) & 0x3);
                regChpFreq = (int)((val >> 4) & 0x3);
            }
        };

        class PgaRegister : public Register
        {
        public:
			PgaRegister(RegisterManager& regManager) : Register(regManager,0x1B, 1, false) { }
            int disableChopper;
            int pgaInv;
            int pgaBypass;
            int ldoMode;
            int rdOptSel;

            long getValue() { return ((disableChopper & 0x1) << 0) | ((pgaInv & 0x1) << 3) | ((pgaBypass & 0x1) << 4) | ((ldoMode & 0x1) << 5) | ((rdOptSel & 0x1) << 6); }
            void setValue(long val)
            {
                disableChopper = (int)((val >> 0) & 0x1);
                pgaInv = (int)((val >> 3) & 0x1);
                pgaBypass = (int)((val >> 4) & 0x1);
                ldoMode = (int)((val >> 5) & 0x1);
                rdOptSel = (int)((val >> 6) & 0x1);
            }
        };

        class PowerCtrlRegister : public Register
        {
        public:
			PowerCtrlRegister(RegisterManager& regManager) : Register(regManager,0x1C, 1, false) { }
            int pgaCurr;
            int adcCurr;
            int masterBiasCurr;
            int pgaCapEn;

            long getValue() { return ((pgaCurr & 0x3) << 0) | ((adcCurr & 0x3) << 2) | ((masterBiasCurr & 0x7) << 4) | ((pgaCapEn & 0x1) << 7); }
            void setValue(long val)
            {
                pgaCurr = (int)((val >> 0) & 0x3);
                adcCurr = (int)((val >> 2) & 0x3);
                masterBiasCurr = (int)((val >> 4) & 0x7);
                pgaCapEn = (int)((val >> 7) & 0x1);
            }
        };

            PuCtrlRegister puCtrl;
            Ctrl1Register ctrl1;
            Ctrl2Register ctrl2;
            I2cCtrlRegister i2cCtrl;
            AdcResultRegister adcResult;
            AdcRegister adc;
            PgaRegister pga;
            PowerCtrlRegister powerCtrl;

		Nau7802Registers(SMBusDevice& device) : RegisterManager(device, true), puCtrl(*this), ctrl1(*this), ctrl2(*this), i2cCtrl(*this), adcResult(*this), adc(*this), pga(*this), powerCtrl(*this)
		{ 
			registers.push_back(&puCtrl);
			registers.push_back(&ctrl1);
			registers.push_back(&ctrl2);
			registers.push_back(&i2cCtrl);
			registers.push_back(&adcResult);
			registers.push_back(&adc);
			registers.push_back(&pga);
			registers.push_back(&powerCtrl);
		}
    };
 }  }  } }
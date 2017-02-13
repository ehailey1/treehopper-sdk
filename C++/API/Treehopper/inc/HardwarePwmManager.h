#pragma once

#include "Treehopper.h"
#include "HardwarePwmFrequency.h"
#include "Pin.h"

namespace Treehopper
{
	class TreehopperUsb;

	class TREEHOPPER_API HardwarePwmManager
	{
		friend class HardwarePwm;

	public:
		HardwarePwmManager(TreehopperUsb* board);
		void frequency(HardwarePwmFrequency value);
		HardwarePwmFrequency frequency();
		double frequencyHz();

	protected:
		enum class EnableMode : uint8_t
		{
			None,
			Pin7,
			Pin7_Pin8,
			Pin7_Pin8_Pin9
		};

		struct Configuration {
			uint8_t opcode;
			EnableMode mode;
			HardwarePwmFrequency frequency;
			uint8_t DutyCycle7_Lo;
			uint8_t DutyCycle7_Hi;
			uint8_t DutyCycle8_Lo;
			uint8_t DutyCycle8_Hi;
			uint8_t DutyCycle9_Lo;
			uint8_t DutyCycle9_Hi;
		} config;

		TreehopperUsb* board;
		void sendConfig();
		void updateDutyCycle(HardwarePwm* pin);
		void start(HardwarePwm* pin);
		void stop(HardwarePwm* pin);
	};
}
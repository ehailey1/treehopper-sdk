#pragma once

#include "Treehopper.Libraries.h"
#include <cstdint>
#include <array>
#include <memory>
#include <vector>

namespace Treehopper {
	namespace Libraries {
		class Register
		{
		public:
			Register(RegisterManager& regManager, int address, int width, bool isBigEndian);
            void write();
			void read();
            virtual long getValue() = 0;
            virtual void setValue(long value) =0;
            std::vector<uint8_t> getBytes();
            void setBytes(std::vector<uint8_t> bytes);
            int address;
            int width;
            bool isBigEndian;
		private:
			RegisterManager& regManager;
		};
	}
}
from treehopper.api import *
from treehopper.utils import *
from treehopper.libraries import RegisterManager, Register, SMBusDevice
from treehopper.libraries.Register import sign_extend

class AlsTimes:
    Time_100ms = 0
    Time_200ms = 1
    Time_300ms = 2
    Time_400ms = 3
    Time_500ms = 4
    Time_600ms = 5
    
class AlsGains:
    Low = 0
    Medium = 1
    High = 2
    Max = 3
    
class InterruptPersistanceFilters:
    EveryAlsCycle = 0
    AnyValueOutsideThreshold = 1
    Consecutive_2 = 2
    Consecutive_3 = 3
    Consecutive_5 = 4
    Consecutive_10 = 5
    Consecutive_15 = 6
    Consecutive_20 = 7
    Consecutive_25 = 8
    Consecutive_30 = 9
    Consecutive_35 = 10
    Consecutive_40 = 11
    Consecutive_45 = 12
    Consecutive_50 = 13
    Consecutive_55 = 14
    Consecutive_60 = 15
    
class Tsl2591Registers(RegisterManager):
    def __init__(self, dev: SMBusDevice):
        RegisterManager.__init__(self, dev, True)
        self.enable = self.EnableRegister(self)
        self.registers.append(self.enable)
        self.config = self.ConfigRegister(self)
        self.registers.append(self.config)
        self.interruptLowThreshold = self.InterruptLowThresholdRegister(self)
        self.registers.append(self.interruptLowThreshold)
        self.interruptHighThreshold = self.InterruptHighThresholdRegister(self)
        self.registers.append(self.interruptHighThreshold)
        self.noPersistLowThreshold = self.NoPersistLowThresholdRegister(self)
        self.registers.append(self.noPersistLowThreshold)
        self.noPersistHighThreshold = self.NoPersistHighThresholdRegister(self)
        self.registers.append(self.noPersistHighThreshold)
        self.persist = self.PersistRegister(self)
        self.registers.append(self.persist)
        self.packageId = self.PackageIdRegister(self)
        self.registers.append(self.packageId)
        self.deviceId = self.DeviceIdRegister(self)
        self.registers.append(self.deviceId)
        self.status = self.StatusRegister(self)
        self.registers.append(self.status)
        self.ch0 = self.Ch0Register(self)
        self.registers.append(self.ch0)
        self.ch1 = self.Ch1Register(self)
        self.registers.append(self.ch1)

    class EnableRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0xA0, 1, False)
            self.powerOn = 0
            self.alsEnable = 0
            self.alsInterruptEnable = 0
            self.sleepAfterInterrupt = 0
            self.noPersistInterruptEnable = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.powerOn & 0x1) << 0) | ((self.alsEnable & 0x1) << 1) | ((self.alsInterruptEnable & 0x1) << 4) | ((self.sleepAfterInterrupt & 0x1) << 6) | ((self.noPersistInterruptEnable & 0x1) << 7)

        def setValue(self, value: int):
            self.powerOn = ((value >> 0) & 0x1)
            self.alsEnable = ((value >> 1) & 0x1)
            self.alsInterruptEnable = ((value >> 4) & 0x1)
            self.sleepAfterInterrupt = ((value >> 6) & 0x1)
            self.noPersistInterruptEnable = ((value >> 7) & 0x1)

        def __str__(self):
            retVal = ""
            retVal += "PowerOn: {} (offset: 0, width: 1)\r\n".format(self.powerOn)
            retVal += "AlsEnable: {} (offset: 1, width: 1)\r\n".format(self.alsEnable)
            retVal += "AlsInterruptEnable: {} (offset: 4, width: 1)\r\n".format(self.alsInterruptEnable)
            retVal += "SleepAfterInterrupt: {} (offset: 6, width: 1)\r\n".format(self.sleepAfterInterrupt)
            retVal += "NoPersistInterruptEnable: {} (offset: 7, width: 1)\r\n".format(self.noPersistInterruptEnable)
            return retVal

    class ConfigRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0xA1, 1, False)
            self.alsTime = 0
            self.alsGain = 0
            self.systemReset = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.alsTime & 0x7) << 0) | ((self.alsGain & 0x3) << 3) | ((self.systemReset & 0x1) << 7)

        def setValue(self, value: int):
            self.alsTime = ((value >> 0) & 0x7)
            self.alsGain = ((value >> 3) & 0x3)
            self.systemReset = ((value >> 7) & 0x1)

        def __str__(self):
            retVal = ""
            retVal += "AlsTime: {} (offset: 0, width: 3)\r\n".format(self.alsTime)
            retVal += "AlsGain: {} (offset: 3, width: 2)\r\n".format(self.alsGain)
            retVal += "SystemReset: {} (offset: 7, width: 1)\r\n".format(self.systemReset)
            return retVal

    class InterruptLowThresholdRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0xA4, 2, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.value & 0xFFFF) << 0)

        def setValue(self, value: int):
            self.value = ((value >> 0) & 0xFFFF)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 0, width: 16)\r\n".format(self.value)
            return retVal

    class InterruptHighThresholdRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0xA6, 2, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.value & 0xFFFF) << 0)

        def setValue(self, value: int):
            self.value = ((value >> 0) & 0xFFFF)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 0, width: 16)\r\n".format(self.value)
            return retVal

    class NoPersistLowThresholdRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0xA8, 2, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.value & 0xFFFF) << 0)

        def setValue(self, value: int):
            self.value = ((value >> 0) & 0xFFFF)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 0, width: 16)\r\n".format(self.value)
            return retVal

    class NoPersistHighThresholdRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0xAa, 2, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.value & 0xFFFF) << 0)

        def setValue(self, value: int):
            self.value = ((value >> 0) & 0xFFFF)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 0, width: 16)\r\n".format(self.value)
            return retVal

    class PersistRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0xAc, 1, False)
            self.interruptPersistanceFilter = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.interruptPersistanceFilter & 0xF) << 0)

        def setValue(self, value: int):
            self.interruptPersistanceFilter = ((value >> 0) & 0xF)

        def __str__(self):
            retVal = ""
            retVal += "InterruptPersistanceFilter: {} (offset: 0, width: 4)\r\n".format(self.interruptPersistanceFilter)
            return retVal

    class PackageIdRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0xB1, 1, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.value & 0xFF) << 0)

        def setValue(self, value: int):
            self.value = ((value >> 0) & 0xFF)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 0, width: 8)\r\n".format(self.value)
            return retVal

    class DeviceIdRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0xB2, 1, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.value & 0xFF) << 0)

        def setValue(self, value: int):
            self.value = ((value >> 0) & 0xFF)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 0, width: 8)\r\n".format(self.value)
            return retVal

    class StatusRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0xB3, 1, False)
            self.alsValud = 0
            self.alsInterrupt = 0
            self.noPersistInterrupt = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.alsValud & 0x1) << 0) | ((self.alsInterrupt & 0x1) << 4) | ((self.noPersistInterrupt & 0x1) << 5)

        def setValue(self, value: int):
            self.alsValud = ((value >> 0) & 0x1)
            self.alsInterrupt = ((value >> 4) & 0x1)
            self.noPersistInterrupt = ((value >> 5) & 0x1)

        def __str__(self):
            retVal = ""
            retVal += "AlsValud: {} (offset: 0, width: 1)\r\n".format(self.alsValud)
            retVal += "AlsInterrupt: {} (offset: 4, width: 1)\r\n".format(self.alsInterrupt)
            retVal += "NoPersistInterrupt: {} (offset: 5, width: 1)\r\n".format(self.noPersistInterrupt)
            return retVal

    class Ch0Register(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0xB4, 2, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.value & 0xFFFF) << 0)

        def setValue(self, value: int):
            self.value = ((value >> 0) & 0xFFFF)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 0, width: 16)\r\n".format(self.value)
            return retVal

    class Ch1Register(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0xB6, 2, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.value & 0xFFFF) << 0)

        def setValue(self, value: int):
            self.value = ((value >> 0) & 0xFFFF)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 0, width: 16)\r\n".format(self.value)
            return retVal


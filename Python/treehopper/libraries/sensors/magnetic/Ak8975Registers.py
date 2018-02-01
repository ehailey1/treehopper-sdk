from treehopper.api import *
from treehopper.utils import *
from treehopper.libraries import RegisterManager, Register, SMBusDevice
from treehopper.libraries.Register import sign_extend

class Ak8975Registers(RegisterManager):
    def __init__(self, dev: SMBusDevice):
        RegisterManager.__init__(self, dev, True)
        self.wia = self.WiaRegister(self)
        self.registers.append(self.wia)
        self.info = self.InfoRegister(self)
        self.registers.append(self.info)
        self.status1 = self.Status1Register(self)
        self.registers.append(self.status1)
        self.hx = self.HxRegister(self)
        self.registers.append(self.hx)
        self.hy = self.HyRegister(self)
        self.registers.append(self.hy)
        self.hz = self.HzRegister(self)
        self.registers.append(self.hz)
        self.status2 = self.Status2Register(self)
        self.registers.append(self.status2)
        self.control = self.ControlRegister(self)
        self.registers.append(self.control)
        self.sensitivityX = self.SensitivityXRegister(self)
        self.registers.append(self.sensitivityX)
        self.sensitivityY = self.SensitivityYRegister(self)
        self.registers.append(self.sensitivityY)
        self.sensitivityZ = self.SensitivityZRegister(self)
        self.registers.append(self.sensitivityZ)

    class WiaRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x00, 1, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def get_value(self):
            return ((self.value & 0xFF) << 0)

        def set_value(self, value: int):
            self.value = ((value >> 0) & 0xFF)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 0, width: 8)\r\n".format(self.value)
            return retVal

    class InfoRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x01, 1, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def get_value(self):
            return ((self.value & 0xFF) << 0)

        def set_value(self, value: int):
            self.value = ((value >> 0) & 0xFF)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 0, width: 8)\r\n".format(self.value)
            return retVal

    class Status1Register(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x02, 1, False)
            self.drdy = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def get_value(self):
            return ((self.drdy & 0x1) << 0)

        def set_value(self, value: int):
            self.drdy = ((value >> 0) & 0x1)

        def __str__(self):
            retVal = ""
            retVal += "Drdy: {} (offset: 0, width: 1)\r\n".format(self.drdy)
            return retVal

    class HxRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x03, 2, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def get_value(self):
            return ((self.value & 0xFFFF) << 0)

        def set_value(self, value: int):
            self.value = sign_extend((value >> 0) & 0xFFFF, 16)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 0, width: 16)\r\n".format(self.value)
            return retVal

    class HyRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x05, 2, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def get_value(self):
            return ((self.value & 0xFFFF) << 0)

        def set_value(self, value: int):
            self.value = sign_extend((value >> 0) & 0xFFFF, 16)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 0, width: 16)\r\n".format(self.value)
            return retVal

    class HzRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x07, 2, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def get_value(self):
            return ((self.value & 0xFFFF) << 0)

        def set_value(self, value: int):
            self.value = sign_extend((value >> 0) & 0xFFFF, 16)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 0, width: 16)\r\n".format(self.value)
            return retVal

    class Status2Register(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x09, 1, False)
            self.derr = 0
            self.hofl = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def get_value(self):
            return ((self.derr & 0x1) << 2) | ((self.hofl & 0x1) << 3)

        def set_value(self, value: int):
            self.derr = ((value >> 2) & 0x1)
            self.hofl = ((value >> 3) & 0x1)

        def __str__(self):
            retVal = ""
            retVal += "Derr: {} (offset: 2, width: 1)\r\n".format(self.derr)
            retVal += "Hofl: {} (offset: 3, width: 1)\r\n".format(self.hofl)
            return retVal

    class ControlRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x0a, 1, False)
            self.mode = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def get_value(self):
            return ((self.mode & 0xF) << 0)

        def set_value(self, value: int):
            self.mode = ((value >> 0) & 0xF)

        def __str__(self):
            retVal = ""
            retVal += "Mode: {} (offset: 0, width: 4)\r\n".format(self.mode)
            return retVal

    class SensitivityXRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x10, 1, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def get_value(self):
            return ((self.value & 0xFF) << 0)

        def set_value(self, value: int):
            self.value = ((value >> 0) & 0xFF)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 0, width: 8)\r\n".format(self.value)
            return retVal

    class SensitivityYRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x11, 1, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def get_value(self):
            return ((self.value & 0xFF) << 0)

        def set_value(self, value: int):
            self.value = ((value >> 0) & 0xFF)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 0, width: 8)\r\n".format(self.value)
            return retVal

    class SensitivityZRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x12, 1, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def get_value(self):
            return ((self.value & 0xFF) << 0)

        def set_value(self, value: int):
            self.value = ((value >> 0) & 0xFF)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 0, width: 8)\r\n".format(self.value)
            return retVal


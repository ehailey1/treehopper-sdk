from treehopper.api import *
from treehopper.utils import *
from treehopper.libraries import RegisterManager, Register, SMBusDevice
from treehopper.libraries.Register import sign_extend

class SdoPuDiscs:
    SdoPullUpDisconnected = 144
    SdoPullUpConnected = 16
    
class HighPassFilterModeSelections:
    NormalMode = 0
    ReferenceSignal = 1
    Normal = 2
    AutoresetOnInterrupt = 3
    
class FullScaleSelections:
    scale_2G = 0
    scale_4G = 1
    scale_8G = 2
    scale_16G = 3
    
class FifoModes:
    Bypass = 0
    Fifo = 1
    Stream = 2
    StreamToFifo = 3
    
class OutputDataRates:
    PowerDown = 0
    Hz_1 = 1
    Hz_10 = 2
    Hz_25 = 3
    Hz_50 = 4
    Hz_100 = 5
    Hz_200 = 6
    Hz_400 = 7
    Hz_1600 = 8
    Hz_1344_5376 = 9
    
class Lis3dhRegisters(RegisterManager):
    def __init__(self, dev: SMBusDevice):
        RegisterManager.__init__(self, dev, True)
        self.statusRegAux = self.StatusRegAuxRegister(self)
        self.registers.append(self.statusRegAux)
        self.outAdc1 = self.OutAdc1Register(self)
        self.registers.append(self.outAdc1)
        self.outAdc2 = self.OutAdc2Register(self)
        self.registers.append(self.outAdc2)
        self.outAdc3 = self.OutAdc3Register(self)
        self.registers.append(self.outAdc3)
        self.whoAmI = self.WhoAmIRegister(self)
        self.registers.append(self.whoAmI)
        self.ctrl0 = self.Ctrl0Register(self)
        self.registers.append(self.ctrl0)
        self.tempCfgReg = self.TempCfgRegRegister(self)
        self.registers.append(self.tempCfgReg)
        self.ctrl2 = self.Ctrl2Register(self)
        self.registers.append(self.ctrl2)
        self.ctrl3 = self.Ctrl3Register(self)
        self.registers.append(self.ctrl3)
        self.ctrl4 = self.Ctrl4Register(self)
        self.registers.append(self.ctrl4)
        self.ctrl5 = self.Ctrl5Register(self)
        self.registers.append(self.ctrl5)
        self.ctrl6 = self.Ctrl6Register(self)
        self.registers.append(self.ctrl6)
        self.reference = self.ReferenceRegister(self)
        self.registers.append(self.reference)
        self.status = self.StatusRegister(self)
        self.registers.append(self.status)
        self.fifoCtrl = self.FifoCtrlRegister(self)
        self.registers.append(self.fifoCtrl)
        self.fifoSrc = self.FifoSrcRegister(self)
        self.registers.append(self.fifoSrc)
        self.int1Cfg = self.Int1CfgRegister(self)
        self.registers.append(self.int1Cfg)
        self.int1Src = self.Int1SrcRegister(self)
        self.registers.append(self.int1Src)
        self.int1Threshold = self.Int1ThresholdRegister(self)
        self.registers.append(self.int1Threshold)
        self.int1Duration = self.Int1DurationRegister(self)
        self.registers.append(self.int1Duration)
        self.int2Cfg = self.Int2CfgRegister(self)
        self.registers.append(self.int2Cfg)
        self.int2Src = self.Int2SrcRegister(self)
        self.registers.append(self.int2Src)
        self.int2Threshold = self.Int2ThresholdRegister(self)
        self.registers.append(self.int2Threshold)
        self.int2Duration = self.Int2DurationRegister(self)
        self.registers.append(self.int2Duration)
        self.clickSource = self.ClickSourceRegister(self)
        self.registers.append(self.clickSource)
        self.clickThreshold = self.ClickThresholdRegister(self)
        self.registers.append(self.clickThreshold)
        self.timeLimit = self.TimeLimitRegister(self)
        self.registers.append(self.timeLimit)
        self.timeLatency = self.TimeLatencyRegister(self)
        self.registers.append(self.timeLatency)
        self.timeWindow = self.TimeWindowRegister(self)
        self.registers.append(self.timeWindow)
        self.activationThreshold = self.ActivationThresholdRegister(self)
        self.registers.append(self.activationThreshold)
        self.activationDuration = self.ActivationDurationRegister(self)
        self.registers.append(self.activationDuration)
        self.ctrl1 = self.Ctrl1Register(self)
        self.registers.append(self.ctrl1)
        self.outX = self.OutXRegister(self)
        self.registers.append(self.outX)
        self.outY = self.OutYRegister(self)
        self.registers.append(self.outY)
        self.outZ = self.OutZRegister(self)
        self.registers.append(self.outZ)

    class StatusRegAuxRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x07, 1, False)
            self.oneAxisDataAvailable = 0
            self.twoAxisDataAvailable = 0
            self.threeAxisDataAvailable = 0
            self.dataAvailable = 0
            self.oneAxisDataOverrun = 0
            self.twoAxisDataOverrun = 0
            self.dataOverrun = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.oneAxisDataAvailable & 0x1) << 0) | ((self.twoAxisDataAvailable & 0x1) << 1) | ((self.threeAxisDataAvailable & 0x1) << 2) | ((self.dataAvailable & 0x1) << 3) | ((self.oneAxisDataOverrun & 0x1) << 4) | ((self.twoAxisDataOverrun & 0x1) << 5) | ((self.dataOverrun & 0x1) << 6)

        def setValue(self, value: int):
            self.oneAxisDataAvailable = ((value >> 0) & 0x1)
            self.twoAxisDataAvailable = ((value >> 1) & 0x1)
            self.threeAxisDataAvailable = ((value >> 2) & 0x1)
            self.dataAvailable = ((value >> 3) & 0x1)
            self.oneAxisDataOverrun = ((value >> 4) & 0x1)
            self.twoAxisDataOverrun = ((value >> 5) & 0x1)
            self.dataOverrun = ((value >> 6) & 0x1)

        def __str__(self):
            retVal = ""
            retVal += "OneAxisDataAvailable: {} (offset: 0, width: 1)\r\n".format(self.oneAxisDataAvailable)
            retVal += "TwoAxisDataAvailable: {} (offset: 1, width: 1)\r\n".format(self.twoAxisDataAvailable)
            retVal += "ThreeAxisDataAvailable: {} (offset: 2, width: 1)\r\n".format(self.threeAxisDataAvailable)
            retVal += "DataAvailable: {} (offset: 3, width: 1)\r\n".format(self.dataAvailable)
            retVal += "OneAxisDataOverrun: {} (offset: 4, width: 1)\r\n".format(self.oneAxisDataOverrun)
            retVal += "TwoAxisDataOverrun: {} (offset: 5, width: 1)\r\n".format(self.twoAxisDataOverrun)
            retVal += "DataOverrun: {} (offset: 6, width: 1)\r\n".format(self.dataOverrun)
            return retVal

    class OutAdc1Register(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x08, 2, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.value & 0x3FF) << 6)

        def setValue(self, value: int):
            self.value = ((value >> 6) & 0x3FF)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 6, width: 10)\r\n".format(self.value)
            return retVal

    class OutAdc2Register(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x0A, 2, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.value & 0x3FF) << 6)

        def setValue(self, value: int):
            self.value = ((value >> 6) & 0x3FF)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 6, width: 10)\r\n".format(self.value)
            return retVal

    class OutAdc3Register(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x0C, 2, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.value & 0x3FF) << 6)

        def setValue(self, value: int):
            self.value = ((value >> 6) & 0x3FF)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 6, width: 10)\r\n".format(self.value)
            return retVal

    class WhoAmIRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x0f, 1, False)
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

    class Ctrl0Register(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x1E, 1, False)
            self.sdoPuDisc = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.sdoPuDisc & 0xFF) << 0)

        def setValue(self, value: int):
            self.sdoPuDisc = ((value >> 0) & 0xFF)

        def __str__(self):
            retVal = ""
            retVal += "SdoPuDisc: {} (offset: 0, width: 8)\r\n".format(self.sdoPuDisc)
            return retVal

    class TempCfgRegRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x1F, 1, False)
            self.adcEn = 0
            self.tempEn = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.adcEn & 0x1) << 7) | ((self.tempEn & 0x1) << 6)

        def setValue(self, value: int):
            self.adcEn = ((value >> 7) & 0x1)
            self.tempEn = ((value >> 6) & 0x1)

        def __str__(self):
            retVal = ""
            retVal += "AdcEn: {} (offset: 7, width: 1)\r\n".format(self.adcEn)
            retVal += "TempEn: {} (offset: 6, width: 1)\r\n".format(self.tempEn)
            return retVal

    class Ctrl2Register(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x21, 1, False)
            self.highPassAoiInt1Enable = 0
            self.highPassAoiInt2Enable = 0
            self.highPassClickEnable = 0
            self.filterDataPassThru = 0
            self.highPassFilterCutoffFrequency = 0
            self.highPassFilterModeSelection = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.highPassAoiInt1Enable & 0x1) << 0) | ((self.highPassAoiInt2Enable & 0x1) << 1) | ((self.highPassClickEnable & 0x1) << 2) | ((self.filterDataPassThru & 0x1) << 3) | ((self.highPassFilterCutoffFrequency & 0x3) << 4) | ((self.highPassFilterModeSelection & 0x3) << 6)

        def setValue(self, value: int):
            self.highPassAoiInt1Enable = ((value >> 0) & 0x1)
            self.highPassAoiInt2Enable = ((value >> 1) & 0x1)
            self.highPassClickEnable = ((value >> 2) & 0x1)
            self.filterDataPassThru = ((value >> 3) & 0x1)
            self.highPassFilterCutoffFrequency = ((value >> 4) & 0x3)
            self.highPassFilterModeSelection = ((value >> 6) & 0x3)

        def __str__(self):
            retVal = ""
            retVal += "HighPassAoiInt1Enable: {} (offset: 0, width: 1)\r\n".format(self.highPassAoiInt1Enable)
            retVal += "HighPassAoiInt2Enable: {} (offset: 1, width: 1)\r\n".format(self.highPassAoiInt2Enable)
            retVal += "HighPassClickEnable: {} (offset: 2, width: 1)\r\n".format(self.highPassClickEnable)
            retVal += "FilterDataPassThru: {} (offset: 3, width: 1)\r\n".format(self.filterDataPassThru)
            retVal += "HighPassFilterCutoffFrequency: {} (offset: 4, width: 2)\r\n".format(self.highPassFilterCutoffFrequency)
            retVal += "HighPassFilterModeSelection: {} (offset: 6, width: 2)\r\n".format(self.highPassFilterModeSelection)
            return retVal

    class Ctrl3Register(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x22, 1, False)
            self.overrun = 0
            self.fifoWatermark = 0
            self.da321 = 0
            self.zyxda = 0
            self.ia2 = 0
            self.ia1 = 0
            self.click = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.overrun & 0x1) << 1) | ((self.fifoWatermark & 0x1) << 2) | ((self.da321 & 0x1) << 3) | ((self.zyxda & 0x1) << 4) | ((self.ia2 & 0x1) << 5) | ((self.ia1 & 0x1) << 6) | ((self.click & 0x1) << 7)

        def setValue(self, value: int):
            self.overrun = ((value >> 1) & 0x1)
            self.fifoWatermark = ((value >> 2) & 0x1)
            self.da321 = ((value >> 3) & 0x1)
            self.zyxda = ((value >> 4) & 0x1)
            self.ia2 = ((value >> 5) & 0x1)
            self.ia1 = ((value >> 6) & 0x1)
            self.click = ((value >> 7) & 0x1)

        def __str__(self):
            retVal = ""
            retVal += "Overrun: {} (offset: 1, width: 1)\r\n".format(self.overrun)
            retVal += "FifoWatermark: {} (offset: 2, width: 1)\r\n".format(self.fifoWatermark)
            retVal += "Da321: {} (offset: 3, width: 1)\r\n".format(self.da321)
            retVal += "Zyxda: {} (offset: 4, width: 1)\r\n".format(self.zyxda)
            retVal += "Ia2: {} (offset: 5, width: 1)\r\n".format(self.ia2)
            retVal += "Ia1: {} (offset: 6, width: 1)\r\n".format(self.ia1)
            retVal += "Click: {} (offset: 7, width: 1)\r\n".format(self.click)
            return retVal

    class Ctrl4Register(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x23, 1, False)
            self.spiInterfaceMode = 0
            self.selfTestEnable = 0
            self.highResolutionOutput = 0
            self.fullScaleSelection = 0
            self.bigEndian = 0
            self.blockDataUpdate = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.spiInterfaceMode & 0x1) << 0) | ((self.selfTestEnable & 0x3) << 1) | ((self.highResolutionOutput & 0x1) << 3) | ((self.fullScaleSelection & 0x3) << 4) | ((self.bigEndian & 0x1) << 6) | ((self.blockDataUpdate & 0x1) << 7)

        def setValue(self, value: int):
            self.spiInterfaceMode = ((value >> 0) & 0x1)
            self.selfTestEnable = ((value >> 1) & 0x3)
            self.highResolutionOutput = ((value >> 3) & 0x1)
            self.fullScaleSelection = ((value >> 4) & 0x3)
            self.bigEndian = ((value >> 6) & 0x1)
            self.blockDataUpdate = ((value >> 7) & 0x1)

        def __str__(self):
            retVal = ""
            retVal += "SpiInterfaceMode: {} (offset: 0, width: 1)\r\n".format(self.spiInterfaceMode)
            retVal += "SelfTestEnable: {} (offset: 1, width: 2)\r\n".format(self.selfTestEnable)
            retVal += "HighResolutionOutput: {} (offset: 3, width: 1)\r\n".format(self.highResolutionOutput)
            retVal += "FullScaleSelection: {} (offset: 4, width: 2)\r\n".format(self.fullScaleSelection)
            retVal += "BigEndian: {} (offset: 6, width: 1)\r\n".format(self.bigEndian)
            retVal += "BlockDataUpdate: {} (offset: 7, width: 1)\r\n".format(self.blockDataUpdate)
            return retVal

    class Ctrl5Register(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x24, 1, False)
            self.enable4DInt2 = 0
            self.latchInt2 = 0
            self.enable4DInt1 = 0
            self.latchInt1 = 0
            self.fifoEnable = 0
            self.rebootMemoryContent = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.enable4DInt2 & 0x1) << 0) | ((self.latchInt2 & 0x1) << 1) | ((self.enable4DInt1 & 0x1) << 2) | ((self.latchInt1 & 0x1) << 3) | ((self.fifoEnable & 0x1) << 4) | ((self.rebootMemoryContent & 0x1) << 5)

        def setValue(self, value: int):
            self.enable4DInt2 = ((value >> 0) & 0x1)
            self.latchInt2 = ((value >> 1) & 0x1)
            self.enable4DInt1 = ((value >> 2) & 0x1)
            self.latchInt1 = ((value >> 3) & 0x1)
            self.fifoEnable = ((value >> 4) & 0x1)
            self.rebootMemoryContent = ((value >> 5) & 0x1)

        def __str__(self):
            retVal = ""
            retVal += "Enable4DInt2: {} (offset: 0, width: 1)\r\n".format(self.enable4DInt2)
            retVal += "LatchInt2: {} (offset: 1, width: 1)\r\n".format(self.latchInt2)
            retVal += "Enable4DInt1: {} (offset: 2, width: 1)\r\n".format(self.enable4DInt1)
            retVal += "LatchInt1: {} (offset: 3, width: 1)\r\n".format(self.latchInt1)
            retVal += "FifoEnable: {} (offset: 4, width: 1)\r\n".format(self.fifoEnable)
            retVal += "RebootMemoryContent: {} (offset: 5, width: 1)\r\n".format(self.rebootMemoryContent)
            return retVal

    class Ctrl6Register(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x25, 1, False)
            self.intPolarity = 0
            self.act = 0
            self.boot = 0
            self.ia2 = 0
            self.ia1 = 0
            self.click = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.intPolarity & 0x1) << 1) | ((self.act & 0x1) << 3) | ((self.boot & 0x1) << 4) | ((self.ia2 & 0x1) << 5) | ((self.ia1 & 0x1) << 6) | ((self.click & 0x1) << 7)

        def setValue(self, value: int):
            self.intPolarity = ((value >> 1) & 0x1)
            self.act = ((value >> 3) & 0x1)
            self.boot = ((value >> 4) & 0x1)
            self.ia2 = ((value >> 5) & 0x1)
            self.ia1 = ((value >> 6) & 0x1)
            self.click = ((value >> 7) & 0x1)

        def __str__(self):
            retVal = ""
            retVal += "IntPolarity: {} (offset: 1, width: 1)\r\n".format(self.intPolarity)
            retVal += "Act: {} (offset: 3, width: 1)\r\n".format(self.act)
            retVal += "Boot: {} (offset: 4, width: 1)\r\n".format(self.boot)
            retVal += "Ia2: {} (offset: 5, width: 1)\r\n".format(self.ia2)
            retVal += "Ia1: {} (offset: 6, width: 1)\r\n".format(self.ia1)
            retVal += "Click: {} (offset: 7, width: 1)\r\n".format(self.click)
            return retVal

    class ReferenceRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x26, 1, False)
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
            Register.__init__(self, reg_manager, 0x27, 1, False)
            self.xda = 0
            self.yda = 0
            self.zda = 0
            self.zyxda = 0
            self.xor = 0
            self.yor = 0
            self.zor = 0
            self.zyxor = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.xda & 0x1) << 0) | ((self.yda & 0x1) << 1) | ((self.zda & 0x1) << 2) | ((self.zyxda & 0x1) << 3) | ((self.xor & 0x1) << 4) | ((self.yor & 0x1) << 5) | ((self.zor & 0x1) << 6) | ((self.zyxor & 0x1) << 7)

        def setValue(self, value: int):
            self.xda = ((value >> 0) & 0x1)
            self.yda = ((value >> 1) & 0x1)
            self.zda = ((value >> 2) & 0x1)
            self.zyxda = ((value >> 3) & 0x1)
            self.xor = ((value >> 4) & 0x1)
            self.yor = ((value >> 5) & 0x1)
            self.zor = ((value >> 6) & 0x1)
            self.zyxor = ((value >> 7) & 0x1)

        def __str__(self):
            retVal = ""
            retVal += "Xda: {} (offset: 0, width: 1)\r\n".format(self.xda)
            retVal += "Yda: {} (offset: 1, width: 1)\r\n".format(self.yda)
            retVal += "Zda: {} (offset: 2, width: 1)\r\n".format(self.zda)
            retVal += "Zyxda: {} (offset: 3, width: 1)\r\n".format(self.zyxda)
            retVal += "Xor: {} (offset: 4, width: 1)\r\n".format(self.xor)
            retVal += "Yor: {} (offset: 5, width: 1)\r\n".format(self.yor)
            retVal += "Zor: {} (offset: 6, width: 1)\r\n".format(self.zor)
            retVal += "Zyxor: {} (offset: 7, width: 1)\r\n".format(self.zyxor)
            return retVal

    class FifoCtrlRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x2E, 1, False)
            self.fifoThreshold = 0
            self.triggerSelection = 0
            self.fifoMode = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.fifoThreshold & 0x1F) << 0) | ((self.triggerSelection & 0x1) << 5) | ((self.fifoMode & 0x3) << 6)

        def setValue(self, value: int):
            self.fifoThreshold = ((value >> 0) & 0x1F)
            self.triggerSelection = ((value >> 5) & 0x1)
            self.fifoMode = ((value >> 6) & 0x3)

        def __str__(self):
            retVal = ""
            retVal += "FifoThreshold: {} (offset: 0, width: 5)\r\n".format(self.fifoThreshold)
            retVal += "TriggerSelection: {} (offset: 5, width: 1)\r\n".format(self.triggerSelection)
            retVal += "FifoMode: {} (offset: 6, width: 2)\r\n".format(self.fifoMode)
            return retVal

    class FifoSrcRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x2F, 1, False)
            self.fss = 0
            self.emtpy = 0
            self.overrunFifo = 0
            self.watermark = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.fss & 0x1F) << 0) | ((self.emtpy & 0x1) << 5) | ((self.overrunFifo & 0x1) << 6) | ((self.watermark & 0x1) << 7)

        def setValue(self, value: int):
            self.fss = ((value >> 0) & 0x1F)
            self.emtpy = ((value >> 5) & 0x1)
            self.overrunFifo = ((value >> 6) & 0x1)
            self.watermark = ((value >> 7) & 0x1)

        def __str__(self):
            retVal = ""
            retVal += "Fss: {} (offset: 0, width: 5)\r\n".format(self.fss)
            retVal += "Emtpy: {} (offset: 5, width: 1)\r\n".format(self.emtpy)
            retVal += "OverrunFifo: {} (offset: 6, width: 1)\r\n".format(self.overrunFifo)
            retVal += "Watermark: {} (offset: 7, width: 1)\r\n".format(self.watermark)
            return retVal

    class Int1CfgRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x30, 1, False)
            self.enableXLowEvent = 0
            self.enableXHighEvent = 0
            self.enableYLowEvent = 0
            self.enableYHighEvent = 0
            self.enableZLowEvent = 0
            self.enableZHighEvent = 0
            self.enable6D = 0
            self.andOrInterruptEvents = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.enableXLowEvent & 0x1) << 0) | ((self.enableXHighEvent & 0x1) << 1) | ((self.enableYLowEvent & 0x1) << 2) | ((self.enableYHighEvent & 0x1) << 3) | ((self.enableZLowEvent & 0x1) << 4) | ((self.enableZHighEvent & 0x1) << 5) | ((self.enable6D & 0x1) << 6) | ((self.andOrInterruptEvents & 0x1) << 7)

        def setValue(self, value: int):
            self.enableXLowEvent = ((value >> 0) & 0x1)
            self.enableXHighEvent = ((value >> 1) & 0x1)
            self.enableYLowEvent = ((value >> 2) & 0x1)
            self.enableYHighEvent = ((value >> 3) & 0x1)
            self.enableZLowEvent = ((value >> 4) & 0x1)
            self.enableZHighEvent = ((value >> 5) & 0x1)
            self.enable6D = ((value >> 6) & 0x1)
            self.andOrInterruptEvents = ((value >> 7) & 0x1)

        def __str__(self):
            retVal = ""
            retVal += "EnableXLowEvent: {} (offset: 0, width: 1)\r\n".format(self.enableXLowEvent)
            retVal += "EnableXHighEvent: {} (offset: 1, width: 1)\r\n".format(self.enableXHighEvent)
            retVal += "EnableYLowEvent: {} (offset: 2, width: 1)\r\n".format(self.enableYLowEvent)
            retVal += "EnableYHighEvent: {} (offset: 3, width: 1)\r\n".format(self.enableYHighEvent)
            retVal += "EnableZLowEvent: {} (offset: 4, width: 1)\r\n".format(self.enableZLowEvent)
            retVal += "EnableZHighEvent: {} (offset: 5, width: 1)\r\n".format(self.enableZHighEvent)
            retVal += "Enable6D: {} (offset: 6, width: 1)\r\n".format(self.enable6D)
            retVal += "AndOrInterruptEvents: {} (offset: 7, width: 1)\r\n".format(self.andOrInterruptEvents)
            return retVal

    class Int1SrcRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x31, 1, False)
            self.xLow = 0
            self.xHigh = 0
            self.yLow = 0
            self.yHigh = 0
            self.zLow = 0
            self.zHigh = 0
            self.interruptActive = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.xLow & 0x1) << 0) | ((self.xHigh & 0x1) << 1) | ((self.yLow & 0x1) << 2) | ((self.yHigh & 0x1) << 3) | ((self.zLow & 0x1) << 4) | ((self.zHigh & 0x1) << 5) | ((self.interruptActive & 0x1) << 6)

        def setValue(self, value: int):
            self.xLow = ((value >> 0) & 0x1)
            self.xHigh = ((value >> 1) & 0x1)
            self.yLow = ((value >> 2) & 0x1)
            self.yHigh = ((value >> 3) & 0x1)
            self.zLow = ((value >> 4) & 0x1)
            self.zHigh = ((value >> 5) & 0x1)
            self.interruptActive = ((value >> 6) & 0x1)

        def __str__(self):
            retVal = ""
            retVal += "XLow: {} (offset: 0, width: 1)\r\n".format(self.xLow)
            retVal += "XHigh: {} (offset: 1, width: 1)\r\n".format(self.xHigh)
            retVal += "YLow: {} (offset: 2, width: 1)\r\n".format(self.yLow)
            retVal += "YHigh: {} (offset: 3, width: 1)\r\n".format(self.yHigh)
            retVal += "ZLow: {} (offset: 4, width: 1)\r\n".format(self.zLow)
            retVal += "ZHigh: {} (offset: 5, width: 1)\r\n".format(self.zHigh)
            retVal += "InterruptActive: {} (offset: 6, width: 1)\r\n".format(self.interruptActive)
            return retVal

    class Int1ThresholdRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x32, 1, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.value & 0x7F) << 0)

        def setValue(self, value: int):
            self.value = ((value >> 0) & 0x7F)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 0, width: 7)\r\n".format(self.value)
            return retVal

    class Int1DurationRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x33, 1, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.value & 0x7F) << 0)

        def setValue(self, value: int):
            self.value = ((value >> 0) & 0x7F)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 0, width: 7)\r\n".format(self.value)
            return retVal

    class Int2CfgRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x34, 1, False)
            self.enableXLowEvent = 0
            self.enableXHighEvent = 0
            self.enableYLowEvent = 0
            self.enableYHighEvent = 0
            self.enableZLowEvent = 0
            self.enableZHighEvent = 0
            self.enable6D = 0
            self.andOrInterruptEvents = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.enableXLowEvent & 0x1) << 0) | ((self.enableXHighEvent & 0x1) << 1) | ((self.enableYLowEvent & 0x1) << 2) | ((self.enableYHighEvent & 0x1) << 3) | ((self.enableZLowEvent & 0x1) << 4) | ((self.enableZHighEvent & 0x1) << 5) | ((self.enable6D & 0x1) << 6) | ((self.andOrInterruptEvents & 0x1) << 7)

        def setValue(self, value: int):
            self.enableXLowEvent = ((value >> 0) & 0x1)
            self.enableXHighEvent = ((value >> 1) & 0x1)
            self.enableYLowEvent = ((value >> 2) & 0x1)
            self.enableYHighEvent = ((value >> 3) & 0x1)
            self.enableZLowEvent = ((value >> 4) & 0x1)
            self.enableZHighEvent = ((value >> 5) & 0x1)
            self.enable6D = ((value >> 6) & 0x1)
            self.andOrInterruptEvents = ((value >> 7) & 0x1)

        def __str__(self):
            retVal = ""
            retVal += "EnableXLowEvent: {} (offset: 0, width: 1)\r\n".format(self.enableXLowEvent)
            retVal += "EnableXHighEvent: {} (offset: 1, width: 1)\r\n".format(self.enableXHighEvent)
            retVal += "EnableYLowEvent: {} (offset: 2, width: 1)\r\n".format(self.enableYLowEvent)
            retVal += "EnableYHighEvent: {} (offset: 3, width: 1)\r\n".format(self.enableYHighEvent)
            retVal += "EnableZLowEvent: {} (offset: 4, width: 1)\r\n".format(self.enableZLowEvent)
            retVal += "EnableZHighEvent: {} (offset: 5, width: 1)\r\n".format(self.enableZHighEvent)
            retVal += "Enable6D: {} (offset: 6, width: 1)\r\n".format(self.enable6D)
            retVal += "AndOrInterruptEvents: {} (offset: 7, width: 1)\r\n".format(self.andOrInterruptEvents)
            return retVal

    class Int2SrcRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x35, 1, False)
            self.xLow = 0
            self.xHigh = 0
            self.yLow = 0
            self.yHigh = 0
            self.zLow = 0
            self.zHigh = 0
            self.interruptActive = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.xLow & 0x1) << 0) | ((self.xHigh & 0x1) << 1) | ((self.yLow & 0x1) << 2) | ((self.yHigh & 0x1) << 3) | ((self.zLow & 0x1) << 4) | ((self.zHigh & 0x1) << 5) | ((self.interruptActive & 0x1) << 6)

        def setValue(self, value: int):
            self.xLow = ((value >> 0) & 0x1)
            self.xHigh = ((value >> 1) & 0x1)
            self.yLow = ((value >> 2) & 0x1)
            self.yHigh = ((value >> 3) & 0x1)
            self.zLow = ((value >> 4) & 0x1)
            self.zHigh = ((value >> 5) & 0x1)
            self.interruptActive = ((value >> 6) & 0x1)

        def __str__(self):
            retVal = ""
            retVal += "XLow: {} (offset: 0, width: 1)\r\n".format(self.xLow)
            retVal += "XHigh: {} (offset: 1, width: 1)\r\n".format(self.xHigh)
            retVal += "YLow: {} (offset: 2, width: 1)\r\n".format(self.yLow)
            retVal += "YHigh: {} (offset: 3, width: 1)\r\n".format(self.yHigh)
            retVal += "ZLow: {} (offset: 4, width: 1)\r\n".format(self.zLow)
            retVal += "ZHigh: {} (offset: 5, width: 1)\r\n".format(self.zHigh)
            retVal += "InterruptActive: {} (offset: 6, width: 1)\r\n".format(self.interruptActive)
            return retVal

    class Int2ThresholdRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x36, 1, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.value & 0x7F) << 0)

        def setValue(self, value: int):
            self.value = ((value >> 0) & 0x7F)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 0, width: 7)\r\n".format(self.value)
            return retVal

    class Int2DurationRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x37, 1, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.value & 0x7F) << 0)

        def setValue(self, value: int):
            self.value = ((value >> 0) & 0x7F)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 0, width: 7)\r\n".format(self.value)
            return retVal

    class ClickSourceRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x39, 1, False)
            self.x = 0
            self.y = 0
            self.z = 0
            self.sign = 0
            self.singleClickEnable = 0
            self.doubleClickEnable = 0
            self.interruptActive = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.x & 0x1) << 0) | ((self.y & 0x1) << 1) | ((self.z & 0x1) << 2) | ((self.sign & 0x1) << 3) | ((self.singleClickEnable & 0x1) << 4) | ((self.doubleClickEnable & 0x1) << 5) | ((self.interruptActive & 0x1) << 6)

        def setValue(self, value: int):
            self.x = ((value >> 0) & 0x1)
            self.y = ((value >> 1) & 0x1)
            self.z = ((value >> 2) & 0x1)
            self.sign = ((value >> 3) & 0x1)
            self.singleClickEnable = ((value >> 4) & 0x1)
            self.doubleClickEnable = ((value >> 5) & 0x1)
            self.interruptActive = ((value >> 6) & 0x1)

        def __str__(self):
            retVal = ""
            retVal += "X: {} (offset: 0, width: 1)\r\n".format(self.x)
            retVal += "Y: {} (offset: 1, width: 1)\r\n".format(self.y)
            retVal += "Z: {} (offset: 2, width: 1)\r\n".format(self.z)
            retVal += "Sign: {} (offset: 3, width: 1)\r\n".format(self.sign)
            retVal += "SingleClickEnable: {} (offset: 4, width: 1)\r\n".format(self.singleClickEnable)
            retVal += "DoubleClickEnable: {} (offset: 5, width: 1)\r\n".format(self.doubleClickEnable)
            retVal += "InterruptActive: {} (offset: 6, width: 1)\r\n".format(self.interruptActive)
            return retVal

    class ClickThresholdRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x3A, 1, False)
            self.threshold = 0
            self.lirClick = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.threshold & 0x7F) << 0) | ((self.lirClick & 0x1) << 7)

        def setValue(self, value: int):
            self.threshold = ((value >> 0) & 0x7F)
            self.lirClick = ((value >> 7) & 0x1)

        def __str__(self):
            retVal = ""
            retVal += "Threshold: {} (offset: 0, width: 7)\r\n".format(self.threshold)
            retVal += "LirClick: {} (offset: 7, width: 1)\r\n".format(self.lirClick)
            return retVal

    class TimeLimitRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x3B, 1, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.value & 0x7F) << 0)

        def setValue(self, value: int):
            self.value = ((value >> 0) & 0x7F)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 0, width: 7)\r\n".format(self.value)
            return retVal

    class TimeLatencyRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x3C, 10, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.value & 0x7FFF) << 0)

        def setValue(self, value: int):
            self.value = ((value >> 0) & 0x7FFF)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 0, width: 79)\r\n".format(self.value)
            return retVal

    class TimeWindowRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x3D, 1, False)
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

    class ActivationThresholdRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x3E, 1, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.value & 0x7F) << 0)

        def setValue(self, value: int):
            self.value = ((value >> 0) & 0x7F)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 0, width: 7)\r\n".format(self.value)
            return retVal

    class ActivationDurationRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0x3F, 1, False)
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

    class Ctrl1Register(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0xA0, 1, False)
            self.xAxisEnable = 0
            self.yAxisEnable = 0
            self.zAxisEnable = 0
            self.lowPowerEnable = 0
            self.outputDataRate = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.xAxisEnable & 0x1) << 0) | ((self.yAxisEnable & 0x1) << 1) | ((self.zAxisEnable & 0x1) << 2) | ((self.lowPowerEnable & 0x1) << 3) | ((self.outputDataRate & 0xF) << 4)

        def setValue(self, value: int):
            self.xAxisEnable = ((value >> 0) & 0x1)
            self.yAxisEnable = ((value >> 1) & 0x1)
            self.zAxisEnable = ((value >> 2) & 0x1)
            self.lowPowerEnable = ((value >> 3) & 0x1)
            self.outputDataRate = ((value >> 4) & 0xF)

        def __str__(self):
            retVal = ""
            retVal += "XAxisEnable: {} (offset: 0, width: 1)\r\n".format(self.xAxisEnable)
            retVal += "YAxisEnable: {} (offset: 1, width: 1)\r\n".format(self.yAxisEnable)
            retVal += "ZAxisEnable: {} (offset: 2, width: 1)\r\n".format(self.zAxisEnable)
            retVal += "LowPowerEnable: {} (offset: 3, width: 1)\r\n".format(self.lowPowerEnable)
            retVal += "OutputDataRate: {} (offset: 4, width: 4)\r\n".format(self.outputDataRate)
            return retVal

    class OutXRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0xA8, 2, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.value & 0x3FF) << 6)

        def setValue(self, value: int):
            self.value = sign_extend((value >> 6) & 0x3FF, 10)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 6, width: 10)\r\n".format(self.value)
            return retVal

    class OutYRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0xAA, 2, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.value & 0x3FF) << 6)

        def setValue(self, value: int):
            self.value = sign_extend((value >> 6) & 0x3FF, 10)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 6, width: 10)\r\n".format(self.value)
            return retVal

    class OutZRegister(Register):
        def __init__(self, reg_manager: RegisterManager):
            Register.__init__(self, reg_manager, 0xAC, 2, False)
            self.value = 0


        def read(self):
            self._manager.read(self)
            return self
            
        def getValue(self):
            return ((self.value & 0x3FF) << 6)

        def setValue(self, value: int):
            self.value = sign_extend((value >> 6) & 0x3FF, 10)

        def __str__(self):
            retVal = ""
            retVal += "Value: {} (offset: 6, width: 10)\r\n".format(self.value)
            return retVal


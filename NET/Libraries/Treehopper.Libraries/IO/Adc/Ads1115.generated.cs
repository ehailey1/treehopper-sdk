/// This file was auto-generated by RegisterGenerator. Any changes to it will be overwritten!
using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Treehopper;
using Treehopper.Libraries.Utilities;

namespace Treehopper.Libraries.IO.Adc
{
    public partial class Ads1115
    {
        public enum ComparatorQueues
        {
            AssertAfterOneConversion = 0,
            AssertAfterTwoConversions = 1,
            AssertAfterFourConversions = 2,
            DisableComparator = 3
        }

        public enum DataRates
        {
            Sps_8 = 0,
            Sps_16 = 1,
            Sps_32 = 2,
            Sps_64 = 3,
            Sps_128 = 4,
            Sps_250 = 5,
            Sps_475 = 6,
            Sps_860 = 7
        }

        public enum Pgas
        {
            Fsr_6144 = 0,
            Fsr_4096 = 1,
            Fsr_2048 = 2,
            Fsr_1024 = 3,
            Fsr_512 = 4,
            Fsr_256 = 5
        }

        internal enum Muxes
        {
            ain0_ain1 = 0,
            ain0_ain3 = 1,
            ain1_ain3 = 2,
            ain2_ain3 = 3,
            ain0_gnd = 4,
            ain1_gnd = 5,
            ain2_gnd = 6,
            ain3_gnd = 7
        }

        internal class Ads1115Registers : RegisterManager
        {
            internal Ads1115Registers(SMBusDevice dev = null) : base(dev, true)
            {
                Conversion = new ConversionRegister(this);
                _registers.Add(Conversion);
                Config = new ConfigRegister(this);
                _registers.Add(Config);
                LowThreshold = new LowThresholdRegister(this);
                _registers.Add(LowThreshold);
                HighThreshold = new HighThresholdRegister(this);
                _registers.Add(HighThreshold);
            }

            internal ConversionRegister Conversion;
            internal ConfigRegister Config;
            internal LowThresholdRegister LowThreshold;
            internal HighThresholdRegister HighThreshold;

            internal class ConversionRegister : Register
            {
                internal ConversionRegister(RegisterManager regManager) : base(regManager, 0x00, 2, true) { }

                public int Value { get; set; }

                public async Task<ConversionRegister> Read()
                {
                    await manager.Read(this).ConfigureAwait(false);
                    return this;
                }
                internal override long GetValue() { return ((Value & 0xFFFF) << 0); }
                internal override void SetValue(long value)
                {
                    Value = (int)(((value >> 0) & 0xFFFF) << (32 - 16)) >> (32 - 16);
                }

                public override string ToString()
                {
                    string retVal = "";
                    retVal += $"Value: { Value } (offset: 0, width: 16)\r\n";
                    return retVal;
                }
            }
            internal class ConfigRegister : Register
            {
                internal ConfigRegister(RegisterManager regManager) : base(regManager, 0x01, 2, false) { }

                public int ComparatorQueue { get; set; }
                public int LatchingComparator { get; set; }
                public int ComparatorPolarity { get; set; }
                public int ComparatorMode { get; set; }
                public int DataRate { get; set; }
                public int OperatingMode { get; set; }
                public int Pga { get; set; }
                public int Mux { get; set; }
                public int OperationalStatus { get; set; }
                public ComparatorQueues GetComparatorQueue() { return (ComparatorQueues)ComparatorQueue; }
                public void SetComparatorQueue(ComparatorQueues enumVal) { ComparatorQueue = (int)enumVal; }
                public DataRates GetDataRate() { return (DataRates)DataRate; }
                public void SetDataRate(DataRates enumVal) { DataRate = (int)enumVal; }
                public Pgas GetPga() { return (Pgas)Pga; }
                public void SetPga(Pgas enumVal) { Pga = (int)enumVal; }
                public Muxes GetMux() { return (Muxes)Mux; }
                public void SetMux(Muxes enumVal) { Mux = (int)enumVal; }

                public async Task<ConfigRegister> Read()
                {
                    await manager.Read(this).ConfigureAwait(false);
                    return this;
                }
                internal override long GetValue() { return ((ComparatorQueue & 0x3) << 0) | ((LatchingComparator & 0x1) << 2) | ((ComparatorPolarity & 0x1) << 3) | ((ComparatorMode & 0x1) << 4) | ((DataRate & 0x7) << 5) | ((OperatingMode & 0x1) << 8) | ((Pga & 0x7) << 9) | ((Mux & 0x7) << 12) | ((OperationalStatus & 0x1) << 15); }
                internal override void SetValue(long value)
                {
                    ComparatorQueue = (int)((value >> 0) & 0x3);
                    LatchingComparator = (int)((value >> 2) & 0x1);
                    ComparatorPolarity = (int)((value >> 3) & 0x1);
                    ComparatorMode = (int)((value >> 4) & 0x1);
                    DataRate = (int)((value >> 5) & 0x7);
                    OperatingMode = (int)((value >> 8) & 0x1);
                    Pga = (int)((value >> 9) & 0x7);
                    Mux = (int)((value >> 12) & 0x7);
                    OperationalStatus = (int)((value >> 15) & 0x1);
                }

                public override string ToString()
                {
                    string retVal = "";
                    retVal += $"ComparatorQueue: { ComparatorQueue } (offset: 0, width: 2)\r\n";
                    retVal += $"LatchingComparator: { LatchingComparator } (offset: 2, width: 1)\r\n";
                    retVal += $"ComparatorPolarity: { ComparatorPolarity } (offset: 3, width: 1)\r\n";
                    retVal += $"ComparatorMode: { ComparatorMode } (offset: 4, width: 1)\r\n";
                    retVal += $"DataRate: { DataRate } (offset: 5, width: 3)\r\n";
                    retVal += $"OperatingMode: { OperatingMode } (offset: 8, width: 1)\r\n";
                    retVal += $"Pga: { Pga } (offset: 9, width: 3)\r\n";
                    retVal += $"Mux: { Mux } (offset: 12, width: 3)\r\n";
                    retVal += $"OperationalStatus: { OperationalStatus } (offset: 15, width: 1)\r\n";
                    return retVal;
                }
            }
            internal class LowThresholdRegister : Register
            {
                internal LowThresholdRegister(RegisterManager regManager) : base(regManager, 0x02, 2, true) { }

                public int Value { get; set; }

                public async Task<LowThresholdRegister> Read()
                {
                    await manager.Read(this).ConfigureAwait(false);
                    return this;
                }
                internal override long GetValue() { return ((Value & 0xFFFF) << 0); }
                internal override void SetValue(long value)
                {
                    Value = (int)(((value >> 0) & 0xFFFF) << (32 - 16)) >> (32 - 16);
                }

                public override string ToString()
                {
                    string retVal = "";
                    retVal += $"Value: { Value } (offset: 0, width: 16)\r\n";
                    return retVal;
                }
            }
            internal class HighThresholdRegister : Register
            {
                internal HighThresholdRegister(RegisterManager regManager) : base(regManager, 0x03, 2, true) { }

                public int Value { get; set; }

                public async Task<HighThresholdRegister> Read()
                {
                    await manager.Read(this).ConfigureAwait(false);
                    return this;
                }
                internal override long GetValue() { return ((Value & 0xFFFF) << 0); }
                internal override void SetValue(long value)
                {
                    Value = (int)(((value >> 0) & 0xFFFF) << (32 - 16)) >> (32 - 16);
                }

                public override string ToString()
                {
                    string retVal = "";
                    retVal += $"Value: { Value } (offset: 0, width: 16)\r\n";
                    return retVal;
                }
            }
        }
    }
}
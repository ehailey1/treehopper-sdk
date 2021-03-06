﻿using System.ComponentModel;
using System.Threading.Tasks;
using Treehopper.Utilities;

namespace Treehopper.Libraries.IO.Adc
{
    /// <summary>
    ///     Base class for ADC peripherals
    /// </summary>
    public class AdcPeripheralPin : AdcPin
    {
        private readonly int bitDepth;
        private int adcValue;
        protected IAdcPeripheral parent;

        /// <summary>
        ///     Construct a new ADC pin that's part of the specified peripheral
        /// </summary>
        /// <param name="parent">The peripheral</param>
        /// <param name="bitDepth">The ADC bitdepth</param>
        /// <param name="refVoltage">The reference voltage used to compare</param>
        public AdcPeripheralPin(IAdcPeripheral parent, int bitDepth, double refVoltage)
        {
            this.parent = parent;
            this.bitDepth = bitDepth;
            ReferenceVoltage = refVoltage;
        }

        /// <summary>
        ///     The reference voltage used for calculating analog voltage
        /// </summary>
        public double ReferenceVoltage { get; internal set; }

        /// <summary>
        ///     The amount the ADC value should change before triggering an event
        /// </summary>
        public int AdcValueChangedThreshold { get; set; }

        /// <summary>
        ///     The raw ADC value
        /// </summary>
        public int AdcValue
        {
            internal set
            {
                if (value.CloseTo(adcValue, AdcValueChangedThreshold))
                    AdcValueChanged?.Invoke(this, new AdcValueChangedEventArgs(adcValue));
                if (analogValueFromAdc(value).CloseTo(analogValueFromAdc(adcValue), AnalogValueChangedThreshold))
                    AnalogValueChanged?.Invoke(this, new AnalogValueChangedEventArgs(analogValueFromAdc(adcValue)));
                if (analogVoltageFromAdc(value).CloseTo(analogVoltageFromAdc(adcValue), AnalogVoltageChangedThreshold))
                    AnalogVoltageChanged?.Invoke(this, new AnalogVoltageChangedEventArgs(analogVoltageFromAdc(adcValue)));
                PropertyChanged?.Invoke(this, new PropertyChangedEventArgs("AdcValue"));
                PropertyChanged?.Invoke(this, new PropertyChangedEventArgs("AnalogValue"));
                PropertyChanged?.Invoke(this, new PropertyChangedEventArgs("AnalogVoltage"));
                adcValue = value;
            }

            get
            {
                if (parent.AutoUpdateWhenPropertyRead)
                    parent.UpdateAsync().Wait();

                return adcValue;
            }
        }

        /// <summary>
        ///     The amount that the analog value (0-1) should change before triggering an event
        /// </summary>
        public double AnalogValueChangedThreshold { get; set; }

        /// <summary>
        ///     The analog value (from 0-1) of the ADC pin
        /// </summary>
        public double AnalogValue => analogValueFromAdc(AdcValue);

        /// <summary>
        ///     The change in voltage required to trigger an event
        /// </summary>
        public double AnalogVoltageChangedThreshold { get; set; }

        /// <summary>
        ///     The analog voltage of the pin
        /// </summary>
        public double AnalogVoltage => analogVoltageFromAdc(AdcValue);

        /// <summary>
        ///     Fires whenever the ADC value changes by the specified threshold
        /// </summary>
        public event OnAdcValueChanged AdcValueChanged;

        /// <summary>
        ///     Fires whenever the analog value changes by the specified threshold
        /// </summary>
        public event OnAnalogValueChanged AnalogValueChanged;

        /// <summary>
        ///     Fires whenever the analog voltage changes by the specified threshold
        /// </summary>
        public event OnAnalogVoltageChanged AnalogVoltageChanged;
        public event PropertyChangedEventHandler PropertyChanged;

        /// <summary>
        ///     Make the pin an analog input. This is unused in most implementations
        /// </summary>
        public Task MakeAnalogInAsync()
        {
            return Task.FromResult<object>(null);
        }

        private double analogValueFromAdc(int adcValue)
        {
            return(double) adcValue / ((1 << bitDepth) - 1);
        }

        private double analogVoltageFromAdc(int adcValue)
        {
            return ReferenceVoltage * analogValueFromAdc(adcValue);
        }
    }
}
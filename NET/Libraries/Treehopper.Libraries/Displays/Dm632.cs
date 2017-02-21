﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Treehopper.Libraries.Interface.PortExpander;
using Treehopper.Utilities;

namespace Treehopper.Libraries.Displays
{
    /// <summary>
    /// Library for the SiTI DM632, DM633, and DM634 16-channel, 16-bit PWM-capable shift-register-type LED driver
    /// </summary>
    public class Dm632 : ChainableShiftRegisterOutput, ILedDriver
    {
        /// <summary>
        /// Construct a DM632 16-channel, 16-bit PWM LED controller attached directly to an SPI port
        /// </summary>
        /// <param name="SpiModule">The SPI module to use</param>
        /// <param name="LatchPin">The latch pin to use</param>
        /// <param name="speedMhz">The speed, in MHz, to use</param>
        public Dm632(Spi SpiModule, SpiChipSelectPin LatchPin, double speedMhz = 6) : base(SpiModule, LatchPin, 32, speedMhz)
        {
            start();
        }

        /// <summary>
        /// Construct a DM632 16-channel, 16-bit PWM LED controller attached to the output of another shift register
        /// </summary>
        /// <param name="upstreamDevice">The shift register this DM632 is attached to</param>
        public Dm632(ChainableShiftRegisterOutput upstreamDevice) : base(upstreamDevice, 32)
        {
            start();
        }

        private void start()
        {
            for (int i = 0; i < 16; i++)
                Leds.Add(new Led(this, i, true));
        }

        private double globalBrightness = 1.0;

        /// <summary>
        /// Gets or sets the brightness of the display
        /// </summary>
        /// <remarks>
        /// <para>The DM632 has no global brightness control, so this property emulates this functionality by scaling each LED's output value by this value.
        /// </para>
        /// </remarks>
        public double Brightness
        {
            get { return globalBrightness; }
            set {
                if (value.CloseTo(globalBrightness)) return;
                if (value < 0 || value > 1)
                    throw new ArgumentOutOfRangeException("Valid brightness is from 0 to 1");
                globalBrightness = value;

                bool savedAutoflushState = AutoFlush;
                AutoFlush = false;
                Leds.ForEach(led => update(led));
                Flush().Wait();
                AutoFlush = savedAutoflushState;
            }
        }

        /// <summary>
        /// Gets whether this display has global brightness control (Hint: it does!)
        /// </summary>
        public bool HasGlobalBrightnessControl { get { return true; } }

        /// <summary>
        /// Gets whether this display has individual brightness control (which it does!)
        /// </summary>
        public bool HasIndividualBrightnessControl { get { return true; } }

        /// <summary>
        /// Gets the list of LEDs associated with this driver
        /// </summary>
        public IList<Led> Leds { get; private set; } = new List<Led>();

        /// <summary>
        /// Clear the outputs of all LEDs
        /// </summary>
        /// <returns>An awaitable task that completes upon success</returns>
        public Task Clear()
        {
            return Write(new byte[32]);
        }

        void ILedDriver.LedBrightnessChanged(Led led)
        {
            update(led);
        }

        void ILedDriver.LedStateChanged(Led led)
        {
            update(led);
        }

        void update(Led led)
        {
            if (led.State)
            {
                CurrentValue[led.Channel * 2 + 1] = (byte)((int)Math.Round(Utility.BrightnessToCieLuminance(led.Brightness * globalBrightness) * 65535) >> 8);
                CurrentValue[led.Channel * 2] = (byte)((int)Math.Round(Utility.BrightnessToCieLuminance(led.Brightness * globalBrightness) * 65535) & 0xFF);
            } else
            {
                CurrentValue[led.Channel * 2] = 0x00;
                CurrentValue[led.Channel * 2 + 1] = 0x00;
            }
            FlushIfAutoFlushEnabled().Wait();
        }

        /// <summary>
        /// Set the individual LED brightness values based on the direct value written to this register
        /// </summary>
        /// <remarks>
        /// <para>Note that the state is always set to true when this is called; only the brightness is adjusted</para>
        /// </remarks>
        protected override void updateFromCurrentValue()
        {
            for (int i = 0; i < Leds.Count; i++)
            {
                UInt16 val = BitConverter.ToUInt16(CurrentValue, i * 2);
                Leds[i].State = true;
                Leds[i].Brightness = (double)val / UInt16.MaxValue;
            }
        }
    }
}

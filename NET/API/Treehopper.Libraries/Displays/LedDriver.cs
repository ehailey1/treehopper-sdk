﻿using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Threading.Tasks;
using Treehopper.Libraries.IO;
using Treehopper.Utilities;

namespace Treehopper.Libraries.Displays
{
    /// <summary>
    ///     Base class that all LED drivers inherit from.
    /// </summary>
    public abstract class LedDriver : ILedDriver
    {
        /// <summary>
        ///     The internally-referenced global brightness of the LED driver
        /// </summary>
        protected double brightness;

        /// <summary>
        ///     Construct an LedDriver
        /// </summary>
        /// <param name="numLeds">The number of LEDs to construct</param>
        /// <param name="HasGlobalBrightnessControl">Whether the controller can globally adjust the LED brightness.</param>
        /// <param name="HasIndividualBrightnessControl">Whether the controller has individual LED brightness control</param>
        public LedDriver(int numLeds, bool HasGlobalBrightnessControl, bool HasIndividualBrightnessControl)
        {
            this.HasGlobalBrightnessControl = HasGlobalBrightnessControl;
            this.HasIndividualBrightnessControl = HasIndividualBrightnessControl;
            for (var i = 0; i < numLeds; i++)
            {
                var led = new Led(this, i, HasIndividualBrightnessControl);
                Leds.Add(led);
            }
        }

        /// <summary>
        ///     Gets or sets whether the display should auto-flush whenever an LED state is changed
        /// </summary>
        public bool AutoFlush { get; set; } = true;

        /// <summary>
        ///     Gets or sets whether this controller supports global brightness control.
        /// </summary>
        public bool HasGlobalBrightnessControl { get; protected set; }

        /// <summary>
        ///     Gets or sets whether this controller's LEDs have individual brightness control (through PWM or otherwise).
        /// </summary>
        public bool HasIndividualBrightnessControl { get; }

        /// <summary>
        ///     The global brightness, from 0.0-1.0, of the LEDs attached to this driver
        /// </summary>
        public double Brightness
        {
            get { return brightness; }

            set
            {
                if (value.CloseTo(brightness)) return;
                if (value < 0 || value > 1)
                    throw new ArgumentOutOfRangeException("Valid brightness is from 0 to 1");
                brightness = value;

                if (HasGlobalBrightnessControl) // might be more efficient
                {
                    SetGlobalBrightness(brightness);
                }
                else if (HasIndividualBrightnessControl)
                {
                    var savedAutoflushState = AutoFlush;
                    AutoFlush = false;
                    foreach (var led in Leds)
                        led.Brightness = brightness;
                    FlushAsync().Wait();
                    AutoFlush = savedAutoflushState;
                }
            }
        }

        /// <summary>
        ///     The collection of LEDs that belong to this driver.
        /// </summary>
        public IList<Led> Leds { get; set; } = new Collection<Led>();

        /// <summary>
        ///     Gets the parent device of this LED driver
        /// </summary>
        public IFlushable Parent { get; protected set; }

        void ILedDriver.LedStateChanged(Led led)
        {
            LedStateChanged(led);
        }

        void ILedDriver.LedBrightnessChanged(Led led)
        {
            LedBrightnessChanged(led);
        }

        /// <summary>
        ///     Clear the display
        /// </summary>
        /// <returns>An awaitable task that completes when the display is cleared</returns>
        public async Task Clear()
        {
            var autoflushSave = AutoFlush;
            AutoFlush = false;
            foreach (var led in Leds)
                led.State = false;
            await FlushAsync(true).ConfigureAwait(false);
            AutoFlush = autoflushSave;
        }

        /// <summary>
        ///     Write out the current values of the LEDs immediately.
        /// </summary>
        /// <param name="force">Whether to write out all values, even if they appear unchanged.</param>
        /// <returns>An awaitable <see cref="Task" /></returns>
        public abstract Task FlushAsync(bool force = false);

        internal abstract void SetGlobalBrightness(double brightness);


        /// <summary>
        ///     Called by the LED when the state changes
        /// </summary>
        /// <param name="led">The LED whose state changed</param>
        internal abstract void LedStateChanged(Led led);


        /// <summary>
        ///     Called by the LED when the brightness changed
        /// </summary>
        /// <param name="led">The LED whose brightness changed</param>
        internal abstract void LedBrightnessChanged(Led led);
    }
}
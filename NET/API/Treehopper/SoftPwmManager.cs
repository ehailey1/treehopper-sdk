﻿using System;
using System.Collections.Generic;
using System.Linq;
using Treehopper.ThirdParty;

namespace Treehopper
{
    /// <summary>
    ///     The SoftPwmManager is used to configure soft-PWM pins on the board
    /// </summary>
    internal class SoftPwmManager : IDisposable
    {
        private readonly TreehopperUsb board;
        private readonly AsyncLock mutex = new AsyncLock();
        private readonly Dictionary<int, SoftPwmPinConfig> pins;
        private readonly double resolution = 0.25; // 0.25 microseconds / tick

        internal SoftPwmManager(TreehopperUsb board)
        {
            this.board = board;
            pins = new Dictionary<int, SoftPwmPinConfig>();
        }

        public void Dispose()
        {
            Stop();
        }

        ~SoftPwmManager()
        {
            Stop();
        }

        public override string ToString()
        {
            if (pins.Count > 1)
                return $"{pins.Count} SoftPwm pins running";
            if (pins.Count == 1)
                return "1 SoftPwm pin running";
            return "No SoftPwm pins running";
        }

        internal void Stop()
        {
            foreach (var entry in pins)
                entry.Value.Pin.Mode = PinMode.DigitalInput;

            pins.Clear();
            UpdateConfig();
        }

        internal void StartPin(Pin pin)
        {
            if (pins.ContainsKey(pin.PinNumber))
                return;
            pins.Add(pin.PinNumber, new SoftPwmPinConfig {Pin = pin, PulseWidthUs = 0, UsePulseWidth = true});
            UpdateConfig();
        }

        internal void StopPin(Pin pin)
        {
            pins.Remove(pin.PinNumber);
            UpdateConfig();
        }

        internal async void SetDutyCycle(Pin pin, double dutyCycle)
        {
            using (await mutex.LockAsync().ConfigureAwait(false))
            {
                pins[pin.PinNumber].DutyCycle = dutyCycle;
                pins[pin.PinNumber].UsePulseWidth = false;
                UpdateConfig();
            }
        }

        internal async void SetPulseWidth(Pin pin, double pulseWidth)
        {
            using (await mutex.LockAsync().ConfigureAwait(false))
            {
                pins[pin.PinNumber].PulseWidthUs = pulseWidth;
                pins[pin.PinNumber].UsePulseWidth = true;
                UpdateConfig();
            }
        }

        internal double GetDutyCycle(Pin pin)
        {
            if (!pins.ContainsKey(pin.PinNumber)) return 0;
            return pins[pin.PinNumber].DutyCycle;
        }

        internal double GetPulseWidth(Pin pin)
        {
            if (!pins.ContainsKey(pin.PinNumber)) return 0;
            return pins[pin.PinNumber].PulseWidthUs;
        }

        private void UpdateConfig()
        {
            if (pins.Count > 0)
            {
                foreach (var entry in pins)
                    // for pins that use pulse width, calculate value based on resolution
                    if (entry.Value.UsePulseWidth)
                    {
                        entry.Value.Ticks = (ushort) (entry.Value.PulseWidthUs / resolution);

                        // just in case the user wants to retrieve duty cycle, update its value, too
                        entry.Value.DutyCycle = entry.Value.Ticks / 65535;
                    }
                    else
                    {
                        // for pins that use duty-cycle, calculate based on period count
                        entry.Value.Ticks = (ushort) Math.Round(entry.Value.DutyCycle * 65535);

                        // just in case the user wants to retrieve pulse width, update its value too
                        entry.Value.PulseWidthUs = (int) (entry.Value.Ticks * resolution);
                    }

                // now the fun part; let's figure out the delta delays between each pin
                var orderedValues = pins.Values.OrderBy(pin => pin.Ticks);

                var list = orderedValues.ToList();

                var count = list.Count() + 1;
                var config = new byte[2 + 3 * count]; // { , (byte)pins.Count, timerVal };
                config[0] = (byte) DeviceCommands.SoftPwmConfig;
                config[1] = (byte) count;
                if (count > 1)
                {
                    var i = 2;
                    var time = 0;

                    for (var j = 0; j < count; j++)
                    {
                        var ticks = 0;

                        if (j < list.Count())
                            ticks = list[j].Ticks - time;
                        else
                            ticks = ushort.MaxValue - time;

                        var tmrVal = ushort.MaxValue - ticks;
                        if (j == 0)
                            config[i++] = 0;
                        else
                            config[i++] = (byte) list[j - 1].Pin.PinNumber;

                        config[i++] = (byte) (tmrVal >> 8);
                        config[i++] = (byte) (tmrVal & 0xff);
                        time += ticks;
                    }
                }
                else
                {
                    config[1] = 0;
                }

                board.SendPeripheralConfigPacket(config);
            }
            else
            {
                // disable SoftPWM
                board.SendPeripheralConfigPacket(new byte[] {(byte) DeviceCommands.SoftPwmConfig, 0});
            }
        }
    }
}
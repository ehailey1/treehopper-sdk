﻿using System;

namespace Treehopper.Libraries.Motors
{
    /// <summary>
    ///     Construct a dual half-bridge-style H-bridge driver with an enable pin
    /// </summary>
    public class DualHalfBridge : MotorSpeedController
    {
        private readonly DigitalOut A;
        private readonly DigitalOut B;
        private readonly DigitalOut enable;
        private readonly Pwm enablePwm;
        private bool enabled;

        private double speed;

        /// <summary>
        ///     Construct a dual half bridge with PWM speed control
        /// </summary>
        /// <param name="A">The "A" channel half-bridge input</param>
        /// <param name="B">The "B" channel half-bridge input</param>
        /// <param name="Enable">The PWM input used to control the output enable</param>
        public DualHalfBridge(DigitalOut A, DigitalOut B, Pwm Enable)
        {
            Enable.EnablePwmAsync();
            Enable.DutyCycle = 0;
            Enable.EnablePwmAsync();
            A.MakeDigitalPushPullOutAsync();
            B.MakeDigitalPushPullOutAsync();

            enablePwm = Enable;
            this.A = A;
            this.B = B;
        }

        /// <summary>
        ///     Construct a dual half bridge with no speed control
        /// </summary>
        /// <param name="A">The "A" channel half-bridge input</param>
        /// <param name="B">The "B" channel half-bridge input</param>
        /// <param name="Enable">An optional Enable pin of the H-bridge</param>
        public DualHalfBridge(DigitalOut A, DigitalOut B, DigitalOut Enable = null)
        {
            if (Enable != null)
            {
                Enable.DigitalValue = false;
                Enable.MakeDigitalPushPullOutAsync();
                enable = Enable;
            }

            A.MakeDigitalPushPullOutAsync();
            B.MakeDigitalPushPullOutAsync();


            this.A = A;
            this.B = B;
        }

        /// <summary>
        ///     Whether to brake -- drive both H-bridge outputs to the same value -- on zero speed
        /// </summary>
        public bool BrakeOnZeroSpeed { get; set; }

        /// <summary>
        ///     Enable or disable the H-bridge outputs
        /// </summary>
        public bool Enabled
        {
            get { return enabled; }

            set
            {
                if (enabled == value) return;
                enabled = value;
                if (enabled == false)
                    setEnabled(0);
            }
        }

        /// <summary>
        ///     Get or set the speed of the motor driver
        /// </summary>
        public double Speed
        {
            get { return speed; }

            set
            {
                if (value < -1.0 || value > 1.0)
                    throw new ArgumentOutOfRangeException("Speed must be between -1.0 and 1.0");
                speed = value;

                if (speed > -0.01 && speed < 0.01) // brake
                {
                    if (BrakeOnZeroSpeed)
                    {
                        setEnabled(1.0);
                        A.DigitalValue = false;
                        B.DigitalValue = false;
                    }
                    else
                    {
                        setEnabled(0.0);
                    }
                }
                else if (speed > 0)
                {
                    A.DigitalValue = true;
                    B.DigitalValue = false;
                    setEnabled(Math.Abs(speed));
                }
                else
                {
                    A.DigitalValue = false;
                    B.DigitalValue = true;
                    setEnabled(Math.Abs(speed));
                }
            }
        }

        private void setEnabled(double value)
        {
            if (enablePwm != null)
            {
                enablePwm.DutyCycle = value;
            }
            else if (enable != null)
            {
                if (value > 0.5)
                    enable.DigitalValue = true;
                else
                    enable.DigitalValue = false;
            }
            else if (value < 0.5)
            {
                // no enable pin; just set both inputs to zero to at least stop the motor
                A.DigitalValue = false;
                B.DigitalValue = false;
            }
        }
    }
}
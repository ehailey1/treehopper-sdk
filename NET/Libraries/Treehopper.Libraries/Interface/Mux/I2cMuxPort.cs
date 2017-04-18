﻿namespace Treehopper.Libraries.Interface.Mux
{
    using System.Threading.Tasks;

    /// <summary>
    /// I2C mux port
    /// </summary>
    public class I2cMuxPort : I2c
    {
        private int index;
        private I2cMux i2cMux;

        internal I2cMuxPort(I2cMux i2cMux, int index)
        {
            this.i2cMux = i2cMux;
            this.index = index;
        }

        /// <summary>
        /// Whether to enable this mux port. This property has no effect.
        /// </summary>
        public bool Enabled { get; set; }

        /// <summary>
        /// The speed to use.
        /// </summary>
        public double Speed { get; set; }

        /// <summary>
        /// Automatically mux this port and send/receive data to the upstream port
        /// </summary>
        /// <param name="address">The slave address</param>
        /// <param name="dataToWrite">The data to write</param>
        /// <param name="numBytesToRead">Number of bytes to read</param>
        /// <returns></returns>
        public Task<byte[]> SendReceive(byte address, byte[] dataToWrite, byte numBytesToRead)
        {
            i2cMux.SetMux(index);
            i2cMux.UpstreamPort.Speed = Speed;
            return i2cMux.UpstreamPort.SendReceive(address, dataToWrite, numBytesToRead);
        }
    }
}

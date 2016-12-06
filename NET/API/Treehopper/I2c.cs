﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Treehopper
{
    public interface I2c
    {
        double Speed { get; set; }
        bool Enabled { get; set; }
        Task<byte[]> SendReceive(byte address, byte[] dataToWrite, byte numBytesToRead);
    }
}

﻿using System;
using System.Collections;
using System.Collections.Generic;
using System.Dynamic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;
using Treehopper.Libraries.Interface;

namespace Treehopper.Libraries
{
    public class RegisterManager : IEnumerable<Register>
    {
        public SMBusDevice Dev { get; set; }

        public Dictionary<string, Register> Registers { get; } = new Dictionary<string, Register>();

        public RegisterManager(SMBusDevice dev)
        {
            Dev = dev;
        }

        public RegisterManager()
        {
        }

        private void Register_RegisterUpdated(Register register)
        {
            if(AutoFlush)
                Dev.WriteBufferData((byte)register.Address, register.Bytes);
        }

        public void Add(Register register)
        {
            Registers.Add(register.Name, register);
            register.RegisterUpdated += Register_RegisterUpdated;
        }

        public void Add(string regName, int address, RegisterAccess access, params RegisterValue[] registerValues)
        {
            Add(new Register(regName, address, access, registerValues));
        }

        public Register this[string register] => Registers[register];

        public int this[string registerName, string registerValue]
        {
            get { return Registers[registerName][registerValue]; }
            set { Registers[registerName][registerValue] = value; }
        }

        public Task WriteRange(string start, string end)
        {
            // get a list of all the registers, in order of address
            var startingAddress = Registers[start].Address;
            var endingAddress = Registers[end].Address;

            var registerList = Registers.Values.Where(reg => reg.Address >= startingAddress && reg.Address <= endingAddress)
                .OrderBy(i => i.Address)
                .ToArray();

            var bytes = registerList.SelectMany(i => i.Bytes).ToArray();

            return Dev.WriteBufferData((byte)startingAddress, bytes);
        }

        public async Task ReadRange(string start, string end)
        {
            var startingAddress = Registers[start].Address;
            var endingAddress = Registers[end].Address;

            var numBytes = endingAddress - startingAddress + Registers[end].TotalBytes;

            var bytes = await Dev.ReadBufferData((byte) startingAddress, numBytes);

            var registers = Registers.Values
                .Where(reg => reg.Address >= startingAddress && reg.Address <= endingAddress)
                .OrderBy(i => i.Address);

            var count = 0;

            foreach(var register in registers)
            {
                register.Bytes = bytes.Skip(count).Take(register.TotalBytes).ToArray();
                count += register.TotalBytes;
            }
        }

        public IEnumerator<Register> GetEnumerator()
        {
            return Registers.Values.GetEnumerator();
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }

        public bool AutoFlush { get; set; } = true;

    }
}

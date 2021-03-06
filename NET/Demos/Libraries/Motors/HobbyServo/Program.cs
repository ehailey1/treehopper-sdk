﻿using System;
using System.Threading.Tasks;
using Treehopper;
using Treehopper.Desktop;
using Treehopper.Libraries.Motors;

namespace Demo
{
    class Program
    {
        static TreehopperUsb board;

        static void Main(string[] args)
        {
            Console.CancelKeyPress += Console_CancelKeyPress;
            App().Wait();
        }

        private static void Console_CancelKeyPress(object sender, ConsoleCancelEventArgs e)
        {
            if (board != null) board.Dispose();
        }

        static async Task App()
        {
            while(true)
            {
                Console.Write("Waiting for board...");
                board = await ConnectionService.Instance.GetFirstDeviceAsync();
                Console.WriteLine("Board Found! Serial: "+board.SerialNumber+".");
                Console.Write("Connecting...");
                await board.ConnectAsync();
                Console.WriteLine("Connected. Starting application...");

                var servo = new HobbyServo(board.Pins[0], 650, 2600);
                while(board.IsConnected)
                {
                    Console.WriteLine("Clockwise...");
                    for (int i = 0; i < 180; i++)
                    {
                        if (!board.IsConnected)
                            break;

                        servo.Angle = i;
                        await Task.Delay(10);
                    }
                    Console.WriteLine("Counterclockwise...");
                    for (int i = 180; i > 0; i--)
                    {
                        if (!board.IsConnected)
                            break;

                        servo.Angle = i;
                        await Task.Delay(10);
                    }
                }
                
            }
            
        }
    }
}

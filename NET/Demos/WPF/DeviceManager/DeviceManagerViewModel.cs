﻿using GalaSoft.MvvmLight;
using GalaSoft.MvvmLight.Command;
using GalaSoft.MvvmLight.Messaging;
using System;
using System.ComponentModel;
using System.Threading.Tasks;
using System.Windows;
using Treehopper;
using Treehopper.Mvvm.ViewModels;
using Treehopper.Mvvm.Messages;
using Treehopper.Firmware;
using Treehopper.Utilities;

namespace DeviceManager.ViewModels
{
    public class DeviceManagerViewModel : ViewModelBase
    {
        public ISelectorViewModel Selector { get; set; }

        public bool CanEdit => board != null;

        private string name = "";
        public string Name { get { return name; } set { Set(ref name, value); } }

        private string firmwareString = "";
        public string FirmwareString { get { return firmwareString; } set { Set(ref firmwareString, value); } }

        private TreehopperUsb board;
        public TreehopperUsb SelectedBoard
        {
            get { return board; }
            set {
                board = value;
                RaisePropertyChanged("Board"); 
                RaisePropertyChanged("CanEdit");
                UpdateNameCommand.RaiseCanExecuteChanged();
                UpdateSerialCommand.RaiseCanExecuteChanged();
                UpdateFirmwareFromEmbeddedImage.RaiseCanExecuteChanged();

                if (board != null)
                {
                    Name = board.Name;
                    FirmwareString = "Current firmware: " + board.VersionString;
                }
                else
                {
                    Name = "";
                    FirmwareString = "";
                }
            }
        }

        private RelayCommand updateNameCommand;

        /// <summary>
        /// Gets the UpdateNameCommand.
        /// </summary>
        public RelayCommand UpdateNameCommand
        {
            get
            {
                return updateNameCommand
                    ?? (updateNameCommand = new RelayCommand(
                    async () =>
                    {
                        await SelectedBoard.UpdateDeviceNameAsync(Name);
                        await SelectedBoard.UpdateSerialNumberAsync(Utility.RandomString(8));
                        SelectedBoard.Reboot();
                        SelectedBoard.Dispose();
                    },
                    () => CanEdit));
            }
        }

        private RelayCommand updateSerialCommand;

        /// <summary>
        /// Gets the UpdateSerialCommand.
        /// </summary>
        public RelayCommand UpdateSerialCommand
        {
            get
            {
                return updateSerialCommand
                    ?? (updateSerialCommand = new RelayCommand(
                    async () =>
                    {
                        await SelectedBoard.UpdateSerialNumberAsync(Utility.RandomString(8));
                        SelectedBoard.Reboot();
                        SelectedBoard.Dispose();
                    },
                    () => CanEdit));
            }
        }

        private RelayCommand updateFirmwareFromEmbeddedImage;

        private bool isUpdating = false;
        public RelayCommand UpdateFirmwareFromEmbeddedImage
        {
            get
            {
                return updateFirmwareFromEmbeddedImage ?? (updateFirmwareFromEmbeddedImage = new RelayCommand(
                    async () =>
                    {
                        isUpdating = true;
                        UpdateFirmwareFromEmbeddedImage.RaiseCanExecuteChanged();
                        Progress = 1;
                        SelectedBoard.RebootIntoBootloader();
                        Progress = 10;
                        await Task.Delay(1000);
                        Progress = 20;
                        await Task.Delay(1000);
                        Progress = 30;
                        await Task.Delay(1000);
                        Progress = 40;
                        await Task.Delay(1000);
                        Progress = 50;

                        var updater = FirmwareConnectionService.Instance.Boards[0];
                        updater.ProgressChanged += (sender, args) => { Progress = args.ProgressPercentage / 2.0 + 50.0; };

                        await updater.LoadAsync();

                        isUpdating = false;
                        Progress = 0;
                        UpdateFirmwareFromEmbeddedImage.RaiseCanExecuteChanged();
                    },
                    () => SelectedBoard != null && isUpdating == false));
            }
        }


        private double progress = 0;
        public double Progress
        {
            get
            {
                return progress;
            }
            set
            {
                Set(ref progress, value);
                FirmwareString = Math.Round(progress).ToString() + "%";
            }
        }

        public DeviceManagerViewModel()
        {
            if (DesignerProperties.GetIsInDesignMode(new DependencyObject()))
                Selector = new SelectorDesignTimeViewModel(true);
            else
                Selector = new SelectorViewModel();

            Messenger.Default.Register<BoardConnectedMessage>(this, (msg) => { SelectedBoard = msg.Board; });
            Messenger.Default.Register<BoardDisconnectedMessage>(this, (msg) => { SelectedBoard = null; });
        }
    }
}

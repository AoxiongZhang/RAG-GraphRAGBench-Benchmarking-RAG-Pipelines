SD cards and USB drives
=======================

As there are ways of remotely transferring files and starting prints, an SD card or USB flash drive is the most common and reliable way to get your files to your machine. Though common and convenient, flash memory is not the most reliable in itself and your storage can be corrupted or fill up without any obvious signs. Therefore, we have put together a small guide on how to maintain, format, and purchase memory for your Original Prusa printer.

## Make sure your SD card is not locked!

The SD card has a latch on the side. Before using your SD card, make sure that the latch is not set to the Locked position. In case it is locked, you will not be able to save files on the card, and the printer will not be able to open the SD card.

## Storage over 32 GB

There is no upper size limit on compatible storage media, but **the built-in Windows formatting tool does not support formatting storage media from a size of 32 GB or more to FAT32.** It will only provide the option for exFAT, which is currently not supported by our printers. There are similar limitations under various versions of Apple's OSx, where a third-party application must be used to format it correctly.

To format such a drive you need a third-party application, like Rufus, FAT32 format, or EaseUS Partition Master. **Be careful when using such programs** so you do not **accidentally format the wrong storage media**, like your hard drive. However, 8-16 GB is more than enough for most use cases, as a G-code file rarely exceeds 100 MB.

## How do I format the USB drive/SD card?

If your SD card or USB drive is full or if you can't read the content of the drive, but the drive is recognized by windows, most often all you need to do is to format the drive.

## How to format on Windows

On Windows, this is very simple. Locate your USB drive or SD card in my computer, right-click, and choose format.

A new small window will pop up. Most of the time you can simply leave everything to default, but the most important thing is that the **File System is set to FAT32.** This and the Volume Label (Name of the drive) is the only thing you want to touch here. Click Start and your drive will be formatted in a matter of seconds.

If the USB stick will not work even after this procedure, it is either broken or its "partitioning scheme" is set as GPT, which is incorrect. **It must be set as MBR (Master Boot Record).** For how to change this, please see [Microsoft's official documentation](https://docs.microsoft.com/en-us/windows-server/storage/disk-management/change-a-gpt-disk-into-an-mbr-disk).

## How to format on Mac

On Mac, it is a few more steps, but still very accessible. Again, you want to choose **FAT32 as your file system**, but you also have the option of changing the "partitioning scheme", which **should always be MBR (Master Boot Record).**

1. Plug the USB drive or SD card into your Mac.
2. Go to _Applications -> Utilities_ and launch _Disk Utility._
3. Click on the icon in the top-left (green arrow) and select "Show All Devices" from the drop-down menu.
4. Right-click on the USB drive/SD card in the sidebar under "External". _Select the top entry for your drive, not a partition located below._
5. Select Erase in the Disk Utility-toolbar (purple arrow).
6. Enter a name for the formatted disk.
7. Click on the Format menu and choose MS-DOS (FAT).
8. Make sure the Scheme is set to "Master Boot Record".
9. Click Erase.
10. Your USB drive will now be erased and re-formatted correctly.

If your SD card is not detected by the printer at all, be sure to check out [SD card not working](http://help.prusa3d.com/article/sd-card-not-working_2095) for further information.

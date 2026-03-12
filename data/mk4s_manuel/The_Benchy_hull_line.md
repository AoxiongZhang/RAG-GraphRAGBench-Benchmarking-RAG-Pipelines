# The Benchy hull line

When printing the famous #3DBenchy test model, you may notice a horizontal line at the hull’s widest part. This is not a print defect but rather a feature of the model itself. The line represents the waterline of the boat.

It is intentionally modeled into the 3D file. Therefore, you do not need to troubleshoot your printer or slicer settings if you observe this line.

## Layer shifting

Layer shifting occurs when one layer is printed offset relative to the previous one. This results in the whole upper part of the print being shifted. It can happen in one or both axes.

### Common causes

- Loose or misaligned belts
- Obstructions on the print bed
- Stepper motor driver overheating
- Printer frame or axis components not tightened properly

### Fixes

- Check and tighten belts
- Remove any obstructions
- Improve cooling for the stepper drivers
- Verify mechanical assembly and re-tighten screws if necessary

## SD cards and USB drives

Sometimes print issues originate from corrupted or incompatible SD cards / USB drives.

### Tips

- Always format cards in FAT32 before using them with your printer.
- Avoid cheap or unbranded cards; use quality brands.
- If you experience random print failures, try another card or drive.
- Safely eject cards from your computer to prevent corruption.

## Extruder blob

An extruder blob, also called a “blob of doom,” is a large accumulation of filament around the nozzle and hotend. It happens when a print detaches from the bed and sticks to the nozzle instead.

### Prevention

- Ensure proper first layer adhesion (clean bed, correct Z-offset).
- Use adhesives like glue stick if needed.
- Check filament path is not obstructed.

### Fix

- Carefully heat the nozzle to soften the blob.
- Remove material with pliers or tweezers.
- Inspect hotend for damage before resuming prints.

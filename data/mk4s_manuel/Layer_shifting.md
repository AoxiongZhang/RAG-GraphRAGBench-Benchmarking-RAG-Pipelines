Layer shifting
==============

**Layer shifting** is a printing issue that causes the layers of the printed object to **shift from their intended positions.** It is usually associated with an abnormal movement of the X-axis and/or the Y-axis, leading the extruder head to be misaligned mid-printing. 

In order to troubleshoot the issue correctly, it is crucial to recognize in which axis the layers shifted. See the three photos below demonstrating three different kinds of layer shifts. Troubleshooting is the same for both axes. 

Layer shifts are most often caused by the wrong tension of the belts or pulleys not being secure.

## Prusa CORE One

### Check your printer’s power mode

Run the printer in **normal mode** rather than in the **stealth mode**. You can change the power mode in _LCD Menu -> Settings_. 

The stealth mode is perfect for small and simple objects. For bigger or more complex prints, the normal mode is recommended.



### Check the XY axes movement and the belt tension

Test movements both from the printer menu (_LCD Menu -> Control -> Move Axis_), and with the printer cold and off, by hand. When testing the movements by hand, test both movements **along the X and Y axes**, and also **along both diagonals**. 

While an inconsistency in X or Y axis movement is most likely related to the belt tension, an inconsistent diagonal movement is related to the motor that controls that diagonal, or the pulley attached to it. 

To check and adjust the belt tension, follow the guidelines from the dedicated [belt adjustment guide](http://help.prusa3d.com/article/adjusting-belt-tension-core-one_845048). When adjusting the belt tension, do not lose alignment of the CoreXY.

### Check your X/Y axis motors and pulleys

If one of the motor pulleys loosens over time, it will misalign and contribute to inconsistent movement. The pulleys are positioned differently on each of the two XY motors. Each motor pulley has **two set screws**, one of which has to be aligned with the **flat part of the motor shaft**.

Looking from the front of the printer: 

* **Left** 
  
  * The teeth for the belt are above the set screws. 

* **Right**
  
  * The teeth for the belt are below the set screws.

## Original Prusa MK-series

### Check your printer’s power mode

Run the printer in **normal mode** rather than in the **stealth mode**. You can change the **power mode** in _LCD Menu -> Settings._ 

The stealth mode is perfect for small and simple objects. For bigger or more complex prints, the normal mode is recommended. Also, note that in stealth mode, the [Crash detection](http://help.prusa3d.com/article/crash-detection_2100) feature is not available.

### Make sure the extruder and the heatbed can move freely

Make sure there are **no obstructions** in the path of the extruder or heatbed and their bearings. For example, there might be a piece of filament stuck around the belt (usually around the Y-axis pulley) from your previous prints.

Another instance of obstruction is when the zip ties, or other parts of the extruder cable bundle, are not optimally positioned as indicated in their respective [assembly guide](http://help.prusa3d.com/attachment/ltlznibfugnpwtwy-jpg_272). If the cables hit the frame before the extruder assembly (MK3 and higher) or before the X end-stop (on MK2/S or MK2.5) the printer detects an inaccurate end position. See the photo below and make sure the cables are arranged accordingly.

Verify if the smooth rods don't bear any deep scratches and if the bearings are properly lubricated. Clean the smooth rods with a clean paper towel before applying lubricant.

The optimal lubricant is our [Prusa Lubricant](https://www.prusa3d.com/product/prusa-lubricant-applicator-set-5g/). A lithium-based, general-purpose **grease** also works well.

### **Check your X/Y axis motors and pulleys**

Make sure the X and Y **motors** are tightened in the motor mount, that the **pulley** is secured on the motor shaft and aligned with the pulley on the opposite end, and that the pulley can move freely. **Both grub screws** need to be tight, **one of them has to be tightened against the flat part of the motor shaft.** A loose or misaligned pulley is usually the main cause of staircase layer shifts.

Both pulleys on both axes also have to be **aligned**, meaning the motor pulley has to be well **centered and the belt has to be moving in a straight line,** not traveling from right to left while the pulley is turning.

### **Check the tension of your belts**

Check your [belt tension](http://help.prusa3d.com/article/adjusting-belt-tension-mk4-s-mk3-9-s-mk3-5-s-mk3-s_112380).

On MK-series printers, a quick way to check it is using our [belt tuner](https://belt.connect.prusa3d.com/), with the instructions in the video below.

On MK3/S/+, it is possible to check the **Belt Status** numbers via _LCD Menu -> Support -> Belt Status_. 

While there is not a precise ideal value, from our experience, the best approximate value is around 250 on the X-axis, and 275 on the Y-axis, with an optimal range at +-15 from these values on either axis. 

The value does not represent a physical quantity, but an arbitrary number inversely proportional to the motor load. The values are with the consideration that the assembly is good and that the parts are in good condition and properly lubricated. Values may not be accurate if there are other problems. 

* If your value is **under** (or close to) 240, you need to **loosen** the belt
* If your value is **over** (or close to) 290, you need to **tighten** the belt
* The values are updated every time you run the Selftest or run the belt test in _LCD menu -> Calibration -> Belt test_. 

Other MK-series models do not have the belt status option. The clue we can give you is that the belt should sound roughly like a low bass string when plucked. It should be possible to pinch the two sides together with your thumb and index finger, but you should feel a little bit of resistance.

! The plastic parts holding the belts can get loose over time.

Use the following technique to test if the pulley is correctly tightened and if the belt is not too loose. Hold the X-axis motor shaft with pliers (take advantage of the flat part of the shaft) and try to move with the extruder. The same procedure can be applied to test the Y-axis pulley and belt. There should be no slack from the belt or any axis movement during the procedure, if there is, then the belt is too loose.

## Original Prusa MINI/+

### **Check your printer’s speed.**

When printing large objects, it’s recommended to decrease the printing speed. During a print, go to _LCD Menu -> Tune -> Speed_ and decrease the number.

### **Check the X/Y belts.**

Make sure that belts are properly tightened. A quick to check this aspect is using our [belt tuner](https://belt.connect.prusa3d.com/), with the instructions in the video below.



Belts should be tight enough to sound like a low bass note when plucked. If the belts are loose, tighten them first: first, loosen the two screws as depicted below. Then, tighten the two screws at the very end of the X-axis. They go directly against the metal rods, so the more tightened they are, the further you move the plastic part. Once you are done, tighten the first two screws again to fix the part in place.



### **Check X/Y axis pulleys.**

Both pulleys on both axes also have to be aligned, meaning the motor pulley has to be well centered and the belt should be perfectly straight. Check whether the X-axis belt is not brushing against printed parts.

Make sure **nothing is blocking the movement of your axis** – Check for any obstructions in the path of the bearings or any possible waste from previous printings stuck around the belt (usually around the Y-axis pulley).

### **Loose X/Y-axis belt pulley**

**If the set-screw on the belt pulley has come loose or it was not secured on the flat side of the motor shaft, it can slip and may cause issues with the axis not moving perfectly in tandem with the motor's rotation.**

The set-screw for the Y-axis is easily accessed, being under the bed, but the X-axis is a bit more tricky. You can access the set-screw for the X-axis through a hole on the top of the extruder (picture below). You will not be able to see if the set screw is aligned with the flat side of the motor-rod and tightening it will only be a temporary fix, but it is a great way of knowing if this is the issue and what needs to be disassembled.

If you only see shiny metal in the hole, you must rotate the motor to reveal the set-screw. Even it is loose, it will move a little with the rotation of the motor, revealing the screw. Access Settings -> Move Axis -> Move X, on the LCD-menu, and rotate the knob to spin the motor.

### Free movement of the axis

Make sure the print head (the part moving along the X-axis) can move freely in the entire range. Especially the cable bundle attached to the extruder should not prevent the print head from reaching the end of the axis.

Also, **verify if the smooth rods are not scratched and if the bearings are properly lubricated**. Clean the smooth rods with a clean paper towel before applying lubricant. 

The optimal lubricant is our [Prusa Lubricant](https://www.prusa3d.com/product/prusa-lubricant-applicator-set-5g/). A lithium-based, general-purpose **grease** also works well.



## Original Prusa XL

### Belt tension

Using the guidelines in the dedicated article, check the [belt tension](http://help.prusa3d.com/article/adjusting-belt-tension-xl_401793). 

Ensure that the belt clamps are in good visible status. To access them, remove the front cover and check the clamps for visual damage.

### XY motor pulleys

Though rare, if one of the motor pulleys loosens over time, it will misalign and contribute to inconsistent movement. The pulleys are positioned differently on each of the two XY motors.

* **Left**
  * Note the orientation of the pulley. The teeth for the belt are **below** the **set screws**.
  * The pulley is **2.5mm higher than the start of the flat part of the motor shaft**. Use the 2.5mm Allen key for reference.
  * Alternatively, **measure the distance between the beginning of the motor shaft and the pulley**, 3.6mm.
* **Right**
  * Note the orientation of the pulley. The teeth for the belt are **above** the **set screws**.
  * The pulley is **flush with the top edge of the motor shaft**.

## **Print geometry and settings**

Objects with **overhangs** are generally harder to print. Some overhangs might even warp upwards during the print, and the nozzle might crash into them. The same can happen in some cases if you choose a **very small infill percentage** when slicing the 3D model.

To prevent printing overhangs, you can cut the object (check out our article on the [Cut tool](http://help.prusa3d.com/article/cut-tool_1779)). You can also try to increase the **print fan speed** or increase the retraction length in PrusaSlicer. Print fan speed is found in _Filament settings -> Cooling_ and retraction length in _Printer Settings -> Extruder 1._

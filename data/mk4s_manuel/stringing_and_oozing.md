# Troubleshooting

## Stringing and oozing

Stringing or oozing, also known as "hairy prints", is the name given for when small strings of filament are left on a printed model. This usually happens when the filament keeps flowing from the nozzle while the extruder is moving to another object. You can see this as a marginal line of filament left between the objects.

This issue is caused by very high printing temperatures and/or using incorrect retraction settings. This can be solved by changing a couple of settings in PrusaSlicer and checking your hardware.

### Stringing from material left on the nozzle

If you print for a long time from a single type of filament, such as PET-G, the filament can create a thin layer in the nozzle. This can cause stringing as the strands of the filament stick to the surface of the print. Therefore, thoroughly clean the nozzle before printing and make sure that any dirt or remnants of previous filaments are removed from the nozzle.

We highly recommend using our official (factory default) preset settings in PrusaSlicer. However, if you are printing with your own settings, make sure that you have the retraction settings configured correctly.

### PrusaSlicer settings

You should start by checking a parameter known as **Retraction**. What does retraction do? When the extruder has finished printing one section/object of your g-code, the filament is pulled back into the nozzle. Once the extruder moves to the next location the printing process continues – the filament is pushed back out and it starts extruding from the nozzle again. Retraction settings can be found in **Printer Settings → Extruder 1**.

Flexible filaments usually need longer retractions, because the material stretches while being pulled back to the nozzle. Flexible materials are a special case and can need a lot of tweaking and tuning.

#### Retraction settings

- **Retraction length**: Amount that the filament is pulled back when a retraction is triggered. On the MK2.5/S and MK3/S/+, the retraction length should be a maximum of 2 mm.
- Due to the Bowden extruder, the retraction length of the Original Prusa **MINI/MINI+** presets are much longer (default **3.2 mm**).
- **Lift Z**: Lifts the extruder during movement. Having this setting lower will improve stringing. Note that disabling this feature may cause the nozzle to hit the printed part.
- **Retraction speed**: Extruder motor speed on retraction. A higher value improves stringing, but if it is too high it may skip steps in the motor.
- **Minimum travel after retraction**: Amount of move that will trigger a retraction (mm). The preset number in PrusaSlicer is **1 mm**, which is a low amount. Having this number higher will get lower printing times, but increase oozing and stringing.
- **Retract on layer change**: Activates retraction when the layer changes to the next one. It is recommended to leave this option on.
- **Wipe while retracting**: Moves the nozzle (wipe) while the retraction is happening. It is recommended to leave this option on.
- **Retract amount before wiping**: This option does a quick retract before doing the wiping movement. More suitable for the Original Prusa **MINI/MINI+**.

#### Other settings that affect retraction

- **Only retract when crossing perimeters** *(Print settings → Infill → Advanced)*: Disables retraction when the travel path does not exceed the upper layer's perimeter. Any oozing that happens will be within the walls and should be invisible.
- **Avoid crossing perimeters** *(Print settings → Layers and perimeters → Quality)*: Optimize travel moves in order to minimize the crossing of perimeters. This will lower the stringing amount, especially in the MINI/MINI+.
- **Sequential printing** *(Print settings → Output options → Sequential printing)*: Printing each object individually has a smaller chance of causing stringing between the parts. When using this feature, PrusaSlicer will warn you of any possibility of the extruder colliding with an already printed part, but follow the print closely.
- **Nozzle temperature** *(Filament settings → Filament → Nozzle)*: Lowering the temperature decreases the occurrence of strings. Try decreasing the nozzle temperature by **5–10 °C** and check whether there’s less stringing.

### Filament

Try using a different spool than the one that is causing the stringing. The filament might have gathered moisture, which will cause a lot of stringing.

### Hotend

Stringing in the nozzle might be caused by a heat dissipation issue in the nozzle. Try re‑applying thermal paste on the threads between the heatbreak and the heatsink.

If you have recently changed any component in the hotend, it is also possible that some individual parts are not in place. Go over the assembly of the hotend and check for any parts that may be different from the instructions.

### Enough settings, pass me my heat‑gun!

If you don’t feel like tweaking any of the settings, well, then there is an alternative. You can get rid of the strings with a heat gun (or often with a lighter – but be very careful). Set your heat‑gun to around **200 °C** and aim at the strings for one or two seconds. This will melt the strings, and the printed object should remain undamaged. Do not leave the heat source on the printed model for longer than one or two seconds, as this may deform the part.

## The Benchy hull line

The 3DBenchy is a 3D model designed by CreativeTools specifically for testing and benchmarking 3D printers. And everyone wants to know, how to print a perfect Benchy. Ever since it’s release, one specific problem seems to be present, in varying degrees of severity, in all of its prints - **the infamous Benchy hull line**.

It’s visible on prints from all FFF **printers** on the market, cheap or expensive. It’s visible no matter the **slicing software**. It’s visible when printing from any **material**. It’s visible even in the Benchy release video from 2015. Again, in **varying degrees of severity** - with some combinations of printer, slicer, and material, it can be almost invisible. Other times, it’s clearly defined, leaving the user disappointed and confused. But once you see it, you’ll be able to find it on essentially all of its prints.

The good news is that **we managed to mostly eliminate the Benchy hull line in our sample G-codes** (not in 100% cases though, more on that later). You can download the G-code here.

The bad news is that **the fix isn’t universal**. And we’re not even sure if such universal fix is physically possible to exist.

### A hardware problem?

When you search for the problem online, you’ll often get an (incorrect) suggestion, that it might be a hardware problem. To give you an example, here are some of the suggestions we found online:

- loose belts
- bent Z-axis rods
- irregularity in your z-axis lead screw at that height

If the problem is one thicker line or two thin lines at height of the Benchy’s deck, it’s most likely not a hardware problem with your printer. On the other hand, if you get uneven layers from top to bottom, it is most likely a hardware problem (which we’ll not discuss here).

### The culprit

We believe that the main culprit is the sudden **transition from sparse infill into full top layers** around the 8 mm height (may vary a bit depending on your layer height and number of top layers).

At this point, there is an abrupt difference in the time a layer takes to print.  
And a few layers later, another sudden change happens. When the deck is finished it’s no longer an almost solid layer, but just a few perimeters again.

Here are the factors that influence the severity of the Benchy hull line:

- Filament material thermal expansion coefficient  
- Print cooling  
- Print environment  
- Other filament properties — dryness, composition

A seemingly similar, yet partly different problem is when printing boxes. They also tend to have a line at the height where the bottom solid layers transition into walls. This has more to do with thin walls, extrusion width, and the material has nowhere to go, but outside. Our slicer team knows about this problem and it's something that will likely improve in the future.

### Why can’t the slicer automatically detect and correct for this?

It’s physics. Plastics, if extruded first from pellets into a filament, and then from filament into a very thin rectangular extrusion, will behave neither as a liquid nor as a solid. The stretching of the plastic will align the long molecular chains of the polymer, introducing internal stresses to the extrusion. This internal stress will pull the extrusion together if not cooled quickly enough. For example, on the MK2 the 3D Benchy has the line more pronounced on the side away from the cooling fan.

It depends on the environment too. Indeed, as many of you found out, in a cool basement the effects are more pronounced. The same G-code printed on the same printer with the same filament can have a Benchy hull line in one room and not in the other. It’s very difficult to automatically compensate for that.

And to compensate for the internal stresses and cooling effects of the filament. One of the reasons being the viscoelastic behavior of the molten plastics, and the dependence of the plastic behavior on its composition, temperature, hydrolysis of the polymer molecular chains. If the filament is not 100% dry (polyesters — PLA & PET are sensitive to hydrolysis, hydrolyzed filament contains shorter polymer chains, thus being less viscous), the effectivity of the cooling, reflections of the cooling air from the already printed objects, etc.

### How did we modify the G-code to eliminate it?

Something that helps, is to make a modifier mesh in the shape of the deck. When aligned at the problematic spot, it can be used to split the hull and the deck. They are then printed separately, plus the infill doesn’t fill the entire area all the way to the hull perimeters.

Then there’s the order of elements inside a layer. For some reason, we got better results when always printing the deck perimeters first, then infill of the deck and then the rest of the layer. We manually edited this order using a text editor.

We’re not sure if it ended up helping, but we also manually edited the G-code in order to slightly lower the flow of solid infill, except for the very top layer (of the deck).

Another thing is to print the perimeters as continuously as possible. Rather than printing perimeters, then infill and then transitioning to the next layer it’s better to print two (or more) layers of perimeters one right after another. The printer then can go back and print the infill, again two layers at a time.

We most likely haven’t discovered all factors and in precisely what ratios they influence the severity of the Benchy hull line. Still, we wanted to share our findings. If you make your own research and tests, let us know of your findings.



## Layer shifting

**Layer shifting** is a printing issue that causes the layers of the printed object to **shift from their intended positions.** It is usually associated with an abnormal movement of the X-axis and/or the Y-axis, leading the extruder head to be misaligned mid-printing. 

In order to troubleshoot the issue correctly, it is crucial to recognize in which axis the layers shifted. See the three photos below demonstrating three different kinds of layer shifts. Troubleshooting is the same for both axes. 

Layer shifts are most often caused by the wrong tension of the belts or pulleys not being secure.

### Prusa CORE One

#### Check your printer’s power mode

Run the printer in **normal mode** rather than in the **stealth mode**. You can change the power mode in _LCD Menu -> Settings_. 

The stealth mode is perfect for small and simple objects. For bigger or more complex prints, the normal mode is recommended.

#### Check the XY axes movement and the belt tension

Test movements both from the printer menu (_LCD Menu -> Control -> Move Axis_), and with the printer cold and off, by hand. When testing the movements by hand, test both movements **along the X and Y axes**, and also **along both diagonals**. 

While an inconsistency in X or Y axis movement is most likely related to the belt tension, an inconsistent diagonal movement is related to the motor that controls that diagonal, or the pulley attached to it. 

To check and adjust the belt tension, follow the guidelines from the dedicated belt adjustment guide When adjusting the belt tension, do not lose alignment of the CoreXY.


#### Check your X/Y axis motors and pulleys

If one of the motor pulleys loosens over time, it will misalign and contribute to inconsistent movement. The pulleys are positioned differently on each of the two XY motors. Each motor pulley has **two set screws**, one of which has to be aligned with the **flat part of the motor shaft**.

Looking from the front of the printer: 

* **Left** 
  
  * The teeth for the belt are above the set screws. 

* **Right**
  
  * The teeth for the belt are below the set screws.

### Original Prusa MK-series

#### Check your printer’s power mode

Run the printer in **normal mode** rather than in the **stealth mode**. You can change the **power mode** in _LCD Menu -> Settings._ 

The stealth mode is perfect for small and simple objects. For bigger or more complex prints, the normal mode is recommended. Also, note that in stealth mode, the Crash detection feature is not available.

#### Make sure the extruder and the heatbed can move freely

Make sure there are **no obstructions** in the path of the extruder or heatbed and their bearings. For example, there might be a piece of filament stuck around the belt (usually around the Y-axis pulley) from your previous prints.

Another instance of obstruction is when the zip ties, or other parts of the extruder cable bundle, are not optimally positioned as indicated in their respective assembly guide. If the cables hit the frame before the extruder assembly (MK3 and higher) or before the X end-stop (on MK2/S or MK2.5) the printer detects an inaccurate end position. See the photo below and make sure the cables are arranged accordingly.

Verify if the smooth rods don't bear any deep scratches and if the bearings are properly lubricated. Clean the smooth rods with a clean paper towel before applying lubricant.

The optimal lubricant is our Prusa Lubricant. A lithium-based, general-purpose **grease** also works well.

#### Check your X/Y axis motors and pulleys

Make sure the X and Y **motors** are tightened in the motor mount, that the **pulley** is secured on the motor shaft and aligned with the pulley on the opposite end, and that the pulley can move freely. **Both grub screws** need to be tight, **one of them has to be tightened against the flat part of the motor shaft.** A loose or misaligned pulley is usually the main cause of staircase layer shifts.

Both pulleys on both axes also have to be **aligned**, meaning the motor pulley has to be well **centered and the belt has to be moving in a straight line,** not traveling from right to left while the pulley is turning.

#### Check the tension of your belts

Check your belt tension.

On MK-series printers, a quick way to check it is using our belt tuner, with the instructions in the video below.

On MK3/S/+, it is possible to check the **Belt Status** numbers via _LCD Menu -> Support -> Belt Status_.

While there is not a precise ideal value, from our experience, the best approximate value is around 250 on the X-axis, and 275 on the Y-axis, with an optimal range at +-15 from these values on either axis. 

The value does not represent a physical quantity, but an arbitrary number inversely proportional to the motor load. The values are with the consideration that the assembly is good and that the parts are in good condition and properly lubricated. Values may not be accurate if there are other problems. 

* If your value is **under** (or close to) 240, you need to **loosen** the belt
* If your value is **over** (or close to) 290, you need to **tighten** the belt
* The values are updated every time you run the Selftest or run the belt test in _LCD menu -> Calibration -> Belt test_. 

Other MK-series models do not have the belt status option. The clue we can give you is that the belt should sound roughly like a low bass string when plucked. It should be possible to pinch the two sides together with your thumb and index finger, but you should feel a little bit of resistance.

Use the following technique to test if the pulley is correctly tightened and if the belt is not too loose. Hold the X-axis motor shaft with pliers (take advantage of the flat part of the shaft) and try to move with the extruder. The same procedure can be applied to test the Y-axis pulley and belt. There should be no slack from the belt or any axis movement during the procedure, if there is, then the belt is too loose.

### Original Prusa MINI/+

#### Check your printer’s speed.

When printing large objects, it’s recommended to decrease the printing speed. During a print, go to _LCD Menu -> Tune -> Speed_ and decrease the number.

#### Check the X/Y belts.

Make sure that belts are properly tightened. A quick to check this aspect is using our belt tuner, with the instructions in the video below.

Belts should be tight enough to sound like a low bass note when plucked. If the belts are loose, tighten them first: first, loosen the two screws as depicted below. Then, tighten the two screws at the very end of the X-axis. They go directly against the metal rods, so the more tightened they are, the further you move the plastic part. Once you are done, tighten the first two screws again to fix the part in place.

#### Check X/Y axis pulleys.

Both pulleys on both axes also have to be aligned, meaning the motor pulley has to be well centered and the belt should be perfectly straight. Check whether the X-axis belt is not brushing against printed parts.

Make sure **nothing is blocking the movement of your axis** – Check for any obstructions in the path of the bearings or any possible waste from previous printings stuck around the belt (usually around the Y-axis pulley).

#### Loose X/Y-axis belt pulley

**If the set-screw on the belt pulley has come loose or it was not secured on the flat side of the motor shaft, it can slip and may cause issues with the axis not moving perfectly in tandem with the motor's rotation.**

The set-screw for the Y-axis is easily accessed, being under the bed, but the X-axis is a bit more tricky. You can access the set-screw for the X-axis through a hole on the top of the extruder (picture below). You will not be able to see if the set screw is aligned with the flat side of the motor-rod and **tightening it will only be a temporary fix**, but it is a great way of knowing if this is the issue and what needs to be disassembled.

If you only see shiny metal in the hole, you must rotate the motor to reveal the set-screw. Even it is loose, it will move a little with the rotation of the motor, revealing the screw. Access _Settings -> Move Axis -> Move X_, on the LCD-menu, and **rotate the knob to spin the motor**.



#### Free movement of the axis

Make sure the print head (the part moving along the X-axis) can move freely in the entire range. Especially the cable bundle attached to the extruder should not prevent the print head from reaching the end of the axis.

Also, **verify if the smooth rods are not scratched and if the bearings are properly lubricated**. Clean the smooth rods with a clean paper towel before applying lubricant. 

The optimal lubricant is our Prusa Lubricant. A lithium-based, general-purpose **grease** also works well.

### Original Prusa XL

#### Belt tension

Using the guidelines in the dedicated article, check the belt tension. 

Ensure that the belt clamps are in good visible status. To access them, remove the front cover and check the clamps for visual damage.

#### XY motor pulleys

Though rare, if one of the motor pulleys loosens over time, it will misalign and contribute to inconsistent movement. The pulleys are positioned differently on each of the two XY motors.

* **Left**
  * Note the orientation of the pulley. The teeth for the belt are **below** the **set screws**.
  * The pulley is **2.5mm higher than the start of the flat part of the motor shaft**. Use the 2.5mm Allen key for reference.
  * Alternatively, **measure the distance between the beginning of the motor shaft and the pulley**, 3.6mm.
* **Right**
  * Note the orientation of the pulley. The teeth for the belt are **above** the **set screws**.
  * The pulley is **flush with the top edge of the motor shaft**.

### **Print geometry and settings**

Objects with **overhangs** are generally harder to print. Some overhangs might even warp upwards during the print, and the nozzle might crash into them. The same can happen in some cases if you choose a **very small infill percentage** when slicing the 3D model.

To prevent printing overhangs, you can cut the object (check out our article on the [Cut tool](http://help.prusa3d.com/article/cut-tool_1779)). You can also try to increase the **print fan speed** or increase the retraction length in PrusaSlicer. Print fan speed is found in _Filament settings -> Cooling_ and retraction length in _Printer Settings -> Extruder 1._

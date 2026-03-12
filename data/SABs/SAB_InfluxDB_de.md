|Col1|Col2|Col3|Standard Arbeitsblatt Arbeitsanweisung|Col5|Blatt 1 von 6|Col7|
|---|---|---|---|---|---|---|
|Arbeitsaufgabe: InfluxDB|||Produkt: GUI||Arbeitsplatz: Smartboard||
|Nr.|Bedienung|Abbildung||Anmerkung||Zeit|
|1|Website aufrufen||||||
||URL in Suchleiste eingeben|||URL: 10.10.151.21:8086|||
||||||||
||Benutzerdaten eingeben und auf „Sign In“ drücken|||Username: cip_hiwi Password: PTW123ptw|||
|2|Condition Monitoring Board||||||
||Boardübersicht öffnen|||Links in der Leiste „Dashboards“ auswählen|||
||||||||
||Bandsägen Dashboard öffnen|||„Bandsaw Condition Monito…“ auswählen|||
||||||||
||Aktualisierungsrate erhöhen|||Rechts oben „Set Auto Refresh“ öffnen|||

|Version: 1.1|Datum: 26.07.23|Erstellt: T. Goodman|Freigegeben: XXX|Knackpunkt|Qualität|
|---|---|---|---|---|---|


-----

|Col1|Col2|Col3|Standard Arbeitsblatt Arbeitsanweisung|Col5|Blatt 2 von 6|Col7|
|---|---|---|---|---|---|---|
|Arbeitsaufgabe: Condition Monitoring|||Produkt: GUI||Arbeitsplatz: Säge||
|Nr.|Bedienung|Abbildung||Anmerkung||Zeit|
||||||||
||Aktualisierungs – Intervall ändern|||„Refresh Intervall“ von „60s“ auf „1s“ ändern (muss manuell eingetragen werden) und auf „Confirm“ bestätigen|||
||||||||
||Jetzt erscheint jede Sekunde ein kreisförmiges Symbol auf jeder Zelle||||||
||Erweiterte Funktionen||||||
|3|Zelle hinzufügen||||||
||Im Bandsaw Dashboard (Schritt 2) eine neue Zelle hinzufügen|||Links oben auf „Add Cell“ drücken. Im neuen Fenster kann die Zelle oben links umbenannt werden – dieser kann im Nachhinein noch verändert werden.|||
||Den richtigen „Bucket“ und „Filter“ wählen|||„cip_data“ als Bucket wählen „sps_saw_conmon_opcua“ als Filter wählen (zu finden unter dem Reiter „measurement“)|||
||Sinnvollen Parameter („Filter“) wählen und rechts „Submit“ wählen|||„Sinnvolle“ Parameter für eine Demonstration sind zB. „CPU_Kuehler_Temp“, „CPU_Temp“, „Position“, alle „TData.T“, alle „Vib“-Werte, i „vVorschub“. Darunter sind anzeigbare Werte zu finden, welche sich gut zu Demo-Zwecken eignen|||

|Version: 1.1|Datum: 26.07.23|Erstellt: T. Goodman|Freigegeben: XXX|Knackpunkt|Qualität|
|---|---|---|---|---|---|


-----

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||Standard Arbeitsblatt Arbeitsanweisung||Blatt 3 von 6||
|Arbeitsaufgabe: InfluxDB|||Produkt: GUI||Arbeitsplatz: Smartboard||
|Nr.|Bedienung|Abbildung||Anmerkung||Zeit|
|3.1|Darstellungsform||||||
||Darstellungsform ggf. ändern|||Links oben auf „Graph“ gehen und geeignete Darstellungsform (Balkendiagramme, Kuchendiagramme, Heatmaps etc.)|||
||Mehr Parameter der Darstellung ändern|||Neben „Graph“ auf „Customize“ gehen und zB. Farbcode, Achsenbeschriftung, Transparenz ändern. Zum Bestätigen einfach auf den grauen Hintergrund über dem Graph drücken|||
|3.2|Angezeigte Werte ändern||||||
||Auswählen welche Art von Messwert angezeigt / ausgewertet wird|||Rechts unten im Reiter „Window Period“ unter „Aggregate Function“ auf „Custom“ gehen und wählen. Sinnvoll zum Zeigen sind z.B. „mean“, „median“, „last“, „derivate“. Da es sich hier um entweder gemittelte, diskrete oder abgeleitete Werte handelt. Alles findet seine Anwendung im Wertstromprozess. Bestätigt wird über den „Submit“ Button (siehe Schritt 3.1)|||
|3.3|Zelle bestätigen||||||
||Die Zelle dem Dashboard hinzufügen|||Um die Zelle dem Dashboard hinzuzufügen, rechts oben auf den grünen Haken drücken|||

|Version: 1.1|Datum: 26.07.23|Erstellt: T. Goodman|Freigegeben: XXX|Knackpunkt|Qualität|
|---|---|---|---|---|---|


-----

|Col1|Col2|Col3|Standard Arbeitsblatt Arbeitsanweisung|Col5|Blatt 4 von 6|Col7|
|---|---|---|---|---|---|---|
|Arbeitsaufgabe: InfluxDB|||Produkt: GUI||Arbeitsplatz: Smartboard||
|Nr.|Bedienung|Abbildung||Anmerkung||Zeit|
|3.4|Bearbeiten im Dashboard||||||
||Bearbeiten einzelner Zellen|||Um jede Zelle nochmal genau zu bearbeiten drückt man auf das kleine Zahnrad, welches sich bei jeder Zelle rechts oben in der Ecke befindet. Danach „Configure“ auswählen|||
||Größe der Zelle im Dashboard bearbeiten|||Um individuelles Größen- bzw. Seitenverhältnis anzupassen rechte untere Ecke in den Zellen mit linker Maustaste per „Drag & Drop“ anpassen|||
||Löschen einzelner Zellen|||Erst Zahnrad auswählen, danach „Delete“ und dann „Confirm Delete“ auswählen|||
|3.5|Angezeigten Zeitbereich anpassen||||||
||Zeitbereich aller angezeigten Zellen anpassen.|||Rechts oben den gewünschten Zeitbereich auswählen. Achtung, man kann im Editor beim Hinzufügen bzw. bearbeiten der Zellen auch Zellen einzelne Zeitbereiche anzeigen lassen.|||
||||||||

|Version: 1.1|Datum: 26.07.23|Erstellt: T. Goodman|Freigegeben: XXX|Knackpunkt|Qualität|
|---|---|---|---|---|---|


-----

|Col1|Col2|Col3|Standard Arbeitsblatt Arbeitsanweisung|Col5|Blatt 5 von 6|Col7|
|---|---|---|---|---|---|---|
|Arbeitsaufgabe: InfluxDB|||Produkt: GUI||Arbeitsplatz: Smartboard||
|Nr.|Bedienung|Abbildung||Anmerkung||Zeit|
|4|Alert zu Demonstrationszwecken einstellen||||||
||ACHTUNG|||Folgender Schritt MUSS rückgängig gemacht werden nach Demo|||
|4.1|Alert hinzufügen||||||
||„Alerts“ wählen|||Links in der Taskleiste „Alerts“ wählen|||
||Sägen Temperatur auswählen|||Auf der linken Seite den Reiter „Saw Motor Temperature“ auswählen|||
||Kritische Temperatur ändern|||Über den Reiter „Thresholds“ rechts unten wird der Wert „40“ [C°] zu einem niedrigen Wert (z.B. 10) geändert werden Wichtig ist, dass der eingestellte Wert unter dem tatsächlichen Wert liegt um vorzuführen was passiert, wenn die Säge eine kritische Temperatur erreicht. Dieser kann aus dem Graph darüber abgelesen werden.|||
||Kritische Parameter bestätigen|||Rechts oben auf den grünen Haken drücken|||
||||||||

|Version: 1.1|Datum: 26.07.23|Erstellt: T. Goodman|Freigegeben: XXX|Knackpunkt|Qualität|
|---|---|---|---|---|---|


-----

|Col1|Col2|Col3|Standard Arbeitsblatt Arbeitsanweisung|Col5|Blatt 6 von 6|Col7|
|---|---|---|---|---|---|---|
|Arbeitsaufgabe: InfluxDB|||Produkt: GUI||Arbeitsplatz: Smartboard||
|Nr.|Bedienung|Abbildung||Anmerkung||Zeit|
|4.2|Warnmeldung auslesen||||||
||„Alerts“ wählen|||Links in der Taskleiste „Alerts“ wählen|||
||Verlauf anzeigen|||Auf dem Reiter „Saw Motor Temperature“ mit der Maus hovern Und am rechten Bildschirm Rand auf das kleine blaue Zahnrad drücken und „View History“ wählen|||
||Warnung kann ausgelesen werden||||||
||||||||
||ACHTUNG|||Dieser Schritt MUSS rückgängig gemacht werden nach Demo. Dazu einfach im Schritt 4.1 den Wert zurück auf „40“ [C°] ändern und bestätigen|||
|5|Mögliche Datenquellen anzeigen||||||
||„Data“ wählen|||Links in der Taskleiste bei dem links dargestellten Symbol „Sources“ wählen|||
||„Sources“ Reiter|||Im Reiter „Sources“ können alle Telegraf Plugins eingesehen werden, welche als mögliche Datenquellen für InfluxDB dienen. Runterscrollen!|||

|Version: 1.1|Datum: 26.07.23|Erstellt: T. Goodman|Freigegeben: XXX|Knackpunkt|Qualität|
|---|---|---|---|---|---|


-----


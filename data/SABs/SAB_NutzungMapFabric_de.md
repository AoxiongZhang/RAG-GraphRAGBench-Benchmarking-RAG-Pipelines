|Col1|Col2|Col3|Standard Arbeitsblatt Arbeitsanweisung|Col5|Blatt X von X|Col7|
|---|---|---|---|---|---|---|
|Arbeitsaufgabe: Erstellung der Karte für das AMR|||Produkt: AMR Sherpa B||Arbeitsplatz: Flowfactory||
|Nr.|Bedienung|Abbildung||Anmerkung||Zeit|
|1|Map erstellen||||||
|1.1||||Hinweis: Die Map kann im Follow- Me Modus, im „Wheels-unlocked“ Modus oder auch durch Steuerung per Controller aufgenommen werden.|||
|1.2||||Tipps für die Erstellung einer präzisen Map (aus Integrator documentation): -Jeden Gang einmal von jeder Richtung abfahren -Positionen mehrmals anfahren -Den Roboter langsam bewegen, besonders dort, wo es später präzise navigieren muss -Wenn ein Docking-System genutzt werden soll, sollten die Pfeiler von jeder Seite abgefahren werden -Wenn ein Objekt, welches nicht dauerhaft in dieser Positon bleibt, zwischen der Wand und dem Roboter steht, sollte der Roboter auch die Strecke zwischen dem Objekt und der Wand abfahren|||



-----

|Col1|Col2|Col3|-Die Aufnahme des Roboters wird nicht durch einen Emergency stop oder den Wechseln eines Fahrmodus beendet. Es ist möglich während der Aufnahme z.B. vom Follow-Me Mode in andere Modi zu wechseln. Wichtig: Die Aufnahme muss in unter 10 Minuten erfolgen, da ansonsten die ältesten Aufnahmen überschrieben werden|Col5|
|---|---|---|---|---|
||Speichern der Aufnahme||Die Aufnahme der letzten 10 Minuten muss nach beenden der Aufnahmephase auf dem AMR gesichert werden. Hierzu auf den Parameter Button klicken und dann auf Save log Während des Speicherns erscheint eine Sanduhr auf dem Display||
|2|Map von AMR auf USB Stick übertragen||||
|2.1|USB Stick in Roboter einstecken||Schwarze Gummi-Abdeckung über dem Power Button nach oben klappen und USB Stick in darunter liegenden Anschluss stecken. Hinweis: Der verwendete USB Stick benötigt die Links dargestellte Ordnerstruktur (?)||



-----

|Col1|Col2|Col3|Standard Arbeitsblatt Arbeitsanweisung|Col5|Blatt X von X|Col7|
|---|---|---|---|---|---|---|
|Nr.|Bedienung|Abbildung||Anmerkung||Zeit|
|2|Map von AMR auf Stick übertragen||||||
|2.2|Als Admin auf AMR anmelden|||Paramter Button anklicken Dann Admin Button anklicken und Paswort eingeben Das Passwort lautet:|||
|2.3|Log exportieren|||Export LOG Button anklicken um den log-file vom AMR auf den USB-Stick zu speichern Dann USB Stick entnehmen Hinweis: Auf dem USB Stick ist die log Datei im Ordner /SMR/logs als log.odo gespeichert Wichtig: bevor der USB Stick entfernt werden kann muss der „Export LOG“ button wieder von grau auf blau wechseln, da der Vorgang ansonsten nicht abgeschlossen ist|||



-----

|Col1|Col2|Col3|Standard Arbeitsblatt Arbeitsanweisung|Col5|Blatt X von X|Col7|
|---|---|---|---|---|---|---|
|Nr.|Bedienung|Abbildung||Anmerkung||Zeit|
|3|Karte in MapFabric erstellen||||||
|3.1|Öffnen einer Datei in MapFabric|||Öffnen des Programms MapFabric.exe Um ein neues Projekt zu erstellen auf “NEW mapFabric project klicken” Um ein vorhandenes Projekt (Karte) zu bearbeiten auf „Open mapFabric project“ klicken|||
|3.2|.log Datei in MapFabric importieren|||USB-Stick mit Datei des AMR in den PC stecken auf dem MapFabric genutzt werden soll In Map Fabric auf “Files“ klicken Anschließend auf das + klicken um Datei zu importieren Wichtig: Die Stettings müssen so eingestellt sein, wie es im Bild zu sehen ist Nachdem die Datei importiert ist, kann das Fenster geschlossen werden|||
||||||||



-----

|Col1|Col2|Col3|Standard Arbeitsblatt Arbeitsanweisung|Col5|Blatt X von X|Col7|
|---|---|---|---|---|---|---|
|Nr.|Bedienung|Abbildung||Anmerkung||Zeit|
|4|Karte in Map Fabric bearbeiten||||||
|4.1|Karte in Map Fabric erstellen|||Um die Karte in Map Fabric zu erstellen, müssen wir die Aufnahmefahrt des AMR im Programm noch einmal im „Replay“ abspielen Hierzu eine neue Project Action „Replay erstellen“ und als file die importierte Datei auswählen. Anschließend öffnen sich die Einstellungen links im Bild mit folgenden Einstellmöglichkeiten: Z: Die Koordinaten in denen der Roboter zum Start der Aufnahme steht. Hiermit kann die Karte verschoben werden Cap: Rotation des Roboters im Startpunkt um die eigene Achse. Hiermit kann die Karte gedreht werden File: ausgewählte Datei (wurde bereits zuvor ausgewählt) From: Legt fest, ab welchem Zeitpunkt (Frame) der Aufnahme die Karte erstellt werden soll. Hiermit können Objekte im Beginn der Aufnahme abgeschnitten werden To: Legt fest, bis zu welchem Zeitpunkt (Frame) der Aufnahme, die Karte erstellt werden soll|||
|4.2|Entfernen von Bewegten Punkten und Objekten in der Karte|||Damit unsere Karte später nur die Dauerhaft platzierten Objekte (Maschinen, Wände etc.) enthält müssen alle anderen in der Aufnahme vom Roboter erkannten Objekte entfernt werden. Hierfür Action „ErasePoly“ auswählen|||



-----

|Col1|Col2|Col3|Dann mit rechtsklick ein Quadrat um die gesamte Karte ziehen und „trig“ auf 70.00 setzen. Dann mit Test die Bereinigung starten und alle nicht konstanten Punkte entfernen. Hinweis: Desto öfter das AMR das selber Objekt an der selben stelle erkannt hat, desto deutlicher ist es in der Karte sichtbar. Sherpa fragen wie man gezeichnete Polygone wieder löschen kann.|Col5|
|---|---|---|---|---|
|4.3|Andere Objekte entfernen||Andere Objekte, die zwar während der gesamten Aufnahme nicht bewegt wurden, an sich aber beweglich sind sollten auch entfernt werden z.B. Hubwagen oder Rolltische) Diese können spätere keine genaue Orientierung für das AMR darstellen Hierzu eine weitere Aktion erasePoly mit trig = 0 anlegen und um alle Punkte und Objekte Rechtecke ziehen, welche nicht dauerhaft an der selben Stelle stehen bleiben sollen. Dann mit „test“ die Aktion durchführen||
|5|Karte erstellen und an den Roboter senden||||
|5.1|Karte erstellen||Die bearbeitete Karte kann mit „release“ erstellt werden und ist dann für die Übertragung auf den Roboter erstellt.||



-----

|Col1|Col2|Col3|Standard Arbeitsblatt Arbeitsanweisung|Col5|Blatt X von X|Col7|
|---|---|---|---|---|---|---|
|Nr.|Bedienung|Abbildung||Anmerkung||Zeit|
|5|Karte erstellen und an den Roboter senden||||||
|5.2|Karte auf Roboter übertragen|||Im Ordner des erstellten MapFabric files findet sich eine map.geo Datei welche wir mithilfe des Fleet-Managers an die AMR Flotte senden können. Hierzu muss diese Datei unter „MapFabric“ hochgeladen werden ->Anleitung Fleet Manager siehe XY|||
||||||||
||||||||
||||||||



-----


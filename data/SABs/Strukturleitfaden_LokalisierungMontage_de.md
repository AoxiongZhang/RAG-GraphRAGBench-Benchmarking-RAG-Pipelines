**St u tu e t ade**

**Lokalisierung**


**att**




**1.1 Forschungsschwerpunkt**

|Arbeitsaufgabe: Vorführung der Lokalisierungs- technologie|Col2|Produkt: Zylinder|Arbeitsplatz: CiP|
|---|---|---|---|
|Datum: 05.10.2022||Erstellt:|Freigegeben: M.Fall|
|Nr||||
|1|Vortrag - Einleitung|||



Ein Forschungsschwerpunkt der Prozesslernfabrik CiP stellt das Wertstrommanagement dar.
Für die Analyse und Gestaltung ganzheitlicher Wertströme liegt der Fokus dabei auf der
simulationsgestützten Planung von Produktionssystemen und innerbetrieblichen
Materialflüssen nach Prinzipien der Schlanken Produktion . Mit dem Demonstrator
„Lokalisierungstechnologien“ wird ein Indoor-Lokalisierungssystem eingesetzt, um die
Transparenz über den Wertstrom der Zylinderproduktion zu erhöhen.

**1.2 Lokalisierungstechnologien**
Für die kontinuierliche Positionsbestimmung von Objekten eignen sich verschiedene
Technologien. Dabei unterscheidet man Lokalisierungstechnologien nach der Signalart
zwischen Sender und Empfänger. Besonders verbreitet sind WLAN, Bluetooth Low Energy
(BLE), Ultrawideband (UWB) und RFID. Die Auswahl der geeigneten Technologie wird
dabei durch den Anwendungsfall bestimmt, die Eigenschaften des vorliegenden
Produktionsumfelds bestimmen Anforderungen an die Technologie. Relevante Parameter sind
dabei der abzudeckende Bereich, die benötigte Genauigkeit, Produktionsgeschwindigkeit, etc.
(siehe Tabelle 1).

Tabelle 1: Eigenschaften verschiedener Lokalisierungstechnologien










|Ausprägung|WLAN|Ultraschall|UWB|RFID|BLE|
|---|---|---|---|---|---|
|Genauigkeit|<5m|mm-dm|<10cm|m|dm|
|Störanfälligkeit|Frequenzband wird UWB/BLE|Temperaturschwan kungen|Koexistenz möglich|Gering|Gleiches Frequenzba nd wie WLAN|
|Kosten|Gering bis hoch|Gering bis moderat|Moderat bis hoch|Hoch|Gering|
|Reichweite|<35m|<10m|10-20m|20-200m|10-50m|
|Latenz|<17ms|>30ms|<1,8ms|Wenige ms|<3ms|
|Energieeffizienz|Moderat|Moderat bis hoch|Hoch|Sehr hoch|Sehr hoch|


-----

**St u tu e t ade**

**Lokalisierung**


**att 3**




**1.3 Anwendung**

|Arbeitsaufgabe: Vorführung der Lokalisierungs- technologie|Col2|Produkt: Zylinder|Arbeitsplatz: CiP|
|---|---|---|---|
|Datum: 05.10.2022|||Freigegeben: M.Fall|
|Nr||||
|1|Einleitung|||



In der CiP werden Pneumatikzylinder für den Einsatz in der Förder- und Antriebstechnik
gefertigt. Die Produktionskette erstreckt sich dabei vom Sägen des Rohmaterials in
Stangenform über Fräs-, Reinigungs- und finale Montagsprozesse. Dabei arbeitet man in der
CiP für den innerbetrieblichen Transport zwischen den einzelnen Prozessschritten mit
Kleinladungsträgern. In den Kleinladungsträgern wird eine Losgröße von vier Zylindern
transportiert.

Für die kontinuierliche Positionsbestimmung der Kleinladungsträger über die Prozesskette
hinweg sind die einzelnen Prozessschritte in jeweils drei Aufenthaltsbereiche unterteilt:

**Liegezonen** : Produkt lagert hier vor der Bearbeitung
**Bearbeitungszon** e: Prozessschritt läuft, das Produkt wird bearbeitet
**Wartezonen** : Bauteile lagern nach der Bearbeitung und warten auf den Weitertransport

Mit Hilfe der Lokalisierungstechnologie können dabei die Aufenthaltszeiten in den jeweiligen
Zonen, die Gesamtdurchlaufzeiten sowie die genaue Position der Bauteile erfasst werden.
Die dabei anfallenden Daten können einzeln oder in Summe ausgewertet werden. In der CiP
werden dabei Verweildauern in verschiedenen Lagern und Fertigungsstationen erfasst.
Dadurch können neben Stückkosten in Echtzeit auch Kennzahlen wie bspw. der Fließgrad
automatisch berechnet werden.

**1.4 Anforderungen an die Technologie**

Das Hallenlayout der CIP ist durch eine verschachtelte Anordnung von Maschinen geprägt, die
Maschinen stellen dabei Hindernisse für den Sichtkontakt zwischen Sender und Empfänger dar
und schirmen die von den Sendern ausgestrahlten Signale ab. Für die Zuordnung zu den Zonen
müssen Genauigkeiten von ca. 50cm erreicht werden, ansonsten kann die Differenzierung
zwischen den Zonen nicht gewährleistet werden. Aufgrund der Größe der CiP entstehen
maximale Distanzen zwischen Sender und Empfänger von 8m.

**1.5 Technische Lösung in der CIP**

Für die technischen Anforderungen an die CiP arbeiten wir mit der UWB-Technologie von
Infsoft. Für die Positionsbestimmung sendet der UWB Tag Daten (ID, timestamp etc.) zu
mehreren Infsoft Locator Nodes (Empfänger) in Reichweite. Dabei wird die **Signallaufzeit**
zwischen einem Tag und mehreren Nodes gemessen. Für die genaue Lokalisierung eines


-----

j p g g, g

zwischen Empfänger und Sender bestehen. Die Position der Kleinladungsträger lässt sich im
praktischen Betrieb mit einer Genauigkeit von 30cm bestimmen. Der Locator Node verarbeitet
die bereitgestellten Daten und sendet sie via Ethernet an die Software von infsoft. Dort wird
die Position bspw. in einer Karte dargestellt. Die Daten werden automatisch in der
Softwarelösung erfasst und werden für rückwirkende weitere Analysen von Durchlaufzeiten
und Route durch die Prozesskette gespeichert.

Abbildung 1: Locator Node von Infsoft
Abbildung 2 UWB-Tag von infsoft

Gemeinsam mit Infsoft wurde dabei das Hallenlayout der CiP digitalisiert um die
Aufenthaltsorte der UWB Tags zuordnen zu können und im weiteren die Aufenthaltszeiten an
den jeweiligen Prozessschritten sowie die Durchlaufzeit der gesamten Produktion erfassen zu
können.

Abbildung 3: Zonenzuordnung in Hallenlayout über infsoft Software

**1.6 Umsetzungsaufwand**

Die Implementierung der Lokalisierungstechnologie aus Locator Nodes und Tags erfordert ein hohes Maß an
Umsetzungsaufwand. Die Nodes müssen in der Fabrik installiert und eingemessen werden. Außerdem müssen
die Zonen definiert und in dem Software Layout hinterlegt werden. Das präzise Arbeiten beim Erstellen des
Layouts ist dabei unerlässlich, es dient als Grundlage für die Auswertung der Bewegungsdaten.

Ist die Installation der Hard,- und Softwarte abgeschlossen, sind individuelle Anpassung (bspw. des
Zonenkonzepts) nach Kundenwünschen sehr flexibel und mit einem niedrigen Grad an Mehraufwand möglich


-----

**St u tu e t ade**

**Lokalisierung**


**att 6**




|Arbeitsaufgabe: Vorführung der Lokalisierungs- technologie|Col2|Produkt: Zylinder|Arbeitsplatz: CiP|
|---|---|---|---|
|Datum: 05.10.2022|||Freigegeben: M.Fall|
|Nr||||
|2|Vortrag – Durchführung der Demonstration|||
||2.1 Vorbereitung der Demonstration Auslegen der Tags nach dem SAB Öffnen der Trackingsoftware von Infsoft Dashboard öffnen für Demonstration von Analyse des Produktionsprozesses|||


**2.2 Demonstration**
**Einleitung**

1.) Vorstellen der CIP - Forschungsschwerpunkt (1.1)
2.) Vorstellen von Lokalisierungstechnologien (1.2)
3.) Vorstellen der Prozesskette: Erläutern der notwendigen Prozesschritte für die Fertigung des

Zylinderbodens – Anwendung (1.3)

4.) Zusammenführen der Informationen aus 1.), 2.) und 3.)

Forschungsziele: Transparenzschaffung (1), auf dem Markt verfügbare Technologien (2) sowie
Prozesskette in CIP und Eigenschaften der Infrastruktur (3) bestimmen die Anforderungen an
die Technologie (1.4)

5.) Vorstellen der Technischen Lösung in der CIP

Hardware vorstellen- Technische Lösung in der CIP (1.5)
UWB-Tag und Locator Node zeigen: darauf hinweisen, dass Sichtkontakt unabdingbar ist, um
eine exakte Positionsbestimmung zu gewährleisten, UWB-Tag steht für Kleinladungsträger mit
einer Loszahl 4, der durch Prozesskette läuft
Eigenschaften wie Akkulaufzeit und Genauigkeit erläutern

6.) Vorstellen des Trackingtools

Umsetzungsaufwand (1.6) erläutern dabei auf das Hallenlayout verweisen und dabei das
Trackingtool der Firma Infsoft genauer erläutern: Auf Zuordnung der Zonen Bezug nehmen.
Hohe Präzision beim Einmessen der Locator Nodes wichtig, um Zuordnung zu Zonen zu
gewährleisten. Die erfassten Daten bilden die Grundlage für die Auswertung der Daten und der
darauf aufbauenden Analyse der Prozesskette mithilfe des Dashboards


7.) Dashboard vorstellen

Beispieldatensatz vom 01.-03.09.2021 öffnen
1.) Vorstellen des Interfaces (Tag 1002 einblenden)

Durchlaufzeiten zeigen, wieder Bezug auf Zonenzuordnung nehmen
Fließgrad, Durchlaufzeit und Kosten erläutern
**Kostenanalyse:** Über Zeitstempel können Prozesskräfte, Energieverbräuche und Temperaturen den
einzelnen Chargen zugeordnet werden. Das ermöglicht Berechnung der Produktionskosten pro
Charge


-----

𝐹𝑙𝑖𝑒ß𝑔𝑟𝑎𝑑= [𝐿𝑖𝑒𝑔𝑒𝑧𝑒𝑖𝑡+ 𝑊𝑎𝑟𝑡𝑒𝑧𝑒𝑖𝑡+ 𝐵𝑒𝑎𝑟𝑏𝑒𝑖𝑡𝑢𝑛𝑔𝑠𝑧𝑒𝑖𝑡]

𝐵𝑒𝑎𝑟𝑏𝑒𝑖𝑡𝑢𝑛𝑔𝑠𝑧𝑒𝑖𝑡

2.) Demonstrieren der Analysemöglichkeiten (Tags 1002, 1003, 1020, 1021, 2022, 1023, 1024, 1025)

einblenden
Bottleneck identifizieren: Übersicht, alle Stationen einblenden (Sägen, Fräsen, Reinigen, QS,
Montage)
Einblenden der einzelnen Sollwerte für Prozessschritte
Abgleich der Sollwerte mit tatsächlich Durchlaufzeiten

Abbildung 4: Abgleich von Sollzeiten an den einzelnen Prozessschritten


Durch den Abgleich der Sollwerte an den jeweiligen Prozessschritten lässt sich

darstellen an welchem Prozessschritt es zu einer erhöhten Durchlaufzeit gekommen ist. Die Dauer der

Liegezeiten wird in dem Fall von der Montagestation dominiert.

Abbildung 5: Tag Inspector: Analyse welcher Tag (Arbeitsauftrag) hohe Liege-und Wartezeiten aufweist

Die Dauer der Liegezeiten wird in dem Fall von der Montagestation dominiert.

Auswählen Tags 1000, 1001, 1002, 1003, 2020, 1021, 1022, 1023, 1024, 1027, 1028,

1029, 1030, 1032, 1033, Tag Inspector Montagestation

Die Einstellung zeigt bei welchen Arbeitsaufträgen es zu einer besonders hohen

Wartezeit gekommen ist und kann im weiteren durch Abgleich mit den Sollzeiten an der

Montagestation genauer analysiert werden


-----

Abbildung 6: Abgleich der Soll-und Durchschnittswerte im Tag-Inspector

Die Analyse der Prozesskette mit dem Dashboard liefert einen erhöhten Grad an

Transparenz.


Aufbauend auf der Transparenzschaffung durch Lokalisierungstechnologie,

Trackingapp und den damit erfassten Daten kann der Anwender in die Ursachenanalyse

und die Problembehebung gehen.

Die Ursachenanalyse kann dabei nicht alleine aus den im Dashboard ausgewerteten

Daten erfolgen, es bedarf dabei einer anwenderspezifischen Analyse des Problems vor

Ort.

**Beispielvorgang:**

**Ursachenanalyse**

Die Lokalisierungstechnologie liefert Transparenz über die Wertschöpfungskette des

Pneumatikzylinders. Aufbauend auf den ausgewerteten Daten muss in der

Ursachenanalyse der Kern des Problems erkannt werden.

Beispiel: Bottleneck

Montage in Nachtschicht unterbesetzt? Allgemein unterbesetzt?

Beispiel: Verspätete Auftragsbedienung

Worauf ist die Verspätung zurückzuführen? An welchen Stationen sind hohe Warte-/

und Liegezeiten entstanden:

Beispiel: Rückruf

Welche Stationen ist das Bauteil durchlaufen? Maschine fehleranfällig?


**Problembehebung**

Aufbauend auf der Ursachenanalyse und dem Identifizieren des Kernproblems können

Konsequenzen gezogen und das erneute Auftreten der Problemstellung verhindert

werden.

Beispiel: Zeigt sich, dass Montagestation grundlegend einen Bottleneck in der

Prozesskette darstellt: Lohnt sich die Anschaffung einer neuen Montagestation oder

reicht der Einsatz von weiterem Personal in Nachtschicht/ Alltagsbetrieb.

Ist der Rückruf auf einen bereits behobenen Werkzeugausfall zurückzuführen oder muss

die Werkzeugmaschine gewartet werden?


-----

**St u tu e t ade**

**Lokalisierung**


**att**






|Arbeitsaufgabe: Vorführung der Lokalisierungs- technologie|Col2|Produkt: Zylinder|Arbeitsplatz: CiP|
|---|---|---|---|
|Datum: 05.10.2022|||Freigegeben: M. Fall|
|Nr||||
|2|Häufige Fragen|||
||• Wie viele Nodes und Tags werden benötigt? Das kommt ganz auf die Gegebenheiten und Anforderungen an. Wesentliche Parameter sind Reichweite, Genauigkeit und Layout des Einsatzortes. • Wie präzise ist die indoor Lokalisierung? Die Genauigkeit hängt wesentlich von dem Gebäudelayout ab (Abschirmung). Außerdem ist entscheidend, wie engmaschig das Netz ist (Wi-Fi-Access Points, Bluetooth Beacons). Prinzipiell gilt: je mehr Hardware, desto genauer. • Was kostet die Implementierung eines Lokalisierungssystems? Die Kosten hängen von dem individuellen Anwendungsfall ab. Meist fallen Lizenzgebühren für die Software sowie Kosten für die Hardware an. Die Hardwarekosten hängen im Wesentlichen von der eingesetzten Technologie sowie der geforderten Genauigkeit ab. • Auf was ist bei der Implementierung eines auf UWB basierenden Lokalisierungssystems zu achten? UWB ist anfällig für Störungen, wenn keine direkte Sichtverbindung zwischen Tag und Node besteht. Das muss bei der Hardwareanordnung berücksichtigt werden. • Wie werden die Nodes und Tags mit Strom versorgt? Grundsätzlich sind verschiedene technische Lösungen vorstellbar. In der CiP werden die Tags über Akku betrieben und die Nodes über Power over Ethernet (PoE). • Besteht die Möglichkeit, die Lösungen von Infsoft mit einem bestehenden SAP/ERP System zu koppeln? Ja. Die „LocAware platform“ von Infsoft bietet bidirektionale Schnittstellen.|||


-----

**St u tu e t ade**

**Lokalisierung**


**att 8**




|Arbeitsaufgabe: Vorführung der Lokalisierungs- technologie|Col2|Produkt: Zylinder|Arbeitsplatz: CiP|
|---|---|---|---|
|Datum: 05.10.2022|||Freigegeben: M.Fall|
|Nr||||
|3|Probleme|||
||• Die Akkus der Tags ermöglichen nur eine kurzzeitige Anwendung. Deshalb ist regelmäßiges Laden notwendig. Eine zu geringe Genauigkeit führt zu einer falschen Einordnung der Tags in die Zonen. Die Analyse der Daten ist somit auch fehlerhaft und verliert Aussagekraft.|||


-----


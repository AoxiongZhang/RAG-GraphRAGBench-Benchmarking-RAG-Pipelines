|Col1|Col2|Strukturleitfaden eKanban|Blatt 1 von 5|
|---|---|---|---|
|Arbeitsaufgabe: Intra-Logistik||Produkt: eKanban-System als direkte Lieferantenschnittstelle|Arbeitsplatz: Industrie 4.0|
|Datum: 30.08.2019||Erstellt: M.Dessel||
|Nr||||
|1|Vortrag|||
||Allgemein/Aufbau Im Lager werden zugekaufte Lieferantenteile gelagert, bis sie auftragsspezifisch entnommen und montiert werden. Mit dem eKanban entsteht hier die direkte Schnittstelle zwischen Fertigung (interne Logistik) und dem Lieferanten. Am Eingang und am Ausgang des Lagers sind RFID-Lesegeräte angebracht. Über diese Lesegeräte werden die Transponder auf den Kanbankarten (bei uns in den Karten) beim Ein- bzw. Auslagern eingelesen. (In der Regel wird das Rollenlager von hinten bestückt, daher sollte der „Einscanner“ auch dort befestigt sein, dies ist bei uns aber aus Demonstrations-Gründen nicht der Fall) Sind alle Ladungsträger/Kisten mit einem RFID-Chip ausgestattet, so lässt sich der Bestand nicht nur visuell Anzeigen, sondern auch Überwachen und Steuern. Funktionen • Bestandsüberwachung - Kontinuierliche Anzeige des Bestands in Echtzeit - Visualisierung als Säulendiagramm - Von überall sichtbar (auch im Büro des Fertigungsplaners) • Steuerlogistik - Automatische Berechnung der Bestellgröße für jedes Lieferantenteil - Signal, sobald Meldebestand erreicht ist - Erstellung von Verbraucherstatistiken • Kanban-Karten-Konfigurator - Reagieren auf Bedarfsschwankungen - Anpassen des Meldebestands an Karten Anzahl - Angleichung externer Lieferungen und interner Milkrunsysteme • Karten-Verwaltung - Auflistung aller Kanban-Karten - Visualisierung als Tabelle - Hinzufügen von Einträgen durch Eingabemaske ➔ Transparenz, Geringer Aufwand, Flexibilität, Übersichtlichkeit|||


-----

|Col1|Standard Arbeitsblatt Arbeitsanweisung|Blatt 2 von 5|
|---|---|---|
|Arbeitsaufgabe: Intra-Logistik|Produkt: eKanban-System|Arbeitsplatz: Industrie 4.0|
|Datum: 30.08.2019|Erstellt: M.Dessel||
|Verschwendungen Vermeidung von: • Überflüssigen Transporten • Wartezeiten • Überlieferung • Undefinierte Prozesse • Überdimensionierte Bestände • Unnötige Tätigkeiten Insbesondere wird die Kommunikation zum Lieferanten deutlich vereinfacht und es werden Standardtätigkeiten des Einkaufs automatisiert. Umsetzungsaufwand Der Implementierungsaufwand in ein vorhandenes Prozessleitsystem ist eher gering Einsatzbereich Innerbetriebliche Lagerhaltung von Lieferantenteilen mit regelmäßigem und hohem Verbrauch (X-Teile) Wichtige Besonderheiten Vor der Führung: Abgleichen der digitalen Bestände in Aprol mit den realen Lagerbeständen, damit keine Fragen bzw. Unstimmigkeiten auftreten. Während der Demonstration sollten Kisten ausgescannt werden, um den Meldebestand zu erreichen. In der Detailansicht soll dann eine Bestellung zu Lieferanten abgeschickt werden. Wichtig: System ist sehr träge! D.h. Wird eine Kiste/Karte kurz vor den Reader gehalten und somit Ein- bzw. Ausgescannt wird zeitlich sehr verzögert geschaltet und der Bestand erst nach einigen Sekunden erhöht/gesenkt.|||


-----

|Col1|Standard Arbeitsblatt Arbeitsanweisung|Blatt 3 von 5|
|---|---|---|
|Arbeitsaufgabe: Intra-Logistik|Produkt: eKanban-System|Arbeitsplatz: Industrie 4.0|
|Datum: 30.08.2019|Erstellt: M.Dessel||
|Der Kanban-Karten-Konfigurator (in der Detail-Ansicht) Die vier Felder dienen zur individuellen Eingabe eines sich ändernden Produktionsprozess. Die Kartenanzahl, die Anzahl der Bauteile pro Kiste, der Kundetakt und die Bedarfsrate sind die entscheidenden Faktoren zur Berechnung des Meldebestands. Das System bietet durch die Synchronisation des externen Informationsflusses zum Lieferanten und dem internen Kanban-System die Möglichkeit, Kanban-Mengen und Bestände an wechselnde Kundentakte und Rahmenbedingungen schnell anzupassen. Die SQL-Kanban-Karten-Datenbank soll nicht gezeigt werden! Sie entspricht einer übersichtlichen Auflistung der sich im Prozess befindenden Kanban- Karten.|||


-----

|Col1|Standard Arbeitsblatt Arbeitsanweisung|Blatt 4 von 5|
|---|---|---|
|Arbeitsaufgabe: Intra-Logistik|Produkt: eKanban-System|Arbeitsplatz: Industrie 4.0|
|Datum: 30.08.2019|Erstellt: M.Dessel||
|2 Häufige Fragen|||


1. Wie Berechnen sich die Demonstrator-Werte?

Wobei:

|Col1|(1)|
|---|---|
||(2)|
||(3)|
||(4)|



-  (1) Analog zur Wertstromanalyse

-  Aus Formel (2) folg durch Umstellen Formel (3) mit:

`o` **q = Antwortzeit (bzw. Wiederbeschaffungszeit)** = Doppelte Maximale Zeit

zwischen 2 Auffüllvorgängen

`o` **Behältermenge** und der **Kundentakt** sind variable Eingabefläche, damit

Anpassung an sich ändernde Produktionsverhältnisse möglich

`o` Anzahl der **Kanban-Karten-Anzahl** über „Slider“ vorgeben

-  Formel (4) ergibt sich aus der Multiplikation von q mit einer **durchschnittlichen**

**Bedarfsrate** .

-  **Sicherheitsbestand = Meldebestand** (Annahme nur hier in der CiP)

2. Wieso ist es möglich einen Ladungsträger **mehrmals ein- oder auszuscannen** ?

Müsste hier nicht eine Sperre hinterlegt sein?
Es ist möglich hier eine Sperre einzubauen und dies sollte in einer laufenden
Produktion auch gemacht werden. Im Umfeld einer Lernfabrik, in der die
Ladungsträger keinem strengen Prozess folgen, ist die Umsetzung jedoch nicht
praktikabel.


-----

|Col1|Col2|Standard Arbeitsblatt Arbeitsanweisung|Blatt 5 von 5|
|---|---|---|---|
|Arbeitsaufgabe: Intra-Logistik||Produkt: eKanban-System|Arbeitsplatz: Industrie 4.0|
|Datum: 30.08.2019||Erstellt: M.Dessel||
|3. Was bedeuten die verschiedenen optischen Signale? - gelb/grün leuchten: Spannung liegt an - gelb/grün blinken: Gerät ist betriebsbereit und lesebereit - oranges blinken: RFID wurde gelesen - 4. Wieso ist das Ein und Ausscannen so träge? Dies liegt an der Implementierung, die ein doppeltes oder ungewolltes Scannen verhindert. Die Karte muss bewusst einige Sekunden vor dem Scanner gehalten werden 5. Wie viel Kostet ein Reader? Die verbauten Reader sind Standard Reader von Pepperl und Fuchs und liegen im Anschaffungswert bei ca. 400€||||
|3|Probleme|||
||- Alle Ladungsträger/Kisten müssen voll sein und richtig einsortiert werden! - RFID-Reader haben nur eine kurze Lesedistanz von ca. 2cm. Das bedeutete, dass die Kisten sehr nah vor den Reader gehalten werden. Bei schweren Ladungsträgern empfiehlt es sich die Karte herauszunehmen, was allerdings einen zusätzlichen Zeitaufwand bedeutet. - Zeitliche Trägheit des Systems!|||


-----


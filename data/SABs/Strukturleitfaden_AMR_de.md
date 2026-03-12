**St u tu e t ade** att o 5

**Allgemein**

|Col1|Col2|AMR|Col4|
|---|---|---|---|
|Arbeitsaufgabe: Intra-Logistik||Produkt: Fahrerloser Transport und Materialübergabe durch Einfachautomatisierung|Arbeitsplatz: Industrie 4.0|
|Datum: 06.03.2024||Erstellt: T. Balzer||
|Nr||||
|1|Vortrag|||



Es gibt intralogistische Strecken in einer Fabrik, die nicht häufig passiert werden, daher wäre
der Einsatz eines Logistikers zu hoch dimensioniert. Die Kombination eines spurlosen
Autonomen Mobilen Roboters (AMR) mit dem sog. Karakuri-Prinzip [1] ermöglicht neue
Konzepte in der innerbetrieblichen Logistik: Ein Automatisierungsmechanismus unter Einsatz
der Schwerkraft aus einfach Profilen und Gelenken ohne jegliche Antriebe oder Sensorik
nimmt den Mitarbeitern einfach Materialtransport zwischen Arbeitsstationen ab. Hierbei wird
auch das Problem der Materialübergabe zwischen Stationen vollautomatisch und dennoch
einfach gelöst.

In diesem Fall handelt es sich bei der Strecke um von Kunden individuell bestellte Zylinder, die
in der Sequenzlinie gefertigt, gewaschen und einer Qualitätskontrolle unterzogen werden. Diese
werden im Anschluss direkt zur Montagelinie gebracht und genießen eine höhere Priorität
gegenüber dem Standard-Zylinder. Alle 3 Minuten wird ein individueller Zylinder in der
Sequenzfertigung gefertigt. Der AMR bringt den vollen KLT² und nimmt die Leeren wieder
mit zurück zur Sequenzlinie.

Im Allgemeinen geht es darum, für kleine Fabriken automatisierte Lösungen zu finden, die
nicht mit hohen Kosten verbunden sind. Die Bedien-Oberfläche des AMR ist sehr
benutzerfreundlich und kann von jedem nach kurzer Einarbeitung genutzt werden.

**Nutzen/Vorteile** ³

-  Keine zusätzliche Infrastruktur (Transponder im Boden etc. nötig)

-  Return on Investment (ROI): ~ 1 Jahr laut Hersteller

-  Vollautomatisierter Materialtransport über größere Strecken

-  Fokus wertvoller Mitarbeiterressourcen auf Kerntätigkeiten: Weniger Lauf- und

Transportwege zwischen Prozessen und Abteilungen

-  Einfache Produktionssteuerung nach dem FIFO-Prinzip, auch für eine schnelle und

simple Einsteuerung von Eilauträgen in eine Montagelinie geeignet


-----

**Sta da d** **be tsb att**


att o 5



|Technische Daten|Col2|
|---|---|
|Max. Ladungsgewicht|100 kg|
|Zugkraft|Max. 300 kg|
|Betriebszeit|10 Stunden oder 20 km|
|Geschwindigkeit|1,5 m/s bzw. 5,4 km/h|
|Ladezeit|3 Stunden (für 100%), 2 Stunden (für 0-80%)|
|Eigengewicht (ohne Ladung)|77 Kg|
|Ladefläche|580mm*890mm (½ Europalette)|

|Col1|Col2|Arbeitsanweisung|Col4|
|---|---|---|---|
|Arbeitsaufgabe: Intra-Logistik||Produkt: Fahrerloser Transport und Materialübergabe durch Einfachautomatisierung|Arbeitsplatz: Industrie 4.0|
|Datum: 06.03.2024||Erstellt: T. Balzer||
||Umsetzungsaufwand gering: Der AMR wird über eine benutzerfreundliche Oberfläche programmiert. Dazu sind keinerlei weiterführenden Programmierkenntnisse notwendig. Alternativ kann eine CAD-Datei der Umgebung hochgeladen werden³. mittel: Der Aufsatz zur Materialübergabe nach dem Karakuri-Prinzip muss dem bestehenden Umfeld entsprechend ausgelegt werden. Lösbare Umsetzungshürden sind Sicherheitsaspekte und Ungenauigkeiten im Fahrweg des AMR sowie dem richtigen Anstellwinkel des Karakuri- Mechanismus. Einsatzbereich Innerbetrieblicher Transport und Übergabe von Kleinladungsträgern bei größeren räumlichen Distanzen in einem Wertstrom Technische Daten Max. Ladungsgewicht 100 kg Zugkraft Max. 300 kg Betriebszeit 10 Stunden oder 20 km Geschwindigkeit 1,5 m/s bzw. 5,4 km/h Ladezeit 3 Stunden (für 100%), 2 Stunden (für 0-80%) Eigengewicht (ohne Ladung) 77 Kg Ladefläche 580mm*890mm (½ Europalette)|||


-----

**Sta da d** **be tsb att**


att 3 o 5




|Col1|Col2|Arbeitsanweisung|Col4|
|---|---|---|---|
|Arbeitsaufgabe: Intra-Logistik||Produkt: Fahrerloser Transport und Materialübergabe durch Einfachautomatisierung|Arbeitsplatz: Industrie 4.0|
|Datum: 06.03.2024||Erstellt: T. Balzer||
||Funktionsweise Verbinden mit dem AMR Man kann sich mit jedem internetfähigen Gerät (Laptop, Handy) mit dem Wifi des AMR verbinden und die Oberfläche im Browser aufrufen. (sowohl die drahtlose Verbindung als auch der Zugang zur Benutzeroberfläche sind Passwort-geschützt). Fahren Zuvor wurde die Karte der Cip durch das Befahren des AMR eingescannt und die verschiedenen Haltepositionen darin gespeichert. Der AMR besitzt: (1) vorne und hinter 360° Laserscanner, (2) eine 3-D Kamera, welche Gegenstände im Fahrweg 50-500 mm über den Boden erkennt und (3) vier Ultraschallscanner, welche durchsichtige Gegenstände im Fahrweg erkennen (z.B. Glastüren). Andocken Durch den V-Marker ist der AMR in der Lage eine Positionsgenauigkeit von +-10 mm einzuhalten. Zuvor wurde die grobe Position des Markers gespeichert und der AMR schafft es selbstständig den Marker zu finden und sich per Ultraschall daran auszurichten. Besonderheiten - Bei blindem Nach-Hinten fahren (während der AMR piepst) wird nicht auf die Gegenstände oder Personen im Weg geachtet, da dies so eingestellt wurde. (Befehl: fahre 2 m nach Hinten) - Die Andockstation und das Gerüst auf dem AMR sind Low-Cost Lösungen, die in Rahmen der studentischen Arbeiten in der CiP entwickelt und umgesetzt wurden.|||


-----

**Sta da d** **be tsb att**


att o 5



|Col1|Col2|Arbeitsanweisung|Col4|
|---|---|---|---|
|Arbeitsaufgabe: Intra-Logistik||Produkt: Fahrerloser Transport und Materialübergabe durch Einfachautomatisierung|Arbeitsplatz: Industrie 4.0|
|Datum: 06.03.2024||Erstellt: T. Balzer||
|2|Häufige Fragen|||
||- Wieviel kostet der AMR? Ca. 25.000 € exkl. Steuern (Stand 08/2022)4|||
|3|Probleme|||
||- Aktives Laden notwendig, da kein Ladestation vorhanden (könnte man theoretisch aber dazu kaufen, dann könnte der AMR selbstständig in die Ladeposition fahren und sich selbst aufladen.)5 ➔ Die AMRs in der Flow Factory können induktiv geladen werden. Zudem wurden hier drei AMR angeschafft, die über ein MES-System gesteuert werden können und dadurch auch untereinander kommunizieren können. - Bei einem Gerüst auf dem AMR, welches über die Standard-Oberfläche herausragt, besteht die Gefahr der Kollision, da der AMR selbst nicht weiß, dass die Abmaße in der Höhe erweitert wurden.|||
|4|Unterscheidung FTS/ AMR und Anwendung in der Industrie|||
||Bei Fahrerlosen Transportsystemen (FTS) erfolgt die Navigation spurgebunden und es ist eine zusätzliche Infrastruktur in Form von Schienen, Markierungen oder im Boden eingelassene Magnetstreifen notwendig. Die Routen werden im Vorhinein genau festgelegt und die FTS sind anschließend an diese gebunden. Änderungen der Navigation sind nur mit entsprechendem zusätzlichem Aufwand verbunden. Autonome Mobile Roboter (AMR) können hingegen ohne zusätzliche Anpassungen an der Infrastruktur flexibel navigiert werden. Sie orientieren sich an einer erfassten Umgebungskarte, können dank Sensoren und Kameras selbstständig Personen und Gegenständen ausweichen und finden dadurch flexibel eine passende Route.⁹ FTS-Systeme gibt es seit ca. der 70er Jahre6 und sind Stand 2022 in verschiedensten Größen, Bauarten und für viele Einsatzgebiete verfügbar. Das können sein: • Innen- oder Außenbereich • Linen-/Flächenbeweglichkeit • Zugfahrzeuge mit Anhängern, Fahrerlose Gabelstapler, Stückguttransporter u.v.m.7|||


-----

|Col1|Col2|Standard Arbeitsblatt Arbeitsanweisung|Blatt 5 von 5|
|---|---|---|---|
|Arbeitsaufgabe: Intra-Logistik||Produkt: Fahrerloser Transport und Materialübergabe durch Einfachautomatisierung|Arbeitsplatz: Industrie 4.0|
|Datum: 06.03.2024||Erstellt: T. Balzer||
||Ein „namhafter deutscher Premiumhersteller von sportlichen Automobilen“ baut mithilfe von autonomen mobilen Robotern von DS Automotion, einem Unternehmen aus Linz in Österreich, seine Produktionskapazität für elektrische Antriebe auf 500.000 Einheiten/Jahr aus. Die FTS kommen bei der Montage der Batterieeinheiten zum Einsatz und bewegen die Produkte durch die verschiedenen Montagestationen. Die Navigation erfolgt durch ein Magnetband im Boden spurgeführt. Routenänderungen sind dadurch flexibel durchführbar. Bei Stationen mit längeren Taktzeiten werden die FTS durch Bodenkontakte geladen.8|||


Quellen & Anmerkungen:

1 https://www.cetpm.de/lexikon/was-ist-karakuri/162/
Karakuri bezeichnet einfache Automatismen aus japanischen Puppen des 18. Jahrhunderts, welche mit
mechanischen Elementen wie Wellen, Zahnrädern und physikalischen Kräften (hier: Gravitationskraft)
arbeiten.

² Abkürzung für Kleinladungsträger
3 Produktseite: https://www.mobile-industrial-robots.com/solutions/robots/mir100/
4 Händler: https://neolog.info/shop/mir-100-mobiler-roboter.html
5 Produktseite: https://www.mobile-industrial-robots.com/solutions/mir-applications/mir-charge-24v/
6 https://www.iph-hannover.de/de/dienstleistungen/automatisierungstechnik/fts-fahrerlose-transportsysteme/
7 www.bito.com/de-de/fachwissen/artikel/fahrerlose-transportsysteme-so-behalten-sie-den- ueberblick/
8 https://www.robotik-produktion.de/mobile-robotik/fts-einsatz-in-der-pkw-batteriemontage/ (05.08.2022)
⁹ https://www.phoenix-mecano.ch/de/produkte/produktion/fahrerlose-transportsysteme-fts/


-----


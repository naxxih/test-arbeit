if __name__ == '__main__':
    
    print("Hello World!")

    # Die iputData.csv einlesen und für jedes Requirement dort einen Testfall aussuchen 
    
    # Hier noch TODO-ÜBERLEGUNG: Der BSI Grundschutz hat so ca. 900 Requirements, da kann ich ja nicht 
    # immer zwei Parameter und ein Value manuell zuordnen, wie mach ich das dann da?

    # Testgefälle werden gemapt z.B. durch Dictionary 

    # Jeder Testfall hat individuelle Parameter, die auch Config kommen 

    # Es gibt Testfälle, die für alle Geräte gleich sind, und es gibt Testfälle die für jedes Gerät unterschiedlich sind
    # Grundsätzlich aber: die Testfälle unterscheiden sich stark je nach Gerät, deswegen Aufteilung nach Geräten 
    # Pls komment falls es keinen Sinn macht so 

    # Dann irgendwie Durchfühung der Testfälle 
    # Noch unklar ob tptester verwendet werden muss
    # Entwurf von einem Testtool wie du schon gemacht hast kann aber gern gezeigt werden 

    # Output 
    # Es soll eine Testcase ID geben 
    # und eine Prüfvorschrift ist jetzt neu 
    # heißt einmal genereller Output welcher testfall passed und welcher nicht und zu welchem requirement das zugeordnet wird

    # Prüfvorschrift bei SDIS bei Christian
    # PrüfID: 123
    # Was geprüft wird: Das Passwort muss dreimal falsch eingegeben werden bei Anmeldung. 
    # Erwartetes Ergebnis: Die Anmeldung ist für 3 min gesperrt. 
    # Tatsächliches Ergebnis: Pass
    # Zugehöriges Requirement: Requ_12345

    # Das ganze ist in Form einer Tabelle, also könnte man doch die Texte direkt hier bei den Python Tests mit dazu schreiben oder?
    # Macht das Sinn? 
    # Dann könnte man es als output csv machen und wieder in DOORS einpflegen und dann kommt ne Tabelle als Word raus - wunderschön 

    # Ich hätte gern nen Logger 
    
    # Machen wir ne WebGUI?

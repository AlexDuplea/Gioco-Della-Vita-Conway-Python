# Gioco-Della-Vita-Conway-Python
Gioco della vita scritto in python, "l'interfaccia grafica" si trova nel terrminale

Esecuzione del Programma

Per ottenere i migliori risultati, eseguite il codice direttamente nel terminale.
Istruzioni per l'esecuzione:

  -Windows:
  
    -Aprite PowerShell
    -Navigate alla directory contenenye il file LA_CITA.py con il comando:
      -cd <percorso_della_cartella>
    -es:
      -cd C:\Users\<nome_utente>\Downloads\gioco_della_vita
    -Eseguite poi il programma con il comando:
      -python LA_CITA.py 

  -Mac/Linux:
  
    -Aprite il terminale
    -Navigate alla directory contenente il file LA_CITA.py con il comando:
      -cd <percorso_della_cartella>
    -es:
      -cd /Users/<nome_utente>/Downloads\gioco_della_vita
    -Eseguite il programma con:
      -python3 LA_CITA.py
    

        

Personalizzazione delle dimensioni dello schermo

Se utilizzate uno schermo di 32 o 16 pollici, il programma funzionerà perfettamente con le impostazioni predefinite.
Per schermi di dimensioni diverse, seguite i passaggi seguenti per regolare manualmente le dimensioni:

  - Disattivare la funzione preset():
    Per farlo, aprite il file LA_CITA.py e aggiungete un # prima della riga che chiama la funzione preset().

  - Attivare la funzione grandezza_schermo():
    Rimuovete il # dalla riga che chiama la funzione grandezza_schermo().
    
  - Testare altezza e larghezza dello schermo:
    Eseguite il programma per vedere i quadretti bianchi nel terminale. Continuate a modificare i valori di h1 (altezza) e l1 (larghezza) fino a ottenere una dimensione ottimale per il vostro schermo.


  - Una volta trovate le dimensioni ideali, potete:
        Inserire i valori direttamente nella funzione gioco().
        Personalizzare la funzione preset() con le nuove dimensioni.

  - Disattivare le funzioni non necessarie:
    Rimuovete il # dalla funzione che volete utilizzare e aggiungetelo a quelle che non vi servono più, per evitare conflitti.

Note
  Per "disattivare" o "attivare" una funzione in Python, basta aggiungere o rimuovere il simbolo # all'inizio della riga corrispondente.
  Assicuratevi di salvare le modifiche al file prima di eseguire il programma.




    

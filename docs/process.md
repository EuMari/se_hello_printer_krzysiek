![Image](https://raw.githubusercontent.com/kbalko/se_hello_printer_app/master/docs/pipeline.PNG)

# Opis procesu

### Po zmianie kodu lokalnie na komputerze:
      
      #do repo gita 
      $git add --all 
      $git commit -m"komentarz"
      $git push 
      
Pliki będące na komputerze lokalnie trafiają fo repozytorium gita, stąd trafia do Jenkinsa i Travis CI. 
 
     # do gitlaba
     $ git push gitlab master
      
Po tej komendzie pliku trafiają do GitLaba. 

### Proces testów 

Travis/Gitlab/Jenkis sprawdzają zgodność zależności z plików requirements.txt i test_requirements.txt. Następnie uruchamiane testy jednostkowe, metryki pokrycia kodu i testy w Robot Framework. Po skryptach testowych na podstawie metryk pokrycia kodu uruchamiane jest narzędzie [Coveralls](https://coveralls.io/github/kbalko/se_hello_printer_app). Proces testów szerzej opisany jest w pliku /docs/proces_todo.md. 

- Jenkins - 127.0.0.1:8080

      # instrukcja uruchomienia
      $ cat README.md
      
      $ git clone https//github.com/kbalko/se_teaching_jenkins
      $ make bulid_jenkins
      $ make run_jenkins 
      
### Docker 

Następnie dzięki odpowiednim targetom zawartym pliku Makefile  i dzięki plikom konfiguracyjnym budowany jest Docker, po zbudowaniu następuje push kontenera na hub.docker.com. 

      # tergety w Makefile
      $ make docker_build
      $ make docker_run
      $ make docker_stop
      $ make docker_push
 
 Kontener Dockera: https://hub.docker.com/r/kbalko/hello-world-printer
 
 ### Heroku
 Następuje deploy aplikacji na Heroku. Aplikcja dostępna dla Klienta pod [linkiem](https://dry-brushlands-36461.herokuapp.com/). 
 
 ### Monitorowanie StatusCake 
 Aplikacja jest połączona z narzędziem StatusCake, które monitoruje czy strona jest aktywyna i wysyła alert e-mail do administratora jeśli strona nie odpowiada. 
 

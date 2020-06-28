# Proces testowy w CI/CD


Proces testowy utrzymany jest w duchu Continous Testing - zautomatywowania wykonywania testów w pipelinie w CI/CD.

**Testy są automatycznie odpalane po każdym pushu do repozytorium w momencie gdy trafiają na Travis CI/Gitlab.**

W każdy momencie można je również odpalać z linii komend.

Linter tool
-----------
Narzędzie: flake8
Analiza kodu pod wzlędem poprawności składni i zgodności z PEP8, pozwala tworzyć czytelniejszy kod. Oszczednośc czasu przy debugowaniu kodu (wyłapytanie "w locie" literówek, formatowania, składni, stylu). Powinny być uruchamiane po każdej wprowadzonej zmianie w kodzie
   
    # uruchomienie 
    $ make lint
    
Smoke Test
----------
Sprawdzenie krytycznej funkjonalności aplikacji. W przypadku tej aplikacji jest _smoke test_ wykonuje prostą komendę _'curl'_ 
    
    # uruchomienie
    $ make test_smoke

Testy jednostkowe
-----------------
Weryfikacja działania pojedyńczych elementów programu. Pozwalają na szybkie wychwycenie i zlokalizowanie zaintnienia defeku w kodzie. 
W pełni zautomatyzowane. Powinny być uruchamiane po każdej wprowadzonej zmianie w kodzie
    # uruchomienie
    $ make test


Metryki pokrycia i złożoności kodu
----------------------------------
Metryki pozwają na ilościową analizę jakości kodu. Ukazuje które moduły programu wymagają jeszcze pokrycia testami czy refraktoryzacji.
Powinny być uruchamiane na bieżąco w traksie tworzenia oprogramowania, by na bieżąco wprowadzać zmiany w kodzie i pokrywać kod testami jednostkowymi.

- testy pokrycia kodu (coverage tests): 
  
      # uruchomienie
      $ make test_cov
      $ make test_xunit

  Używane narzędzie - Coveralls - dostarcza statystyk i grafik dotyczących pokrycia kody testami.
  
- testy złożoności (complexity tests):
  
      # uruchomienie
      $ make test_complexity


 
Testy akceptacyjne/ testy UI
----------------------------
Testy automatyczne: biblioteka Selenium i Robot Framework.
Weryfikacja poprawoności działania aplikacji zgodnie z specyfikacją i opracowanymi przypadkami testowymi. 
Dostarcza reportów i logów z przeprowadzonych testów a także screenshotów z ew. awarii. 

      # uruchamianie
      $ make robot_test
 

testy obciążeniowe / performance test
-------------------------------------
Sprawdzają działnie/dostępniość aplikacji przy symulowanym ruchu użytkowników.
    
     # instalacja siege
     $ sudo apt install siege
     
     # uruchomienie 
     $ make test_siege


Monitoring
----------
Statuscake - administrator dostaje informację e-mail w momencie braku dostępności aplikacji i powrotu do działania z czasem trwania awarii. 
Gitlab - informacja e-mail w razie gdy bulid i deploy aplikacji nie przejdzie pomyślnie a także informacja gdy kolejny bulid i deploy przejdą pomyślnie.

Ponadto w kodzie aplikacjii zaimplemetnowana jest funkcja, która wysyła do administratora e-maila z logiem awarii, gdy strona odpowie na zapytanie użytkownika kodem HTTP - '500'.

# Testresultaten - ...

In dit document staan de verschillende resultaten van het testen van het prototype uitgewerkt.

Developer: Robin Bozan

Reviewer 1: Rahmat Syamsuddin

Reviewer 2: Sander Teunissen

## Accuraatheid

Onder het onderdeel accuraatheid zijn een aantal verschillende zaken van het prototype getest beteft de accuraatheid van de gemaakte voorspelling.

#### Dataset grootte

Het eerste onderdeel dat getest is, is de toename van de accuraatheid van het algoritme naarmate de hoeveelheid beschikbare trainingsdata groter wordt. Dit is getest door het prototype te trainen kleinere hoeveelheden data van de volledige dataset.

De onderstaande tabel bevat de waardes van de gemiddelde accuraatheids percentage van de applicatie die zijn gevonden door de applicatie te testen met de testdataset.

| Percentage data         | Developer | Reviewer 1 | Reviewer 2 |
| ----------------------- | --------- | ---------- | ---------- |
| **25% van de dataset**  | 76,67%    | 76,67%     | 76,67%     |
| **50% van de dataset**  | 80%       | 80,00%     | 80%        |
| **75% van de dataset**  | 83,33%    | 83,33%     | 83,33%     |
| **100% van de dataset** | 86,67%    | 86,67%     | 86,67%     |

#### Aantal ingevoerde symptomen

Naast de afhankelijkheid van de accuraatheid ten opzichte van de grootte van de dataset is ook de accuraatheid van het prototype getest ten opzichte van het aantal ingevoerde symptomen waarmee de voorspelling moet worden gedaan.

In de onderstaande tabellen staan de resultaten van de tests die zijn uitgevoerd om de accuraatheid te bepalen.

| 1 symptoom ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| -------------------- | --------------------- | ------------------ | ----------------- | ---------------------- | ------------------------------- |
| developer            | vrouw                 | 32                 | hoesten           | verkoudheid            | n (bronchitis)                  |
| developer            | man                   | 64                 | kortademig        | astma                  | j                               |
| developer            | vrouw                 | 63                 | koorts            | griep                  | j                               |
| developer            | man                   | 12                 | neusvleugelen     | longontsteking         | n (astma)                       |
| reviewer 1           | man                   | 23                 | spierpijn         | bronchitis             | n (verkoudheid)                 |
| reviewer 1           | vrouw                 | 23                 | spierpijn         | verkoudheid            | j                               |
| reviewer 1           | man                   | 18                 | hoesten           | longontsteking         | n (astma)                       |
| reviewer 1           | vrouw                 | 12                 | koorts            | verkoudheid            | n (bronchitis)                  |
| reviewer 2           | man                   | 42                 | Hoesten           | Verkoudheid            | n (astma)                       |
| reviewer 2           | vrouw                 | 36                 | Spierpijn         | Griep                  | n (bronchitis)                  |
| reviewer 2           | vrouw                 | 58                 | Kortademig        | Astma                  | j                               |
| reviewer 2           | man                   | 21                 | Verstopte neus    | Verkoudheid            | j                               |

| 2 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom               | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | ------------------------------- | ---------------------- | ------------------------------- |
| developer             | man                   | 33                 | hoesten, koorts                 | longontsteking         | n (bronchitis)                  |
| developer             | vrouw                 | 63                 | koorts, verstopte neus          | griep                  | j                               |
| developer             | man                   | 75                 | niezen, hoesten                 | verkoudheid            | n (astma)                       |
| developer             | vrouw                 | 21                 | koorts, kortademig              | longontsteking         | j                               |
| reviewer 1            | man                   | 33                 | spierpijn, koorts               | bronchitis             | j                               |
| reviewer 1            | man                   | 49                 | keelpijn, verstopte neus        | griep                  | j                               |
| reviewer 1            | vrouw                 | 12                 | koorst, keelpijn                | verkoudheid            | n (griep)                       |
| reviewer 1            | vrouw                 | 12                 | neusvleugelen, hoofdpijn        | longontsteking         | j                               |
| reviewer 2            | man                   | 9                  | Keelpijn, hoofdpijn             | griep                  | n (verkoudheid)                 |
| reviewer 2            | Vrouw                 | 19                 | Keelpijn,  Hoge slijmproductie  | longontsteking         | n (bronchitis)                  |
| reviewer 2            | man                   | 33                 | kortademig, piepende ademhaling | astma                  | j                               |
| reviewer 2            | vrouw                 | 64                 | Hoesten,  Hoge slijmproductie   | bronchitis             | j                               |

| 3 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                                     | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | ----------------------------------------------------- | ---------------------- | ------------------------------- |
| developer             | man                   | 53                 | hoesten, koorts, pijn bij borst                       | longontsteking         | j                               |
| developer             | vrouw                 | 64                 | hoesten, hoge slijmproductie, koorts                  | bronchitis             | j                               |
| developer             | man                   | 23                 | kortademig, benauwdheid, piepende ademhaling          | astma                  | j                               |
| developer             | man                   | 44                 | koorts, hoofdpijn, hoesten                            | griep                  | j                               |
| reviewer 1            | man                   | 16                 | gebrek aan eetlust, kortademig, koorts                | longontsteking         | j                               |
| reviewer 1            | man                   | 28                 | kortademig, benauwdheid, hoesten                      | astma                  | j                               |
| reviewer 1            | vrouw                 | 15                 | gebrek aan eetlust, spierpijn, koorts                 | verkoudheid            | n (griep)                       |
| reviewer 1            | vrouw                 | 55                 | verstopte neus, spierpijn, keelpijn, hoesten          | griep                  | j                               |
| reviewer 2            | man                   | 27                 | Hoesten,  Pijn bij borst,  Kortademig                 | Longontsteking         | N (Bronchitis)                  |
| reviewer 2            | man                   | 44                 | Hoesten, Keelpijn,  Hoge slijmproductie               | Bronchitis             | J                               |
| reviewer 2            | Vrouw                 | 25                 | Benauwdheid, Hoge slijmproductie, Piepende ademhaling | Bronchitis             | J                               |
| reviewer 2            | vrouw                 | 81                 | hoesten, niezen, spierpijn                            | verkoudheid            | j                               |

| 4 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                                        | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | -------------------------------------------------------- | ---------------------- | ------------------------------- |
| developer             | man                   | 63                 | kortademig, benauwdheid, hoesten, piepende ademhaling    | astma                  | j                               |
| developer             | man                   | 12                 | verstopte neus, spierpijn, keelpijn, hoesten, gebrek aan eetlust | griep          | n (verkoudheid)                 |
| developer             | vrouw                 | 32                 | pijn bij borst, hoofdpijn, vermoeidheid, gebrek aan eetlust | longontsteking      | j                               |
| developer             | vrouw                 | 44                 | hoesten, niezen, koorts, keelpijn                        | verkoudheid            | n (longontsteking)              |
| reviewer 1            | man               | 12                 | hoesten, niezen, spierpijn, hoofdpijn                    | verkoudheid            | j                               |
| reviewer 1            | man               | 34                 | gebrek aan eetlust, spierpijn, keelpijn, hoesten         | griep                  | j                               |
| reviewer 1            | vrouw              | 22                 | pijn bij borst, koorts, kortademig, gebrek aan eetlust   | benauwdheid            | n (longontsteking)              |
| reviewer 1            | vrouw              | 11                 | vermoeidheid, neusvleugelen, hoesten, gebrek aan eetlust | longontsteking         | j                               |
| reviewer 2            | vrouw | 55 | verstopte neus, vermoeidheid, koorts, keelpijn | verkoudheid | n (longontsteking) |
| reviewer 2            | vrouw | 15 | Hoesten,  Koorts, Gebrek aan eetlust, Niezen | Verkoudheid | J |
| reviewer 2            | man | 42 | Keelpijn, Hoofdpijn, Spierpijn,  Vermoeidheid | Griep | n (verkoudheid) |
| reviewer 2            | man | 33 | Benauwdheid,  Kortademig,  Hoesten,  Piepende ademhaling | Astma | j |

| 5 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                                                | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | ---------------------------------------------------------------- | ---------------------- | ------------------------------- |
| developer             | vrouw                 | 24                 | hoesten, hoge slijmproductie, piepende ademhaling, koorts, spierpijn | bronchitis         | j                               |
| developer             | man                   | 19                 | hoesten, koorts, kortademig, hoofdpijn, vermoeidheid             | longontsteking         | j                               |
| developer             | vrouw                 | 21                 | koorts, hoofdpijn, hoesten, keelpijn, spierpijn                  | griep                  | j                               |
| developer             | vrouw                 | 55                 | gebrek aan eetlust, koorts, keelpijn, hoesten, niezen            | verkoudheid            | n (griep)                       |
| reviewer 1            | man               | 14                 | koorts, hoofdpijn, verstopte neus, spierpijn, keelpijn           | griep                  | j                               |
| reviewer 1            | man               | 19                 | keelpijn, hoesten, hoofdpijn, niezen, spierpijn                  | benauwdheid            | n (verkoudheid)                 |
| reviewer 1            | vrouw              | 15                 | kortademig, benauwdheid, hoesten, piepende ademhaling, spierpijn | astma                  | j                               |
| reviewer 1            | vrouw              | 44                 | vermoeidheid, hoofdpijn, niezen, hoesten, verstopte neus         | verkoudheid            | j                               |
| reviewer 2            | vrouw | 89 | Keelpijn, Hoofdpijn, Spierpijn,  Vermoeidheid,  Verstopte Neus | griep | j |
| reviewer 2            | man | 59 | Hoesten, Koorts, Pijn bij borst, hoofdpijn, verstopte neus | longontsteking | j |
| reviewer 2            | vrouw | 26 | hoofdpijn, keelpijn, koorts, kortademig, Pijn bij borst | longontsteking | j |
| reviewer 2            | man | 47 | koorts, hoofdpijn, verstopte neus, hoge slijmproductie, keelpijn | bronchitis | n (griep) |

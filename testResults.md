# Testresultaten - ...

In dit document staan de verschillende resultaten van het testen van het prototype uitgewerkt.

Developer: Robin Bozan

Reviewer 1: Rahmat Syamsuddin

Reviewer 2:

## Accuraatheid

Onder het onderdeel accuraatheid zijn een aantal verschillende zaken van het prototype getest beteft de accuraatheid van de gemaakte voorspelling.

#### Dataset grootte

Het eerste onderdeel dat getest is, is de toename van de accuraatheid van het algoritme naarmate de hoeveelheid beschikbare trainingsdata groter wordt. Dit is getest door het prototype te trainen kleinere hoeveelheden data van de volledige dataset.

De onderstaande tabel bevat de waardes van de gemiddelde accuraatheids percentage van de applicatie die zijn gevonden door de applicatie te testen met de testdataset.

| Percentage data         | Developer | Reviewer 1 | Reviewer 2 |
| ----------------------- | --------- | ---------- | ---------- |
| **25% van de dataset**  |           | 76.67%     |            |
| **50% van de dataset**  |           | 80.00%     |            |
| **75% van de dataset**  |           | 83.33%     |            |
| **100% van de dataset** |           | 86.67%     |            |

#### Aantal ingevoerde symptomen

Naast de afhankelijkheid van de accuraatheid ten opzichte van de grootte van de dataset is ook de accuraatheid van het prototype getest ten opzichte van het aantal ingevoerde symptomen waarmee de voorspelling moet worden gedaan.

In de onderstaande tabellen staan de resultaten van de tests die zijn uitgevoerd om de accuraatheid te bepalen.

| 1 symptoom ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| -------------------- | --------------------- | ------------------ | ----------------- | ---------------------- | ------------------------------- |
| developer            | vrouw (0)             | 32                 | hoesten           | verkoudheid            | n (bronchitis)                  |
| developer            |                       |                    |                   |                        |                                 |
| developer            |                       |                    |                   |                        |                                 |
| developer            |                       |                    |                   |                        |                                 |
| reviewer 1           | man (1)               | 23                 | spierpijn         | bronchitis             | n (verkoudheid)                 |
| reviewer 1           | vrouw (0)             | 23                 | spierpijn         | verkoudheid            | j                               |
| reviewer 1           | man (1)               | 18                 | hoesten           | longontsteking         | n (astma)                       |
| reviewer 1           | vrouw (0)             | 12                 | koorts            | verkoudheid            | n (bronchitis)                  |
| reviewer 2           |                       |                    |                   |                        |                                 |
| reviewer 2           |                       |                    |                   |                        |                                 |
| reviewer 2           |                       |                    |                   |                        |                                 |
| reviewer 2           |                       |                    |                   |                        |                                 |

| 2 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom        | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | ------------------------ | ---------------------- | ------------------------------- |
| developer             |                       |                    |                          |                        |                                 |
| developer             |                       |                    |                          |                        |                                 |
| developer             |                       |                    |                          |                        |                                 |
| developer             |                       |                    |                          |                        |                                 |
| reviewer 1            | man (1)               | 33                 | spierpijn, koorts        | bronchitis             | j                               |
| reviewer 1            | man (1)               | 49                 | keelpijn, verstopte neus | griep                  | j                               |
| reviewer 1            | vrouw (0)             | 12                 | koorst, keelpijn         | verkoudheid            | n (griep)                       |
| reviewer 1            | vrouw (0)             | 12                 | neusvleugelen, hoofdpijn | longontsteking         | j                               |
| reviewer 2            |                       |                    |                          |                        |                                 |
| reviewer 2            |                       |                    |                          |                        |                                 |
| reviewer 2            |                       |                    |                          |                        |                                 |
| reviewer 2            |                       |                    |                          |                        |                                 |

| 3 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                            | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | -------------------------------------------- | ---------------------- | ------------------------------- |
| developer             |                       |                    |                                              |                        |                                 |
| developer             |                       |                    |                                              |                        |                                 |
| developer             |                       |                    |                                              |                        |                                 |
| developer             |                       |                    |                                              |                        |                                 |
| reviewer 1            | man (1)               | 16                 | gebrek aan eetlust, kortademig, koorts       | longontsteking         | j                               |
| reviewer 1            | man (1)               | 28                 | kortademig, benauwdheid, hoesten             | astma                  | j                               |
| reviewer 1            | vrouw(0)              | 15                 | gebrek aan eetlust, spierpijn, koorts        | verkoudheid            | n (griep)                       |
| reviewer 1            | vrouw (0)             | 55                 | verstopte neus, spierpijn, keelpijn, hoesten | griep                  | j                               |
| reviewer 2            |                       |                    |                                              |                        |                                 |
| reviewer 2            |                       |                    |                                              |                        |                                 |
| reviewer 2            |                       |                    |                                              |                        |                                 |
| reviewer 2            |                       |                    |                                              |                        |                                 |

| 4 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                                        | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | -------------------------------------------------------- | ---------------------- | ------------------------------- |
| developer             |                       |                    |                                                          |                        |                                 |
| developer             |                       |                    |                                                          |                        |                                 |
| developer             |                       |                    |                                                          |                        |                                 |
| developer             |                       |                    |                                                          |                        |                                 |
| reviewer 1            | man (1)               | 12                 | hoesten, niezen, spierpijn, hoofdpijn                    | verkoudheid            | j                               |
| reviewer 1            | man (1)               | 34                 | gebrek aan eetlust, spierpijn, keelpijn, hoesten         | griep                  | j                               |
| reviewer 1            | vrouw(0)              | 22                 | pijn bij borst, koorts, kortademig, gebrek aan eetlust   | benauwdheid            | n (longontsteking)              |
| reviewer 1            | vrouw(0)              | 11                 | vermoeidheid, neusvleugelen, hoesten, gebrek aan eetlust | longontsteking         | j                               |
| reviewer 2            |                       |                    |                                                          |                        |                                 |
| reviewer 2            |                       |                    |                                                          |                        |                                 |
| reviewer 2            |                       |                    |                                                          |                        |                                 |
| reviewer 2            |                       |                    |                                                          |                        |                                 |

| 5 symptomen ingevoerd | **Gebruikt geslacht** | Gebruikte leeftijd | Gebruikt symptoom                                                | Verwachte voorspelling | **Correcte voorspelling (j/n)** |
| --------------------- | --------------------- | ------------------ | ---------------------------------------------------------------- | ---------------------- | ------------------------------- |
| developer             |                       |                    |                                                                  |                        |                                 |
| developer             |                       |                    |                                                                  |                        |                                 |
| developer             |                       |                    |                                                                  |                        |                                 |
| developer             |                       |                    |                                                                  |                        |                                 |
| reviewer 1            | man (1)               | 14                 | koorts, hoofdpijn, verstopte neus, spierpijn, keelpijn           | griep                  | j                               |
| reviewer 1            | man (1)               | 19                 | keelpijn, hoesten, hoofdpijn, niezen, spierpijn                  | benauwdheid            | n (verkoudheid)                 |
| reviewer 1            | vrouw(0)              | 15                 | kortademig, benauwdheid, hoesten, piepende ademhaling, spierpijn | astma                  | j                               |
| reviewer 1            | vrouw(0)              | 44                 | vermoeidheid, hoofdpijn, niezen, hoesten, verstopte neus         | verkoudheid            | j                               |
| reviewer 2            |                       |                    |                                                                  |                        |                                 |
| reviewer 2            |                       |                    |                                                                  |                        |                                 |
| reviewer 2            |                       |                    |                                                                  |                        |                                 |
| reviewer 2            |                       |                    |                                                                  |                        |                                 |

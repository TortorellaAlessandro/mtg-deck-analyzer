# MTG Deck Analyzer

Un tool scritto in **Python** per analizzare mazzi di **Magic: The Gathering**, con statistiche e grafici generati automaticamente usando le API di [Scryfall](https://scryfall.com/docs/api).

## Funzionalità:

- Caricamento di un mazzo da file `.txt` o mediante copia incolla della lista
- Recupero automatico delle informazioni delle carte da **Scryfall API**
- Analisi della curva di mana
- Distribuzione dei colori nel mazzo
- Distribuzione card types presenti nel mazzo
- Distribuzione delle stat delle creature presenti
- Cache locale delle carte (per evitare troppe chiamate all’API)
- Visualizzazione grafica

## Installazione:

Clona la repo e installa i pacchetti richiesti:

'''bash
git clone https://github.com/TortorellaAlessandro/mtg-deck-analyzer.git
cd mtg-deck-analyzer
pip install -r requirements.txt

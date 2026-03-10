
# Automatische Bildklassifikation von Haushaltsabfällen im Rahmen einer fiktiven Non-Profit-Organisation

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Deep-Learning-Projekt zur Klassifikation von Haushaltsabfällen anhand eines Bilderdatensatzes, um ein KI-Assistenzsystem für die automatische Sortierung auf einem Recyclinghof zu entwickeln.

## Features

- Bildbasierte Klassifikation von Müllobjekten (z.B. Papier, Plastik, Metall, Glas, Restmüll)
- Trainingsskripte für ein Deep-Learning-Modell
- Stratifizierter Train/Validation/Test Split (60/20/20)
- Evaluierung der Modellgüte mit Gesamt-Accuracy, Macro-F1-Score und F1-Score je Klasse

## Installation

```bash
git clone git@github.com:vegedy/Wiederwerte.git
cd Wiederwerte
python -m venv .venv
source .venv/bin/activate  # unter Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Dieses Projekt lädt [Mostafa Mohameds](https://www.kaggle.com/mostafaabla) [Garbage Classification](https://www.kaggle.com/datasets/mostafaabla/garbage-classification) Datensatz von Kaggle, lizenziert unter Open Database License (ODbL) 1.0 – Contents: © Original Authors. Siehe http://opendatacommons.org/licenses/odbl/1.0/.


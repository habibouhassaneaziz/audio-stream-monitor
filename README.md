# Audio Stream Monitor – Python

Simulation d'un flux audio en UDP inspiré des protocoles broadcast (RTP/AES67).

## Comment ça marche
1. `python receiver.py` — met en écoute
2. `python sender.py` — envoie les paquets audio
3. `python metrics.py` — affiche les métriques réseau

## Technologies
- Python, UDP, socket
- Inspiré de AES67 et RTP broadcast

## Résultats
- 44 paquets envoyés et reçus
- 0% de perte sur réseau local

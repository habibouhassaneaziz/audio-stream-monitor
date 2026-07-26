def calculate_loss(sent, received):
    if sent == 0:
        return 0
    loss = ((sent - received) / sent) * 100
    print(f"Paquets envoyés : {sent}")
    print(f"Paquets reçus : {received}")
    print(f"Perte de paquets : {loss:.2f}%")
    return loss

# Exemple
calculate_loss(100, 95)
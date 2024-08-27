python
import matplotlib.pyplot as plt
import deepxde as dde

def plot_pinn_training(losshistory, train_state):
    # Visualize loss history
    plt.figure(figsize=(10, 6))
    plt.plot(losshistory.steps, losshistory.loss_train, label='Training loss')
    plt.plot(losshistory.steps, losshistory.loss_test, label='Test loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

# Eksempel på hvordan du kan kalle funksjonen etter å ha trent modellen
# plot_pinn_training(losshistory, train_state)
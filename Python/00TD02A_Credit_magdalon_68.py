python
trafikk_modell = Sinusfunksjon(amplitude=100, periode=24, faseforskyvning=6, likevektslinje=200)

t = np.linspace(0, 48, 100)  # Simulerer trafikk over 48 timer
plt.plot(t, trafikk_modell(t))
plt.xlabel("Tid (timer)")
plt.ylabel("Trafikk (kbps)")
plt.title("Modellert nettverkstrafikk")
plt.grid(True)
plt.show()
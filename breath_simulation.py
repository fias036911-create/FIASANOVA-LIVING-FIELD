import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def breath_dynamics(S, t, Phi=0.0, alpha=1.0, beta=0.05, gamma=1.0,
                    delta=1.186, epsilon=1.0, zeta=0.05, omega=2*np.pi*0.183):
    """
    Breath dynamics system with coupled oscillations.
    
    States:
        I: Inhale amplitude
        P: Process (intermediate) amplitude
        E: Exhale amplitude
    """
    I, P, E = S
    dI = alpha * (E - I) - beta * Phi * I
    dP = gamma * (I - P) + delta * np.sin(omega * t) * P
    dE = epsilon * (P - E) - zeta * Phi * E
    return [dI, dP, dE]


if __name__ == "__main__":
    # Time span: 20 full breath cycles
    period = 2 * np.pi / (2 * np.pi * 0.183)   # one cycle length
    t = np.linspace(0, 20 * period, 2000)      # many points for smooth curve

    # Starting values (small numbers to begin)
    S0 = [0.1, 0.05, 0.08]

    # Run simulation - Resonant case (perfect breathing, Phi=0)
    sol_res = odeint(breath_dynamics, S0, t, args=(0.0,))

    # Quick text summary (since we can't always see plots right away)
    print("Resonant breathing - last few values:")
    print("Time (last 5):", t[-5:])
    print("Inhale I:", sol_res[-5:, 0])
    print("Process P:", sol_res[-5:, 1])
    print("Exhale E:", sol_res[-5:, 2])

    # Plot the curves
    plt.figure(figsize=(10, 6))
    plt.plot(t, sol_res[:, 0], label='Inhale (I)', linewidth=2)
    plt.plot(t, sol_res[:, 1], label='Process (P)', linewidth=2)
    plt.plot(t, sol_res[:, 2], label='Exhale (E)', linewidth=2)
    plt.xlabel('Time (seconds)')
    plt.ylabel('State amplitude')
    plt.title('Breath Protocol - Resonant Case (Sustained Breathing)')
    plt.legend()
    plt.grid(True)
    plt.show()
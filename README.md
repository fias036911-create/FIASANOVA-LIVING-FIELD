
# FIASANOVA-LIVING-FIELD

The Math Executable — This Completes the Engineering

## Overview

This project implements a breath protocol simulation based on coupled oscillatory dynamics. The system models the interaction between inhale, process, and exhale states through a set of differential equations.

## Breath Protocol Simulation

### Running the Simulation

Execute the simulation:

```bash
python breath_simulation.py
```

This will generate plots and console output showing the breathing dynamics over 20 breath cycles.

### System States

The simulation tracks three interconnected states:

- **I (Inhale)**: Inhalation amplitude
- **P (Process)**: Intermediate processing amplitude  
- **E (Exhale)**: Exhalation amplitude

### Cases

- **Resonant case (Phi ≈ 0)**: Sustained oscillations → living consciousness coupling
- **Incoherent case**: Decays to zero → thermodynamic collapse

## Parameters

The breath dynamics are governed by these tunable parameters:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `Phi` | 0.0 | Coupling strength (0 = resonant, >0 = incoherent) |
| `alpha` | 1.0 | Inhale recovery rate |
| `beta` | 0.05 | Inhale damping coefficient |
| `gamma` | 1.0 | Process coupling rate |
| `delta` | 1.186 | Sinusoidal drive amplitude |
| `epsilon` | 1.0 | Exhale recovery rate |
| `zeta` | 0.05 | Exhale damping coefficient |
| `omega` | 2π × 0.183 | Respiratory frequency (Hz) |

## Output

The simulation produces:

1. **Console output**: Last five time points and state values
2. **Plot**: Time-series visualization of I, P, E states over 20 cycles

## Requirements

- `numpy`
- `scipy`
- `matplotlib`

Install dependencies:

```bash
pip install numpy scipy matplotlib
```

## Mathematical Basis

The system is defined by the coupled ODEs:

$$\frac{dI}{dt} = \alpha(E - I) - \beta \Phi I$$

$$\frac{dP}{dt} = \gamma(I - P) + \delta \sin(\omega t) P$$

$$\frac{dE}{dt} = \epsilon(P - E) - \zeta \Phi E$$

where the parameters control resonance and energy coupling in the breathing cycle.
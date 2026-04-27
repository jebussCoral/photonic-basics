# Photonic Basics

This repository documents a step-by-step learning process in integrated photonics, moving from ideal physical models to realistic computational behavior.

The objective is to understand how photonic systems perform computation under real-world constraints such as loss and noise.

---

# Day 1 — Ideal Mach-Zehnder Interferometer (MZI)

We implemented an ideal MZI based on optical interference:

E_out = E1 + E2 · exp(i·phi)  
I_out = |E_out|²  

## Key Concepts

- Optical field vs optical power  
- Phase difference (phi)  
- Constructive and destructive interference  
- Perfect extinction (ideal cancellation)  

## Results

- Maximum intensity at phi = 0  
- Minimum intensity at phi = pi  
- Periodicity of 2π  

In the ideal case:
- Equal amplitudes  
- Perfect phase opposition → complete cancellation  

---

# Day 2 — Lossy Mach-Zehnder Interferometer

We extended the model to include realistic losses:

E1 = sqrt(P1) · alpha1  
E2 = sqrt(P2) · alpha2  

Where alpha is the field transmission factor of each arm.

## Physical Meaning of Alpha

- alpha = 1 → no loss  
- alpha < 1 → attenuation of the optical field  

Important: losses affect the **field**, not directly the intensity.

---

## Observations

- Perfect cancellation is no longer achieved  
- Minimum intensity increases (I_min > 0)  
- Maximum intensity decreases  

---

## Key Insight

The system loses balance:

E1 ≠ E2 → incomplete destructive interference  

---

## Separation Between Logical States

Define:

Δ = I_max - I_min  

This separation determines how distinguishable the logical states are.

---

## Extinction Ratio

ER = 10 · log10(I_max / I_min)

- High ER → good contrast  
- Low ER → poor contrast  

---

## Decision Threshold

T = (I_max + I_min) / 2  

- I > T → logical 1  
- I < T → logical 0  

---

## Engineering Rule

- I_min < 0.1 · I_max → acceptable  
- I_min ≈ I_max → system not usable  

---

# Day 3 — Noise and Error Probability

We introduced measurement noise to simulate realistic system behavior:

I_measured = I_real + noise  

Where noise follows a Gaussian distribution:

noise ~ N(0, σ)

---

## Key Change in Perspective

Previous days:

```text
Input (phase) → Output (intensity)
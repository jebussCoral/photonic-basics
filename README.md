# Photonic Basics

This repository documents a step-by-step learning process in integrated photonics, starting from fundamental optical models to more advanced computational architectures.

The goal is to build physical intuition and engineering criteria for designing photonic systems.

---

# Day 1 — Ideal Mach-Zehnder Interferometer (MZI)

We implemented an ideal MZI model based on optical interference:

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

Where alpha represents the transmission factor of each arm.

## Physical Meaning of Alpha

- alpha = 1 → no loss  
- alpha < 1 → attenuation of the optical field  

Important: losses affect the **field**, not directly the intensity.

---

## Observations

Even with correct phase (phi = pi):

- Perfect cancellation no longer occurs  
- Minimum intensity is greater than zero  
- Maximum intensity is reduced  

---

## Key Insight

The system no longer satisfies the balance condition:

E1 = E2

Therefore:

E1 - E2 ≠ 0 → incomplete destructive interference

---

# Extinction Ratio and System Usability

In real systems, logic is not determined by absolute values (0 or 1), but by **separation between states**.

## Definitions

Let:

- I_max → maximum output intensity  
- I_min → minimum output intensity  

### Separation

Δ = I_max - I_min  

Larger Δ → better distinction between logical states

---

### Extinction Ratio (ER)

ER = 10 · log10(I_max / I_min)

- High ER → good contrast  
- Low ER → poor contrast  

---

## Decision Threshold

A practical threshold can be defined as:

T = (I_max + I_min) / 2  

Then:

- I > T → logical 1  
- I < T → logical 0  

---

## When is the system usable?

A system is usable when:

(I_max - I_min) >> noise

or equivalently:

I_min is sufficiently smaller than I_max

---

## Engineering Rule of Thumb

- I_min < 0.1 · I_max → acceptable  
- I_min ≈ I_max → not usable  

---

## Critical Insight

The limitation is not that I_min ≠ 0  

The real limitation is:

lack of separation between states

---

# Repository Structure

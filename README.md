# Photonic Basics

This repository documents a step-by-step learning process in integrated photonics, evolving from basic physical models to realistic computational systems.

The objective is to understand how photonic devices perform computation under real-world constraints such as loss and noise.

---

# Day 1 — Ideal Mach-Zehnder Interferometer (MZI)

The MZI is modeled using optical interference:

E_out = E1 + E2 · exp(i·φ)  
I_out = |E_out|²  

## Complex Representation of Optical Fields

Using Euler’s formula:

exp(iφ) = cos(φ) + i·sin(φ)

An optical field is a complex quantity:
- cos(φ) → real component  
- sin(φ) → imaginary component  

## Key Physical Cases

φ = 0:

exp(i·0) = 1  
→ constructive interference  
→ maximum intensity  

φ = π:

exp(i·π) = -1  
→ destructive interference  
→ minimum intensity  

## Results

- Maximum intensity at φ = 0  
- Minimum intensity at φ = π  
- Periodicity of 2π  

In the ideal case:
- E1 = E2  
- Perfect cancellation occurs at φ = π  

---

# Day 2 — Lossy Mach-Zehnder Interferometer

We introduce losses:

E1 = sqrt(P1) · α1  
E2 = sqrt(P2) · α2  

Where α is the field transmission factor.

## Interpretation

- α = 1 → no loss  
- α < 1 → attenuation  

Important:
Loss affects the **field**, not directly the intensity.

## Effect of Loss

When α1 ≠ α2:
- imbalance between arms  
- incomplete cancellation  
- I_min > 0  
- I_max decreases  

## Separation Between States

Δ = I_max - I_min  

## Extinction Ratio

ER = 10 log10(I_max / I_min)

## Decision Threshold

T = (I_max + I_min) / 2  

---

# Day 3 — Noise and Statistical Behavior

Real systems include noise:

I_measured = I_real + noise  
noise ~ N(0, σ)

## Key Concept Change

Instead of deterministic outputs:

Input → Output  

we now have:

Same input → distribution of outputs  

## Logical States Under Noise

- Logical 0 → distribution around I_min  
- Logical 1 → distribution around I_max  

## Error Mechanism

Errors occur when distributions overlap:
- false positive  
- false negative  

## Role of Noise

- small σ → low error  
- large σ → high error  

## Role of Loss

Loss reduces Δ → increases sensitivity to noise  

---

# Day 4 — Photonic Logic (Part 1: Ideal XOR)

## Bit Encoding (Phase Encoding)

- 0 → φ = 0  
- 1 → φ = π  

## Phase Difference

Δφ = φ1 - φ2  

## Interference Behavior

- Δφ = 0 → constructive → high output  
- Δφ = π → destructive → low output  

## Logical Mapping (Physical)

| A | B | Output |
|---|---|--------|
| 0 | 0 | High   |
| 1 | 1 | High   |
| 0 | 1 | Low    |
| 1 | 0 | Low    |

This is:

XNOR (natural behavior of MZI)

## XOR Construction

XOR = NOT(XNOR)

Steps:
1. Normalize intensity (divide by max)
2. Invert

Important insight:

Photonic logic is not explicitly programmed  
It **emerges from interference**

---

# Day 4 — Photonic Logic (Part 2: Realistic XOR)

Now we include real-world effects:

- α → loss  
- σ → noise  

Output becomes continuous, not binary.

## Statistical Modeling

We define:

μ0 → mean output for logical 0  
μ1 → mean output for logical 1  

Δ = μ1 - μ0  

Threshold:

T = (μ0 + μ1) / 2  

Decision:

- output > T → 1  
- output < T → 0  

## Error Rate

Error rate = incorrect / total  

---

# Core Design Principle

System reliability depends on:

Δ / σ

## Interpretation

- Δ/σ > 10 → very robust  
- Δ/σ ≈ 5 → acceptable  
- Δ/σ ≈ 2–3 → unstable  
- Δ/σ < 1 → unusable  

---

# Key Insight (Day 4)

- Loss reduces Δ  
- Noise spreads distributions  
- Error appears when Δ ≈ σ  

---

# Engineering Meaning

A photonic logic gate:

- is not deterministic  
- behaves as a probabilistic classifier  

---

# Design Strategy

To reduce error:

- increase α → reduce losses, balance arms  
- decrease σ → better detection, stable source  
- maximize Δ/σ  

---

---

# Day 5 — Cascaded Photonic Logic

In Day 5, we moved from a single photonic logic gate to a small circuit composed of two XOR gates in cascade.

The objective was to understand how error propagates when multiple photonic logic operations are connected sequentially.

---

## Circuit Structure

The simulated circuit is:

C = A XOR B  
D = C XOR E  

or equivalently:

D = (A XOR B) XOR E  

This creates a two-stage logic system:

```text
A ──┐
    ├── XOR1 ── C ──┐
B ──┘               ├── XOR2 ── D
E ──────────────────┘
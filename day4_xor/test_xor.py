from xor_mzi import xnor_mzi, xor_mzi


inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]

print("A B → XNOR intensity → XOR")

for A, B in inputs:
    xnor_intensity = xnor_mzi(A, B)
    xor_output = xor_mzi(A, B)

    print(A, B, "→", round(xnor_intensity, 3), "→", round(xor_output, 3))
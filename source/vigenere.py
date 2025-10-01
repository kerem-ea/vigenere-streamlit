import streamlit as st

st.title("📖 Vigenère-kryptering - Matematikken")

st.markdown(r"""
Vigenère-kryptering tildeler hvert bogstav et tal:  
$$
\begin{aligned}
A &= 0 \\ B &= 1 \\ C &= 2 \\ &\vdots \\ Å &= 28
\end{aligned}
$$
Krypteringsfunktionen: $C_i = (M_i + K_{(i \bmod m)}) \bmod 29$  
Dekrypteringsfunktionen: $M_i = (C_i - K_{(i \bmod m)}) \bmod 29$
""")

# Prefilled key and message
key = st.text_input("Nøgle", value="PROGRAMMERING")
message = st.text_area("Besked", value="SUKKERTOPPEN")
mode = st.radio("Vælg handling", ["encrypt", "decrypt"])
st.write("---")

def vigenere_cipher(message, key, mode="encrypt"):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
    letter_to_num = {c:i for i,c in enumerate(alphabet)} 
    num_to_letter = {i:c for i,c in enumerate(alphabet)}
    n = len(alphabet)
    
    message = "".join(ch for ch in message.upper() if ch in letter_to_num)
    key = "".join(ch for ch in key.upper() if ch in letter_to_num)
    if not message or not key: return ""
    
    result = [
        num_to_letter[(letter_to_num[m] + letter_to_num[key[i%len(key)]]) % n] 
        if mode=="encrypt" else 
        num_to_letter[(letter_to_num[m] - letter_to_num[key[i%len(key)]]) % n]
        for i,m in enumerate(message)
    ]
    return "".join(result)

if key and message:
    st.subheader("Resultat")
    st.write(vigenere_cipher(message, key, mode))

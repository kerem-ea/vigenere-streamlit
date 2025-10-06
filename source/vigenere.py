import streamlit as st

st.title("Matematik bag Vigenere-kryptering")

st.markdown(r"""
Vigenère-kryptering tildeler hvert bogstav et tal:  
$$
\begin{aligned}
A &= 0 \\ B &= 1 \\ C &= 2 \\ &\vdots \\ Å &= 28
\end{aligned}
$$

Krypteringsfunktionen:  
$$
C_i = (M_i + K_{(i \bmod m)}) \bmod 29
$$

Dekrypteringsfunktionen:  
$$
M_i = (C_i - K_{(i \bmod m)}) \bmod 29
$$ 

29 er længden af det danske alfabet.

Her er:  
- $M_i$ den numeriske værdi af det $i$-te bogstav i originalbeskeden.  
- $K$ er nøglen, som består af en sekvens af bostaver (der er oversat til tal).  
- $m$ er længden af nøglen $K$.  
- $C_i$ er den numeriske værdi af det krypterede $i$-te bogstav (chifferteksten).  

$K_{(i \bmod m)}$ betyder, at nøglen gentages gennem beskeden, hvis den er kortere end beskedens længde.
""")

# Prefilled key og message
key = st.text_input("Nøgle", value="PROGRAMMERING")
message = st.text_area("Besked", value="SUKKERTOPPEN")
mode = st.radio("Vælg handling", ["encrypt", "decrypt"])
st.write("---")

def vigenere_cipher(message, key, mode="encrypt"):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
    letter_to_num = {char: idx for idx, char in enumerate(alphabet)}  # Bogstav -> Tal
    num_to_letter = {idx: char for idx, char in enumerate(alphabet)}  # Tal -> Bogstav
    
    n = len(alphabet)  # Størrelse af alfabetet (29)
    
    # Rens beskeden og nøglen (Fjern tegn som ikke findes i alfabetet og sæt til store bogstaver)
    clean_message = "".join(ch for ch in message.upper() if ch in letter_to_num)
    clean_key = "".join(ch for ch in key.upper() if ch in letter_to_num)
    
    # Hvis besked eller nøgle er tomme efter rensning, returner tom streng
    if not clean_message or not clean_key:
        return ""
    
    result = []
    
    # Gennemgå hvert bogstav i beskeden sammen med dens indeks
    for i, char in enumerate(clean_message):
        message_num = letter_to_num[char]  # Talværdi for beskedbogstav
        key_num = letter_to_num[clean_key[i % len(clean_key)]]  # Talværdi for nøglebogstav 
        
        if mode == "encrypt":
            # Kryptering (læg talværdier sammen modulo alfabetets størrelse)
            cipher_num = (message_num + key_num) % n
        else:
            # Dekryptering (træk nøglens talværdi fra beskedens talværdi modulo alfabetets størrelse)
            cipher_num = (message_num - key_num) % n
        
        # Konverter tal tilbage til bogstav og tilføj til resultat
        result.append(num_to_letter[cipher_num])
    
    # Sammensæt resultatlisten til en streng og returner
    return "".join(result)

if key and message: # Hvis key og message er givet
    st.subheader("Resultat")
    st.write(vigenere_cipher(message, key, mode))

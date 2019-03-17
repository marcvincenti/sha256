# SHA-256

This repo aim to be a cryptanalysis of SHA-2 using the PCP theorem.  

The basic idea is to use the PCP theorem to prove that there are some bits
combinations wich prevent to solve the SHA-2 function.  

However, at this point, we are using an ersatz of the karloff-zwick algorithm to
determine some bits (but without any advantage).

### Minimum digests :

 + Without prefix & a 1 byte nonce (max=7) :
 `[10] -> 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b`

 + Without prefix & a 2 bytes nonce (max=15) :
 `[207, 102] -> 0001098c33b66779505bc2e3b14d50c818e2abf25c99afa5194f954b07a454cf`

 + Without prefix & a 3 bytes nonce (max=23) :
 `[192, 126, 158] -> 00000176a5edb8cf94b99cfab18e92f2ceb5c0d8acff8b5fa2f0b570c6a936c3`

 + Without prefix & a 4 bytes nonce (max=31) :
 `[93, 130, 40, 90] -> 00000001c3f27bca3121f0560c25a022ac5020a9e8b83c874357a01e33a5a9c3`

 + With prefix **0xDEADBEEF** & a 1 byte nonce (max=7) :
 `[158] -> 010c3aec44f423fdcafd8e424a1cbd5841ef4ae99aa6fb31cd1c22512789dba1`

 + With prefix **0xDEADBEEF** & a 2 byte nonce (max=15) :
 `[197, 220] -> 0001818077937da851ee6996d8aaf1a3e4ff0fc2e3c50a5a80a3f9f1d3e92832`

 + With prefix **0xDEADBEEF** & a 3 byte nonce (max=23) :
 `[14, 48, 172] -> 000001c8b9dfcaf59a9107651f4740c12335392a80e684f18c508ba44bbca0a4`

 + With prefix **0xDEADBEEF** & a 4 byte nonce (max=32) :
 `[83, 45, 4, 233] -> 00000000e7af12ee7745c91e893cab85f33d48d8fd7f9806f8448688c7f39bd4`

 + With prefix **0xC0FFEE** & a 1 byte nonce (max=7) :
 `[143] -> 018564ed0c0f7b0be0ed51b3763c1bf8db120a99b89ee3337632bc8e87661657`

 + With prefix **0xC0FFEE** & a 2 byte nonce (max=16) :
 `[229, 247] -> 0000c1e5281ad54f1e63a4bace0394e857f2713901f3adb6af7a6fe0136974e0`

 + With prefix **0xC0FFEE** & a 3 byte nonce (max=30) :
 `[83, 109, 175] -> 000000038103dc50eecd9b439c3af66d1d949a2063a4364a59469caa59918b9a`

 + With prefix **0xC0FFEE** & a 4 byte nonce (max=32) :
 `[250, 144, 203, 120] -> 00000000f9312abca0741d04db30521c34bc60bba71d8c5dd0e2a64cf992dfa7`

 + With prefix **0xBADF00D** & a 1 byte nonce (max=12) :
 `[24] -> 000e59f85471c65f5a2c58516ceb81bb339e489dbe5173d342efe757a24558b8`

 + With prefix **0xBADF00D** & a 2 byte nonce (max=15) :
 `[235, 48] -> 0001bbe1b8101a4e7cfd3502368abb1ebf1baaf4e74ebbdac0e54aab6060bfff`

 + With prefix **0xBADF00D** & a 3 byte nonce (max=22) :
 `[203, 72, 52] -> 00000341c6b3244ba3ba08ea1aa10e503291645792c9e885d0de3984feeb4de5`

 + With prefix **0xBADF00D** & a 4 byte nonce (max=32) :
 `[64, 213, 255, 172] -> 00000000cce6a2ff9720c5375e6507f6fa7ddf0d3b35fad5b0146b274d83944e`

 + With prefix **0xFEEDC0DE** & a 1 byte nonce (max=8) :
 `[202] -> 00c370d81b3238cc7ca698881ff7ef2cd3b4f47b4361c8a8f527ed61104ee05c`

 + With prefix **0xFEEDC0DE** & a 2 byte nonce (max=17) :
 `[244, 151] -> 00004833e6b3db232c922ab00f21173996571b57b4ef4c4714ad38bfd8a80003`

 + With prefix **0xFEEDC0DE** & a 3 byte nonce (max=23) :
 `[218, 8, 169] -> 00000122f7cda0fa552342f8762b2a581c18937afa274ba4a9c35fe9f218c1ef`

 + With prefix **0xFEEDC0DE** & a 4 byte nonce (max=30) :
 `[220, 162, 208, 234] -> 00000002ddac21e509fe8cfc7a3118201e048caecdc66145b034014931f01881`

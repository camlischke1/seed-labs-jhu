# seed-labs-jhu
Records & Reports for Seedlabs (https://seedsecuritylabs.org/) on Ubuntu 16.04

---

---

## References

Du, W. (2019). [*Computer & Internet Security: A Hands-on Approach.*](https://www.handsonsecurity.net/) Wenliang Du.

Export `bibtex` as:

```bibtex
@book{du2019computer,
  title={Computer \& Internet Security: A Hands-on Approach},
  author={Du, W.},
  isbn={9781733003933},
  url={https://books.google.com/books?id=HclQxQEACAAJ},
  year={2019},
  publisher={Wenliang Du}
}
```

Besides,

### Thanks to

- Some code from the seed book: https://github.com/kevin-w-du/BookCode
- Figures in the seed book: https://www.handsonsecurity.net/files/misc/SEEDBook_figs_2nd.pdf 

---

## To-do List

Ref: http://www.cis.syr.edu/~wedu/seed/toc.pdf

- [ ] Software Security
    - [x] [Buffer Overflow Vulnerability Lab](./BufferOverflow)
    - [x] [Return-to-libc Attack Lab](./ReturnToLibc)
    - [ ] Format String Vulnerability Lab()
    - [ ] Race Condition Vulnerability Lab()
    - [x] [Environment Variable and Set-UID Lab](./Env-SetUID)
    - [x] [Shellshock Attack Lab](./Shellshock)
    - [ ] *Dirty COW Attack Lab*
- [ ] *Web Security (deprecated, just used to test `snort`)*
    - [ ] Cross-Site Request Forgery Attack Lab( )
    - [x] [Cross-Site Scripting Attack Lab](./Cross-Site-Scripting-Attack)
    - [x] [SQL Injection Attack Lab](./SQL-Injection-Attack)
- [ ] Network Security
    - [ ] Packet Sniffing & Spoofing Lab( )
    - [x] [TCP Attack Lab](./TCP-IP)
    - [x] [Linux Firewall Lab](./Firewall)
    - [ ] Bypassing Firewall using VPN( )
    - [x] [Local DNS Attack Lab](./LocalDNS)
    - [x] [Remote DNS Cache Poisoning Attack Lab](./RemoteDNS)
    - [ ] *Heartbleed Attack Lab (only for Ubuntu 12.04)*( )
    - [ ] VPN Lab
- [ ] Crypto
    - [x]  [Secret-Key Encryption Lab](./Secret-Key-Encryption)
    - [x]  [Pseudo Random Number Generation Lab](./Pseudo-Random-Number-Generation)
    - [ ]  MD5 Collision Attack Lab( )
    - [ ]  RSA Encryption and Signature Lab( )
    - [x]  Public-Key Infrastructure (PKI) Lab(./PKI)
    - [ ]  Hash Length Extension Attack Lab]( )  (*Azure Ubuntu 20.4*)
    - [ ]  Transport Layer Security (TLS) Lab( ) (*Azure Ubuntu 20.4*)
- [x] System Security
    - [ ] Meltdown Attack Lab( )
    - [ ] Spectre Attack Lab( )
- [ ] Mobile Security
    - [ ] Android Repackaging Attack Lab
    - [ ] Android Rooting Lab
    - [ ] Android ClickJacking Attack Lab

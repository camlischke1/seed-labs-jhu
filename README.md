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
    - [x] [Buffer Overflow Vulnerability Lab](./Buffer-Overflow)
    - [x] [Return-to-libc Attack Lab](./Return-to-libc-Attack)
    - [ ] [Format String Vulnerability Lab](./Format-String-Vulnerability)
    - [ ] [Race Condition Vulnerability Lab](./Race-Condition-Vulnerability)
    - [x] [Environment Variable and Set-UID Lab](Environment-Variable-and-Set-UID-Program-Lab)
    - [x] [Shellshock Attack Lab](./Shellshock-Attack)
    - [ ] *Dirty COW Attack Lab*
- [ ] *Web Security (deprecated, just used to test `snort`)*
    - [x] [Cross-Site Request Forgery Attack Lab](./Cross-Site-Request-Forgery)
    - [x] [Cross-Site Scripting Attack Lab](./Cross-Site-Scripting-Attack)
    - [x] [SQL Injection Attack Lab](./SQL-Injection-Attack)
- [ ] Network Security
    - [x] [Packet Sniffing & Spoofing Lab](./Packet-Sniffing-and-Spoofing)
    - [x] [TCP Attack Lab](./TCP-IP-Attack)
    - [x] [Linux Firewall Lab](./Firewall-Exploration)
    - [ ] [Bypassing Firewall using VPN](./Firewall-VPN)
    - [x] Local DNS Attack Lab
    - [x] Remote DNS Cache Poisoning Attack Lab
    - [ ] [*Heartbleed Attack Lab (only for Ubuntu 12.04)*](./Heartbleed-Attack)
    - [ ] VPN Lab
- [ ] Crypto
    - [x]  [Secret-Key Encryption Lab](./Secret-Key-Encryption)
    - [x]  [Pseudo Random Number Generation Lab](./Pseudo-Random-Number-Generation)
    - [ ]  [MD5 Collision Attack Lab](./MD5-Collision-Attack)
    - [ ]  [RSA Encryption and Signature Lab](./RSA-Encryption-and-Signature)
    - [ ]  [Public-Key Infrastructure (PKI) Lab](./PKI)
    - [ ]  [Hash Length Extension Attack Lab](./Hash-Length-Extension-Attack)  (*Azure Ubuntu 20.4*)
    - [ ]  [Transport Layer Security (TLS) Lab](./TLS-Lab) (*Azure Ubuntu 20.4*)
- [x] System Security
    - [ ] [Meltdown Attack Lab](./Meltdown-Attack)
    - [ ] [Spectre Attack Lab](./Spectre-Attack)
- [ ] Mobile Security
    - [ ] Android Repackaging Attack Lab
    - [ ] Android Rooting Lab
    - [ ] Android ClickJacking Attack Lab

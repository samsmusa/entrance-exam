# 4. Number Theory

> **Syllabus (official):**
> - Well-ordering principle
> - Primality and coprimality
> - Modular arithmetic
> - Continued fractions
> - RSA cryptosystem
>
> **How to study this file:** Sections 2–7 are 🟢 core: gcd, primes, mod calculations, inverses, Fermat/Euler powers, small RSA. Sections 1 and 8 are 🟡: learn the facts in the boxes.
> Time: about 3–4 hours for the 🟢 sections, 30 minutes for the 🟡 sections. Practise the powers mod $n$ until you can do them in 1 minute.

## Contents
1. [Well-ordering principle](#1-well-ordering-principle-) 🟡
2. [Divisibility, primes, gcd and lcm](#2-divisibility-primes-gcd-and-lcm-) 🟢
3. [Modular arithmetic: the basics](#3-modular-arithmetic-the-basics-) 🟢
4. [Inverses and linear congruences](#4-inverses-and-linear-congruences-) 🟢
5. [Big powers: Fermat and Euler](#5-big-powers-fermat-and-euler-) 🟢
6. [Chinese Remainder Theorem](#6-chinese-remainder-theorem-) 🟢
7. [RSA cryptosystem](#7-rsa-cryptosystem-) 🟢
8. [Continued fractions](#8-continued-fractions-) 🟡
9. [Formula sheet](#formula-sheet)
10. [Practice MCQs](#practice-mcqs)

---

## 1. Well-ordering principle 🟡

### What it means
$\mathbb N=\{0,1,2,\dots\}$. **Well-ordering principle (WOP):** every **non-empty** subset of $\mathbb N$ has a **smallest element**.

### Must-know facts
> 1. WOP is **equivalent to mathematical induction**.
> 2. $\{n\in\mathbb Z: n\ge-10\}$ is well-ordered (it is a shifted copy of $\mathbb N$).
> 3. $\mathbb Z$ is **not** well-ordered (no smallest element).
> 4. $[0,\infty)$ and $\mathbb Q_{\ge0}$ are **not** well-ordered: the subset $(0,1)$ has no smallest element.
> 5. Typical use: "take the **smallest counterexample**" and show that an even smaller one exists, which is a contradiction. Example: every $n\ge2$ is a product of primes.

> **Trap:** $[0,\infty)$ **has** a smallest element ($0$), but it is still not well-ordered. "Every non-empty subset" is the important part.

---

## 2. Divisibility, primes, gcd and lcm 🟢

### What it means
- $a\mid b$ ("$a$ divides $b$"): $b=k\cdot a$ for some integer $k$. Example: $3\mid12$.
- A **prime** is $p>1$ whose only positive divisors are $1$ and $p$. **1 is not prime.** 2 is the only even prime.
- $\gcd(a,b)$ = greatest common divisor. $\operatorname{lcm}(a,b)$ = least common multiple.
- $a,b$ are **coprime** if $\gcd(a,b)=1$. Example: $8$ and $15$.

### Prime factorization
Every $n\ge2$ is a product of primes in exactly one way (up to order). Example: $360=2^3\cdot3^2\cdot5$.

**Is $n$ prime?** Test only the primes $p\le\sqrt n$.
Example: $221$. $\sqrt{221}<15$, so test $2,3,5,7,11,13$: $221=13\cdot17$. Not prime.
Numbers that look prime but are not: $51=3\cdot17$, $87=3\cdot29$, $91=7\cdot13$, $119=7\cdot17$.

### gcd and lcm with factorizations
| Formula | Meaning |
|---|---|
| $\gcd$ | take each common prime with the **smaller** exponent |
| $\operatorname{lcm}$ | take each prime with the **larger** exponent |
| $\gcd(a,b)\cdot\operatorname{lcm}(a,b)=a\cdot b$ | for two numbers |
| number of divisors $\tau(n)$ | $n=p_1^{e_1}\cdots p_k^{e_k}\Rightarrow\tau(n)=(e_1+1)\cdots(e_k+1)$ |

**Example:** $12=2^2\cdot3$, $18=2\cdot3^2$. $\gcd=2\cdot3=6$, $\operatorname{lcm}=2^2\cdot3^2=36$. Check: $6\cdot36=216=12\cdot18$ ✓.
**Example:** $\tau(72)$: $72=2^3\cdot3^2$, so $\tau=4\cdot3=12$.

### Euclidean algorithm (for big numbers)
Rule: $\gcd(a,b)=\gcd(b,\ a\bmod b)$. Repeat until the remainder is $0$. The last non-zero remainder is the gcd.

**Example:** $\gcd(252,198)$.
1. $252=1\cdot198+54$
2. $198=3\cdot54+36$
3. $54=1\cdot36+18$
4. $36=2\cdot18+0$ → $\gcd=18$.

### Bézout's identity
There are integers $x,y$ with $ax+by=\gcd(a,b)$. You get them by going **backwards** through the Euclidean algorithm (see Section 4).

### Two classic proofs (official problems 3 and 10)
**Infinitely many primes (Euclid).** Suppose $p_1,\dots,p_r$ are all the primes. Let $N=p_1\cdots p_r+1$. Dividing $N$ by any $p_i$ leaves remainder $1$. But $N>1$ has some prime factor. Contradiction.

**$\sqrt3$ is irrational.** Suppose $\sqrt3=p/q$ in lowest terms. Then $p^2=3q^2$, so $3\mid p$. Write $p=3r$: $9r^2=3q^2$, so $q^2=3r^2$ and $3\mid q$. Both are divisible by 3: contradiction.
General: $\sqrt n$ is rational only if $n$ is a perfect square ($\sqrt{49}=7$).

> **Trap:** $p_1\cdots p_r+1$ is **not always prime**: $2\cdot3\cdot5\cdot7\cdot11\cdot13+1=30031=59\cdot509$.

---

## 3. Modular arithmetic: the basics 🟢

### What it means
$a\equiv b\pmod m$ means: $a$ and $b$ have the **same remainder** when divided by $m$. Equivalent: $m\mid(a-b)$.
Example: $17\equiv2\pmod5$, because $17-2=15$.
$a\bmod m$ = the remainder, a number in $\{0,1,\dots,m-1\}$.

This is an equivalence relation (official problem 9). There are $m$ classes $[0],\dots,[m-1]$; together they form $\mathbb Z_m$.

### Rules
If $a\equiv b$ and $c\equiv d\pmod m$, then:
$$a+c\equiv b+d,\qquad a\cdot c\equiv b\cdot d,\qquad a^k\equiv b^k\pmod m.$$
So you may **reduce the numbers first**, then calculate.

**Example:** $47\cdot53\bmod 5$. $47\equiv2$, $53\equiv3$, so $2\cdot3=6\equiv1$.
**Negative numbers:** $-7\bmod5$: add $5$ until positive: $-7+10=3$. So $-7\equiv3\pmod5$.

### Fast remainders from the digits
| Modulus | Rule |
|---|---|
| 2, 5, 10 | last digit |
| 4 | last two digits |
| 3, 9 | sum of the digits |
| 11 | alternating sum of digits, starting from the right |

**Example:** $12345678$. Mod 5: last digit $8$, so $3$. Mod 9: digit sum $36$, so $0$. Mod 11: $8-7+6-5+4-3+2-1=4$.

### Last digit of a power (mod 10)
Last digits of powers repeat in a cycle.

| Last digit of base | Cycle | Length |
|---|---|---|
| 0, 1, 5, 6 | stays the same | 1 |
| 2 | 2, 4, 8, 6 | 4 |
| 3 | 3, 9, 7, 1 | 4 |
| 4 | 4, 6 | 2 |
| 7 | 7, 9, 3, 1 | 4 |
| 8 | 8, 4, 2, 6 | 4 |
| 9 | 9, 1 | 2 |

**Example:** last digit of $3^{2026}$.
1. Cycle $3,9,7,1$ (length 4).
2. $2026\bmod4=2$ → second entry.
3. Answer: $9$.
(If the remainder is $0$, take the **last** entry of the cycle.)

> **Trap:** you can only **cancel** a factor $c$ if $\gcd(c,m)=1$. Example: $2\cdot3\equiv2\cdot8\pmod{10}$, but $3\not\equiv8\pmod{10}$.

---

## 4. Inverses and linear congruences 🟢

### What it means
The **inverse** of $a$ mod $m$ is a number $x$ with $a\cdot x\equiv1\pmod m$. We write $x=a^{-1}\bmod m$.
$$a^{-1}\bmod m\text{ exists}\iff\gcd(a,m)=1.$$
So in $\mathbb Z_p$ ($p$ prime) every $a\neq0$ has an inverse: $\mathbb Z_p$ is a field. In $\mathbb Z_6$, $2$ and $3$ have no inverse.

### Method 1: try (small $m$)
$3^{-1}\bmod7$: $3\cdot5=15\equiv1$. So $3^{-1}=5$.

### Method 2: extended Euclid (bigger $m$)
**Example:** $7^{-1}\bmod26$.
1. $26=3\cdot7+5$
2. $7=1\cdot5+2$
3. $5=2\cdot2+1$
Now go backwards:
4. $1=5-2\cdot2$
5. $\ \ =5-2(7-5)=3\cdot5-2\cdot7$
6. $\ \ =3(26-3\cdot7)-2\cdot7=3\cdot26-11\cdot7$.
So $-11\cdot7\equiv1$, and $7^{-1}\equiv-11\equiv15\pmod{26}$. Check: $7\cdot15=105=4\cdot26+1$ ✓.

**MCQ shortcut:** multiply $a$ by each answer option and see which gives remainder 1.

### Linear congruence $ax\equiv b\pmod m$
Let $d=\gcd(a,m)$.
- If $d\nmid b$: **no** solution.
- If $d\mid b$: exactly **$d$ solutions** in $\{0,\dots,m-1\}$.

**Example:** $6x\equiv4\pmod{10}$. $d=\gcd(6,10)=2$, and $2\mid4$, so 2 solutions. Divide everything by 2: $3x\equiv2\pmod5$, so $x\equiv4\pmod5$. Solutions: $x=4$ and $x=9$.

### Linear Diophantine equation $ax+by=c$ (integers $x,y$)
Solvable $\iff\gcd(a,b)\mid c$.
- $6x+9y=21$: $\gcd=3$ divides 21 → solvable ($x=2,y=1$).
- $6x+9y=20$: $3\nmid20$ → no solution.

> **Trap:** $4$ has no inverse mod $6$ ($\gcd(4,6)=2$). Do not "divide by 4" in mod 6.

---

## 5. Big powers: Fermat and Euler 🟢

### What it means
To compute $a^k\bmod n$ for huge $k$, we find a power of $a$ that is $\equiv1$. Then the powers repeat.

### Formulas
**Euler's phi function:** $\varphi(n)$ = how many numbers in $\{1,\dots,n\}$ are coprime to $n$.

| Case | $\varphi$ |
|---|---|
| $p$ prime | $\varphi(p)=p-1$ |
| prime power | $\varphi(p^k)=p^k-p^{k-1}$ |
| $\gcd(m,n)=1$ | $\varphi(mn)=\varphi(m)\varphi(n)$ |
| general | $\varphi(n)=n\prod_{p\mid n}\left(1-\frac1p\right)$ |

Examples: $\varphi(7)=6$, $\varphi(15)=2\cdot4=8$, $\varphi(36)=36\cdot\frac12\cdot\frac23=12$, $\varphi(100)=100\cdot\frac12\cdot\frac45=40$.

**Fermat's little theorem:** $p$ prime, $p\nmid a$ $\Rightarrow$ $a^{p-1}\equiv1\pmod p$.
**Euler's theorem:** $\gcd(a,n)=1$ $\Rightarrow$ $a^{\varphi(n)}\equiv1\pmod n$.
**Wilson's theorem:** $p$ prime $\Rightarrow(p-1)!\equiv-1\pmod p$.

### Recipe for $a^k\bmod p$
1. Reduce the base: $a\to a\bmod p$.
2. Reduce the exponent: $k\to k\bmod(p-1)$.
3. Compute the small power.

### Worked example (official problem 21): $12345678^{78}\bmod5$
1. Base: last digit $8$, so $12345678\equiv3\pmod5$.
2. Exponent: $p-1=4$, $78=4\cdot19+2$, so $78\bmod4=2$.
3. $3^2=9\equiv4$. **Answer: 4.**

### Worked example: $3^{100}\bmod7$
1. Fermat: $3^6\equiv1\pmod7$.
2. $100=6\cdot16+4$.
3. $3^4=81=11\cdot7+4\equiv4$.

### Worked example: $2^{100}\bmod13$
$2^{12}\equiv1$, $100\bmod12=4$, $2^4=16\equiv3$.

**Other way (always works):** list the powers until you see $1$. Mod 5: $3^1=3,\ 3^2=4,\ 3^3=2,\ 3^4=1$, then it repeats.

> **Trap:** reduce the **exponent** mod $p-1$ (or $\varphi(n)$), **not** mod $p$. And only when $\gcd(a,n)=1$.

---

## 6. Chinese Remainder Theorem 🟢

### What it means
If the moduli $m_1,\dots,m_k$ are pairwise coprime, the system
$$x\equiv a_1\pmod{m_1},\ \dots,\ x\equiv a_k\pmod{m_k}$$
has exactly **one** solution modulo $M=m_1\cdots m_k$.

### Fast method (small numbers): list candidates
**Example:** $x\equiv2\pmod5$, $x\equiv3\pmod7$.
1. Numbers $\equiv2\pmod5$: $2,7,12,17,22,\dots$
2. Check mod 7: $2,0,5,3$ ← $17=14+3$ ✓.
3. Answer: $x\equiv17\pmod{35}$.

**Example:** $x\equiv2\pmod3$, $x\equiv3\pmod5$. Candidates $3,8,13$: $8=6+2$ ✓. So $x\equiv8\pmod{15}$.

**MCQ shortcut:** test each answer option against every condition.

> **Trap:** if the moduli are not coprime, there may be no solution. $x\equiv1\pmod4$ and $x\equiv2\pmod6$: the first says $x$ is odd, the second says $x$ is even. Impossible.

---

## 7. RSA cryptosystem 🟢

### What it means
RSA is a **public-key** system. Everybody knows the public key $(n,e)$ and can encrypt. Only the owner knows $d$ and can decrypt.
Security: it is hard to **factor** $n=pq$ when $p,q$ are huge.

### Formulas (the 4 steps)
| Step | Formula |
|---|---|
| 1. two primes | $n=p\cdot q$ |
| 2. phi | $\varphi(n)=(p-1)(q-1)$ |
| 3. public exponent | choose $e$ with $\gcd(e,\varphi(n))=1$ |
| 4. private exponent | $d=e^{-1}\bmod\varphi(n)$, so $e\cdot d\equiv1\pmod{\varphi(n)}$ |
| encrypt | $c=m^e\bmod n$ |
| decrypt | $m=c^d\bmod n$ |

### Worked example (very small)
$p=3$, $q=11$, $e=3$.
1. $n=33$, $\varphi(n)=2\cdot10=20$.
2. $\gcd(3,20)=1$ ✓.
3. $d$: $3\cdot7=21\equiv1\pmod{20}$, so $d=7$.
4. Encrypt $m=2$: $c=2^3=8$.
5. Decrypt: $8^7\bmod33$. $8^2=64\equiv31\equiv-2$. $8^4\equiv(-2)^2=4$. $8^7=8^4\cdot8^2\cdot8\equiv4\cdot(-2)\cdot8=-64\equiv-64+66=2$ ✓.

### Worked example 2
$p=5$, $q=11$, $e=3$: $n=55$, $\varphi=40$, $d=27$ (since $3\cdot27=81=2\cdot40+1$).
Encrypt $m=9$: $9^3=729=13\cdot55+14$, so $c=14$.

### Must-know facts
- Public: $n$, $e$. Secret: $p$, $q$, $\varphi(n)$, $d$.
- $e$ must be coprime to $\varphi(n)$. $\varphi(n)$ is even, so $e$ is always **odd**.
- If someone knows $\varphi(n)$, they can find $d$ and break the key.

> **Trap:** $d$ is the inverse modulo $\varphi(n)$, **not** modulo $n$.

---

## 8. Continued fractions 🟡

### What it means
A **continued fraction** writes a number as
$$[a_0;a_1,a_2,\dots]=a_0+\cfrac{1}{a_1+\cfrac{1}{a_2+\cdots}}.$$
For a fraction $a/b$, the numbers $a_i$ are exactly the **quotients of the Euclidean algorithm**.

### Worked example: $\frac{10}{7}$
1. $10=1\cdot7+3$ → $a_0=1$
2. $7=2\cdot3+1$ → $a_1=2$
3. $3=3\cdot1+0$ → $a_2=3$
So $\frac{10}7=[1;2,3]$. Check: $1+\cfrac{1}{2+\frac13}=1+\frac37=\frac{10}7$ ✓.

### Must-know facts
> 1. **Rational** number $\iff$ **finite** continued fraction.
> 2. **Periodic** (repeating) continued fraction $\iff$ root of a quadratic equation (like $\sqrt2$).
> 3. $\sqrt2=[1;2,2,2,\dots]$. Its approximations (**convergents**) are $1,\ \frac32,\ \frac75,\ \frac{17}{12},\dots$
> 4. $[1;1,1,1,\dots]=\frac{1+\sqrt5}2$ (golden ratio): from $x=1+\frac1x$, so $x^2-x-1=0$.
> 5. Convergents of $\pi=[3;7,15,1,\dots]$: $3,\ \frac{22}7,\ \frac{333}{106},\ \frac{355}{113}$.
> 6. Next convergent: $p_n=a_np_{n-1}+p_{n-2}$, $q_n=a_nq_{n-1}+q_{n-2}$. Example for $\sqrt2$: $\frac{2\cdot7+3}{2\cdot5+2}=\frac{17}{12}$.

---

## Formula sheet

| Topic | Formula / fact |
|---|---|
| WOP | every non-empty subset of $\mathbb N$ has a smallest element; equivalent to induction |
| Euclid | $\gcd(a,b)=\gcd(b,a\bmod b)$ |
| gcd·lcm | $\gcd(a,b)\operatorname{lcm}(a,b)=ab$ |
| divisors | $\tau(p_1^{e_1}\cdots p_k^{e_k})=(e_1+1)\cdots(e_k+1)$ |
| prime test | check primes $\le\sqrt n$ |
| congruence | $a\equiv b\pmod m\iff m\mid a-b$ |
| digits | mod 5/10: last digit; mod 3/9: digit sum; mod 11: alternating sum |
| inverse | $a^{-1}\bmod m$ exists $\iff\gcd(a,m)=1$ |
| $ax\equiv b\ (m)$ | solvable $\iff d=\gcd(a,m)\mid b$; then $d$ solutions |
| $ax+by=c$ | solvable $\iff\gcd(a,b)\mid c$ |
| $\varphi$ | $\varphi(p)=p-1$; $\varphi(p^k)=p^k-p^{k-1}$; $\varphi(mn)=\varphi(m)\varphi(n)$ if coprime |
| Fermat | $a^{p-1}\equiv1\pmod p$ if $p\nmid a$ |
| Euler | $a^{\varphi(n)}\equiv1\pmod n$ if $\gcd(a,n)=1$ |
| Wilson | $(p-1)!\equiv-1\pmod p$ |
| CRT | coprime moduli → one solution mod $m_1\cdots m_k$ |
| RSA | $n=pq$, $\varphi=(p-1)(q-1)$, $d=e^{-1}\bmod\varphi$, $c=m^e$, $m=c^d\pmod n$ |
| CF | rational $\iff$ finite; $\sqrt2=[1;2,2,\dots]$; $[1;1,1,\dots]=\frac{1+\sqrt5}2$ |

---

## Practice MCQs

**Q1.** What is $\gcd(84,36)$?
A) 6  B) 12  C) 4  D) 18
<details><summary>Answer</summary>

**B** — $84=2\cdot36+12$, $36=3\cdot12+0$. So $\gcd=12$.

</details>

**Q2.** What is $\operatorname{lcm}(12,18)$?
A) 36  B) 72  C) 216  D) 6
<details><summary>Answer</summary>

**A** — $\gcd(12,18)=6$, so $\operatorname{lcm}=\frac{12\cdot18}{6}=36$.

</details>

**Q3.** What is $-7\bmod5$?
A) 2  B) $-2$  C) 7  D) 3
<details><summary>Answer</summary>

**D** — $-7+10=3$, and $3\in\{0,\dots,4\}$. Check: $-7-3=-10$ is divisible by 5.

</details>

**Q4.** Which number is prime?
A) 91  B) 87  C) 97  D) 51
<details><summary>Answer</summary>

**C** — $91=7\cdot13$, $87=3\cdot29$, $51=3\cdot17$. For 97 test $2,3,5,7$ (since $\sqrt{97}<10$): none divides it.

</details>

**Q5.** What is $\varphi(15)$?
A) 8  B) 14  C) 10  D) 6
<details><summary>Answer</summary>

**A** — $\varphi(15)=\varphi(3)\varphi(5)=2\cdot4=8$.

</details>

**Q6.** What is the inverse of $3$ modulo $7$?
A) 2  B) 4  C) 6  D) 5
<details><summary>Answer</summary>

**D** — $3\cdot5=15=2\cdot7+1\equiv1$.

</details>

**Q7.** How many positive divisors does $72$ have?
A) 8  B) 12  C) 6  D) 10
<details><summary>Answer</summary>

**B** — $72=2^3\cdot3^2$, so $\tau=(3+1)(2+1)=12$.

</details>

**Q8.** What is $12345678\bmod9$?
A) 0  B) 3  C) 6  D) 8
<details><summary>Answer</summary>

**A** — Digit sum $1+2+\dots+8=36$, and $36\equiv0\pmod9$.

</details>

**Q9.** What is the last digit of $3^{2026}$?
A) 3  B) 7  C) 9  D) 1
<details><summary>Answer</summary>

**C** — The cycle is $3,9,7,1$. $2026\bmod4=2$ → second entry: $9$.

</details>

**Q10.** What is $2^{10}\bmod11$?
A) 10  B) 1  C) 2  D) 0
<details><summary>Answer</summary>

**B** — Fermat with $p=11$: $2^{10}\equiv1$. (Direct: $1024=93\cdot11+1$.)

</details>

**Q11.** What is $13^{43}\bmod5$?
A) 2  B) 3  C) 4  D) 1
<details><summary>Answer</summary>

**A** — $13\equiv3$. Powers of 3 mod 5: $3,4,2,1$. $43\bmod4=3$ → third entry: $2$.

</details>

**Q12.** What is $3^{100}\bmod7$?
A) 1  B) 3  C) 2  D) 4
<details><summary>Answer</summary>

**D** — $3^6\equiv1$ (Fermat), $100=6\cdot16+4$, $3^4=81=77+4\equiv4$.

</details>

**Q13.** What is $2^{100}\bmod13$?
A) 1  B) 3  C) 9  D) 12
<details><summary>Answer</summary>

**B** — $2^{12}\equiv1$, $100\bmod12=4$, $2^4=16\equiv3$.

</details>

**Q14.** What is the inverse of $7$ modulo $26$?
A) 11  B) 4  C) 15  D) 19
<details><summary>Answer</summary>

**C** — $7\cdot15=105=4\cdot26+1\equiv1$. (Test the options: $7\cdot11=77\equiv25$, $7\cdot4=28\equiv2$, $7\cdot19=133\equiv3$.)

</details>

**Q15.** Find $x$ in $\{0,\dots,34\}$ with $x\equiv2\pmod5$ and $x\equiv3\pmod7$.
A) 12  B) 22  C) 27  D) 17
<details><summary>Answer</summary>

**D** — $17=15+2$ and $17=14+3$. Check the others: $12\equiv5$, $22\equiv1$, $27\equiv6\pmod7$.

</details>

**Q16.** How many solutions does $6x\equiv4\pmod{10}$ have in $\{0,1,\dots,9\}$?
A) 0  B) 1  C) 2  D) 6
<details><summary>Answer</summary>

**C** — $d=\gcd(6,10)=2$ divides 4, so there are 2 solutions: $x=4$ ($24\equiv4$) and $x=9$ ($54\equiv4$).

</details>

**Q17.** Which equation has **no** integer solution $(x,y)$?
A) $6x+9y=20$  B) $6x+9y=21$  C) $3x+5y=7$  D) $4x+6y=10$
<details><summary>Answer</summary>

**A** — $\gcd(6,9)=3$ and $3\nmid20$. B: $x=2,y=1$. C: $x=4,y=-1$. D: $x=1,y=1$.

</details>

**Q18.** RSA with $p=5$, $q=11$. What is $\varphi(n)$?
A) 55  B) 40  C) 50  D) 16
<details><summary>Answer</summary>

**B** — $\varphi(55)=(5-1)(11-1)=4\cdot10=40$.

</details>

**Q19.** Same key: $n=55$, $\varphi(n)=40$, $e=3$. What is the private exponent $d$?
A) 13  B) 7  C) 37  D) 27
<details><summary>Answer</summary>

**D** — $3\cdot27=81=2\cdot40+1\equiv1\pmod{40}$. Check the trap options: $3\cdot13=39$, $3\cdot7=21$, $3\cdot37=111\equiv31$.

</details>

**Q20.** Same key ($n=55$, $e=3$). What is the ciphertext of $m=9$?
A) 14  B) 27  C) 9  D) 31
<details><summary>Answer</summary>

**A** — $9^3=729=13\cdot55+14$, so $c=14$.

</details>

**Q21.** In RSA, $\varphi(n)=40$. Which value can be used as the public exponent $e$?
A) 5  B) 4  C) 7  D) 10
<details><summary>Answer</summary>

**C** — $e$ needs $\gcd(e,40)=1$. $\gcd(7,40)=1$ ✓. The others share the factor 2 or 5 with 40.

</details>

**Q22.** Which set is well-ordered under the usual order $\le$?
A) $\mathbb Z$  B) $\{n\in\mathbb Z: n\ge-10\}$  C) $[0,\infty)$  D) $\mathbb Q_{\ge0}$
<details><summary>Answer</summary>

**B** — It is $\mathbb N$ shifted by $-10$. $\mathbb Z$ has no minimum. In C and D the subset of numbers $>0$ has no smallest element.

</details>

**Q23.** What is the continued fraction of $\frac{10}{7}$?
A) $[1;3,2]$  B) $[1;2,3]$  C) $[1;2,1,2]$  D) $[0;1,2,3]$
<details><summary>Answer</summary>

**B** — Euclid: $10=1\cdot7+3$, $7=2\cdot3+1$, $3=3\cdot1$. Quotients $1,2,3$.

</details>

**Q24.** Which number is **rational**?
A) $\sqrt{12}$  B) $\sqrt{18}$  C) $\sqrt{50}$  D) $\sqrt{49}$
<details><summary>Answer</summary>

**D** — $\sqrt n$ is rational only for perfect squares. $49=7^2$. The others are $2\sqrt3$, $3\sqrt2$, $5\sqrt2$.

</details>

**Q25.** Which statement is **false**?
A) $p_1p_2\cdots p_r+1$ is always prime  B) every integer $n\ge2$ has a prime divisor  C) $\mathbb Z_6$ is not a field  D) $10!\equiv10\pmod{11}$
<details><summary>Answer</summary>

**A** — $2\cdot3\cdot5\cdot7\cdot11\cdot13+1=30031=59\cdot509$. C: $2\cdot3\equiv0$ in $\mathbb Z_6$. D: Wilson, $10!\equiv-1\equiv10$.

</details>

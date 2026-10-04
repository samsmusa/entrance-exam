# 3. Discrete Mathematics

> **Syllabus:** Logic, sets and relations · Mathematical induction · Pigeonhole principle · Counting techniques · Generating functions
>
> **How to study this file:** Sections 1–8 are 🟢 core. Learn them well: they match the official practice problems (binomial theorem, stars and bars, preimages, injections, $\mathbb N\times\mathbb N$, mod $k$). Sections 9–10 are 🟡: read the facts once. Time: about 4–5 hours, plus 1 hour for the MCQs.

## Contents
1. [Logic](#1-logic-) 🟢
2. [Sets](#2-sets-) 🟢
3. [Functions, images and preimages](#3-functions-images-and-preimages-) 🟢
4. [Countable and uncountable sets](#4-countable-and-uncountable-sets-) 🟢
5. [Relations](#5-relations-) 🟢
6. [Mathematical induction](#6-mathematical-induction-) 🟢
7. [Pigeonhole principle](#7-pigeonhole-principle-) 🟢
8. [Counting techniques](#8-counting-techniques-) 🟢
9. [Recurrences](#9-recurrences-) 🟡
10. [Generating functions](#10-generating-functions-) 🟡
11. [Formula sheet](#formula-sheet)
12. [Practice MCQs](#practice-mcqs)

---

## 1. Logic 🟢

**Symbols.** $p,q$ are statements (true T or false F).

| Symbol | Read as | True when |
|---|---|---|
| $\neg p$ | "not $p$" | $p$ is false |
| $p\land q$ | "$p$ and $q$" | both are true |
| $p\lor q$ | "$p$ or $q$" | at least one is true |
| $p\to q$ | "if $p$ then $q$" | always, **except** $p$ = T and $q$ = F |
| $p\leftrightarrow q$ | "$p$ if and only if $q$" | $p$ and $q$ have the same value |

**Plain words.** "If $p$ then $q$" is only broken when $p$ happens and $q$ does not.
So "if $1=2$ then the moon is green" is TRUE (the "if" part is false).

**Key rules.**
$$p\to q\ \equiv\ \neg p\lor q\ \equiv\ \neg q\to\neg p\quad\text{(contrapositive)}$$
$$\neg(p\to q)\equiv p\land\neg q,\qquad \neg(p\land q)\equiv\neg p\lor\neg q,\qquad \neg(p\lor q)\equiv\neg p\land\neg q\ \text{(De Morgan)}$$

| Name | Form | Same as $p\to q$? |
|---|---|---|
| Contrapositive | $\neg q\to\neg p$ | ✅ yes |
| Converse | $q\to p$ | ❌ no |
| Inverse | $\neg p\to\neg q$ | ❌ no |

**Quantifiers.** $\forall x$ = "for all $x$". $\exists x$ = "there exists an $x$".
To negate: **swap $\forall\leftrightarrow\exists$ and negate the inside.**
$$\neg\,\forall x\,P(x)\equiv\exists x\,\neg P(x),\qquad \neg\,\exists x\,P(x)\equiv\forall x\,\neg P(x)$$

**Worked example.** Negate "$\forall x\in\mathbb R\ \exists y\in\mathbb R: y>x$".
1. Swap $\forall\to\exists$ and $\exists\to\forall$: $\exists x\ \forall y$.
2. Negate the inside: $y>x$ becomes $y\le x$.
3. Answer: $\exists x\ \forall y: y\le x$ ("there is a largest real number").

**Language tips.** "$p$ only if $q$" = $p\to q$. "$p$ is sufficient for $q$" = $p\to q$. "$p$ is necessary for $q$" = $q\to p$.

**Truth tables.** With $n$ variables there are $2^n$ rows. A **tautology** is true in every row.

> **Trap:** the negation of "if $p$ then $q$" is "$p$ and not $q$", **not** "if not $p$ then not $q$".

---

## 2. Sets 🟢

**Symbols.** $x\in A$: $x$ is in $A$. $A\subseteq B$: every element of $A$ is in $B$. $\emptyset$: the empty set. $|A|$: the number of elements.

| Operation | Meaning |
|---|---|
| $A\cup B$ (union) | in $A$ **or** in $B$ |
| $A\cap B$ (intersection) | in $A$ **and** in $B$ |
| $A\setminus B$ (difference) | in $A$ but not in $B$ |
| $A^c$ (complement) | not in $A$ |
| $A\times B$ (product) | all pairs $(a,b)$ with $a\in A$, $b\in B$ |
| $\mathcal P(A)$ (power set) | the set of all subsets of $A$ |

**Formulas.**
$$|A\cup B|=|A|+|B|-|A\cap B|,\qquad |A\times B|=|A|\cdot|B|,\qquad |\mathcal P(A)|=2^{|A|}$$
De Morgan: $(A\cup B)^c=A^c\cap B^c$ and $(A\cap B)^c=A^c\cup B^c$.

**Worked example.** $A=\{1,2,3\}$.
- $\mathcal P(A)=\{\emptyset,\{1\},\{2\},\{3\},\{1,2\},\{1,3\},\{2,3\},\{1,2,3\}\}$: $8=2^3$ sets.
- $|A\times A|=3\cdot3=9$.

**How to prove $X=Y$ for sets:** show $x\in X\Rightarrow x\in Y$ and $x\in Y\Rightarrow x\in X$.

> **Trap:** $\emptyset$ and $A$ itself are **both** subsets of $A$. Do not forget them when you count.

---

## 3. Functions, images and preimages 🟢

**Symbols.** $f:A\to B$ gives each $a\in A$ exactly one value $f(a)\in B$.

| Word | Meaning in plain words | Formula |
|---|---|---|
| **injective** (one-to-one) | different inputs give different outputs | $f(a)=f(a')\Rightarrow a=a'$ |
| **surjective** (onto) | every $b\in B$ is hit | $\forall b\ \exists a: f(a)=b$ |
| **bijective** | both; $f$ has an inverse | |

**Image and preimage.**
- Image of $U\subseteq A$: $f(U)=\{f(u):u\in U\}$ (where $U$ goes to).
- Preimage of $Y\subseteq B$: $f^{-1}(Y)=\{a\in A: f(a)\in Y\}$ (what lands in $Y$). It exists even if $f$ has no inverse.

**Worked example (official Exercise 6).** Show $f^{-1}(Y\cup Z)=f^{-1}(Y)\cup f^{-1}(Z)$.
$$x\in f^{-1}(Y\cup Z)\iff f(x)\in Y\cup Z\iff f(x)\in Y\text{ or }f(x)\in Z\iff x\in f^{-1}(Y)\cup f^{-1}(Z).$$

| Identity | Always true? |
|---|---|
| $f^{-1}(Y\cup Z)=f^{-1}(Y)\cup f^{-1}(Z)$ | ✅ |
| $f^{-1}(Y\cap Z)=f^{-1}(Y)\cap f^{-1}(Z)$ | ✅ |
| $f^{-1}(B\setminus Y)=A\setminus f^{-1}(Y)$ | ✅ |
| $f(U\cup V)=f(U)\cup f(V)$ | ✅ |
| $f(U\cap V)=f(U)\cap f(V)$ | ❌ only $\subseteq$ (true if $f$ injective) |
| $f(f^{-1}(Y))=Y$ | ❌ only $\subseteq$ (true if $f$ surjective) |
| $f^{-1}(f(U))=U$ | ❌ only $\supseteq$ (true if $f$ injective) |

**Memory rule:** preimages keep everything; images keep only unions.

**Counterexample to remember.** $f(x)=x^2$, $U=\{-1\}$, $V=\{1\}$. Then $f(U\cap V)=f(\emptyset)=\emptyset$, but $f(U)\cap f(V)=\{1\}$.

**Composition $g\circ f$** (first $f$, then $g$):
- $f,g$ injective ⇒ $g\circ f$ injective. $f,g$ surjective ⇒ $g\circ f$ surjective.
- $g\circ f$ injective ⇒ $f$ injective. $g\circ f$ surjective ⇒ $g$ surjective.

**Official Exercise 17.** If $A\ne\emptyset$ and $f:A\to B$ is injective, then there is a surjection $g:B\to A$.
Idea: fix $a_0\in A$. If $b=f(a)$, send $b$ back to $a$. Otherwise send $b$ to $a_0$. Every $a$ is hit, because $g(f(a))=a$.

**Counting functions** from a set with $m$ elements to a set with $n$ elements:

| Type | Number | Example $m=3$, $n=4$ |
|---|---|---|
| all functions | $n^m$ | $64$ |
| injective ($m\le n$) | $n(n-1)\cdots(n-m+1)$ | $4\cdot3\cdot2=24$ |
| bijective ($m=n$) | $n!$ | – |

**Finite sets:** if $|A|=|B|$ is finite, then injective ⇔ surjective ⇔ bijective.

> **Trap:** "$f(U\cap V)=f(U)\cap f(V)$" is the classic "NOT always true" answer.

---

## 4. Countable and uncountable sets 🟢

**Plain words.** A set is **countable** if you can list its elements as $a_1,a_2,a_3,\dots$ (finite sets count too). Formally: there is an injection into $\mathbb N$.

| Countable | Uncountable |
|---|---|
| $\mathbb N,\ \mathbb Z,\ \mathbb Q$ | $\mathbb R$, any interval $[a,b]$ with $a<b$ |
| $\mathbb N\times\mathbb N$, $\mathbb Q\times\mathbb Q$ | $\mathcal P(\mathbb N)$ (all subsets of $\mathbb N$) |
| finite subsets of $\mathbb N$ | infinite 0-1 sequences |
| finite words over a finite alphabet | irrational numbers |
| a countable union of countable sets | $\mathbb R^2$, $\mathbb C$ |

**Official Exercise 18: $\mathbb N\times\mathbb N$ is countable.**
The map $(a,b)\mapsto 2^a3^b$ is injective. Reason: prime factorization is unique, so $2^a3^b=2^c3^d$ forces $a=c$, $b=d$.

**Uncountable (Cantor's diagonal idea).** Take any list of numbers in $(0,1)$. Build a new number whose $k$-th digit differs from the $k$-th digit of the $k$-th number. It is not in the list.

> **Trap:** $\mathbb Q$ is countable even though it is "dense". $[0,1]$ and $\mathbb R$ have the **same** size.

---

## 5. Relations 🟢

**Symbols.** A relation $R$ on $A$ is a set of pairs. We write $aRb$ if $(a,b)\in R$.

| Property | Meaning |
|---|---|
| reflexive | $aRa$ for all $a$ |
| symmetric | $aRb\Rightarrow bRa$ |
| antisymmetric | $aRb$ and $bRa\Rightarrow a=b$ |
| transitive | $aRb$ and $bRc\Rightarrow aRc$ |

- **Equivalence relation** = reflexive + symmetric + transitive.
- **Partial order** = reflexive + antisymmetric + transitive.

**Equivalence classes.** $[a]=\{b: aRb\}$. The classes do not overlap and cover all of $A$ (a **partition**).

**Worked example (official Exercise 9).** On $\mathbb Z$: $x\sim y\iff k\mid x-y$ ("$k$ divides $x-y$").
1. Reflexive: $x-x=0=k\cdot0$. ✓
2. Symmetric: $x-y=kq\Rightarrow y-x=k(-q)$. ✓
3. Transitive: $x-y=kq$, $y-z=kr\Rightarrow x-z=k(q+r)$. ✓

There are exactly $k$ classes: $[0],[1],\dots,[k-1]$ (the remainders mod $k$).

| Relation | R | S | AS | T | Type |
|---|---|---|---|---|---|
| $=$ | ✓ | ✓ | ✓ | ✓ | both equivalence and partial order |
| $\le$ on $\mathbb R$ | ✓ | ✗ | ✓ | ✓ | partial (even total) order |
| $<$ on $\mathbb R$ | ✗ | ✗ | ✓ | ✓ | strict order |
| $\subseteq$ on $\mathcal P(A)$ | ✓ | ✗ | ✓ | ✓ | partial order |
| $a\mid b$ on $\mathbb N$ | ✓ | ✗ | ✓ | ✓ | partial order |
| $x\equiv y\pmod k$ | ✓ | ✓ | ✗ | ✓ | equivalence, $k$ classes |
| $\lvert x-y\rvert\le1$ on $\mathbb R$ | ✓ | ✓ | ✗ | ✗ | not transitive: $0\sim1\sim2$, $0\not\sim2$ |

**Counting relations** on a set with $n$ elements: all relations $2^{n^2}$; reflexive $2^{n^2-n}$; symmetric $2^{n(n+1)/2}$.

> **Trap:** "symmetric + transitive ⇒ reflexive" is FALSE. Example: the empty relation on $\{1\}$.

---

## 6. Mathematical induction 🟢

**Plain words.** Like dominoes: (1) the first one falls, (2) each one knocks over the next. Then all fall.

**Method.** To prove $P(n)$ for all $n\ge n_0$:
1. **Base case:** check $P(n_0)$.
2. **Inductive step:** assume $P(n)$ (the *induction hypothesis*), then prove $P(n+1)$.

**Worked example.** Prove $1+2+\dots+n=\frac{n(n+1)}2$.
1. Base $n=1$: $1=\frac{1\cdot2}2$. ✓
2. Step: $1+\dots+n+(n+1)=\frac{n(n+1)}2+(n+1)=\frac{(n+1)(n+2)}2$. ✓

**Useful sums (all provable by induction).**

| Sum | Value |
|---|---|
| $1+2+\dots+n$ | $\frac{n(n+1)}2$ |
| $1^2+2^2+\dots+n^2$ | $\frac{n(n+1)(2n+1)}6$ |
| $1+3+5+\dots+(2n-1)$ | $n^2$ |
| $1+r+r^2+\dots+r^n$ ($r\ne1$) | $\frac{r^{n+1}-1}{r-1}$ |

**Official Exercise 2: binomial theorem by induction.** Claim: $(x+y)^n=\sum_{k=0}^n\binom nk x^ky^{n-k}$.
- Base $n=0$: $1=1$.
- Step: multiply the formula for $n$ by $(x+y)$, shift the index in one sum, and combine with **Pascal's rule** $\binom n{k-1}+\binom nk=\binom{n+1}k$.

**Inequalities.** $2^n>n^2$ holds for all $n\ge5$ (at $n=4$: $16=16$, not $>$). $n!>2^n$ holds for $n\ge4$.

**Divisibility example.** $3\mid 4^n-1$. Step: $4^{n+1}-1=4(4^n-1)+3$, and both parts are divisible by 3.

> **Trap:** a correct step without a base case proves nothing. Example: "$n=n+1$" has a correct step but no base case.

---

## 7. Pigeonhole principle 🟢

**Plain words.** If you put more pigeons than boxes, some box gets at least two pigeons.

**Formula.** $N$ objects in $k$ boxes ⇒ some box has at least $\lceil N/k\rceil$ objects. ($\lceil x\rceil$ = round up.)
To **guarantee** $r$ objects in one box you need $k(r-1)+1$ objects.

**Worked example 1.** How many people guarantee that 3 share a birth month?
1. Boxes = 12 months, $r=3$.
2. Worst case: 2 people in every month = 24 people, nobody has 3.
3. Answer: $12\cdot2+1=25$.

**Worked example 2.** How many numbers from $\{1,\dots,10\}$ guarantee that two of them sum to 11?
1. Boxes: $\{1,10\},\{2,9\},\{3,8\},\{4,7\},\{5,6\}$, so 5 boxes.
2. With 6 numbers, two are in the same box. Answer: **6**.

**Classic facts.**
- $n+1$ integers: two have the same remainder mod $n$.
- Socks in $k$ colours: $k+1$ socks guarantee a pair.

> **Trap:** "minimum to guarantee" = worst case **+ 1**. Do not forget the $+1$.

---

## 8. Counting techniques 🟢

### 8.1 Basic rules
- **Sum rule:** choose A **or** B (no overlap): add.
- **Product rule:** choose A **and then** B: multiply.
- $n!=1\cdot2\cdots n$, and $0!=1$.

### 8.2 The four selection formulas (choose $k$ from $n$)

| | order matters | order does not matter |
|---|---|---|
| no repetition | $\dfrac{n!}{(n-k)!}$ | $\dbinom nk=\dfrac{n!}{k!\,(n-k)!}$ |
| repetition allowed | $n^k$ | $\dbinom{n+k-1}{k}$ |

**Worked example.** 5 runners. How many ways for gold, silver and bronze? Order matters: $5\cdot4\cdot3=60$. How many 3-person teams? Order does not matter: $\binom53=10$.

### 8.3 Binomial coefficients and the binomial theorem
$$(x+y)^n=\sum_{k=0}^n\binom nk x^ky^{n-k}$$

| Fact | Formula |
|---|---|
| symmetry | $\binom nk=\binom n{n-k}$ |
| Pascal | $\binom nk=\binom{n-1}{k-1}+\binom{n-1}k$ |
| all subsets | $\sum_k\binom nk=2^n$ (put $x=y=1$) |
| alternating | $\sum_k(-1)^k\binom nk=0$ for $n\ge1$ (put $x=-1,y=1$) |
| weighted | $\sum_k k\binom nk=n2^{n-1}$ |

**Worked example.** Coefficient of $x^2$ in $(1+3x)^4$.
1. The term is $\binom42(3x)^2=6\cdot9x^2$.
2. Answer: $54$.

> **Trap:** in $(a x+b)^n$ the number $a$ is also raised to the power $k$. Signs count too: $(2x-1)^3$ has $x^2$-coefficient $\binom32\cdot2^2\cdot(-1)=-12$.

### 8.4 Words with repeated letters
$$\frac{n!}{n_1!\,n_2!\cdots}$$
**Example.** LEVEL: 5 letters, L twice, E twice, V once: $\frac{5!}{2!\,2!}=30$.

### 8.5 Stars and bars
**Plain words.** Share $n$ identical sweets among $k$ children. Write $n$ stars and $k-1$ bars in a row.

| Condition | Number of solutions of $x_1+\dots+x_k=n$ |
|---|---|
| $x_i\ge0$ | $\dbinom{n+k-1}{k-1}$ |
| $x_i\ge1$ | $\dbinom{n-1}{k-1}$ |

**Worked example (official Exercise 16).** $x+y+z=n$, $x,y,z\ge0$: $\binom{n+2}2$. For $n=4$: $\binom62=15$.

**Worked example.** $x+y+z=10$ with $x\ge2$.
1. Put $x'=x-2\ge0$: $x'+y+z=8$.
2. Answer: $\binom{10}2=45$.

> **Trap:** "$\ge0$" and "$\ge1$" give different answers. Read the question carefully.

### 8.6 Inclusion–exclusion
$$|A\cup B|=|A|+|B|-|A\cap B|$$
$$|A\cup B\cup C|=|A|+|B|+|C|-|A\cap B|-|A\cap C|-|B\cap C|+|A\cap B\cap C|$$

**Worked example.** How many of $1,\dots,30$ are divisible by 2 or 5?
1. By 2: 15. By 5: 6. By both (by 10): 3.
2. Answer: $15+6-3=18$.

> **Trap:** "divisible by 4 and 6" means divisible by $\operatorname{lcm}(4,6)=12$, not by 24.

### 8.7 Derangements 🟡
A **derangement** is a permutation with no element in its own place. $D_n=n!\left(1-\frac1{1!}+\frac1{2!}-\dots\pm\frac1{n!}\right)$.

| $n$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $D_n$ | 0 | 1 | 2 | 9 | 44 |

### 8.8 Other numbers 🟡

> **Must-know facts**
> - Circular arrangements of $n$ people: $(n-1)!$.
> - Lattice paths from $(0,0)$ to $(a,b)$ with steps right/up: $\binom{a+b}{a}$.
> - Catalan numbers $C_n=\frac1{n+1}\binom{2n}n$: $1,1,2,5,14,42$ (balanced brackets).
> - Surjections from a 3-set onto a 2-set: $2^3-2=6$.
> - Number of diagonals of a convex $n$-gon: $\frac{n(n-3)}2$.

---

## 9. Recurrences 🟡

**Plain words.** A recurrence gives each term from earlier terms. Example: Fibonacci $F_n=F_{n-1}+F_{n-2}$: $0,1,1,2,3,5,8,13,\dots$

**Fast MCQ method:** compute the first terms by hand and compare with the options.

**Worked example.** $a_n=2a_{n-1}+1$, $a_0=0$.
1. Terms: $0,1,3,7,15,31$.
2. Guess $a_n=2^n-1$ (Tower of Hanoi). Check: $2(2^{n-1}-1)+1=2^n-1$. ✓

**Linear recurrence $a_n=c_1a_{n-1}+c_2a_{n-2}$.**
1. Solve $r^2=c_1r+c_2$.
2. Two different roots $r_1,r_2$: $a_n=\alpha r_1^n+\beta r_2^n$.
3. Double root $r$: $a_n=(\alpha+\beta n)r^n$.

**Example.** $a_n=5a_{n-1}-6a_{n-2}$: $r^2-5r+6=0$, $r=2,3$, so $a_n=\alpha2^n+\beta3^n$.

> **Trap:** with a double root, do not forget the factor $n$.

---

## 10. Generating functions 🟡

**Plain words.** Store a sequence $a_0,a_1,a_2,\dots$ as a power series $A(x)=a_0+a_1x+a_2x^2+\dots$

> **Must-know facts**
> - $\dfrac1{1-x}=1+x+x^2+\dots$, so $a_n=1$.
> - $\dfrac1{1-ax}$ gives $a_n=a^n$.
> - $(1+x)^m$ gives $a_n=\binom mn$.
> - $\dfrac1{(1-x)^k}$ gives $a_n=\binom{n+k-1}{k-1}$ (the same number as stars and bars).
> - Multiplying two generating functions: $[x^n]A(x)B(x)=\sum_{j=0}^n a_jb_{n-j}$.
> - Exponential generating function: $\sum a_n\frac{x^n}{n!}$; e.g. $e^{x}$ gives $a_n=1$.

**Example.** Coefficient of $x^3$ in $\frac1{(1-x)^2}$: $\binom{3+1}{1}=4$. (Indeed $\frac1{(1-x)^2}=1+2x+3x^2+4x^3+\dots$)

---

## Formula sheet

| Topic | Formula |
|---|---|
| Implication | $p\to q\equiv\neg p\lor q\equiv\neg q\to\neg p$; negation $p\land\neg q$ |
| Quantifier negation | $\neg\forall x P\equiv\exists x\neg P$; $\neg\exists xP\equiv\forall x\neg P$ |
| Union | $\lvert A\cup B\rvert=\lvert A\rvert+\lvert B\rvert-\lvert A\cap B\rvert$ |
| Power set | $\lvert\mathcal P(A)\rvert=2^{\lvert A\rvert}$ |
| Preimage | keeps $\cup,\cap$, complement; image keeps only $\cup$ |
| Functions $m\to n$ | all $n^m$; injective $\frac{n!}{(n-m)!}$; bijective $n!$ |
| Countable | $\mathbb N,\mathbb Z,\mathbb Q,\mathbb N\times\mathbb N$; uncountable $\mathbb R,\mathcal P(\mathbb N)$ |
| Equivalence | reflexive + symmetric + transitive; mod $k$ has $k$ classes |
| Sums | $\sum k=\frac{n(n+1)}2$; $\sum k^2=\frac{n(n+1)(2n+1)}6$; $\sum(2k-1)=n^2$ |
| Pigeonhole | some box $\ge\lceil N/k\rceil$; guarantee $r$: $k(r-1)+1$ |
| Ordered, no repetition | $\frac{n!}{(n-k)!}$ |
| Unordered, no repetition | $\binom nk$ |
| Ordered, repetition | $n^k$ |
| Unordered, repetition | $\binom{n+k-1}k$ |
| Binomial theorem | $(x+y)^n=\sum\binom nk x^ky^{n-k}$; $\sum\binom nk=2^n$ |
| Words | $\frac{n!}{n_1!n_2!\cdots}$ |
| Stars and bars | $\ge0$: $\binom{n+k-1}{k-1}$; $\ge1$: $\binom{n-1}{k-1}$ |
| Inclusion–exclusion | $\lvert A\cup B\cup C\rvert=\sum\lvert A\rvert-\sum\lvert A\cap B\rvert+\lvert A\cap B\cap C\rvert$ |
| Derangements | $0,1,2,9,44$ for $n=1..5$ |
| Generating function | $\frac1{(1-x)^k}\to\binom{n+k-1}{k-1}$ |

---

## Practice MCQs

**Q1.** What is $\binom62$?
- A. 12
- B. 30
- C. 15
- D. 36

<details><summary>Answer</summary>

**C** — $\binom62=\frac{6\cdot5}{2\cdot1}=15$. (30 is the ordered count $6\cdot5$.)

</details>

**Q2.** How many subsets does a set with 5 elements have?
- A. 32
- B. 25
- C. 10
- D. 31

<details><summary>Answer</summary>

**A** — $2^5=32$. This includes $\emptyset$ and the whole set.

</details>

**Q3.** The negation of "if it rains, then I stay home" is
- A. If it does not rain, I do not stay home.
- B. It rains and I do not stay home.
- C. If I stay home, it rains.
- D. It does not rain and I stay home.

<details><summary>Answer</summary>

**B** — $\neg(p\to q)\equiv p\land\neg q$. A is the inverse and C is the converse.

</details>

**Q4.** Which statement is equivalent to "if $n$ is divisible by 4, then $n$ is even"?
- A. If $n$ is even, then $n$ is divisible by 4.
- B. If $n$ is not divisible by 4, then $n$ is odd.
- C. $n$ is divisible by 4 and $n$ is odd.
- D. If $n$ is odd, then $n$ is not divisible by 4.

<details><summary>Answer</summary>

**D** — This is the contrapositive $\neg q\to\neg p$. A is the converse, B the inverse, C the negation.

</details>

**Q5.** How many solutions does $x+y+z=5$ have with $x,y,z\ge0$ integers?
- A. 10
- B. 15
- C. 6
- D. 21

<details><summary>Answer</summary>

**D** — Stars and bars: $\binom{5+2}{2}=\binom72=21$.

</details>

**Q6.** A drawer has socks in 4 colours. How many socks must you take (without looking) to be sure of a pair of the same colour?
- A. 4
- B. 5
- C. 8
- D. 9

<details><summary>Answer</summary>

**B** — Worst case: one sock of each colour (4). The next sock makes a pair: $4+1=5$.

</details>

**Q7.** How many functions are there from a 3-element set to a 4-element set?
- A. 64
- B. 81
- C. 24
- D. 12

<details><summary>Answer</summary>

**A** — Each of the 3 elements has 4 choices: $4^3=64$. (81 is $3^4$, the wrong direction.)

</details>

**Q8.** How many **injective** functions are there from $\{1,2,3\}$ to $\{1,2,3,4,5\}$?
- A. 125
- B. 10
- C. 60
- D. 243

<details><summary>Answer</summary>

**C** — The images must be different: $5\cdot4\cdot3=60$.

</details>

**Q9.** On $\mathbb Z$ let $x\sim y\iff 7\mid x-y$. How many equivalence classes are there?
- A. 6
- B. 7
- C. 8
- D. infinitely many

<details><summary>Answer</summary>

**B** — The classes are the remainders $[0],[1],\dots,[6]$.

</details>

**Q10.** $|A|=20$, $|B|=15$, $|A\cap B|=5$. What is $|A\cup B|$?
- A. 35
- B. 25
- C. 40
- D. 30

<details><summary>Answer</summary>

**D** — $20+15-5=30$.

</details>

**Q11.** What is $\sum_{k=0}^{6}\binom6k$?
- A. 36
- B. 64
- C. 720
- D. 63

<details><summary>Answer</summary>

**B** — Put $x=y=1$ in the binomial theorem: $2^6=64$.

</details>

**Q12.** What is the coefficient of $x^3$ in $(1+2x)^5$?
- A. 10
- B. 40
- C. 80
- D. 160

<details><summary>Answer</summary>

**C** — The term is $\binom53(2x)^3=10\cdot8\,x^3=80x^3$. (10 forgets the factor $2^3$.)

</details>

**Q13.** Let $f:A\to B$ and $U,V\subseteq A$, $Y,Z\subseteq B$. Which statement is NOT true for every $f$?
- A. $f^{-1}(Y\cup Z)=f^{-1}(Y)\cup f^{-1}(Z)$
- B. $f^{-1}(Y\cap Z)=f^{-1}(Y)\cap f^{-1}(Z)$
- C. $f(U\cup V)=f(U)\cup f(V)$
- D. $f(U\cap V)=f(U)\cap f(V)$

<details><summary>Answer</summary>

**D** — Counterexample: $f(x)=x^2$, $U=\{-1\}$, $V=\{1\}$. Then $f(U\cap V)=\emptyset$ but $f(U)\cap f(V)=\{1\}$.

</details>

**Q14.** The relation $a\le b$ on $\mathbb Z$ is
- A. an equivalence relation
- B. a partial order
- C. symmetric
- D. not transitive

<details><summary>Answer</summary>

**B** — It is reflexive, antisymmetric and transitive. It is not symmetric ($1\le2$ but $2\not\le1$), so it is not an equivalence relation.

</details>

**Q15.** In how many ways can 10 identical sweets be given to 4 children so that **every child gets at least one**?
- A. 84
- B. 286
- C. 210
- D. 120

<details><summary>Answer</summary>

**A** — Positive solutions: $\binom{10-1}{4-1}=\binom93=84$. (286 $=\binom{13}3$ allows zero.)

</details>

**Q16.** How many integers in $\{1,\dots,100\}$ are divisible by 2 or by 3?
- A. 83
- B. 50
- C. 67
- D. 66

<details><summary>Answer</summary>

**C** — By 2: 50. By 3: 33. By 6: 16. So $50+33-16=67$.

</details>

**Q17.** How many different words can be made from the letters of BANANA?
- A. 720
- B. 60
- C. 120
- D. 20

<details><summary>Answer</summary>

**B** — 6 letters, A three times, N twice: $\frac{6!}{3!\,2!}=\frac{720}{12}=60$.

</details>

**Q18.** What is the smallest $n_0$ such that $2^n>n^2$ for **all** $n\ge n_0$?
- A. 3
- B. 4
- C. 1
- D. 5

<details><summary>Answer</summary>

**D** — $2^3=8<9$ and $2^4=16=16$ (not $>$). From $n=5$ on: $32>25$, and induction continues.

</details>

**Q19.** Which set is uncountable?
- A. $\mathbb Q$
- B. $\mathbb N\times\mathbb N$
- C. $\mathcal P(\mathbb N)$, the set of all subsets of $\mathbb N$
- D. the set of finite subsets of $\mathbb N$

<details><summary>Answer</summary>

**C** — By Cantor's theorem $\mathcal P(\mathbb N)$ is bigger than $\mathbb N$. The others are countable (B by $(a,b)\mapsto2^a3^b$).

</details>

**Q20.** How many numbers must you choose from $\{1,2,\dots,10\}$ to be sure that two of them add up to 11?
- A. 6
- B. 5
- C. 7
- D. 11

<details><summary>Answer</summary>

**A** — 5 boxes $\{1,10\},\{2,9\},\{3,8\},\{4,7\},\{5,6\}$. With 6 numbers two share a box. 5 is not enough: $1,2,3,4,5$.

</details>

**Q21.** A committee of 3 is chosen from 5 men and 4 women. How many committees have **exactly 2 women**?
- A. 84
- B. 30
- C. 40
- D. 60

<details><summary>Answer</summary>

**B** — Choose 2 women: $\binom42=6$. Choose 1 man: $\binom51=5$. Product rule: $6\cdot5=30$.

</details>

**Q22.** $a_0=0$ and $a_n=2a_{n-1}+1$. What is $a_5$?
- A. 32
- B. 16
- C. 31
- D. 63

<details><summary>Answer</summary>

**C** — Terms: $0,1,3,7,15,31$. In general $a_n=2^n-1$.

</details>

**Q23.** How many permutations of $\{1,2,3,4\}$ leave **no** number in its own place?
- A. 6
- B. 8
- C. 12
- D. 9

<details><summary>Answer</summary>

**D** — Derangements: $D_4=24\left(1-1+\frac12-\frac16+\frac1{24}\right)=12-4+1=9$.

</details>

**Q24.** What is the coefficient of $x^4$ in $\dfrac1{(1-x)^3}$?
- A. 10
- B. 15
- C. 20
- D. 35

<details><summary>Answer</summary>

**B** — $\binom{n+k-1}{k-1}$ with $n=4$, $k=3$: $\binom62=15$. (Same as solutions of $x+y+z=4$.)

</details>

**Q25.** For $n\ge1$, what is $\sum_{k=0}^{n}(-1)^k\binom nk$?
- A. 0
- B. 1
- C. $2^n$
- D. $(-1)^n$

<details><summary>Answer</summary>

**A** — Put $x=-1$, $y=1$ in the binomial theorem: $(-1+1)^n=0^n=0$.

</details>

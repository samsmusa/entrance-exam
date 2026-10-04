# 2. Algebra

> **Syllabus (official):**
> - Group theory, rings, fields
> - Homeo-/iso-morphisms
> - Eigenvalues, eigenvectors
> - Linear operators
> - Galois theory
>
> **How to study this file:** Sections 1–6 are 🟢 core. Learn them well: determinants, rank, linear maps, eigenvalues, groups and $\mathbb Z_m$. Sections 7–8 are 🟡: learn only the facts in the boxes.
> Time: about 4–5 hours for the 🟢 sections, 30 minutes for the 🟡 sections. Then do the MCQs at the end.

## Contents
1. [Matrices and determinants](#1-matrices-and-determinants-) 🟢
2. [Linear systems and rank](#2-linear-systems-and-rank-) 🟢
3. [Linear operators (linear maps)](#3-linear-operators-linear-maps-) 🟢
4. [Eigenvalues and eigenvectors](#4-eigenvalues-and-eigenvectors-) 🟢
5. [Groups](#5-groups-) 🟢
6. [Rings and fields](#6-rings-and-fields-) 🟢
7. [Homomorphisms and isomorphisms](#7-homomorphisms-and-isomorphisms-) 🟡
8. [Galois theory](#8-galois-theory-) 🟡
9. [Formula sheet](#formula-sheet)
10. [Practice MCQs](#practice-mcqs)

---

## 1. Matrices and determinants 🟢

### What it means
The **determinant** $\det A$ is one number that you compute from a square matrix $A$ ($n$ rows, $n$ columns).
- $\det A\neq 0$ means $A$ is **invertible** (there is $A^{-1}$ with $AA^{-1}=I$).
- $\det A=0$ means $A$ is **singular** (not invertible).
- Geometric meaning: $|\det A|$ is the area (in 2D) or volume (in 3D) of the shape made by the columns.

### Formulas
**$2\times2$:**
$$\det\begin{pmatrix}a&b\\c&d\end{pmatrix}=ad-bc,\qquad A^{-1}=\frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}.$$

**$3\times3$ (expansion along the first row):**
$$\det\begin{pmatrix}a&b&c\\d&e&f\\g&h&i\end{pmatrix}=a(ei-fh)-b(di-fg)+c(dh-eg).$$

**Triangular matrix** (all zeros below or above the diagonal): $\det$ = product of the diagonal entries.

### Worked example 1 ($2\times2$)
$A=\begin{pmatrix}2&1\\5&3\end{pmatrix}$.
1. $\det A=2\cdot3-1\cdot5=6-5=1$.
2. $A^{-1}=\frac11\begin{pmatrix}3&-1\\-5&2\end{pmatrix}$.
3. Check: $\begin{pmatrix}2&1\\5&3\end{pmatrix}\begin{pmatrix}3&-1\\-5&2\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}$ ✓.

### Worked example 2 ($3\times3$)
$A=\begin{pmatrix}1&2&0\\3&1&2\\0&1&1\end{pmatrix}$.
1. First entry $1$: $1\cdot(1\cdot1-2\cdot1)=1\cdot(-1)=-1$.
2. Second entry $2$ (minus sign!): $-2\cdot(3\cdot1-2\cdot0)=-2\cdot3=-6$.
3. Third entry $0$: gives $0$.
4. $\det A=-1-6+0=-7$.

### Rules (very important for the MCQ)
Here $A,B$ are $n\times n$ and $\alpha$ is a number.

| Rule | Formula |
|---|---|
| scalar times matrix | $\det(\alpha A)=\alpha^n\det A$ |
| product | $\det(AB)=\det A\cdot\det B$ |
| inverse | $\det(A^{-1})=\dfrac1{\det A}$ |
| transpose | $\det(A^T)=\det A$ |
| power | $\det(A^k)=(\det A)^k$ |
| swap two rows | sign changes |
| multiply one row by $c$ | det is multiplied by $c$ |
| add a multiple of one row to another | det does not change |
| two equal rows, or a zero row | $\det=0$ |

**Example (official problem 7):** $A$ is $3\times3$ with $\det A=2$. Then $\det(3A)=3^3\cdot2=54$.

**Example:** $A$ is $4\times4$ with $\det A=5$. Then $\det(-A)=(-1)^4\cdot5=5$ and $\det(2A^{-1})=2^4\cdot\frac15=\frac{16}5$.

### Volume (official problem 8)
For vectors $a,b,c\in\mathbb R^3$: volume of the box (parallelepiped) $=|\det(a\ b\ c)|$.
Area of a parallelogram in $\mathbb R^2$ $=|\det(a\ b)|$. Volume $0$ means the vectors are linearly dependent.

**Example:** $a=(1,0,0)$, $b=(1,2,0)$, $c=(1,1,3)$. The matrix with these rows is triangular, so $\det=1\cdot2\cdot3=6$. Volume $=6$.

> **Trap:** $\det(\alpha A)$ is $\alpha^n\det A$, **not** $\alpha\det A$. Also $\det(A+B)\neq\det A+\det B$ in general.

---

## 2. Linear systems and rank 🟢

### What it means
The **rank** of a matrix $A$ = the number of linearly independent rows (= number of independent columns).
To find it: bring $A$ to row echelon form (Gauss elimination). Rank = number of non-zero rows.

### Worked example
$A=\begin{pmatrix}1&2&3\\2&4&6\\1&0&1\end{pmatrix}$.
1. Row 2 minus $2\cdot$Row 1: $(0,0,0)$.
2. Row 3 minus Row 1: $(0,-2,-2)$.
3. Non-zero rows: $(1,2,3)$ and $(0,-2,-2)$. So $\operatorname{rank}A=2$.
4. Since rank $<3$: $\det A=0$.

### Solving $Ax=b$
$A$ has $m$ rows and $n$ columns ($n$ = number of unknowns). $(A\mid b)$ is $A$ with the extra column $b$.

| Situation | Result |
|---|---|
| $\operatorname{rank}A<\operatorname{rank}(A\mid b)$ | **no** solution |
| $\operatorname{rank}A=\operatorname{rank}(A\mid b)=n$ | **exactly one** solution |
| $\operatorname{rank}A=\operatorname{rank}(A\mid b)=r<n$ | **infinitely many**: $n-r$ free parameters |

The solution set is "one particular solution + all solutions of $Ax=0$".
- If $b=0$, it is a **linear subspace** of dimension $n-r$.
- If $b\neq0$, it is an **affine subspace** (a shifted subspace) of dimension $n-r$.

**Example (official problem 12):** $A$ is $m\times(m+2)$, $\operatorname{rank}A=\operatorname{rank}(A\mid b)=m-1$.
Free parameters $=(m+2)-(m-1)=3$. The solutions form a 3-dimensional affine subspace.

**Square systems:** $A$ is $n\times n$. Then $Ax=b$ has exactly one solution for every $b$ $\iff\det A\neq0$.

> **Trap:** "more unknowns than equations" does **not** guarantee a solution. It only means: if there is a solution, there are infinitely many.

---

## 3. Linear operators (linear maps) 🟢

### What it means
A map $T:V\to W$ between vector spaces is **linear** if
$$T(u+v)=T(u)+T(v)\quad\text{and}\quad T(\alpha v)=\alpha T(v).$$
A **linear operator** is a linear map from a space to itself ($V\to V$).
Every linear map $\mathbb R^n\to\mathbb R^m$ is $T(x)=Ax$ for an $m\times n$ matrix $A$. The **columns of $A$ are the images of the basis vectors** $e_1,\dots,e_n$.

- **Kernel** $\ker T=\{v: T(v)=0\}$ (what is sent to zero).
- **Image** $\operatorname{im}T=\{T(v)\}$ (everything you can reach). $\dim\operatorname{im}T=\operatorname{rank}A$.

### Rank–nullity formula
$$\dim\ker T+\operatorname{rank}T=\dim V\ (=n,\text{ the number of columns}).$$

### Worked example
$T:\mathbb R^3\to\mathbb R^2$, $T(x,y,z)=(x+y,\ y+z)$.
1. Matrix: $A=\begin{pmatrix}1&1&0\\0&1&1\end{pmatrix}$. Rank $=2$ (two independent rows).
2. Rank–nullity: $\dim\ker T=3-2=1$.
3. Check: $T(x,y,z)=0\Rightarrow y=-x,\ z=x$. So $\ker T=\{t(1,-1,1)\}$, a line ✓.
4. Image has dimension 2 $=\dim\mathbb R^2$, so $T$ is surjective (onto).

### Quick tests
| Statement | When true |
|---|---|
| $T$ injective (one-to-one) | $\ker T=\{0\}$ |
| $T$ surjective (onto) | $\operatorname{rank}T=\dim W$ |
| $T:\mathbb R^n\to\mathbb R^m$ with $n>m$ | never injective |
| $T:\mathbb R^n\to\mathbb R^m$ with $n<m$ | never surjective |
| operator on $\mathbb R^n$ (square $A$) | injective $\iff$ surjective $\iff\det A\neq0$ |

**Is it linear?** Quick check: $T(0)$ must be $0$. So $T(x)=x+1$ is **not** linear. $T(x)=x^2$ is not linear either ($T(2x)\neq2T(x)$).

**Standard examples:** rotation in $\mathbb R^2$ ($\det=1$), reflection ($\det=-1$), projection onto the $x$-axis $\begin{pmatrix}1&0\\0&0\end{pmatrix}$ (rank 1). Differentiation $D(p)=p'$ on polynomials is linear; its kernel is the constants.

> **Trap:** a function like $f(x)=2x+3$ is called "linear" in school, but it is **not** a linear map (it is affine), because $f(0)\neq0$.

---

## 4. Eigenvalues and eigenvectors 🟢

### What it means
A vector $v\neq0$ is an **eigenvector** of $A$ if $A$ only stretches it:
$$Av=\lambda v.$$
The number $\lambda$ is the **eigenvalue**. ($\lambda$ may be $0$; $v$ may **not** be $0$.)

### How to compute
1. Solve the **characteristic equation** $\det(A-\lambda I)=0$. The roots are the eigenvalues.
2. For each $\lambda$, solve $(A-\lambda I)v=0$ to get the eigenvectors.

**Shortcut for $2\times2$:** $\lambda^2-(\operatorname{tr}A)\lambda+\det A=0$, where $\operatorname{tr}A$ (trace) = sum of the diagonal entries.

### Worked example
$A=\begin{pmatrix}4&1\\2&3\end{pmatrix}$.
1. $\operatorname{tr}A=4+3=7$, $\det A=12-2=10$.
2. $\lambda^2-7\lambda+10=0\Rightarrow(\lambda-2)(\lambda-5)=0$, so $\lambda=2$ or $\lambda=5$.
3. $\lambda=5$: $A-5I=\begin{pmatrix}-1&1\\2&-2\end{pmatrix}$, so $-x+y=0$, $v=(1,1)$.
4. $\lambda=2$: $A-2I=\begin{pmatrix}2&1\\2&1\end{pmatrix}$, so $2x+y=0$, $v=(1,-2)$.
5. Check: $A(1,1)^T=(5,5)^T=5\cdot(1,1)^T$ ✓.

### Facts you can use without calculation
| Fact | Formula |
|---|---|
| sum of eigenvalues | $=\operatorname{tr}A$ |
| product of eigenvalues | $=\det A$ |
| triangular / diagonal matrix | eigenvalues = diagonal entries |
| $A^k$, $A^{-1}$, $A+cI$, $cA$ | $\lambda^k$, $1/\lambda$, $\lambda+c$, $c\lambda$ (same eigenvectors) |
| $A^T$ | same eigenvalues as $A$ |
| $0$ is an eigenvalue | $\iff\det A=0$ |
| real symmetric $A=A^T$ | all eigenvalues are real |
| every row sums to $s$ | $s$ is an eigenvalue, eigenvector $(1,\dots,1)$ |

**Example:** a $3\times3$ matrix has eigenvalues $1,2,3$. Then $\operatorname{tr}A=6$, $\det A=6$, and $A^2$ has eigenvalues $1,4,9$.

### Diagonalizable
$A$ ($n\times n$) is **diagonalizable** if it has $n$ linearly independent eigenvectors. Then $A=PDP^{-1}$ with $D$ diagonal (eigenvalues) and $P$ = eigenvectors as columns.
- $n$ **different** eigenvalues $\Rightarrow$ diagonalizable.
- Real symmetric $\Rightarrow$ diagonalizable.
- Standard counterexample: $\begin{pmatrix}1&1\\0&1\end{pmatrix}$. Eigenvalue $1$ (twice), but only one eigenvector direction $(1,0)$. **Not** diagonalizable.

> **Trap:** a repeated eigenvalue does not always mean "not diagonalizable" ($I$ is diagonal!). Also: do **not** row-reduce $A$ before computing eigenvalues; that changes them.

---

## 5. Groups 🟢

### What it means
A **group** $(G,\ast)$ is a set $G$ with an operation $\ast$ such that:
1. **Closed:** $a\ast b\in G$.
2. **Associative:** $(a\ast b)\ast c=a\ast(b\ast c)$.
3. **Identity** $e$: $e\ast a=a\ast e=a$.
4. **Inverses:** every $a$ has $a^{-1}$ with $a\ast a^{-1}=a^{-1}\ast a=e$.

**Abelian** group: also $a\ast b=b\ast a$ for all $a,b$.

### Examples
| Set and operation | Group? | Reason |
|---|---|---|
| $(\mathbb Z,+)$, $(\mathbb Q,+)$, $(\mathbb R,+)$ | yes | identity 0, inverse $-a$ |
| $(\mathbb Z,\cdot)$ | **no** | $2$ has no inverse in $\mathbb Z$ |
| $(\mathbb R\setminus\{0\},\cdot)$ | yes | inverse $1/a$ |
| $(\mathbb N,+)$ | **no** | no negatives |
| $(\mathbb Z_n,+)$ (remainders mod $n$) | yes | |
| invertible $n\times n$ matrices, $\cdot$ | yes, **not** abelian ($n\ge2$) | |
| $S_n$ (permutations of $n$ objects) | yes, $\lvert S_n\rvert=n!$, not abelian for $n\ge3$ | |

### Basic rules (official problem 5)
- **Cancellation:** $xz=yz\Rightarrow x=y$. Proof: multiply on the right by $z^{-1}$:
  $x=x(zz^{-1})=(xz)z^{-1}=(yz)z^{-1}=y$.
- $(ab)^{-1}=b^{-1}a^{-1}$ (order changes!).
- The identity and each inverse are unique.

### Order of an element
The **order** of $a$ = the smallest $k\ge1$ with $a^k=e$ (in additive notation: $k\cdot a=0$).

In $(\mathbb Z_n,+)$: $\operatorname{ord}(k)=\dfrac{n}{\gcd(k,n)}$.

**Example:** order of $8$ in $\mathbb Z_{12}$: $\frac{12}{\gcd(8,12)}=\frac{12}{4}=3$. Check: $8,\ 16\equiv4,\ 24\equiv0$ ✓.

### Lagrange's theorem
If $H$ is a subgroup of a finite group $G$, then $|H|$ divides $|G|$. So also $\operatorname{ord}(a)$ divides $|G|$.

**Example:** $|G|=12$. Possible subgroup orders: $1,2,3,4,6,12$. A subgroup of order $5$ is impossible.

Consequence: a group of **prime** order $p$ is cyclic (generated by any $a\neq e$).

### Cyclic groups
$G$ is **cyclic** if $G=\{g^k\}$ for one element $g$ (a **generator**).
In $\mathbb Z_n$: $k$ is a generator $\iff\gcd(k,n)=1$. Example: generators of $\mathbb Z_8$ are $1,3,5,7$.

### Permutations (short)
$\sigma=(1\,2\,3)(4\,5)$ means $1\to2\to3\to1$ and $4\leftrightarrow5$.
Order of a permutation = **lcm** of the lengths of its disjoint cycles. Example: $\operatorname{lcm}(3,2)=6$.

> **Trap:** in a non-abelian group, $xz=zy$ does **not** give $x=y$. Cancel only on the same side.

---

## 6. Rings and fields 🟢

### What it means
- A **ring** has $+$ and $\cdot$. With $+$ it is an abelian group, $\cdot$ is associative, and the distributive law holds. Examples: $\mathbb Z$, $\mathbb Z_n$, polynomials, $n\times n$ matrices.
- A **field** is a commutative ring where every element $\neq0$ has a multiplicative inverse. Examples: $\mathbb Q$, $\mathbb R$, $\mathbb C$, $\mathbb Z_p$ ($p$ prime). Not fields: $\mathbb Z$, $\mathbb Z_6$.
- A **zero divisor** is $a\neq0$ with $ab=0$ for some $b\neq0$. A field has **no** zero divisors.

### The key fact (official problem 20)
$$\mathbb Z_m\text{ is a field}\iff m\text{ is prime}.$$
$$a\text{ has an inverse in }\mathbb Z_m\iff\gcd(a,m)=1.$$

**Why composite $m$ fails:** $m=ab$ with $1<a,b<m$. Then $a\neq0$, $b\neq0$, but $a\cdot b=m\equiv0$. Zero divisors, so no field.
Example: in $\mathbb Z_6$, $2\cdot3=6\equiv0$.

### Worked example: inverse in $\mathbb Z_7$
Find $3^{-1}$ in $\mathbb Z_7$. Try the multiples of 3: $3\cdot1=3$, $3\cdot2=6$, $3\cdot3=9\equiv2$, $3\cdot4=12\equiv5$, $3\cdot5=15\equiv1$ ✓. So $3^{-1}=5$.

### Units and zero divisors in $\mathbb Z_{12}$
- Units (invertible): $\gcd(a,12)=1$: $\{1,5,7,11\}$, that is $\varphi(12)=4$ elements.
- Zero divisors: the other non-zero elements $\{2,3,4,6,8,9,10\}$. Example: $4\cdot3=12\equiv0$.

### Characteristic
$\operatorname{char}F$ = the smallest $n\ge1$ with $1+1+\dots+1$ ($n$ times) $=0$; it is $0$ if this never happens.
$\operatorname{char}\mathbb Q=\operatorname{char}\mathbb R=0$, $\operatorname{char}\mathbb Z_p=p$. A field has characteristic $0$ or a prime.

### Polynomials (short)
- A polynomial of degree $n$ over a field has **at most $n$ roots**.
- Degree 2 or 3: irreducible (cannot be factored) $\iff$ it has **no root** in the field.
- Example: $x^2+1$ has no real root, so it is irreducible over $\mathbb R$. Over $\mathbb C$ it is $(x-i)(x+i)$.

> **Trap:** $\mathbb Z_4$ is **not** a field ($2\cdot2=0$). A finite field with 4 elements exists, but it is a different object ($\mathbb F_4$).

---

## 7. Homomorphisms and isomorphisms 🟡

### What it means
A **homomorphism** is a map that respects the operation: $f(a\ast b)=f(a)\ast f(b)$.
An **isomorphism** is a homomorphism that is also bijective. "Isomorphic" ($G\cong H$) means: the same structure, only different names.
A **homeomorphism** is something different (topology): a continuous bijection whose inverse is also continuous.

### Must-know facts
> 1. A homomorphism sends identity to identity: $f(e)=e$. So $f(x)=x+1$ on $(\mathbb Z,+)$ is **not** a homomorphism.
> 2. **Kernel** $\ker f=\{a: f(a)=e\}$. $f$ is injective $\iff\ker f=\{e\}$.
> 3. Example: $f:\mathbb Z\to\mathbb Z_5$, $f(k)=k\bmod5$. Kernel $=5\mathbb Z$ (multiples of 5).
> 4. Example: $\exp:(\mathbb R,+)\to(\mathbb R_{>0},\cdot)$, $e^{x+y}=e^xe^y$. It is an isomorphism.
> 5. $\det:$ invertible matrices $\to\mathbb R\setminus\{0\}$ is a homomorphism, since $\det(AB)=\det A\det B$.
> 6. Isomorphic groups have the same size and the same element orders. $\mathbb Z_4\not\cong\mathbb Z_2\times\mathbb Z_2$ ($\mathbb Z_4$ has an element of order 4, the other does not). Homeomorphism example: $(0,1)$ and $\mathbb R$ are homeomorphic.

> **Trap:** homo**morphism** (algebra) ≠ homeo**morphism** (topology).

---

## 8. Galois theory 🟡

### What it means (one line)
Galois theory connects the roots of a polynomial with a group (the **Galois group**) that permutes these roots.

### Must-know facts
> 1. **Field extension** $L/K$: $K\subseteq L$ are fields. The **degree** $[L:K]$ = dimension of $L$ as a vector space over $K$. Example: $[\mathbb C:\mathbb R]=2$ (basis $1,i$), $[\mathbb Q(\sqrt2):\mathbb Q]=2$ (basis $1,\sqrt2$).
> 2. **Tower law:** $[M:K]=[M:L]\cdot[L:K]$. Example: $[\mathbb Q(\sqrt2,\sqrt3):\mathbb Q]=2\cdot2=4$.
> 3. $[\mathbb Q(\sqrt[3]2):\mathbb Q]=3$, because $x^3-2$ is irreducible over $\mathbb Q$.
> 4. Galois group of $x^2-2$ over $\mathbb Q$ has 2 elements (swap $\sqrt2\leftrightarrow-\sqrt2$). For a polynomial of degree $n$ the Galois group is a subgroup of $S_n$.
> 5. **Abel–Ruffini:** the general polynomial of degree $\ge5$ cannot be solved by radicals (no formula with $+,-,\cdot,/,\sqrt[k]{\ }$). Degrees $\le4$ can.
> 6. **Constructions** with ruler and compass: doubling the cube and trisecting a general angle are impossible.

---

## Formula sheet

| Topic | Formula / fact |
|---|---|
| $2\times2$ det | $ad-bc$ |
| $2\times2$ inverse | $\frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$ |
| scalar | $\det(\alpha A)=\alpha^n\det A$ |
| product, inverse, transpose | $\det(AB)=\det A\det B$, $\det A^{-1}=1/\det A$, $\det A^T=\det A$ |
| triangular | det = product of diagonal |
| volume | $V=\lvert\det(a\ b\ c)\rvert$ |
| invertible | $\det A\neq0\iff\operatorname{rank}A=n\iff0$ not an eigenvalue |
| $Ax=b$ | solvable $\iff\operatorname{rank}A=\operatorname{rank}(A\mid b)$; free parameters $=n-\operatorname{rank}A$ |
| rank–nullity | $\dim\ker T+\operatorname{rank}T=\dim V$ |
| eigen ($2\times2$) | $\lambda^2-(\operatorname{tr}A)\lambda+\det A=0$ |
| eigen sums | $\sum\lambda_i=\operatorname{tr}A$, $\prod\lambda_i=\det A$ |
| eigen of $A^k$, $A^{-1}$, $A+cI$ | $\lambda^k$, $1/\lambda$, $\lambda+c$ |
| group inverse | $(ab)^{-1}=b^{-1}a^{-1}$ |
| order in $\mathbb Z_n$ | $n/\gcd(k,n)$ |
| Lagrange | $\lvert H\rvert$ divides $\lvert G\rvert$ |
| permutation order | lcm of cycle lengths; $\lvert S_n\rvert=n!$ |
| $\mathbb Z_m$ | field $\iff m$ prime; $a$ invertible $\iff\gcd(a,m)=1$ |
| tower law | $[M:K]=[M:L][L:K]$ |

---

## Practice MCQs

**Q1.** What is $\det\begin{pmatrix}3&2\\1&4\end{pmatrix}$?
A) 14  B) 10  C) 12  D) 2
<details><summary>Answer</summary>

**B** — $3\cdot4-2\cdot1=12-2=10$.

</details>

**Q2.** $A$ is a $3\times3$ matrix with $\det A=2$. What is $\det(3A)$?
A) 6  B) 18  C) 27  D) 54
<details><summary>Answer</summary>

**D** — $\det(3A)=3^3\cdot\det A=27\cdot2=54$. (The answer 6 is the trap $\alpha\det A$.)

</details>

**Q3.** $\det A=5$. What is $\det(A^{-1})$?
A) $\frac15$  B) $-5$  C) $5$  D) $25$
<details><summary>Answer</summary>

**A** — $\det(A^{-1})=1/\det A=1/5$.

</details>

**Q4.** What are the eigenvalues of $\begin{pmatrix}2&5\\0&7\end{pmatrix}$?
A) $5$ and $7$  B) $2$ and $5$  C) $2$ and $7$  D) $0$ and $9$
<details><summary>Answer</summary>

**C** — The matrix is triangular, so the eigenvalues are the diagonal entries $2$ and $7$.

</details>

**Q5.** Which of these is a field?
A) $\mathbb Z_6$  B) $\mathbb Z_9$  C) $\mathbb Z$  D) $\mathbb Z_7$
<details><summary>Answer</summary>

**D** — $\mathbb Z_m$ is a field exactly when $m$ is prime; $7$ is prime. In $\mathbb Z$ the element $2$ has no inverse.

</details>

**Q6.** What is the inverse of $3$ in $\mathbb Z_7$?
A) 5  B) 4  C) 2  D) 3
<details><summary>Answer</summary>

**A** — $3\cdot5=15=2\cdot7+1\equiv1$.

</details>

**Q7.** What is the rank of $\begin{pmatrix}1&2\\2&4\end{pmatrix}$?
A) 0  B) 1  C) 2  D) 4
<details><summary>Answer</summary>

**B** — Row 2 $=2\cdot$Row 1, so only one independent row. (Also $\det=4-4=0$, so the rank is less than 2.)

</details>

**Q8.** A group $G$ has 12 elements. Which number **cannot** be the order of a subgroup?
A) 4  B) 6  C) 5  D) 3
<details><summary>Answer</summary>

**C** — By Lagrange the subgroup order divides 12. $5$ does not divide 12.

</details>

**Q9.** What is the order of the element $8$ in $(\mathbb Z_{12},+)$?
A) 4  B) 8  C) 12  D) 3
<details><summary>Answer</summary>

**D** — $12/\gcd(8,12)=12/4=3$. Check: $8+8+8=24\equiv0$.

</details>

**Q10.** In any group, $(ab)^{-1}$ equals
A) $a^{-1}b^{-1}$  B) $b^{-1}a^{-1}$  C) $ba$  D) $ab$
<details><summary>Answer</summary>

**B** — $(ab)(b^{-1}a^{-1})=a(bb^{-1})a^{-1}=aa^{-1}=e$.

</details>

**Q11.** $A$ is $4\times4$ with $\det A=3$. What is $\det(2A^T)$?
A) 6  B) 24  C) 48  D) 81
<details><summary>Answer</summary>

**C** — $\det(2A^T)=2^4\det A^T=16\cdot3=48$.

</details>

**Q12.** $\det A=2$ and $\det B=-3$ ($A,B$ are $n\times n$). What is $\det(AB^{-1})$?
A) $-\frac23$  B) $-6$  C) $\frac23$  D) $-1$
<details><summary>Answer</summary>

**A** — $\det(AB^{-1})=\det A\cdot\frac1{\det B}=2\cdot\frac1{-3}=-\frac23$.

</details>

**Q13.** $A$ is a $3\times5$ matrix, and $\operatorname{rank}A=\operatorname{rank}(A\mid b)=3$. The system $Ax=b$ has
A) no solution  B) exactly one solution  C) infinitely many solutions, with 3 free parameters  D) infinitely many solutions, with 2 free parameters
<details><summary>Answer</summary>

**D** — The ranks are equal, so it is solvable. Free parameters $=5-3=2$.

</details>

**Q14.** $T:\mathbb R^5\to\mathbb R^3$ is linear and surjective. What is $\dim\ker T$?
A) 2  B) 3  C) 5  D) 0
<details><summary>Answer</summary>

**A** — Surjective means rank $=3$. Rank–nullity: $\dim\ker T=5-3=2$.

</details>

**Q15.** What are the eigenvalues of $\begin{pmatrix}4&1\\2&3\end{pmatrix}$?
A) $1$ and $6$  B) $3$ and $4$  C) $-2$ and $-5$  D) $2$ and $5$
<details><summary>Answer</summary>

**D** — $\operatorname{tr}=7$, $\det=10$: $\lambda^2-7\lambda+10=(\lambda-2)(\lambda-5)$.

</details>

**Q16.** A $3\times3$ matrix $A$ has eigenvalues $1,2,3$. What is $\det(2A)$?
A) 12  B) 48  C) 6  D) 36
<details><summary>Answer</summary>

**B** — $\det A=1\cdot2\cdot3=6$, so $\det(2A)=2^3\cdot6=48$.

</details>

**Q17.** Which matrix is **not** diagonalizable?
A) $\begin{pmatrix}1&1\\0&1\end{pmatrix}$  B) $\begin{pmatrix}2&0\\0&2\end{pmatrix}$  C) $\begin{pmatrix}1&2\\2&1\end{pmatrix}$  D) $\begin{pmatrix}1&0\\0&3\end{pmatrix}$
<details><summary>Answer</summary>

**A** — Eigenvalue 1 twice, but $(A-I)v=0$ gives only $v=(t,0)$: one direction. B and D are already diagonal, and C is symmetric.

</details>

**Q18.** What is the order of the permutation $(1\,2\,3)(4\,5)$ in $S_5$?
A) 5  B) 3  C) 6  D) 2
<details><summary>Answer</summary>

**C** — The cycles are disjoint, with lengths 3 and 2. Order $=\operatorname{lcm}(3,2)=6$.

</details>

**Q19.** Which element of $\mathbb Z_8$ is a zero divisor?
A) 3  B) 4  C) 5  D) 7
<details><summary>Answer</summary>

**B** — $4\cdot2=8\equiv0$ with $4\neq0$, $2\neq0$. The others are coprime to 8, so they are invertible.

</details>

**Q20.** Which map $f:(\mathbb Z,+)\to(\mathbb Z,+)$ is a group homomorphism?
A) $f(x)=x+1$  B) $f(x)=x^2$  C) $f(x)=3x$  D) $f(x)=\lvert x\rvert$
<details><summary>Answer</summary>

**C** — $3(x+y)=3x+3y$. A fails ($f(0)=1\neq0$). B fails: $f(1+1)=4\neq2$. D fails: $f(1+(-1))=0\neq2$.

</details>

**Q21.** What is the volume of the parallelepiped spanned by $(1,0,0)$, $(1,2,0)$, $(1,1,3)$?
A) 6  B) 3  C) 5  D) 1
<details><summary>Answer</summary>

**A** — The matrix with these rows is lower triangular: $\det=1\cdot2\cdot3=6$.

</details>

**Q22.** Is $v=(1,1)$ an eigenvector of $\begin{pmatrix}2&1\\1&2\end{pmatrix}$? If yes, for which eigenvalue?
A) No  B) Yes, $\lambda=1$  C) Yes, $\lambda=2$  D) Yes, $\lambda=3$
<details><summary>Answer</summary>

**D** — $Av=(2+1,\ 1+2)=(3,3)=3v$.

</details>

**Q23.** How many invertible elements (units) does $\mathbb Z_{12}$ have?
A) 4  B) 6  C) 11  D) 2
<details><summary>Answer</summary>

**A** — Units are the $a$ with $\gcd(a,12)=1$: $1,5,7,11$. That is $\varphi(12)=4$.

</details>

**Q24.** What is the degree $[\mathbb Q(\sqrt2,\sqrt3):\mathbb Q]$?
A) 2  B) 3  C) 6  D) 4
<details><summary>Answer</summary>

**D** — Tower law: $[\mathbb Q(\sqrt2):\mathbb Q]=2$, and $\sqrt3\notin\mathbb Q(\sqrt2)$ gives another factor 2. So $2\cdot2=4$.

</details>

**Q25.** $A$ is a $3\times3$ matrix with $\det A=0$. Which statement is **true**?
A) $A$ is invertible  B) $0$ is an eigenvalue of $A$  C) $\operatorname{rank}A=3$  D) $Ax=b$ has exactly one solution for every $b$
<details><summary>Answer</summary>

**B** — $\det A=\prod\lambda_i=0$, so some eigenvalue is 0. The other statements all mean "$\det A\neq0$".

</details>

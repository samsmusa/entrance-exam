# 2. Algebra

> **Official topics (Placement Test guide):** groups and group homomorphisms; rings, ideals and fields; kernels; vector spaces, linear maps and determinants; eigenvalues, eigenvectors, characteristic and minimal polynomial; field extensions and basics of Galois theory.
>
> **Exam:** 7 questions on this topic, 5 options each, about 85 seconds per question. Mostly definitions and standard facts, sometimes a 2×2 / 3×3 calculation.
>
> **How to study this file:** sections 1–8 are 🟢 core. Section 9 (Galois) is 🟡: learn the facts in the box. Time: about 5 hours for 🟢, 45 minutes for 🟡, then the MCQs.
>
> *Removed (not on the official list):* homeomorphisms (topology), ruler-and-compass constructions. Linear systems $Ax=b$ are kept only as a short part of section 2 (they are an application of rank–nullity).

## Contents
1. [Vector spaces, bases, dimension](#1-vector-spaces-bases-dimension-) 🟢
2. [Linear maps, kernel, image, rank](#2-linear-maps-kernel-image-rank-) 🟢
3. [Determinants](#3-determinants-) 🟢
4. [Eigenvalues, eigenvectors, characteristic polynomial](#4-eigenvalues-eigenvectors-characteristic-polynomial-) 🟢
5. [Minimal polynomial, Cayley–Hamilton, diagonalization](#5-minimal-polynomial-cayleyhamilton-diagonalization-) 🟢
6. [Groups](#6-groups-) 🟢
7. [Group homomorphisms, kernels, normal subgroups](#7-group-homomorphisms-kernels-normal-subgroups-) 🟢
8. [Rings, ideals and fields](#8-rings-ideals-and-fields-) 🟢
9. [Field extensions and Galois theory](#9-field-extensions-and-galois-theory-) 🟡
10. [Formula sheet](#formula-sheet)
11. [Practice MCQs](#practice-mcqs) (30 questions, 5 options)

---

## 1. Vector spaces, bases, dimension 🟢

### What it means
A **vector space** $V$ over a field $K$ (usually $\mathbb R$ or $\mathbb C$) is a set with addition and scalar multiplication such that
- $(V,+)$ is an abelian group (zero vector $0$, negatives $-v$),
- $\alpha(u+v)=\alpha u+\alpha v$, $(\alpha+\beta)v=\alpha v+\beta v$, $(\alpha\beta)v=\alpha(\beta v)$, $1\cdot v=v$.

**Subspace test.** $U\subseteq V$ is a subspace ⇔ $0\in U$, and $U$ is closed under $+$ and under scalar multiplication.

| Set | Subspace? | Why |
|---|---|---|
| $\{(x,y,z):x+2y-z=0\}$ | yes | solution set of $Ax=0$ |
| $\{(x,y):x+y=1\}$ | **no** | $0\notin U$ (it is an affine line) |
| $\{(x,y):x\ge0,y\ge0\}$ | **no** | $(-1)\cdot(1,1)\notin U$ |
| $\{(x,y):xy=0\}$ (the two axes) | **no** | $(1,0)+(0,1)=(1,1)\notin U$ |
| $\ker T$, $\operatorname{im}T$ of a linear map | yes | |

### Basis and dimension
- $v_1,\dots,v_k$ are **linearly independent** if $\alpha_1v_1+\dots+\alpha_kv_k=0$ only for $\alpha_1=\dots=\alpha_k=0$.
- **Span** = all linear combinations. A **basis** = linearly independent **and** spanning.
- **Dimension** = number of vectors in any basis (all bases have the same size).
- In an $n$-dimensional space: more than $n$ vectors are always dependent; $n$ independent vectors are automatically a basis.
- $n$ vectors in $K^n$ form a basis ⇔ the matrix with these columns has $\det\ne0$.

| Space | Dimension |
|---|---|
| $\mathbb R^n$ | $n$ |
| polynomials of degree $\le n$ | $n+1$ (basis $1,x,\dots,x^n$) |
| $m\times n$ matrices | $mn$ |
| symmetric $n\times n$ matrices | $\frac{n(n+1)}2$ |
| $\mathbb C$ over $\mathbb R$ | $2$ (basis $1,i$) |
| $C[a,b]$, all polynomials | infinite |

**Dimension formula:** $\dim(U+W)=\dim U+\dim W-\dim(U\cap W)$.

### Worked example
Are $(1,2,3)$, $(0,1,4)$, $(5,6,0)$ a basis of $\mathbb R^3$?
1. $\det\begin{pmatrix}1&2&3\\0&1&4\\5&6&0\end{pmatrix}=1(0-24)-2(0-20)+3(0-5)=-24+40-15=1$.
2. $\det\ne0$ ⇒ independent ⇒ basis (3 vectors in a 3-dim space).

> **Trap:** "dimension of polynomials of degree $\le3$" is $4$, not $3$ (don't forget the constant $1$).

---

## 2. Linear maps, kernel, image, rank 🟢

### What it means
$T:V\to W$ is **linear** if $T(u+v)=T(u)+T(v)$ and $T(\alpha v)=\alpha T(v)$. A **linear operator** is a linear map $V\to V$.
Every linear map $K^n\to K^m$ is $T(x)=Ax$ for an $m\times n$ matrix $A$; the **columns of $A$ are the images of the basis vectors** $e_1,\dots,e_n$.

- **Kernel** $\ker T=\{v:T(v)=0\}$ — a subspace of $V$.
- **Image** $\operatorname{im}T=\{T(v)\}$ — a subspace of $W$; $\dim\operatorname{im}T=\operatorname{rank}A$.
- **Rank** of $A$ = number of independent rows = number of independent columns = number of non-zero rows after Gauss elimination.

### Rank–nullity formula
$$\dim\ker T+\operatorname{rank}T=\dim V\ (=n,\text{ the number of columns}).$$

### Worked example
$T:\mathbb R^3\to\mathbb R^2$, $T(x,y,z)=(x+y,\ y+z)$.
1. $A=\begin{pmatrix}1&1&0\\0&1&1\end{pmatrix}$, rank $2$.
2. $\dim\ker T=3-2=1$: $\ker T=\{t(1,-1,1)\}$.
3. $\dim\operatorname{im}T=2=\dim\mathbb R^2$ ⇒ surjective.

**Rank by elimination.** $A=\begin{pmatrix}1&2&3\\2&4&6\\1&0&1\end{pmatrix}$: Row 2 minus $2 \cdot$ Row 1 $=(0, 0, 0)$, Row 3 − Row 1 $=(0,-2,-2)$. Two non-zero rows ⇒ rank $2$ ⇒ $\det A=0$.

### Quick tests
| Statement | When true |
|---|---|
| $T$ injective | $\ker T=\{0\}$ |
| $T$ surjective | $\operatorname{rank}T=\dim W$ |
| $T:K^n\to K^m$, $n>m$ | never injective |
| $T:K^n\to K^m$, $n<m$ | never surjective |
| operator on a finite-dim. space | injective ⇔ surjective ⇔ bijective ⇔ $\det\ne0$ |

**Is it linear?** $T(0)$ must be $0$: $T(x)=x+1$ is not linear (affine); $T(x)=x^2$ is not linear. Differentiation $p\mapsto p'$ is linear; its kernel is the constants.

### Linear systems $Ax=b$ ($A$ is $m\times n$)
| Situation | Result |
|---|---|
| $\operatorname{rank}A<\operatorname{rank}(A\mid b)$ | no solution |
| $\operatorname{rank}A=\operatorname{rank}(A\mid b)=n$ | exactly one solution |
| $\operatorname{rank}A=\operatorname{rank}(A\mid b)=r<n$ | infinitely many: $n-r$ free parameters |

Solution set = particular solution + $\ker A$ (an affine subspace of dimension $n-r$).
Example (official problem 12): $A$ is $m\times(m+2)$, both ranks $m-1$ ⇒ $3$ free parameters.

### Change of basis
The same operator in another basis has matrix $B=P^{-1}AP$ (**similar** matrices). Similar matrices have the same determinant, trace, rank, eigenvalues and characteristic/minimal polynomial. So $\det T$, $\operatorname{tr}T$ are well-defined for an operator $T$.

> **Trap:** $f(x)=2x+3$ is "linear" in school, but it is **not** a linear map ($f(0)\ne0$).

---

## 3. Determinants 🟢

### Formulas
$$\det\begin{pmatrix}a&b\\c&d\end{pmatrix}=ad-bc,\qquad A^{-1}=\frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}.$$
$$\det\begin{pmatrix}a&b&c\\d&e&f\\g&h&i\end{pmatrix}=a(ei-fh)-b(di-fg)+c(dh-eg).$$
**Triangular matrix:** $\det$ = product of the diagonal entries.

**Worked example.** $\det\begin{pmatrix}1&2&0\\3&1&2\\0&1&1\end{pmatrix}=1(1-2)-2(3-0)+0=-7$.

### Rules ($A,B$ are $n\times n$)
| Rule | Formula |
|---|---|
| scalar | $\det(\alpha A)=\alpha^n\det A$ |
| product | $\det(AB)=\det A\det B$ |
| inverse, transpose, power | $\det A^{-1}=\frac1{\det A}$, $\det A^T=\det A$, $\det A^k=(\det A)^k$ |
| swap two rows | sign changes |
| one row times $c$ | det times $c$ |
| add multiple of a row to another | no change |
| two equal rows / zero row | $\det=0$ |

Examples: $3\times3$, $\det A=2$ ⇒ $\det(3A)=27\cdot2=54$. $4\times4$, $\det A=5$ ⇒ $\det(2A^{-1})=\frac{16}{5}$.

**Volume:** $\lvert\det(a\ b\ c)\rvert$ = volume of the parallelepiped spanned by $a,b,c$; $0$ ⇔ dependent.

### The big equivalence (official example 2)
For an operator $T$ on an $n$-dimensional space (matrix $A$):
$$T\text{ invertible}\iff\det A\ne0\iff\ker T=\{0\}\iff\operatorname{rank}A=n\iff0\text{ is not an eigenvalue}.$$
Trace, real eigenvalues, diagonalizability have **nothing** to do with invertibility: $\operatorname{diag}(1,-1)$ is invertible with trace $0$; the zero matrix is diagonalizable but not invertible; a nilpotent matrix is never invertible.

> **Trap:** $\det(\alpha A)=\alpha^n\det A$, not $\alpha\det A$; and $\det(A+B)\ne\det A+\det B$ in general.

---

## 4. Eigenvalues, eigenvectors, characteristic polynomial 🟢

### What it means
$v\ne0$ is an **eigenvector** of $A$ with **eigenvalue** $\lambda$ if $Av=\lambda v$. ($\lambda=0$ is allowed; $v=0$ is not.)
The **eigenspace** $E_\lambda=\ker(A-\lambda I)$.

### Characteristic polynomial
$$p_A(\lambda)=\det(\lambda I-A)\quad(\text{some books use }\det(A-\lambda I)\text{, same roots}).$$
- Degree $n$, monic: $p_A(\lambda)=\lambda^n-(\operatorname{tr}A)\lambda^{n-1}+\dots+(-1)^n\det A$.
- The eigenvalues are exactly the roots of $p_A$.
- $2\times2$: $p_A(\lambda)=\lambda^2-(\operatorname{tr}A)\lambda+\det A$.

**Worked example.** $A=\begin{pmatrix}4&1\\2&3\end{pmatrix}$.
1. $\operatorname{tr}A=7$, $\det A=10$: $p_A=\lambda^2-7\lambda+10=(\lambda-2)(\lambda-5)$.
2. $\lambda=5$: $(A-5I)v=0$ ⇒ $-x+y=0$, $v=(1,1)$.
3. $\lambda=2$: $2x+y=0$, $v=(1,-2)$.

### Multiplicities
- **Algebraic multiplicity** of $\lambda$ = its multiplicity as a root of $p_A$.
- **Geometric multiplicity** = $\dim E_\lambda=n-\operatorname{rank}(A-\lambda I)$.
- Always $1\le\text{geometric}\le\text{algebraic}$.

### Facts you can use without calculation
| Fact | Formula |
|---|---|
| sum / product of eigenvalues | $\operatorname{tr}A$ / $\det A$ |
| triangular / diagonal | eigenvalues = diagonal entries |
| $A^k$, $A^{-1}$, $A+cI$, $cA$ | $\lambda^k$, $1/\lambda$, $\lambda+c$, $c\lambda$ |
| $A^T$, similar matrices | same eigenvalues |
| $0$ is an eigenvalue | $\iff\det A=0$ |
| real symmetric | all eigenvalues real, orthogonal eigenvectors |
| orthogonal ($A^TA=I$) | $\lvert\lambda\rvert=1$ |
| every row sums to $s$ | $s$ is an eigenvalue, $v=(1,\dots,1)$ |
| rotation by $90^\circ$ $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ | $p=\lambda^2+1$: no real eigenvalues ($\pm i$) |

> **Trap:** do **not** row-reduce $A$ before computing eigenvalues — row operations change them.

---

## 5. Minimal polynomial, Cayley–Hamilton, diagonalization 🟢

### What it means
The **minimal polynomial** $m_A$ is the monic polynomial of **smallest degree** with $m_A(A)=0$.

### Must-know facts
> 1. **Cayley–Hamilton:** $p_A(A)=0$. Hence $m_A$ **divides** $p_A$, and $\deg m_A\le n$.
> 2. $m_A$ and $p_A$ have the **same roots** (the eigenvalues), only the multiplicities can be smaller in $m_A$.
> 3. $A$ is **diagonalizable** ⇔ $m_A$ is a product of **distinct** linear factors (no repeated root).
> 4. Similar matrices have the same $m_A$.
> 5. Exponent of $(x-\lambda)$ in $m_A$ = size of the largest Jordan block for $\lambda$.

### Examples
| $A$ | $p_A$ | $m_A$ | Diagonalizable? |
|---|---|---|---|
| $I_n$ | $(x-1)^n$ | $x-1$ | yes |
| $\operatorname{diag}(2,2,3)$ | $(x-2)^2(x-3)$ | $(x-2)(x-3)$ | yes |
| $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ | $(x-1)^2$ | $(x-1)^2$ | **no** |
| nilpotent $N\ne0$ ($N^k=0$) | $x^n$ | $x^j$, $j\ge2$ | **no** |
| projection $P^2=P$ | | divides $x^2-x$ | yes (eigenvalues $0,1$) |

### Using Cayley–Hamilton to invert
$A=\begin{pmatrix}2&1\\0&3\end{pmatrix}$: $p_A=x^2-5x+6$, so $A^2-5A+6I=0$.
1. $A(5I-A)=6I$.
2. $A^{-1}=\frac16(5I-A)=\frac16\begin{pmatrix}3&-1\\0&2\end{pmatrix}$.

### Diagonalizable
$A$ ($n\times n$) is **diagonalizable** ⇔ it has $n$ linearly independent eigenvectors ⇔ geometric = algebraic multiplicity for every eigenvalue. Then $A=PDP^{-1}$ ($D$ = eigenvalues, $P$ = eigenvectors as columns).
- $n$ **distinct** eigenvalues ⇒ diagonalizable.
- Real symmetric ⇒ diagonalizable (even with an orthogonal $P$).

> **Trap:** a repeated eigenvalue does **not** mean "not diagonalizable" ($I$ is diagonal). Check $m_A$ or the eigenspace dimension.

---

## 6. Groups 🟢

### What it means
A **group** $(G,\ast)$: closed, associative, has an **identity** $e$, every $a$ has an **inverse** $a^{-1}$. **Abelian:** $a\ast b=b\ast a$.

| Set and operation | Group? | Reason |
|---|---|---|
| $(\mathbb Z,+)$, $(\mathbb Q,+)$, $(\mathbb R,+)$ | yes | |
| $(\mathbb Z,\cdot)$, $(\mathbb N,+)$ | **no** | no inverses |
| $(\mathbb R\setminus\{0\},\cdot)$ | yes | |
| $(\mathbb Z_n,+)$ | yes, cyclic | |
| $(\mathbb Z_n^\times,\cdot)$ (units mod $n$) | yes, order $\varphi(n)$ | |
| $GL_n(\mathbb R)$ (invertible matrices) | yes, **not** abelian ($n\ge2$) | |
| $S_n$ (permutations) | yes, $\lvert S_n\rvert=n!$, not abelian for $n\ge3$ | |

### Basic rules
- **Cancellation:** $xz=yz\Rightarrow x=y$ (multiply by $z^{-1}$ on the right).
- $(ab)^{-1}=b^{-1}a^{-1}$. Identity and inverses are unique.

### Subgroups, order, Lagrange
- **Subgroup test:** $H\ne\emptyset$ and $a,b\in H\Rightarrow ab^{-1}\in H$.
- **Order** of $a$: smallest $k\ge1$ with $a^k=e$. In $(\mathbb Z_n,+)$: $\operatorname{ord}(k)=\frac{n}{\gcd(k,n)}$. Example: $\operatorname{ord}(8)$ in $\mathbb Z_{12}$ is $3$.
- **Cosets** $aH$ partition $G$; **index** $[G:H]=\lvert G\rvert/\lvert H\rvert$.
- **Lagrange:** $\lvert H\rvert$ divides $\lvert G\rvert$; so $\operatorname{ord}(a)$ divides $\lvert G\rvert$ and $a^{\lvert G\rvert}=e$.
- A group of prime order $p$ is cyclic.

### Cyclic groups
$G=\langle g\rangle$. Every cyclic group is $\cong\mathbb Z$ or $\cong\mathbb Z_n$. In $\mathbb Z_n$: $k$ is a generator ⇔ $\gcd(k,n)=1$ (generators of $\mathbb Z_8$: $1,3,5,7$). Subgroups of cyclic groups are cyclic.

### Permutations
$(1\,2\,3)(4\,5)$: $1\to2\to3\to1$, $4\leftrightarrow5$. Order = **lcm** of the disjoint cycle lengths ($=6$). A $k$-cycle is a product of $k-1$ transpositions; **sign** $=(-1)^{\#\text{transpositions}}$.

> **Trap:** in a non-abelian group, $xz=zy$ does **not** give $x=y$. Cancel only on the same side.

---

## 7. Group homomorphisms, kernels, normal subgroups 🟢

### What it means
A **homomorphism** $f:G\to H$ satisfies $f(ab)=f(a)f(b)$. An **isomorphism** is a bijective homomorphism ($G\cong H$: same structure, different names).

### Must-know facts
> 1. $f(e_G)=e_H$ and $f(a^{-1})=f(a)^{-1}$. So $f(x)=x+1$ on $(\mathbb Z,+)$ is **not** a homomorphism.
> 2. **Kernel** $\ker f=\{a:f(a)=e_H\}$ is a **normal** subgroup of $G$; the **image** is a subgroup of $H$.
> 3. $f$ injective ⇔ $\ker f=\{e\}$.
> 4. **Normal subgroup** $N\trianglelefteq G$: $gNg^{-1}=N$ for all $g$ (left cosets = right cosets). Every subgroup of an abelian group is normal; every subgroup of index 2 is normal. Then $G/N$ is a group (**quotient group**).
> 5. **First isomorphism theorem:** $G/\ker f\cong\operatorname{im}f$. Hence $\lvert G\rvert=\lvert\ker f\rvert\cdot\lvert\operatorname{im}f\rvert$ for finite $G$.
> 6. Isomorphic groups have the same order, same element orders, both abelian or both not. $\mathbb Z_4\not\cong\mathbb Z_2\times\mathbb Z_2$; $\mathbb Z_m\times\mathbb Z_n\cong\mathbb Z_{mn}\iff\gcd(m,n)=1$.

### Standard examples
| Homomorphism | Kernel | Image |
|---|---|---|
| $\mathbb Z\to\mathbb Z_n$, $k\mapsto k\bmod n$ | $n\mathbb Z$ | $\mathbb Z_n$ ⇒ $\mathbb Z/n\mathbb Z\cong\mathbb Z_n$ |
| $\det:GL_n(\mathbb R)\to\mathbb R\setminus\{0\}$ | $SL_n$ ($\det=1$) | $\mathbb R\setminus\{0\}$ |
| $\operatorname{sgn}:S_n\to\{\pm1\}$ | $A_n$, $\lvert A_n\rvert=\frac{n!}2$ | $\{\pm1\}$ ($n\ge2$) |
| $\exp:(\mathbb R,+)\to(\mathbb R_{>0},\cdot)$ | $\{0\}$ | all (isomorphism) |
| linear map $T$ (on $(V,+)$) | $\ker T$ | $\operatorname{im}T$ |

### Worked example
$f:\mathbb Z_{12}\to\mathbb Z_{12}$, $f(x)=3x$.
1. Homomorphism: $3(x+y)=3x+3y$ ✓.
2. $\ker f=\{x:3x\equiv0\}=\{0,4,8\}$, $\operatorname{im}f=\{0,3,6,9\}$.
3. Check: $3\cdot4=12=\lvert\mathbb Z_{12}\rvert$ ✓. So $\mathbb Z_{12}/\{0,4,8\}\cong\mathbb Z_4$.

> **Trap:** homo**morphism** (algebra) ≠ homeo**morphism** (topology, continuous bijection with continuous inverse).

---

## 8. Rings, ideals and fields 🟢

### Definitions
- **Ring** $(R,+,\cdot)$: $(R,+)$ abelian group, $\cdot$ associative, distributive laws. (Here: with $1$.)
- **Zero divisor:** $a\ne0$ with $ab=0$ for some $b\ne0$. **Unit:** element with a multiplicative inverse.
- **Integral domain:** commutative, $1\ne0$, no zero divisors.
- **Field:** commutative, $1\ne0$, every $a\ne0$ is a unit.
- Field ⇒ integral domain. A **finite** integral domain is a field.

| Ring | Integral domain? | Field? | Why not |
|---|---|---|---|
| $\mathbb Q,\mathbb R,\mathbb C$, $\mathbb Z_p$ ($p$ prime) | yes | **yes** | |
| $\mathbb Z$ | yes | no | $2$ has no inverse |
| $\mathbb R[x]$ (polynomials) | yes | no | $x$ has no inverse |
| $\mathbb Z_6$, $\mathbb Z_4$ | no | no | $2\cdot3=0$, $2\cdot2=0$ |
| $M_n(\mathbb R)$, $n\ge2$ | no (not commutative) | no | zero divisors |

(Official example 1: among $\mathbb Z/6\mathbb Z$, $\mathbb Q$, $\mathbb R[x]$, $\mathbb Z$, $\mathbb Z/4\mathbb Z$ only $\mathbb Q$ is a field.)

### $\mathbb Z_m$
$$\mathbb Z_m\text{ is a field}\iff m\text{ prime};\qquad a\text{ is a unit in }\mathbb Z_m\iff\gcd(a,m)=1.$$
- Inverse of $3$ in $\mathbb Z_7$: $3\cdot5=15\equiv1$, so $3^{-1}=5$.
- $\mathbb Z_{12}$: units $\{1,5,7,11\}$ ($\varphi(12)=4$); every other non-zero element is a zero divisor.

### Ideals
An **ideal** $I\subseteq R$ is an additive subgroup that **absorbs** multiplication: $r\in R,\ a\in I\Rightarrow ra\in I$.

> **Must-know facts**
> 1. Ideals of $\mathbb Z$: exactly $n\mathbb Z$ (every ideal is **principal**, generated by one element). $(a,b)=(\gcd(a,b))$, e.g. $(4,6)=2\mathbb Z$.
> 2. The **kernel of a ring homomorphism** is an ideal (just as group kernels are normal subgroups).
> 3. **Quotient ring** $R/I$ (cosets $a+I$). Example: $\mathbb Z/n\mathbb Z=\mathbb Z_n$.
> 4. An ideal containing a unit (e.g. $1$) is the whole ring. A **field has only the ideals $\{0\}$ and itself.**
> 5. **Prime ideal** $P\ne R$: $ab\in P\Rightarrow a\in P$ or $b\in P$. ⇔ $R/P$ is an integral domain.
> 6. **Maximal ideal** $M\ne R$: no ideal strictly between $M$ and $R$. ⇔ $R/M$ is a **field**. Maximal ⇒ prime.
> 7. In $\mathbb Z$: $n\mathbb Z$ is maximal ⇔ $n$ prime. $\{0\}$ is prime but not maximal ($\mathbb Z$ is a domain, not a field).
> 8. In $K[x]$: $(p)$ is maximal ⇔ $p$ irreducible. Example: $\mathbb R[x]/(x^2+1)\cong\mathbb C$; $\mathbb Z_2[x]/(x^2+x+1)$ is the field with 4 elements.

**Worked example.** Is $\{0,3\}$ an ideal of $\mathbb Z_6$? Additive subgroup ✓; $r\cdot3\in\{0,3\}$ for all $r$ ✓ ($2\cdot3=0$, $5\cdot3=15\equiv3$). Yes. $\mathbb Z_6/\{0,3\}\cong\mathbb Z_3$ is a field ⇒ $\{0,3\}$ is maximal.

### Characteristic and polynomials
- $\operatorname{char}F$ = smallest $n\ge1$ with $\underbrace{1+\dots+1}_n=0$ (or $0$). $\operatorname{char}\mathbb Q=0$, $\operatorname{char}\mathbb Z_p=p$. A field has characteristic $0$ or a prime.
- A degree-$n$ polynomial over a field has at most $n$ roots.
- Degree 2 or 3: irreducible ⇔ no root in the field. $x^2+1$ is irreducible over $\mathbb R$, not over $\mathbb C$.

> **Trap:** $\mathbb Z_4$ is **not** a field ($2\cdot2=0$). The field with 4 elements, $\mathbb F_4$, is a different object.

---

## 9. Field extensions and Galois theory 🟡

### What it means
Galois theory connects a field extension $L/K$ with a group (the **Galois group**) of symmetries of $L$ that fix $K$.

### Must-know facts
> 1. **Field extension** $L/K$: $K\subseteq L$ fields. **Degree** $[L:K]=\dim_KL$. $[\mathbb C:\mathbb R]=2$, $[\mathbb Q(\sqrt2):\mathbb Q]=2$, $[\mathbb R:\mathbb Q]=\infty$.
> 2. $\alpha$ is **algebraic** over $K$ if it is a root of some non-zero $f\in K[x]$. Its **minimal polynomial** is the monic irreducible polynomial in $K[x]$ with root $\alpha$, and $[K(\alpha):K]=\deg$ of it. Example: $\sqrt[3]2$ has minimal polynomial $x^3-2$ (Eisenstein, $p=2$), so $[\mathbb Q(\sqrt[3]2):\mathbb Q]=3$.
> 3. **Tower law:** $[M:K]=[M:L][L:K]$. $[\mathbb Q(\sqrt2,\sqrt3):\mathbb Q]=2\cdot2=4$.
> 4. **Splitting field** of $f$: smallest extension in which $f$ splits into linear factors.
> 5. **Galois group** $\operatorname{Gal}(L/K)$ = automorphisms of $L$ that fix every element of $K$. They permute the roots of each polynomial over $K$, so for the splitting field of a degree-$n$ polynomial it is a subgroup of $S_n$.
> 6. $L/K$ is **Galois** (normal + separable; in characteristic $0$: a splitting field) ⇒ $\lvert\operatorname{Gal}(L/K)\rvert=[L:K]$.
> 7. **Fundamental theorem:** for Galois $L/K$, subgroups of $\operatorname{Gal}(L/K)$ ↔ intermediate fields $K\subseteq E\subseteq L$, inclusion-reversing, $[L:E]=\lvert H\rvert$.

| Extension | Degree | Galois group |
|---|---|---|
| $\mathbb C/\mathbb R$ | 2 | $\mathbb Z_2$ (complex conjugation) |
| $\mathbb Q(\sqrt2)/\mathbb Q$ | 2 | $\mathbb Z_2$ ($\sqrt2\mapsto-\sqrt2$) |
| $\mathbb Q(\sqrt2,\sqrt3)/\mathbb Q$ | 4 | $\mathbb Z_2\times\mathbb Z_2$ |
| splitting field of $x^3-2$ over $\mathbb Q$, $=\mathbb Q(\sqrt[3]2,\omega)$ | 6 | $S_3$ |
| $\mathbb Q(\sqrt[3]2)/\mathbb Q$ | 3 | **not** Galois (only 1 automorphism; other roots are complex) |
| $\mathbb F_{p^n}/\mathbb F_p$ | $n$ | $\mathbb Z_n$, generated by Frobenius $x\mapsto x^p$ |

> 8. **Finite fields:** a finite field has $p^n$ elements ($p$ prime); for each $p^n$ there is exactly one up to isomorphism. No field with $6$, $10$, $12$ elements.
> 9. **Abel–Ruffini / Galois:** $f$ is solvable by radicals ⇔ its Galois group is solvable. The general polynomial of degree $\ge5$ is not ($S_5$ is not solvable); degrees $\le4$ always are.

---

## Formula sheet

| Topic | Formula / fact |
|---|---|
| subspace | contains $0$, closed under $+$ and scalars |
| dimension | $\dim P_n=n+1$, $\dim M_{m\times n}=mn$, $\dim(U+W)=\dim U+\dim W-\dim U\cap W$ |
| rank–nullity | $\dim\ker T+\operatorname{rank}T=\dim V$ |
| $Ax=b$ | solvable ⇔ $\operatorname{rank}A=\operatorname{rank}(A\mid b)$; free parameters $n-\operatorname{rank}A$ |
| $2\times2$ | $\det=ad-bc$; $A^{-1}=\frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$ |
| det rules | $\det(\alpha A)=\alpha^n\det A$, $\det(AB)=\det A\det B$, $\det A^{-1}=1/\det A$ |
| invertible | $\det\ne0\iff\ker=\{0\}\iff\operatorname{rank}=n\iff0$ not an eigenvalue |
| char. polynomial | $p_A=\det(\lambda I-A)$; $2\times2$: $\lambda^2-\operatorname{tr}A\,\lambda+\det A$ |
| eigen sums | $\sum\lambda_i=\operatorname{tr}A$, $\prod\lambda_i=\det A$ |
| Cayley–Hamilton | $p_A(A)=0$; $m_A\mid p_A$; same roots |
| diagonalizable | $\iff m_A$ has distinct linear factors $\iff$ geo = alg multiplicity |
| groups | $(ab)^{-1}=b^{-1}a^{-1}$; $\operatorname{ord}_{\mathbb Z_n}(k)=n/\gcd(k,n)$; Lagrange $\lvert H\rvert\mid\lvert G\rvert$ |
| homomorphism | $G/\ker f\cong\operatorname{im}f$; $\ker$ is normal; injective ⇔ $\ker=\{e\}$ |
| permutations | order = lcm of cycle lengths; $\lvert S_n\rvert=n!$, $\lvert A_n\rvert=n!/2$ |
| $\mathbb Z_m$ | field ⇔ $m$ prime; $a$ unit ⇔ $\gcd(a,m)=1$ |
| ideals | $R/M$ field ⇔ $M$ maximal; $R/P$ domain ⇔ $P$ prime; ideals of $\mathbb Z$: $n\mathbb Z$ |
| extensions | $[K(\alpha):K]=\deg$ min. poly; tower law; Galois: $\lvert\operatorname{Gal}\rvert=[L:K]$ |
| finite fields | size $p^n$ |

---

## Practice MCQs

**Q1.** (official example 1) Which of the following is a field?
A) $\mathbb Z/6\mathbb Z$  B) $\mathbb Q$  C) $\mathbb R[x]$  D) $\mathbb Z$  E) $\mathbb Z/4\mathbb Z$
<details><summary>Answer</summary>

**B** — $\mathbb Z_6$, $\mathbb Z_4$ have zero divisors ($2\cdot3=0$, $2\cdot2=0$); $x$ has no inverse in $\mathbb R[x]$; $2$ has no inverse in $\mathbb Z$.

</details>

**Q2.** (official example 2) A linear operator $T$ on a finite-dimensional vector space is invertible if and only if
A) $\det(T)\ne0$  B) $\operatorname{tr}(T)\ne0$  C) all its eigenvalues are real  D) it is diagonalizable  E) it is nilpotent
<details><summary>Answer</summary>

**A** — Invertible ⇔ $\ker T=\{0\}$ ⇔ $\det T\ne0$. $\operatorname{diag}(1,-1)$ is invertible with trace $0$; the zero matrix is diagonalizable but not invertible.

</details>

**Q3.** Which set is a subspace of $\mathbb R^3$?
A) $\{x:x_1+x_2+x_3=1\}$  B) $\{x:x_1\ge0\}$  C) $\{x:x_1x_2=0\}$  D) $\{x:x_1+2x_2-x_3=0\}$  E) $\{x:x_1^2=x_2\}$
<details><summary>Answer</summary>

**D** — Kernel of a linear map. A misses $0$; B fails for $-1\cdot x$; C fails under addition; E is not closed under scaling.

</details>

**Q4.** The dimension of the space of real polynomials of degree at most $3$ is
A) $3$  B) $4$  C) $6$  D) $9$  E) infinite
<details><summary>Answer</summary>

**B** — Basis $1,x,x^2,x^3$.

</details>

**Q5.** $T:\mathbb R^5\to\mathbb R^3$ is linear and surjective. $\dim\ker T=$
A) $2$  B) $3$  C) $5$  D) $0$  E) $8$
<details><summary>Answer</summary>

**A** — Rank $3$; rank–nullity: $5-3=2$.

</details>

**Q6.** $A$ is $3\times5$ and $\operatorname{rank}A=\operatorname{rank}(A\mid b)=3$. Then $Ax=b$ has
A) no solution  B) exactly one solution  C) infinitely many, 3 free parameters  D) infinitely many, 2 free parameters  E) exactly two solutions
<details><summary>Answer</summary>

**D** — Solvable; free parameters $=5-3=2$.

</details>

**Q7.** $A$ is $3\times3$ with $\det A=2$. $\det(3A)=$
A) $6$  B) $18$  C) $27$  D) $54$  E) $8$
<details><summary>Answer</summary>

**D** — $3^3\cdot2=54$. ($6$ is the trap $\alpha\det A$.)

</details>

**Q8.** $\det A=2$, $\det B=-3$. $\det(AB^{-1})=$
A) $-\frac23$  B) $-6$  C) $\frac23$  D) $-1$  E) $-\frac32$
<details><summary>Answer</summary>

**A** — $2\cdot\frac1{-3}$.

</details>

**Q9.** The eigenvalues of $\begin{pmatrix}2&5\\0&7\end{pmatrix}$ are
A) $5,7$  B) $2,5$  C) $2,7$  D) $0,9$  E) $2,5,7$
<details><summary>Answer</summary>

**C** — Triangular: diagonal entries.

</details>

**Q10.** The characteristic polynomial of $\begin{pmatrix}1&2\\3&4\end{pmatrix}$ is
A) $\lambda^2-5\lambda-2$  B) $\lambda^2+5\lambda-2$  C) $\lambda^2-5\lambda+10$  D) $\lambda^2-4\lambda+3$  E) $\lambda^2-2$
<details><summary>Answer</summary>

**A** — $\lambda^2-(\operatorname{tr})\lambda+\det$ with $\operatorname{tr}=5$, $\det=4-6=-2$.

</details>

**Q11.** A $3\times3$ matrix has eigenvalues $1,2,3$. $\det(2A)=$
A) $12$  B) $48$  C) $6$  D) $36$  E) $24$
<details><summary>Answer</summary>

**B** — $\det A=6$, $\det(2A)=8\cdot6=48$.

</details>

**Q12.** The minimal polynomial of $\operatorname{diag}(2,2,3)$ is
A) $(x-2)^2(x-3)$  B) $(x-2)(x-3)$  C) $x-2$  D) $(x-2)(x-3)^2$  E) $x^3-7x$
<details><summary>Answer</summary>

**B** — Monic, smallest degree, kills $A$: $(A-2I)(A-3I)=0$ already. Distinct linear factors ⇔ diagonalizable ✓.

</details>

**Q13.** Which matrix is **not** diagonalizable?
A) $\begin{pmatrix}1&1\\0&1\end{pmatrix}$  B) $\begin{pmatrix}2&0\\0&2\end{pmatrix}$  C) $\begin{pmatrix}1&2\\2&1\end{pmatrix}$  D) $\begin{pmatrix}1&0\\0&3\end{pmatrix}$  E) $\begin{pmatrix}1&5\\0&2\end{pmatrix}$
<details><summary>Answer</summary>

**A** — $m_A=(x-1)^2$ has a repeated root (one eigenvector direction). E has distinct eigenvalues $1,2$; C is symmetric.

</details>

**Q14.** The Cayley–Hamilton theorem states that
A) every matrix is diagonalizable  B) $p_A(A)=0$  C) $m_A=p_A$  D) $\det A=\operatorname{tr}A$  E) eigenvalues are real
<details><summary>Answer</summary>

**B** — A matrix satisfies its own characteristic polynomial. (C is false in general: see Q12.)

</details>

**Q15.** $N\ne0$ is nilpotent ($N^k=0$ for some $k$). Which is true?
A) $N$ is invertible  B) all eigenvalues of $N$ are $0$  C) $N$ is diagonalizable  D) $\operatorname{tr}N=1$  E) $\det N=1$
<details><summary>Answer</summary>

**B** — $Nv=\lambda v\Rightarrow0=N^kv=\lambda^kv\Rightarrow\lambda=0$. So $\det N=0$, $\operatorname{tr}N=0$, and $m_N=x^j$ with $j\ge2$ ⇒ not diagonalizable.

</details>

**Q16.** A group $G$ has 12 elements. Which number **cannot** be the order of a subgroup?
A) $4$  B) $6$  C) $5$  D) $3$  E) $1$
<details><summary>Answer</summary>

**C** — Lagrange: subgroup orders divide 12.

</details>

**Q17.** The order of $8$ in $(\mathbb Z_{12},+)$ is
A) $4$  B) $8$  C) $12$  D) $3$  E) $6$
<details><summary>Answer</summary>

**D** — $12/\gcd(8,12)=3$.

</details>

**Q18.** The order of $(1\,2\,3)(4\,5)\in S_5$ is
A) $5$  B) $3$  C) $6$  D) $2$  E) $120$
<details><summary>Answer</summary>

**C** — $\operatorname{lcm}(3,2)=6$.

</details>

**Q19.** Which map $(\mathbb Z,+)\to(\mathbb Z,+)$ is a group homomorphism?
A) $x+1$  B) $x^2$  C) $3x$  D) $\lvert x\rvert$  E) $x^3$
<details><summary>Answer</summary>

**C** — $3(x+y)=3x+3y$. A: $f(0)\ne0$. B, D, E fail additivity (e.g. $f(1+1)\ne f(1)+f(1)$ for B, E; $f(1-1)\ne f(1)+f(-1)$ for D).

</details>

**Q20.** The kernel of a group homomorphism $f:G\to H$ is always
A) equal to $G$  B) a normal subgroup of $G$  C) a subgroup of $H$  D) trivial  E) cyclic
<details><summary>Answer</summary>

**B** — $gkg^{-1}\mapsto f(g)e f(g)^{-1}=e$. It is trivial only when $f$ is injective.

</details>

**Q21.** $f:G\to H$ is a surjective homomorphism, $\lvert G\rvert=24$, $\lvert\ker f\rvert=6$. Then $\lvert H\rvert=$
A) $4$  B) $6$  C) $18$  D) $30$  E) $144$
<details><summary>Answer</summary>

**A** — $G/\ker f\cong H$ ⇒ $\lvert H\rvert=24/6$.

</details>

**Q22.** The kernel of $\operatorname{sgn}:S_4\to\{\pm1\}$ has how many elements?
A) $4$  B) $6$  C) $12$  D) $24$  E) $2$
<details><summary>Answer</summary>

**C** — The kernel is $A_4$, $\lvert A_4\rvert=4!/2=12$.

</details>

**Q23.** Which subset of $\mathbb Z$ is an ideal?
A) $\mathbb N$  B) the odd integers  C) $6\mathbb Z$  D) $\{-1,0,1\}$  E) $\{0,1\}$
<details><summary>Answer</summary>

**C** — Additive subgroup and $r\cdot6k\in6\mathbb Z$. A has no negatives; B, D, E are not closed under $+$.

</details>

**Q24.** Which ideal of $\mathbb Z$ is maximal?
A) $\{0\}$  B) $4\mathbb Z$  C) $6\mathbb Z$  D) $7\mathbb Z$  E) $\mathbb Z$
<details><summary>Answer</summary>

**D** — $n\mathbb Z$ maximal ⇔ $\mathbb Z/n\mathbb Z$ field ⇔ $n$ prime. $\mathbb Z$ itself is not proper.

</details>

**Q25.** The quotient ring $\mathbb R[x]/(x^2+1)$ is isomorphic to
A) $\mathbb R$  B) $\mathbb R^2$ with componentwise product  C) $\mathbb C$  D) $\mathbb Z_2$  E) $\mathbb R[x]$
<details><summary>Answer</summary>

**C** — $x\mapsto i$. $x^2+1$ is irreducible over $\mathbb R$ ⇒ the ideal is maximal ⇒ the quotient is a field.

</details>

**Q26.** A field $F$ has how many ideals?
A) none  B) exactly one  C) exactly two: $\{0\}$ and $F$  D) infinitely many  E) depends on $\operatorname{char}F$
<details><summary>Answer</summary>

**C** — An ideal $I\ne\{0\}$ contains some $a\ne0$, hence $a^{-1}a=1$, hence everything.

</details>

**Q27.** Which element of $\mathbb Z_8$ is a zero divisor?
A) $3$  B) $4$  C) $5$  D) $7$  E) $1$
<details><summary>Answer</summary>

**B** — $4\cdot2=8\equiv0$. The others are coprime to 8 (units).

</details>

**Q28.** $[\mathbb Q(\sqrt2,\sqrt3):\mathbb Q]=$
A) $2$  B) $3$  C) $6$  D) $4$  E) $5$
<details><summary>Answer</summary>

**D** — Tower law: $2\cdot2$.

</details>

**Q29.** $[\mathbb Q(\sqrt[3]2):\mathbb Q]=$
A) $2$  B) $3$  C) $6$  D) $1$  E) infinite
<details><summary>Answer</summary>

**B** — Minimal polynomial $x^3-2$ (irreducible, Eisenstein with $p=2$) has degree 3.

</details>

**Q30.** A finite field can have how many elements?
A) $6$  B) $10$  C) $12$  D) $9$  E) $15$
<details><summary>Answer</summary>

**D** — The size of a finite field is a prime power: $9=3^2$.

</details>

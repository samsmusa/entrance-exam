# 5. Differential Equations

> **Syllabus:**
> - ODEs (homogeneous, inhomogeneous): higher order linear, separation of variables, Bernoulli equation, exact differential equations, existence and uniqueness results
> - PDEs: elliptic, parabolic, hyperbolic; classical solution methods for Laplace, Poisson, heat and wave equation
> - Systems of ODEs
> - Dynamical systems
> - Principles of self-organization

> **How to study this file:** Sections 1–9 and 11 are 🟢 core. Learn the recipes and do every example yourself on paper. Sections 10 and 12 are 🟡: only read the "Must-know facts" boxes.
> Time: about 2 study days for the 🟢 parts, plus 1 hour for the 🟡 parts and the MCQs.
> The official test problem (No. 25) is: solve $y'=y+t$, $y(0)=1$. Answer: $y=2e^t-t-1$. This is the level you need.

## Contents
1. [Basic words](#1-basic-words-) 🟢
2. [The fastest trick: plug in and check](#2-the-fastest-trick-plug-in-and-check-) 🟢
3. [Separable equations](#3-separable-equations-) 🟢
4. [Linear first-order equations (integrating factor)](#4-linear-first-order-equations-integrating-factor-) 🟢
5. [Bernoulli equations](#5-bernoulli-equations-) 🟢
6. [Exact equations](#6-exact-equations-) 🟢
7. [Second-order linear equations with constant coefficients](#7-second-order-linear-equations-with-constant-coefficients-) 🟢
8. [Inhomogeneous second-order equations](#8-inhomogeneous-second-order-equations-) 🟢
9. [Systems $\mathbf x'=A\mathbf x$ and stability](#9-systems-xax-and-stability-) 🟢
10. [Existence and uniqueness](#10-existence-and-uniqueness-) 🟡
11. [PDEs: classification and the three famous equations](#11-pdes-classification-and-the-three-famous-equations-) 🟢
12. [Advanced topics: PDE solutions, dynamical systems, self-organization](#12-advanced-topics-) 🟡
13. [Formula sheet](#formula-sheet)
14. [Practice MCQs](#practice-mcqs)

---

## 1. Basic words 🟢

An **ordinary differential equation (ODE)** is an equation for an unknown function $y(t)$ that contains derivatives $y', y'', \dots$
- $t$ = the variable (often time). Sometimes it is called $x$.
- $y' = \frac{dy}{dt}$ = first derivative, $y''$ = second derivative.

| Word | Meaning | Example |
|---|---|---|
| **Order** | the highest derivative in the equation | $y''+y=0$ has order 2 |
| **Linear** | $y, y', y'', \dots$ appear only to the power 1. They are not multiplied together. No $y^2$, $\sin y$, $yy'$ | $y''+t^2y=\cos t$ is linear |
| **Nonlinear** | not linear | $y'=y^2$, $y'=\sin y$ |
| **Homogeneous** (linear ODE) | the right side (the part without $y$) is $0$ | $y''+y=0$ |
| **Inhomogeneous** | the right side is not $0$ | $y''+y=t$ |
| **Initial value problem (IVP)** | ODE + start values like $y(0)=1$ | $y'=y$, $y(0)=1$ |
| **General solution** | all solutions; contains free constants $C, C_1, C_2$ | $y=Ce^t$ |
| **Particular solution** | one single solution, no free constants | $y=e^t$ |

**Key rule:** an ODE of order $n$ has a general solution with $n$ free constants. So you need $n$ initial conditions to fix them.

**Structure rule (linear ODEs):**
$$y = y_h + y_p$$
- $y_h$ = general solution of the homogeneous equation (right side $=0$),
- $y_p$ = one particular solution of the full equation.

**Trap:** $t^2$ in front of $y$ is fine for linearity ($t^2 y$ is linear). Only powers or functions **of $y$** make it nonlinear.

---

## 2. The fastest trick: plug in and check 🟢

In a multiple-choice test you often do **not** need to solve. You only need to test the options.

**Recipe**
- Step 1: Check the initial condition (put $t=0$). Cross out options that fail.
- Step 2: Compute $y'$ of the remaining options and put it into the ODE.

**Example.** Which function solves $y'=y+t$, $y(0)=1$?
A) $e^t+t$  B) $2e^t-t-1$
- A: $y(0)=1$ ✓. $y'=e^t+1$, but $y+t=e^t+2t$. Not equal ✗.
- B: $y(0)=2-0-1=1$ ✓. $y'=2e^t-1$ and $y+t=2e^t-t-1+t=2e^t-1$ ✓.

**Answer B.**

**Trap:** always check **both** the ODE and the initial condition. Many wrong options satisfy only one of them.

---

## 3. Separable equations 🟢

**Plain words:** the right side is "a function of $t$" times "a function of $y$". You can put all $y$ on one side and all $t$ on the other.

**Form:** $y' = g(t)\,h(y)$

**Recipe**
- Step 1: Write $\frac{dy}{dt}=g(t)h(y)$.
- Step 2: Separate: $\frac{dy}{h(y)}=g(t)\,dt$.
- Step 3: Integrate both sides: $\int\frac{dy}{h(y)}=\int g(t)\,dt + C$.
- Step 4: Solve for $y$. Use the initial condition to find $C$.
- Step 5: Check if $h(y_0)=0$ for some number $y_0$. Then $y\equiv y_0$ is also a solution (a constant solution).

**Example.** $y'=2ty$, $y(0)=3$.
- Step 2: $\frac{dy}{y}=2t\,dt$.
- Step 3: $\ln|y| = t^2 + C$.
- Step 4: $y = Ke^{t^2}$ (with $K=\pm e^C$). $y(0)=K=3$. So $\boxed{y=3e^{t^2}}$.
- Check: $y'=3\cdot 2t\,e^{t^2}=2t\cdot y$ ✓.

**Important special case:** $y' = ky$ ($k$ a constant) gives $y = y(0)\,e^{kt}$.
- $k>0$: exponential growth. $k<0$: exponential decay.

**Trap:** when you divide by $h(y)$ you lose the constant solutions with $h(y)=0$. Example: $y'=2ty$ also has $y\equiv0$.

---

## 4. Linear first-order equations (integrating factor) 🟢

**Plain words:** $y$ and $y'$ appear linearly. We multiply by a clever function $\mu(t)$ so that the left side becomes the derivative of a product.

**Form:** $y' + p(t)\,y = q(t)$

**Recipe**
- Step 1: Bring the equation to the form $y'+p(t)y=q(t)$. (Watch the sign of $p$!)
- Step 2: Integrating factor $\mu(t)=e^{\int p(t)\,dt}$.
- Step 3: Then $(\mu y)' = \mu\, q$.
- Step 4: Integrate: $\mu y = \int \mu q\,dt + C$.
- Step 5: Divide by $\mu$. Use the initial condition.

**Example 1 (official problem).** $y'=y+t$, $y(0)=1$.
- Step 1: $y'-y=t$, so $p=-1$, $q=t$.
- Step 2: $\mu=e^{-t}$.
- Step 3: $(ye^{-t})'=te^{-t}$.
- Step 4: $\int te^{-t}dt = -te^{-t}-e^{-t}$ (integration by parts). So $ye^{-t}=-te^{-t}-e^{-t}+C$.
- Step 5: $y=Ce^t-t-1$. $y(0)=C-1=1$, so $C=2$: $\boxed{y=2e^t-t-1}$.

**Example 2.** $y'+2y=4$, $y(0)=0$.
- $\mu=e^{2t}$, $(ye^{2t})'=4e^{2t}$, $ye^{2t}=2e^{2t}+C$, $y=2+Ce^{-2t}$.
- $y(0)=2+C=0$, so $C=-2$: $\boxed{y=2-2e^{-2t}}$. For $t\to\infty$, $y\to2$.

**Example 3.** $y'+\frac{2}{t}y=t$ ($t>0$).
- $\mu=e^{\int 2/t\,dt}=e^{2\ln t}=t^2$.
- $(t^2y)'=t^3$, so $t^2y=\frac{t^4}{4}+C$ and $y=\frac{t^2}{4}+\frac{C}{t^2}$.

**Shortcut for constant $p$ and $q$:** $y'=ay+b$ ($a\neq0$) has the solution $y=Ce^{at}-\frac{b}{a}$.

**Trap:** the sign. $y'=y+t$ must first become $y'-y=t$, so $p=-1$ and $\mu=e^{-t}$ (not $e^{t}$).

---

## 5. Bernoulli equations 🟢

**Plain words:** almost linear, but with an extra power $y^n$ on the right. A substitution makes it linear.

**Form:** $y'+p(t)\,y=q(t)\,y^n$ with $n\neq0,1$.

**Recipe**
- Step 1: Find $n$.
- Step 2: Substitute $v=y^{1-n}$.
- Step 3: The new equation is linear: $v'+(1-n)p(t)\,v=(1-n)\,q(t)$.
- Step 4: Solve it with Section 4. Then go back: $y=v^{1/(1-n)}$.

**Example.** $y'=y-y^2$ (this is the logistic equation).
- Write $y'-y=-y^2$: $p=-1$, $q=-1$, $n=2$.
- $v=y^{1-2}=1/y$. Step 3: $v'+(-1)(-1)v=(-1)(-1)$, so $v'+v=1$.
- Solution: $v=1+Ce^{-t}$. So $\boxed{y=\dfrac{1}{1+Ce^{-t}}}$.

| $n$ | substitution $v=y^{1-n}$ |
|---|---|
| 2 | $v=y^{-1}$ |
| 3 | $v=y^{-2}$ |
| $\frac12$ | $v=y^{1/2}$ |

**Trap:** the exponent is $1-n$, **not** $n$ and not $n-1$. For $y'+y=ty^3$ you use $v=y^{-2}$.

---

## 6. Exact equations 🟢

**Plain words:** the equation is the total derivative of some function $F(x,y)$. Then the solution is simply $F(x,y)=C$.

**Form:** $M(x,y)\,dx+N(x,y)\,dy=0$

**Recipe**
- Step 1: Test: is $\dfrac{\partial M}{\partial y}=\dfrac{\partial N}{\partial x}$? If yes, the equation is **exact**.
- Step 2: Integrate $M$ in $x$: $F=\int M\,dx + h(y)$. ($h(y)$ is the "constant" that may depend on $y$.)
- Step 3: Take $\partial F/\partial y$ and set it equal to $N$. This gives $h'(y)$, then $h(y)$.
- Step 4: The solution is $F(x,y)=C$.

**Example.** $(2xy+3)\,dx+(x^2+4y)\,dy=0$.
- Step 1: $M_y=2x$, $N_x=2x$ ✓ exact.
- Step 2: $F=\int(2xy+3)\,dx=x^2y+3x+h(y)$.
- Step 3: $F_y=x^2+h'(y)=x^2+4y$, so $h'(y)=4y$ and $h=2y^2$.
- Step 4: $\boxed{x^2y+3x+2y^2=C}$.
- Check: $F_x=2xy+3=M$ ✓, $F_y=x^2+4y=N$ ✓.

**Trap:** compare $M_y$ (derivative of $M$ in **$y$**) with $N_x$ (derivative of $N$ in **$x$**). Do not compare $M_x$ with $N_y$.

---

## 7. Second-order linear equations with constant coefficients 🟢

**Plain words:** $a y''+b y'+c y=0$ with numbers $a,b,c$. We guess $y=e^{rt}$. This turns the ODE into a quadratic equation for $r$.

**Recipe**
- Step 1: Write the **characteristic equation** $ar^2+br+c=0$. (Replace $y''\to r^2$, $y'\to r$, $y\to1$.)
- Step 2: Find the roots $r_1,r_2$.
- Step 3: Use the table.
- Step 4: Use the initial conditions to find $C_1,C_2$.

| Roots | General solution |
|---|---|
| two different real roots $r_1\neq r_2$ | $y=C_1e^{r_1t}+C_2e^{r_2t}$ |
| one double root $r$ | $y=(C_1+C_2t)\,e^{rt}$ |
| complex roots $r=\alpha\pm i\beta$ | $y=e^{\alpha t}\big(C_1\cos\beta t+C_2\sin\beta t\big)$ |

**Example 1 (real roots).** $y''-5y'+6y=0$, $y(0)=1$, $y'(0)=0$.
- $r^2-5r+6=0$, so $(r-2)(r-3)=0$, $r=2,3$.
- $y=C_1e^{2t}+C_2e^{3t}$, $y'=2C_1e^{2t}+3C_2e^{3t}$.
- $C_1+C_2=1$ and $2C_1+3C_2=0$. So $C_2=-2$, $C_1=3$: $\boxed{y=3e^{2t}-2e^{3t}}$.

**Example 2 (double root).** $y''-4y'+4y=0$: $(r-2)^2=0$, $r=2$ twice. $y=(C_1+C_2t)e^{2t}$.

**Example 3 (complex roots).** $y''+2y'+5y=0$: $r=\frac{-2\pm\sqrt{4-20}}{2}=-1\pm2i$. So $\alpha=-1$, $\beta=2$:
$y=e^{-t}(C_1\cos2t+C_2\sin2t)$. This is a decaying oscillation.

**Useful facts**
- $y''+\omega^2y=0$ ⇒ $y=C_1\cos\omega t+C_2\sin\omega t$ (harmonic oscillator).
- $y''-\omega^2y=0$ ⇒ $y=C_1e^{\omega t}+C_2e^{-\omega t}$ (or $\cosh$, $\sinh$).

**Trap:** for a double root you need the extra factor $t$: $te^{rt}$. Writing $C_1e^{rt}+C_2e^{rt}$ is wrong (it has only one free constant).

---

## 8. Inhomogeneous second-order equations 🟢

**Plain words:** $ay''+by'+cy=g(t)$. Solution $= y_h + y_p$. You find $y_h$ with Section 7. You **guess** $y_p$ with the same form as $g(t)$ ("method of undetermined coefficients").

**Recipe**
- Step 1: Solve the homogeneous equation → $y_h$.
- Step 2: Choose a trial function $y_p$ from the table.
- Step 3: Put $y_p$ into the ODE and compare coefficients.
- Step 4: $y=y_h+y_p$. Then use the initial conditions (on the full $y$!).

| Right side $g(t)$ | Trial $y_p$ |
|---|---|
| constant $k$ | $A$ |
| polynomial of degree $m$ | polynomial of degree $m$: $A_mt^m+\dots+A_0$ |
| $ke^{at}$ | $Ae^{at}$ |
| $k\cos\omega t$ or $k\sin\omega t$ | $A\cos\omega t+B\sin\omega t$ (always both!) |

**Resonance rule:** if your trial function already solves the homogeneous equation, multiply it by $t$ (by $t^2$ for a double root).

**Example 1.** $y''-3y'+2y=4$. Trial $y_p=A$: $2A=4$, $A=2$.
Roots $r=1,2$, so $y=C_1e^t+C_2e^{2t}+2$.

**Example 2.** $y''-y=e^{2t}$. Trial $y_p=Ae^{2t}$: $4A-A=1$, $A=\frac13$. So $y_p=\frac13e^{2t}$.

**Example 3.** $y''+y=t$. Trial $y_p=At+B$: $0+At+B=t$, so $A=1,B=0$. $y=C_1\cos t+C_2\sin t+t$.

**Example 4 (resonance).** $y''-3y'+2y=e^t$. The roots are $1,2$, so $e^t$ already solves the homogeneous equation. Trial $y_p=Ate^t$.
$y_p'=A(1+t)e^t$, $y_p''=A(2+t)e^t$. Put in: $A[(2+t)-3(1+t)+2t]e^t=-Ae^t=e^t$, so $A=-1$. $y_p=-te^t$.

**Other method (know the name):** *variation of parameters* works for any $g(t)$, but is longer. The *Wronskian* $W=y_1y_2'-y_1'y_2$ is $\neq0$ exactly when $y_1,y_2$ are independent solutions. Example: $W(e^t,e^{2t})=e^{3t}$.

**Trap:** first add $y_h+y_p$, **then** use the initial conditions. Using them on $y_h$ alone is wrong.

---

## 9. Systems $\mathbf x'=A\mathbf x$ and stability 🟢

**Plain words:** two unknown functions $x_1(t), x_2(t)$ that depend on each other. We write them as a vector $\mathbf x=\binom{x_1}{x_2}$ and a matrix $A$. The **eigenvalues** $\lambda$ of $A$ decide everything.

### 9.1 Solving
**Recipe** (for a $2\times2$ matrix $A$ with two different real eigenvalues)
- Step 1: Eigenvalues: solve $\det(A-\lambda I)=0$, i.e. $\lambda^2-(\operatorname{tr}A)\lambda+\det A=0$.
  - $\operatorname{tr}A$ = trace = sum of the diagonal entries. $\det A$ = determinant.
- Step 2: For each $\lambda_i$, find an eigenvector $\mathbf v_i$: $(A-\lambda_iI)\mathbf v_i=0$.
- Step 3: $\mathbf x(t)=C_1e^{\lambda_1t}\mathbf v_1+C_2e^{\lambda_2t}\mathbf v_2$.

**Example.** $A=\begin{pmatrix}1&2\\2&1\end{pmatrix}$, $\mathbf x(0)=\binom20$.
- $\operatorname{tr}A=2$, $\det A=1-4=-3$. $\lambda^2-2\lambda-3=0$, so $\lambda=3$ and $\lambda=-1$.
- $\lambda=3$: $\mathbf v_1=\binom11$. $\lambda=-1$: $\mathbf v_2=\binom1{-1}$.
- $\mathbf x(0)=C_1\binom11+C_2\binom1{-1}=\binom20$ gives $C_1=C_2=1$.
- $x_1=e^{3t}+e^{-t}$, $x_2=e^{3t}-e^{-t}$.

**Second-order ODE → system:** $y''+py'+qy=0$ becomes, with $x_1=y$, $x_2=y'$:
$$\mathbf x'=\begin{pmatrix}0&1\\-q&-p\end{pmatrix}\mathbf x.$$
Example: $y''+3y'+2y=0$ → $A=\begin{pmatrix}0&1\\-2&-3\end{pmatrix}$, eigenvalues $-1,-2$ (same as the roots of $r^2+3r+2$).

### 9.2 Equilibria and stability in 1D
An **equilibrium** (fixed point) $x^*$ of $x'=f(x)$ is a point with $f(x^*)=0$. If you start there, you stay there.

| Test | Result |
|---|---|
| $f'(x^*)<0$ | **stable** (nearby solutions move towards $x^*$) |
| $f'(x^*)>0$ | **unstable** (nearby solutions move away) |
| $f'(x^*)=0$ | test does not decide |

**Example.** $y'=y(1-y)=y-y^2$. Equilibria: $y=0$ and $y=1$. $f'(y)=1-2y$.
$f'(0)=1>0$ → unstable. $f'(1)=-1<0$ → stable.

### 9.3 Stability of $\mathbf x'=A\mathbf x$ (2D)
The origin $\mathbf 0$ is always an equilibrium. Let $\tau=\operatorname{tr}A$, $\Delta=\det A$.

| Eigenvalues | Name | Stable? |
|---|---|---|
| both real, both $<0$ | stable node | yes ✓ |
| both real, both $>0$ | unstable node | no |
| real, opposite signs ($\Delta<0$) | **saddle** | no |
| complex $\alpha\pm i\beta$, $\alpha<0$ | stable spiral | yes ✓ |
| complex, $\alpha>0$ | unstable spiral | no |
| pure imaginary $\pm i\beta$ ($\tau=0$, $\Delta>0$) | **center** (closed circles/ellipses) | stable, but not asymptotically |

**Short rule:** asymptotically stable ⇔ all eigenvalues have negative real part ⇔ (for $2\times2$) $\tau<0$ **and** $\Delta>0$.
Spiral or node? Look at $\tau^2-4\Delta$: $<0$ spiral, $>0$ node.

**Example.** $A=\begin{pmatrix}-1&2\\-2&-1\end{pmatrix}$: $\tau=-2$, $\Delta=1+4=5$, $\tau^2-4\Delta=-16<0$. Eigenvalues $-1\pm2i$ → stable spiral.

**Trap:** check $\Delta$ first. If $\det A<0$, it is a **saddle** (unstable), no matter what the trace is.

---

## 10. Existence and uniqueness 🟡

> **Must-know facts**
> - **Picard–Lindelöf:** if $f(t,y)$ is continuous **and Lipschitz in $y$** (e.g. $\partial f/\partial y$ is continuous), then $y'=f(t,y)$, $y(t_0)=y_0$ has exactly one solution near $t_0$ (existence **and** uniqueness).
> - **Peano:** if $f$ is only continuous, a solution exists, but it may **not** be unique.
> - Classic example: $y'=\sqrt{y}$, $y(0)=0$ has many solutions: $y\equiv0$ and $y=t^2/4$ (and more). Reason: $\sqrt y$ is not Lipschitz at $0$.
> - Solutions may exist only for a short time: $y'=y^2$, $y(0)=1$ gives $y=\frac{1}{1-t}$, which blows up at $t=1$.
> - Linear ODEs with continuous coefficients have a unique solution on the whole interval.
> - Uniqueness means: two different solution curves of $y'=f(t,y)$ never cross.

---

## 11. PDEs: classification and the three famous equations 🟢

A **partial differential equation (PDE)** has an unknown function of several variables, e.g. $u(x,t)$ or $u(x,y)$.
Notation: $u_x=\frac{\partial u}{\partial x}$, $u_{xx}=\frac{\partial^2u}{\partial x^2}$, $u_{xy}=\frac{\partial^2u}{\partial x\partial y}$.

### 11.1 Classification
For a second-order linear PDE
$$Au_{xx}+Bu_{xy}+Cu_{yy}+(\text{lower terms like }u_x,u_y,u)=G,$$
compute the **discriminant** $D=B^2-4AC$.

| $B^2-4AC$ | Type | Famous example |
|---|---|---|
| $<0$ | **elliptic** | Laplace $u_{xx}+u_{yy}=0$ |
| $=0$ | **parabolic** | heat $u_t=ku_{xx}$ |
| $>0$ | **hyperbolic** | wave $u_{tt}=c^2u_{xx}$ |

**Recipe**
- Step 1: Bring everything to one side.
- Step 2: Read $A$ (coefficient of $u_{xx}$), $B$ (of $u_{xy}$), $C$ (of $u_{yy}$). Ignore $u_x$, $u_y$, $u$.
- Step 3: Compute $B^2-4AC$ and use the table.

**Examples**
- $u_{xx}+4u_{xy}+3u_{yy}=0$: $16-12=4>0$ → hyperbolic.
- $u_{xx}+2u_{xy}+u_{yy}=0$: $4-4=0$ → parabolic.
- $u_{xx}+u_{xy}+u_{yy}=0$: $1-4=-3<0$ → elliptic.
- Heat $u_t-u_{xx}=0$ (variables $x,t$): $A=-1$, $B=0$, $C=0$ (no $u_{tt}$) → $0$ → parabolic.
- Wave $u_{tt}-u_{xx}=0$: $A=-1$, $C=1$ → $0-4(-1)(1)=4>0$ → hyperbolic.

**Trap:** first-order terms ($u_x$, $u_t$, $u$) **never** change the type. The heat equation has only $u_t$ (first order in $t$), so it is parabolic.

### 11.2 Recognize the famous equations

| Name | Equation | Type | Describes | Data needed |
|---|---|---|---|---|
| **Laplace** | $\Delta u=u_{xx}+u_{yy}=0$ | elliptic | steady state, equilibrium | boundary values |
| **Poisson** | $\Delta u=f$ | elliptic | steady state with a source | boundary values |
| **Heat / diffusion** | $u_t=k\,u_{xx}$ ($k>0$) | parabolic | spreading of heat or particles | $u(x,0)$ + boundary |
| **Wave** | $u_{tt}=c^2u_{xx}$ | hyperbolic | vibrating string, waves with speed $c$ | $u(x,0)$ **and** $u_t(x,0)$ + boundary |

- $\Delta$ = Laplace operator = sum of second derivatives.
- A function with $\Delta u=0$ is called **harmonic**. Examples: $x^2-y^2$, $xy$, $e^x\sin y$. Not harmonic: $x^2+y^2$ (here $\Delta u=4$).

**Example (check harmonic).** $u=x^2-y^2$: $u_{xx}=2$, $u_{yy}=-2$, sum $=0$ ✓.

**Trap:** heat needs **one** initial condition (first derivative in $t$); wave needs **two** ($u$ and $u_t$), like a second-order ODE.

---

## 12. Advanced topics 🟡

> **Must-know facts: solving PDEs**
> - Main method: **separation of variables** $u(x,t)=X(x)T(t)$. It gives sums of sine/cosine modes (Fourier series).
> - Heat on $[0,\pi]$ with $u=0$ at the ends: $u(x,0)=\sin(nx)$ gives $u=e^{-n^2kt}\sin(nx)$. Higher modes die faster. Heat always smooths and decays.
> - Wave on the whole line: **d'Alembert** $u=\frac{f(x+ct)+f(x-ct)}{2}$ (if $u_t(x,0)=0$). Two waves move left and right with speed $c$. Example: $f=\sin x$, $c=1$ gives $u=\sin x\cos t$. Waves do not decay.
> - **Maximum principle:** a harmonic function (and a solution of the heat equation) takes its max and min on the boundary. The wave equation has no maximum principle.
> - Heat spreads with infinite speed; waves travel with finite speed $c$.

> **Must-know facts: dynamical systems**
> - A **dynamical system** is a rule for how a state changes in time: $\mathbf x'=\mathbf f(\mathbf x)$ (continuous) or $x_{n+1}=F(x_n)$ (discrete).
> - **Phase portrait** = picture of all solution curves (trajectories) in the $(x_1,x_2)$-plane.
> - A **limit cycle** is an isolated closed orbit (periodic motion), e.g. the Van der Pol oscillator.
> - **Poincaré–Bendixson:** in the plane (2D) there is no chaos. Chaos needs at least 3 dimensions for ODEs (example: Lorenz system).
> - **Bifurcation** = the qualitative picture changes when a parameter crosses a critical value. Example $x'=rx-x^3$ (pitchfork): for $r<0$ one stable point $0$; for $r>0$, $0$ is unstable and $\pm\sqrt r$ are stable.
> - **Hopf bifurcation:** a pair of complex eigenvalues crosses the imaginary axis → a limit cycle is born.

> **Must-know facts: self-organization**
> - **Self-organization** = order (patterns, rhythms) appears by itself from many interacting parts, without an outside plan. It happens in **open** systems **far from equilibrium** (energy flows through).
> - **Control parameter:** outside parameter we change (e.g. heating). At a critical value the old state becomes unstable.
> - **Order parameter:** a few slow variables that describe the new order (e.g. size of convection rolls).
> - **Slaving principle (Haken):** fast variables follow the slow order parameters.
> - Examples: Bénard convection rolls, laser, Belousov–Zhabotinsky chemical oscillations, Turing patterns (animal skin stripes; need an inhibitor that diffuses faster than the activator).

---

## Formula sheet

| Topic | Form | Recipe / Result |
|---|---|---|
| Exponential | $y'=ky$ | $y=y(0)e^{kt}$ |
| Separable | $y'=g(t)h(y)$ | $\int\frac{dy}{h(y)}=\int g\,dt$; don't forget $h(y_0)=0$ |
| Linear 1st order | $y'+p y=q$ | $\mu=e^{\int p}$, $(\mu y)'=\mu q$ |
| Constant coeff. 1st order | $y'=ay+b$ | $y=Ce^{at}-b/a$ |
| Bernoulli | $y'+py=qy^n$ | $v=y^{1-n}$ → $v'+(1-n)pv=(1-n)q$ |
| Exact | $M\,dx+N\,dy=0$ | test $M_y=N_x$; $F_x=M$, $F_y=N$; $F=C$ |
| 2nd order, const. coeff. | $ay''+by'+cy=0$ | $ar^2+br+c=0$ |
| — real $r_1\ne r_2$ | | $C_1e^{r_1t}+C_2e^{r_2t}$ |
| — double $r$ | | $(C_1+C_2t)e^{rt}$ |
| — complex $\alpha\pm i\beta$ | | $e^{\alpha t}(C_1\cos\beta t+C_2\sin\beta t)$ |
| Inhomogeneous | $\dots=g(t)$ | $y=y_h+y_p$; trial like $g$; ×$t$ at resonance |
| System | $\mathbf x'=A\mathbf x$ | $\sum C_ie^{\lambda_it}\mathbf v_i$; $\lambda^2-\tau\lambda+\Delta=0$ |
| 1D stability | $x'=f(x)$ | $f'(x^*)<0$ stable, $>0$ unstable |
| 2D stability | $\tau=\operatorname{tr}$, $\Delta=\det$ | stable ⇔ $\tau<0,\Delta>0$; $\Delta<0$ saddle; $\tau=0,\Delta>0$ center |
| Existence | Picard–Lindelöf | continuous + Lipschitz ⇒ unique |
| PDE type | $B^2-4AC$ | $<0$ elliptic, $=0$ parabolic, $>0$ hyperbolic |
| Famous PDEs | | Laplace (elliptic), heat (parabolic), wave (hyperbolic) |

---

## Practice MCQs

**Q1.** The ODE $y''+3y'=t^2$ is
A) first order, linear  B) second order, linear  C) second order, nonlinear  D) third order, linear

<details><summary>Answer</summary>

**B** — The highest derivative is $y''$, so order 2. $y'$ and $y''$ appear only to the power 1, so it is linear. ($t^2$ is on the right side; that is fine.)

</details>

**Q2.** Which function solves $y'=3y$, $y(0)=5$?
A) $3e^{5t}$  B) $5e^{t}$  C) $e^{3t}+4$  D) $5e^{3t}$

<details><summary>Answer</summary>

**D** — $y'=ky$ gives $y=y(0)e^{kt}=5e^{3t}$. Check: $y'=15e^{3t}=3y$ ✓. (C has $y(0)=5$ but $y'=3e^{3t}\ne3y$.)

</details>

**Q3.** The solution of $y'=y+t$, $y(0)=1$ is
A) $2e^t-t-1$  B) $e^t+t$  C) $e^t-t$  D) $2e^t+t-1$

<details><summary>Answer</summary>

**A** — $y'-y=t$, $\mu=e^{-t}$, $y=Ce^t-t-1$. $y(0)=C-1=1$, so $C=2$.
Check: $y'=2e^t-1$ and $y+t=2e^t-1$ ✓.

</details>

**Q4.** What is the integrating factor $\mu(t)$ for $y'+2y=e^t$?
A) $e^{-2t}$  B) $e^{2t}$  C) $e^{t}$  D) $2t$

<details><summary>Answer</summary>

**B** — The form is $y'+p y=q$ with $p=2$. So $\mu=e^{\int2\,dt}=e^{2t}$.

</details>

**Q5.** The solution of $y'=2ty$, $y(0)=3$ is
A) $3e^{2t}$  B) $e^{t^2}+2$  C) $3e^{t^2}$  D) $3t^2$

<details><summary>Answer</summary>

**C** — Separable: $\frac{dy}{y}=2t\,dt$, $\ln|y|=t^2+C$, $y=Ke^{t^2}$. $y(0)=K=3$.

</details>

**Q6.** The general solution of $y''-5y'+6y=0$ is
A) $C_1e^{2t}+C_2e^{3t}$  B) $C_1e^{-2t}+C_2e^{-3t}$  C) $C_1\cos2t+C_2\sin3t$  D) $(C_1+C_2t)e^{5t}$

<details><summary>Answer</summary>

**A** — Characteristic equation $r^2-5r+6=(r-2)(r-3)=0$, so $r=2,3$.

</details>

**Q7.** The general solution of $y''+4y=0$ is
A) $C_1e^{2t}+C_2e^{-2t}$  B) $C_1\cos2t+C_2\sin2t$  C) $C_1\cos4t+C_2\sin4t$  D) $(C_1+C_2t)e^{2t}$

<details><summary>Answer</summary>

**B** — $r^2+4=0$ gives $r=\pm2i$ ($\alpha=0$, $\beta=2$). Trap: $\beta=\sqrt4=2$, not $4$.

</details>

**Q8.** The general solution of $y''-4y'+4y=0$ is
A) $C_1e^{2t}+C_2e^{-2t}$  B) $C_1e^{4t}+C_2$  C) $e^{2t}(C_1\cos t+C_2\sin t)$  D) $(C_1+C_2t)e^{2t}$

<details><summary>Answer</summary>

**D** — $r^2-4r+4=(r-2)^2=0$: double root $r=2$. A double root needs the extra factor $t$.

</details>

**Q9.** The heat equation $u_t=u_{xx}$ is
A) elliptic  B) hyperbolic  C) parabolic  D) not a PDE

<details><summary>Answer</summary>

**C** — Only $u_{xx}$ is second order: $A=1$, $B=0$, $C=0$, so $B^2-4AC=0$ → parabolic.

</details>

**Q10.** For $y'=y(1-y)$, which statement is true?
A) $y=0$ is unstable and $y=1$ is stable  B) both equilibria are stable  C) $y=0$ is stable and $y=1$ is unstable  D) there are no equilibria

<details><summary>Answer</summary>

**A** — $f(y)=y-y^2=0$ at $y=0,1$. $f'(y)=1-2y$: $f'(0)=1>0$ unstable, $f'(1)=-1<0$ stable.

</details>

**Q11.** Which substitution turns $y'+y=t\,y^3$ into a linear equation?
A) $v=y^3$  B) $v=y^2$  C) $v=y^{-2}$  D) $v=y^{-3}$

<details><summary>Answer</summary>

**C** — Bernoulli with $n=3$: $v=y^{1-n}=y^{-2}$. The new equation is $v'-2v=-2t$.

</details>

**Q12.** The equation $(2xy+3)\,dx+(x^2+4y)\,dy=0$ has the solution
A) $xy^2+3x+4y=C$  B) $x^2y+3x+2y^2=C$  C) $x^2y+3y+2x^2=C$  D) it is not exact

<details><summary>Answer</summary>

**B** — $M_y=2x=N_x$, so exact. $F=\int M\,dx=x^2y+3x+h(y)$; $F_y=x^2+h'=x^2+4y$ gives $h=2y^2$.

</details>

**Q13.** The general solution of $y''+2y'+5y=0$ is
A) $C_1e^{-t}+C_2e^{-5t}$  B) $e^{t}(C_1\cos2t+C_2\sin2t)$  C) $e^{-2t}(C_1\cos t+C_2\sin t)$  D) $e^{-t}(C_1\cos2t+C_2\sin2t)$

<details><summary>Answer</summary>

**D** — $r=\frac{-2\pm\sqrt{4-20}}{2}=-1\pm2i$. So $\alpha=-1$ (in the exponent) and $\beta=2$ (in cos/sin).

</details>

**Q14.** The solution of $y''-y=0$, $y(0)=2$, $y'(0)=0$ is
A) $e^t+e^{-t}$  B) $2e^t$  C) $2\cos t$  D) $e^t-e^{-t}$

<details><summary>Answer</summary>

**A** — $r=\pm1$, $y=C_1e^t+C_2e^{-t}$. $C_1+C_2=2$ and $C_1-C_2=0$, so $C_1=C_2=1$. (This is $2\cosh t$.) C solves $y''+y=0$, not this one.

</details>

**Q15.** For $y''-3y'+2y=e^t$, the correct trial function for $y_p$ is
A) $Ae^t$  B) $Ate^t$  C) $At^2e^t$  D) $Ae^{2t}$

<details><summary>Answer</summary>

**B** — Roots $r=1,2$. $e^t$ already solves the homogeneous equation (resonance), so multiply by $t$. Result: $y_p=-te^t$.

</details>

**Q16.** A particular solution of $y''-3y'+2y=4$ is
A) $y_p=4$  B) $y_p=4t$  C) $y_p=2$  D) $y_p=\frac12$

<details><summary>Answer</summary>

**C** — Trial $y_p=A$ (constant): $y_p'=y_p''=0$, so $2A=4$ and $A=2$.

</details>

**Q17.** The general solution of $y'+\frac2t\,y=t$ ($t>0$) is
A) $y=\frac{t^2}{3}+\frac{C}{t^2}$  B) $y=\frac t2+Ce^{-2t}$  C) $y=t^2\ln t+Ct^2$  D) $y=\frac{t^2}{4}+\frac{C}{t^2}$

<details><summary>Answer</summary>

**D** — $\mu=e^{\int2/t\,dt}=t^2$. $(t^2y)'=t^3$, so $t^2y=\frac{t^4}{4}+C$. Divide by $t^2$.

</details>

**Q18.** The origin of $\mathbf x'=\begin{pmatrix}1&2\\2&1\end{pmatrix}\mathbf x$ is
A) a stable node  B) a saddle  C) an unstable spiral  D) a center

<details><summary>Answer</summary>

**B** — $\det A=1-4=-3<0$ → saddle. Indeed the eigenvalues are $3$ and $-1$ (opposite signs).

</details>

**Q19.** A $2\times2$ matrix $A$ has trace $-3$ and determinant $2$. The origin of $\mathbf x'=A\mathbf x$ is
A) a stable node  B) a saddle  C) an unstable node  D) a center

<details><summary>Answer</summary>

**A** — $\lambda^2+3\lambda+2=0$ gives $\lambda=-1,-2$: both real and negative. (Check: $\tau<0$, $\Delta>0$, $\tau^2-4\Delta=1>0$.)

</details>

**Q20.** The origin of $\mathbf x'=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\mathbf x$ is
A) a stable spiral  B) a saddle  C) a center  D) an unstable node

<details><summary>Answer</summary>

**C** — $\tau=0$, $\Delta=1>0$. Eigenvalues $\pm i$ (pure imaginary). Solutions move on circles: stable, but not asymptotically stable.

</details>

**Q21.** The PDE $u_{xx}+4u_{xy}+3u_{yy}=0$ is
A) hyperbolic  B) parabolic  C) elliptic  D) elliptic only for $x>0$

<details><summary>Answer</summary>

**A** — $A=1$, $B=4$, $C=3$: $B^2-4AC=16-12=4>0$ → hyperbolic.

</details>

**Q22.** Which function is harmonic ($u_{xx}+u_{yy}=0$)?
A) $x^2+y^2$  B) $x^2-y^2$  C) $x^3$  D) $e^x\cos x$

<details><summary>Answer</summary>

**B** — $u_{xx}=2$, $u_{yy}=-2$, sum $0$. For A the sum is $4$; for C it is $6x$.

</details>

**Q23.** For the IVP $y'=\sqrt{y}$, $y(0)=0$ ($y\ge0$):
A) $y\equiv0$ is the only solution  B) there is no solution  C) there is more than one solution  D) the solution blows up at $t=1$

<details><summary>Answer</summary>

**C** — Both $y\equiv0$ and $y=t^2/4$ work (check: $y'=t/2=\sqrt{t^2/4}$ ✓). Uniqueness fails because $\sqrt y$ is not Lipschitz at $0$.

</details>

**Q24.** Which equation describes a vibrating string and needs two initial conditions $u(x,0)$ and $u_t(x,0)$?
A) Laplace equation $u_{xx}+u_{yy}=0$  B) heat equation $u_t=ku_{xx}$  C) Poisson equation $\Delta u=f$  D) wave equation $u_{tt}=c^2u_{xx}$

<details><summary>Answer</summary>

**D** — The wave equation is second order in $t$, so it needs $u$ and $u_t$ at $t=0$. It is hyperbolic.

</details>

**Q25.** The solution of $u_t=u_{xx}$ on $0<x<\pi$, $u(0,t)=u(\pi,t)=0$, $u(x,0)=\sin x$ is
A) $\cos t\,\sin x$  B) $e^{t}\sin x$  C) $e^{-t}\sin x$  D) $e^{-t^2}\sin x$

<details><summary>Answer</summary>

**C** — Try $u=T(t)\sin x$: $T'\sin x=-T\sin x$, so $T'=-T$, $T=e^{-t}$. Check boundary: $\sin0=\sin\pi=0$ ✓. Heat decays; it does not oscillate.

</details>

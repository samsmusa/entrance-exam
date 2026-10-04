# 08. Statistics

> **Syllabus:**
> - Expectation, variance, higher moments
> - Probability distributions
> - Confidence intervals
> - Descriptive statistics
> - Hypothesis testing
>
> **How to study this file:** Sections 1–7 are 🟢 core: learn them well and redo every worked example.
> Sections 8–9 are 🟡: read the "Must-know facts" only. Time: about 3–4 hours, plus 1 hour for the MCQs.
> Probability basics (Bayes, densities, CLT) are in file 07.

## Contents
1. [Descriptive statistics](#1-descriptive-statistics-) 🟢
2. [Expectation, variance, higher moments](#2-expectation-variance-higher-moments-) 🟢
3. [Probability distributions (summary)](#3-probability-distributions-summary-) 🟢
4. [The normal distribution and the z-table](#4-the-normal-distribution-and-the-z-table-) 🟢
5. [Estimators and the standard error](#5-estimators-and-the-standard-error-) 🟢
6. [Confidence interval for a mean](#6-confidence-interval-for-a-mean-) 🟢
7. [Hypothesis testing: z-test, t-test, p-value, errors](#7-hypothesis-testing-) 🟢
8. [Correlation and regression](#8-correlation-and-regression-) 🟡
9. [Chi-square, t and F distributions; MLE](#9-chi-square-t-and-f-distributions-mle-) 🟡
10. [Formula sheet](#formula-sheet)
11. [Practice MCQs](#practice-mcqs)

**Symbols used in this file**

| Symbol | Meaning |
|---|---|
| $x_1,\dots,x_n$ | the data (a sample of size $n$) |
| $\bar x$ | sample mean |
| $s^2$, $s$ | sample variance, sample standard deviation |
| $\mu$, $\sigma$ | true (population) mean and standard deviation — usually unknown |
| $H_0$, $H_1$ | null hypothesis, alternative hypothesis |
| $\alpha$ | significance level (for example $0.05$) |
| $\Phi(z)$ | $P(Z\le z)$ for a standard normal $Z\sim N(0,1)$ |

---

## 1. Descriptive statistics 🟢

**Meaning.** Descriptive statistics are simple numbers that summarise data: a "centre" and a "spread".

**Centre.**

| Measure | How to compute | Robust to outliers? |
|---|---|---|
| Mean $\bar x$ | $\frac1n\sum x_i$ | no |
| Median | sort the data; take the middle value (for even $n$: average of the two middle values) | yes |
| Mode | the most frequent value | — |

**Spread.**

| Measure | Formula |
|---|---|
| Range | max − min |
| Sample variance | $s^2=\frac{1}{n-1}\sum_{i=1}^n(x_i-\bar x)^2$ |
| Sample SD | $s=\sqrt{s^2}$ |
| Quartiles | $Q_1$ = median of the lower half, $Q_3$ = median of the upper half |
| IQR (interquartile range) | $Q_3-Q_1$ |

**Outliers (boxplot rule).** A value is an outlier if it is below $Q_1-1.5\cdot IQR$ or above $Q_3+1.5\cdot IQR$.
A **boxplot** shows min, $Q_1$, median, $Q_3$, max (the "five-number summary").

**Worked example.** Data: $2,4,4,4,5,5,7,9$ ($n=8$).
1. Mean: $\frac{2+4+4+4+5+5+7+9}{8}=\frac{40}{8}=5$.
2. Median: the two middle values are $4$ and $5$, so median $=4.5$.
3. Mode: $4$ (appears 3 times).
4. Deviations squared: $9,1,1,1,0,0,4,16$; sum $=32$.
5. $s^2=\frac{32}{7}\approx4.57$, $s\approx2.14$. (Dividing by $n=8$ gives $4$, the "population variance".)

**Worked example (outliers).** $Q_1=20$, $Q_3=30$. Then $IQR=10$, and the fences are $20-15=5$ and $30+15=45$. A value $47$ is an outlier; $44$ is not.

**Shape.**
- Symmetric data: mean ≈ median.
- **Right-skewed** (long tail to the right, e.g. incomes): mean > median.
- Left-skewed: mean < median.

**Linear change of data** $y_i=ax_i+b$: $\bar y=a\bar x+b$, $s_y=\lvert a\rvert s_x$. Adding a constant changes the mean, **not** the SD.

> **Trap:** the sample variance divides by $n-1$, not $n$. And one big outlier changes the mean a lot, but the median almost not at all.

---

## 2. Expectation, variance, higher moments 🟢

**Meaning.** These are the "population versions" of the mean and variance (see file 07, Section 7).

| Quantity | Formula | Meaning |
|---|---|---|
| Mean | $\mu=E[X]$ | centre |
| Variance | $\sigma^2=E[(X-\mu)^2]=E[X^2]-\mu^2$ | spread |
| $k$-th moment | $E[X^k]$ | |
| $k$-th central moment | $E[(X-\mu)^k]$ | |
| Skewness | $\frac{E[(X-\mu)^3]}{\sigma^3}$ | asymmetry |
| Kurtosis | $\frac{E[(X-\mu)^4]}{\sigma^4}$ | heavy tails |

**Rules.** $E[aX+b]=a\mu+b$, $\operatorname{Var}(aX+b)=a^2\sigma^2$, $\operatorname{SD}(aX+b)=\lvert a\rvert\sigma$.

**Worked example.** $P(X=0)=0.5$, $P(X=1)=0.3$, $P(X=2)=0.2$.
1. $E[X]=0\cdot0.5+1\cdot0.3+2\cdot0.2=0.7$.
2. $E[X^2]=0+1\cdot0.3+4\cdot0.2=1.1$.
3. $\operatorname{Var}X=1.1-0.7^2=1.1-0.49=0.61$.

> **Must-know facts (higher moments) 🟡**
> - Skewness $>0$: long right tail. Skewness $<0$: long left tail. Symmetric distribution: skewness $0$.
> - Normal distribution: skewness $0$, kurtosis $3$ ("excess kurtosis" $=3-3=0$).
> - Exponential distribution: skewness $2$ (right-skewed).
> - Adding a constant does not change variance, skewness or kurtosis.

> **Trap:** $E[X^2]$ is **not** $(E[X])^2$. Their difference is exactly the variance.

---

## 3. Probability distributions (summary) 🟢

Here $q=1-p$. The full explanation is in file 07, Section 8.

| Name | Mean | Variance | Remember |
|---|---|---|---|
| Bernoulli$(p)$ | $p$ | $pq$ | one yes/no trial |
| Binomial$(n,p)$ | $np$ | $npq$ | $P(X=k)=\binom nkp^kq^{n-k}$ |
| Geometric$(p)$ (trials until 1st success) | $\frac1p$ | $\frac q{p^2}$ | memoryless (discrete) |
| Poisson$(\lambda)$ | $\lambda$ | $\lambda$ | mean = variance |
| Uniform$[a,b]$ | $\frac{a+b}2$ | $\frac{(b-a)^2}{12}$ | |
| Exponential$(\lambda)$ | $\frac1\lambda$ | $\frac1{\lambda^2}$ | $P(X>t)=e^{-\lambda t}$, memoryless |
| Normal $N(\mu,\sigma^2)$ | $\mu$ | $\sigma^2$ | bell curve, symmetric |

**Worked example.** $X\sim U[2,8]$. Mean $=\frac{2+8}2=5$. Variance $=\frac{(8-2)^2}{12}=\frac{36}{12}=3$.

**Worked example.** $X\sim\text{Bin}(10,0.3)$. Mean $=3$, variance $=10\cdot0.3\cdot0.7=2.1$.

**Worked example (Poisson approximation).** 1000 items, each defective with probability $0.002$. Then $X\approx\text{Poisson}(\lambda=np=2)$, and $P(X=0)\approx e^{-2}\approx0.135$.

**Memoryless.** For the exponential: $P(X>s+t\mid X>s)=P(X>t)$. "An old light bulb is as good as a new one." The exponential is the only continuous memoryless distribution; the geometric is the only discrete one.

> **Trap:** for Poisson, mean **=** variance. For Binomial, variance $npq$ is **smaller** than the mean $np$.

---

## 4. The normal distribution and the z-table 🟢

**Meaning.** $N(\mu,\sigma^2)$ is the bell curve with centre $\mu$ and spread $\sigma$. To use the table, change $X$ to the **standard normal** $Z\sim N(0,1)$.

**Formula (standardize).**
$$Z=\frac{X-\mu}{\sigma},\qquad P(X\le x)=\Phi\!\left(\frac{x-\mu}{\sigma}\right),\qquad \Phi(-z)=1-\Phi(z)$$

**z-table.**

| $z$ | 0 | 0.5 | 1 | 1.28 | 1.5 | 1.645 | 1.96 | 2 | 2.326 | 2.576 | 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $\Phi(z)$ | 0.5 | 0.6915 | 0.8413 | 0.90 | 0.9332 | 0.95 | 0.975 | 0.9772 | 0.99 | 0.995 | 0.9987 |

**Critical values (learn these three!)**

| Value | Two-sided level | One-sided level |
|---|---|---|
| $1.645$ | 90% CI / $\alpha=0.10$ | $\alpha=0.05$ |
| $1.96$ | 95% CI / $\alpha=0.05$ | $\alpha=0.025$ |
| $2.576$ | 99% CI / $\alpha=0.01$ | $\alpha=0.005$ |

**68–95–99.7 rule:** $P(\lvert Z\rvert\le1)\approx0.68$, $P(\lvert Z\rvert\le2)\approx0.95$, $P(\lvert Z\rvert\le3)\approx0.997$.

**Worked example.** IQ $\sim N(100,15^2)$. $P(\text{IQ}>130)$?
1. $z=\frac{130-100}{15}=2$.
2. $P=1-\Phi(2)=1-0.9772=0.0228$.

**Worked example 2.** $X\sim N(50,4^2)$. $P(46<X<54)$?
1. $z$-values: $\frac{46-50}{4}=-1$ and $\frac{54-50}4=1$.
2. $P=\Phi(1)-\Phi(-1)=2\cdot0.8413-1=0.6826$.

**Sum of independent normals** is normal: $N(\mu_1,\sigma_1^2)+N(\mu_2,\sigma_2^2)=N(\mu_1+\mu_2,\ \sigma_1^2+\sigma_2^2)$.

> **Trap:** $N(\mu,\sigma^2)$ uses the **variance** as second number. $N(100,225)$ means $\sigma=15$, not $225$.

---

## 5. Estimators and the standard error 🟢

**Meaning.** We do not know $\mu$ or $\sigma$. We **estimate** them from the data. An estimator is a formula using the data, e.g. $\bar x$.

**Key ideas.**
- **Unbiased:** the estimator is correct "on average": $E[\hat\theta]=\theta$.
- $\bar X$ is unbiased for $\mu$.
- $S^2=\frac1{n-1}\sum(X_i-\bar X)^2$ is unbiased for $\sigma^2$. **This is why we divide by $n-1$.**
- With $n$ in the denominator, the estimator is a bit too small on average: $E=\frac{n-1}{n}\sigma^2$.

**Standard error (SE)** = standard deviation of $\bar X$:
$$SE=\frac{\sigma}{\sqrt n}\quad(\text{or }\frac{s}{\sqrt n}\text{ if }\sigma\text{ is unknown})$$

**Worked example.** $\sigma=10$, $n=100$: $SE=\frac{10}{\sqrt{100}}=1$. With $n=400$: $SE=\frac{10}{20}=0.5$.
So **4 times more data gives half the SE.**

> **Trap:** the SE gets smaller with $\sqrt n$, not with $n$. Doubling $n$ does **not** halve the SE.

---

## 6. Confidence interval for a mean 🟢

**Meaning.** A confidence interval (CI) is a range of plausible values for the unknown mean $\mu$. A 95% CI is made by a method that catches the true $\mu$ in 95% of repeated samples.

**Formulas.**

| Case | CI at level $1-\alpha$ |
|---|---|
| $\sigma$ known (or $n$ large) | $\bar x\pm z\cdot\frac{\sigma}{\sqrt n}$ with $z=1.645$ (90%), $1.96$ (95%), $2.576$ (99%) |
| $\sigma$ unknown, normal data | $\bar x\pm t_{n-1}\cdot\frac{s}{\sqrt n}$, $t$-value with $n-1$ degrees of freedom |
| Proportion (large $n$) | $\hat p\pm z\sqrt{\frac{\hat p(1-\hat p)}{n}}$ |

The part after $\pm$ is the **margin of error** $E$. The width is $2E$.

**Worked example ($z$-interval).** $\bar x=50$, $\sigma=10$, $n=100$, 95%.
1. $SE=\frac{10}{\sqrt{100}}=1$.
2. Margin $=1.96\cdot1=1.96$.
3. CI $=[50-1.96,\ 50+1.96]=[48.04,\ 51.96]$.

**Worked example ($t$-interval).** $n=16$, $\bar x=20$, $s=4$, 95%, $\sigma$ unknown.
1. $SE=\frac{4}{\sqrt{16}}=1$.
2. Degrees of freedom $=15$, $t_{15}=2.131$ (from a $t$-table).
3. CI $=20\pm2.131=[17.869,\ 22.131]$.

**Some $t$-values** (95%, two-sided): df 5: 2.571; df 9: 2.262; df 15: 2.131; df 29: 2.045; df $\infty$: 1.96.

**What makes the CI wider?**

| Change | Width |
|---|---|
| higher confidence (95% → 99%) | wider |
| larger $\sigma$ | wider |
| larger $n$ | narrower ($\propto\frac1{\sqrt n}$) |
| $t$ instead of $z$ (small $n$) | wider |

**Sample size.** For margin $E$: $n=\left(\frac{z\,\sigma}{E}\right)^2$, round **up**.
Example: $\sigma=10$, $E=2$, 95%: $n=\left(\frac{1.96\cdot10}{2}\right)^2=96.04$, so $n=97$.

**Correct interpretation.** "If we repeat the sampling many times, about 95% of the intervals contain $\mu$."
Wrong: "95% of the data lie in the CI." Wrong: "$\mu$ changes randomly."

> **Trap:** to make the CI **half** as wide you need **4 times** the sample size, not 2 times.

---

## 7. Hypothesis testing 🟢

**Meaning.** We have a claim $H_0$ (for example "$\mu=50$"). We check if the data are very unlikely when $H_0$ is true. If yes, we **reject** $H_0$.

### 7.1 The steps
1. Write $H_0$ (with "=") and $H_1$ (what we want to show).
   - two-sided: $H_1:\mu\neq\mu_0$; one-sided: $H_1:\mu>\mu_0$ or $\mu<\mu_0$.
2. Choose $\alpha$ (usually $0.05$).
3. Compute the test statistic.
4. Compare with the critical value (or compare the p-value with $\alpha$).
5. Decide: reject $H_0$ or "do not reject $H_0$".

### 7.2 Test statistics

| Test | Statistic | Use when |
|---|---|---|
| $z$-test | $z=\dfrac{\bar x-\mu_0}{\sigma/\sqrt n}$ | $\sigma$ known |
| $t$-test | $t=\dfrac{\bar x-\mu_0}{s/\sqrt n}$, df $=n-1$ | $\sigma$ unknown |
| paired $t$-test | same as $t$-test on the differences $d_i$ | before/after on the same people |

**Reject $H_0$** (two-sided, $\alpha=0.05$) if $\lvert z\rvert>1.96$. One-sided ($H_1:\mu>\mu_0$, $\alpha=0.05$): reject if $z>1.645$.

**Worked example.** $H_0:\mu=50$, $H_1:\mu\neq50$, $\sigma=8$, $n=64$, $\bar x=52$.
1. $SE=\frac{8}{\sqrt{64}}=1$.
2. $z=\frac{52-50}{1}=2$.
3. $\alpha=0.05$: $\lvert z\rvert=2>1.96$, so **reject** $H_0$.
4. $\alpha=0.01$: $2<2.576$, so **do not reject**.
5. p-value $=2(1-\Phi(2))=2\cdot0.0228\approx0.046$.

### 7.3 The p-value
**Meaning.** The p-value is the probability, **if $H_0$ is true**, of getting a result at least as extreme as the one we observed.

- Small p-value = strong evidence against $H_0$.
- **Rule:** reject $H_0$ if $p\le\alpha$.
- Two-sided $z$-test: $p=2\,(1-\Phi(\lvert z\rvert))$. One-sided: $p=1-\Phi(z)$.

**Worked example.** $p=0.03$: reject at $\alpha=0.05$ (since $0.03\le0.05$); do not reject at $\alpha=0.01$.

> **Trap:** the p-value is **not** "the probability that $H_0$ is true". And "not rejecting $H_0$" does **not** prove $H_0$.

### 7.4 Type I and type II errors

|  | $H_0$ is true | $H_0$ is false |
|---|---|---|
| Reject $H_0$ | **Type I error** (probability $\alpha$) | correct (probability = **power** $=1-\beta$) |
| Do not reject $H_0$ | correct | **Type II error** (probability $\beta$) |

Memory help (court): $H_0$ = "innocent". Type I = an innocent person goes to prison. Type II = a guilty person goes free.

**Power** $=1-\beta=P(\text{reject }H_0\mid H_0\text{ false})$. Power gets **bigger** when:
- $n$ is bigger,
- the true effect is bigger,
- $\sigma$ is smaller,
- $\alpha$ is bigger.

If you make $\alpha$ smaller (with the same $n$), then $\beta$ gets bigger. There is a trade-off.

### 7.5 CI and test are connected
A two-sided test at level $\alpha$ rejects $H_0:\mu=\mu_0$ **exactly when** $\mu_0$ is **outside** the $(1-\alpha)$ CI.
Example: 95% CI $=[12.1,\ 15.3]$. Test $\mu_0=16$ at 5%: reject. Test $\mu_0=14$: do not reject.

> **Trap:** $\alpha$ is the probability of a type I error, chosen **before** the test. $\alpha+\beta$ is in general **not** 1.

---

## 8. Correlation and regression 🟡

**Short idea.** The correlation $r$ measures how close the points $(x_i,y_i)$ are to a straight line.
$$r=\frac{\sum(x_i-\bar x)(y_i-\bar y)}{\sqrt{\sum(x_i-\bar x)^2\,\sum(y_i-\bar y)^2}}$$
Regression line $\hat y=a+bx$: $b=\frac{\sum(x_i-\bar x)(y_i-\bar y)}{\sum(x_i-\bar x)^2}$, $a=\bar y-b\bar x$.

> **Must-know facts**
> - $-1\le r\le1$. $r=\pm1$ means all points lie on a line. $r=0$ means no **linear** relation (there can still be a nonlinear one, e.g. $y=x^2$).
> - $r$ has no units. Changing units (cm → m, kg → g) does **not** change $r$.
> - Correlation is **not** causation.
> - The regression line goes through $(\bar x,\bar y)$. $R^2=r^2$ = share of the variance of $y$ explained by the line.
> - Example: $x=1,2,3,4,5$; $y=2,4,5,4,5$ gives $b=\frac6{10}=0.6$, $a=4-0.6\cdot3=2.2$, so $\hat y=2.2+0.6x$.

---

## 9. Chi-square, t and F distributions; MLE 🟡

> **Must-know facts**
> - $\chi^2_k$ (chi-square with $k$ degrees of freedom) = sum of $k$ squared independent $N(0,1)$ variables. Mean $k$, variance $2k$. Only positive values.
> - $\chi^2$ tests: goodness of fit has df $=$ (number of classes) $-1$; independence test in an $r\times c$ table has df $=(r-1)(c-1)$. Statistic $\sum\frac{(O-E)^2}{E}$ ($O$ = observed, $E$ = expected count).
> - $t_\nu$ is symmetric like $N(0,1)$ but has **heavier tails**, so $t$-values are bigger than $z$-values. As $\nu\to\infty$, $t_\nu\to N(0,1)$.
> - $F$ distribution = ratio of two scaled $\chi^2$ variables; used to compare two variances (and in ANOVA).
> - **MLE** (maximum likelihood estimator) = the parameter value that makes the observed data most likely. Examples: Bernoulli $\hat p=\bar x$; Poisson $\hat\lambda=\bar x$; Exponential $\hat\lambda=\frac1{\bar x}$; Normal $\hat\mu=\bar x$.

---

## Formula sheet

| Topic | Formula |
|---|---|
| Mean | $\bar x=\frac1n\sum x_i$ |
| Sample variance | $s^2=\frac1{n-1}\sum(x_i-\bar x)^2$ |
| IQR | $Q_3-Q_1$; outlier if outside $[Q_1-1.5\,IQR,\ Q_3+1.5\,IQR]$ |
| Variance | $\operatorname{Var}X=E[X^2]-(EX)^2$ |
| Linear change | $E[aX+b]=a\mu+b$, $\operatorname{SD}(aX+b)=\lvert a\rvert\sigma$ |
| Binomial | mean $np$, variance $npq$ |
| Poisson | mean $=$ variance $=\lambda$ |
| Uniform$[a,b]$ | mean $\frac{a+b}2$, variance $\frac{(b-a)^2}{12}$ |
| Exponential | mean $\frac1\lambda$, variance $\frac1{\lambda^2}$, $P(X>t)=e^{-\lambda t}$ |
| Standardize | $z=\frac{x-\mu}{\sigma}$, $\Phi(-z)=1-\Phi(z)$ |
| Standard error | $SE=\frac{\sigma}{\sqrt n}$ |
| CI ($\sigma$ known) | $\bar x\pm z\frac{\sigma}{\sqrt n}$ |
| CI ($\sigma$ unknown) | $\bar x\pm t_{n-1}\frac{s}{\sqrt n}$ |
| Sample size | $n=\left(\frac{z\sigma}{E}\right)^2$, round up |
| $z$-test | $z=\frac{\bar x-\mu_0}{\sigma/\sqrt n}$ |
| $t$-test | $t=\frac{\bar x-\mu_0}{s/\sqrt n}$, df $n-1$ |
| Decision | reject $H_0$ if $p\le\alpha$ |
| Errors | type I: $P=\alpha$; type II: $P=\beta$; power $=1-\beta$ |
| $z$ critical values | 1.645 (90%), 1.96 (95%), 2.576 (99%) |
| $\chi^2$ df | $k-1$ (fit), $(r-1)(c-1)$ (independence) |

---

## Practice MCQs

**Q1.** What is the median of the data $3,\ 1,\ 7,\ 5,\ 9$?
- A) $3$
- B) $5$
- C) $7$
- D) $5.5$

<details><summary>Answer</summary>

**B** — Sort: $1,3,5,7,9$. The middle (3rd) value is $5$.

</details>

**Q2.** Data: $2,4,4,4,5,5,7,9$. Mean, median and mode are
- A) $5,\ 4.5,\ 4$
- B) $5,\ 5,\ 4$
- C) $4.5,\ 5,\ 4$
- D) $5,\ 4.5,\ 5$

<details><summary>Answer</summary>

**A** — Mean $\frac{40}8=5$. Median $\frac{4+5}2=4.5$. Mode $4$ (three times).

</details>

**Q3.** The number $10$ is added to every value of a data set. What happens?
- A) Mean and SD both increase by 10
- B) Mean stays the same, SD increases by 10
- C) Mean increases by 10, SD does not change
- D) Nothing changes

<details><summary>Answer</summary>

**C** — Shifting all data moves the centre but not the spread.

</details>

**Q4.** $X\sim\text{Bin}(10,\,0.3)$. $\operatorname{Var}(X)=$
- A) $3$
- B) $0.21$
- C) $7$
- D) $2.1$

<details><summary>Answer</summary>

**D** — $npq=10\cdot0.3\cdot0.7=2.1$.

</details>

**Q5.** For which distribution are the mean and the variance always equal?
- A) Poisson
- B) Binomial
- C) Exponential
- D) Uniform

<details><summary>Answer</summary>

**A** — Poisson$(\lambda)$: mean $\lambda$ and variance $\lambda$.

</details>

**Q6.** $X\sim U[2,8]$. Mean and variance are
- A) $(5,\ 6)$
- B) $(5,\ 3)$
- C) $(5,\ 36)$
- D) $(4,\ 3)$

<details><summary>Answer</summary>

**B** — Mean $\frac{2+8}2=5$. Variance $\frac{6^2}{12}=3$.

</details>

**Q7.** A type I error means
- A) not rejecting $H_0$ when $H_0$ is false
- B) choosing $\alpha$ too big
- C) rejecting $H_0$ when $H_0$ is true
- D) rejecting $H_0$ when $H_0$ is false

<details><summary>Answer</summary>

**C** — Type I = false alarm. Its probability is $\alpha$. A is a type II error; D is a correct decision.

</details>

**Q8.** The p-value is
- A) the probability that $H_0$ is true
- B) the probability of a type II error
- C) the probability that $H_1$ is true
- D) the probability, if $H_0$ is true, of a result at least as extreme as the observed one

<details><summary>Answer</summary>

**D** — This is the definition. A and C are the most common wrong answers.

</details>

**Q9.** The sample variance uses $n-1$ in the denominator because
- A) then $E[S^2]=\sigma^2$ (unbiased)
- B) then $S$ is robust to outliers
- C) then $S^2$ is always smaller
- D) then $S$ is unbiased for $\sigma$

<details><summary>Answer</summary>

**A** — With $n-1$ the estimator is correct on average. (With $n$ it would be too small on average.)

</details>

**Q10.** Data: $3,7,8,5,12$. The sample variance $s^2$ is
- A) $9.2$
- B) $46$
- C) $11.5$
- D) $7$

<details><summary>Answer</summary>

**C** — $\bar x=7$. Squared deviations: $16,0,1,4,25$, sum $46$. $s^2=\frac{46}{5-1}=11.5$. (9.2 divides by $n$.)

</details>

**Q11.** $Q_1=20$ and $Q_3=30$. With the $1.5\cdot IQR$ rule, which value is an outlier?
- A) $6$
- B) $44$
- C) $35$
- D) $47$

<details><summary>Answer</summary>

**D** — $IQR=10$. Fences: $20-15=5$ and $30+15=45$. Only $47$ is outside.

</details>

**Q12.** IQ $\sim N(100,15^2)$. $P(\text{IQ}>130)\approx$
- A) $0.0228$
- B) $0.0456$
- C) $0.1587$
- D) $0.9772$

<details><summary>Answer</summary>

**A** — $z=\frac{130-100}{15}=2$. $1-\Phi(2)=1-0.9772=0.0228$.

</details>

**Q13.** $X\sim N(50,\,16)$. $P(46<X<54)\approx$
- A) $0.95$
- B) $0.68$
- C) $0.50$
- D) $0.99$

<details><summary>Answer</summary>

**B** — $\sigma=\sqrt{16}=4$. The interval is $\mu\pm1\sigma$, so $2\Phi(1)-1\approx0.68$.

</details>

**Q14.** $\bar x=50$, $\sigma=10$ known, $n=100$. The 95% CI for $\mu$ is
- A) $[48.355,\ 51.645]$
- B) $[47.424,\ 52.576]$
- C) $[30.4,\ 69.6]$
- D) $[48.04,\ 51.96]$

<details><summary>Answer</summary>

**D** — $SE=\frac{10}{10}=1$; $50\pm1.96$. A uses 1.645 (90%), B uses 2.576 (99%), C forgets $\sqrt n$.

</details>

**Q15.** You want a CI that is half as wide (same level, same $\sigma$). The sample size must be
- A) doubled
- B) multiplied by 4
- C) halved
- D) multiplied by $\sqrt2$

<details><summary>Answer</summary>

**B** — Width $\propto\frac1{\sqrt n}$. To halve it, $\sqrt n$ must double, so $n$ must be 4 times bigger.

</details>

**Q16.** $n=16$ normal observations, $\bar x=20$, $s=4$, $\sigma$ unknown. The 95% CI for $\mu$ is
- A) $20\pm1.96\cdot1$
- B) $20\pm2.131\cdot4$
- C) $20\pm2.131\cdot1$
- D) $20\pm1.96\cdot4$

<details><summary>Answer</summary>

**C** — $\sigma$ unknown, so use $t$ with $15$ df: $2.131$. $SE=\frac{4}{\sqrt{16}}=1$.

</details>

**Q17.** Test $H_0:\mu=50$ against $H_1:\mu\neq50$ with $\sigma=8$, $n=64$, $\bar x=52$. Which is correct?
- A) $z=0.25$; do not reject at 5%
- B) $z=2$; reject at 5% but not at 1%
- C) $z=2$; reject at 1%
- D) $z=16$; reject at every level

<details><summary>Answer</summary>

**B** — $SE=\frac8{8}=1$, $z=\frac{52-50}1=2$. $1.96<2<2.576$.

</details>

**Q18.** A test gives $p=0.03$. Which statement is true?
- A) $H_0$ is rejected at $\alpha=0.01$
- B) $H_0$ is true with probability 3%
- C) $H_0$ is rejected at $\alpha=0.05$
- D) The effect is large

<details><summary>Answer</summary>

**C** — $0.03\le0.05$, so reject at 5%. But $0.03>0.01$. The p-value says nothing about $P(H_0)$ or the size of the effect.

</details>

**Q19.** All else equal, which change **increases** the power of a test?
- A) a larger sample size
- B) a smaller $\alpha$
- C) a smaller sample size
- D) a larger population SD

<details><summary>Answer</summary>

**A** — Larger $n$ gives a smaller SE, so it is easier to detect a true effect. B, C and D reduce the power.

</details>

**Q20.** A 95% CI for $\mu$ is $[12.1,\ 15.3]$. A two-sided test at $\alpha=0.05$
- A) rejects $H_0:\mu=14$
- B) rejects $H_0:\mu=13$
- C) rejects $H_0:\mu=12.5$
- D) rejects $H_0:\mu=16$

<details><summary>Answer</summary>

**D** — The test rejects exactly the values outside the CI. Only $16$ is outside $[12.1,15.3]$.

</details>

**Q21.** What is the critical value for a **one-sided** $z$-test at $\alpha=0.05$?
- A) $1.96$
- B) $2.576$
- C) $1.645$
- D) $1.28$

<details><summary>Answer</summary>

**C** — One-sided 5%: $\Phi(z)=0.95$, so $z=1.645$. (1.96 is for two-sided 5%.)

</details>

**Q22.** A data set is strongly right-skewed (like incomes). Usually
- A) mean < median
- B) mean > median
- C) mean = median
- D) skewness < 0

<details><summary>Answer</summary>

**B** — The long right tail pulls the mean up, but not the median.

</details>

**Q23.** Height (in cm) and weight (in kg) have correlation $r=0.6$. Height is changed to metres and weight to grams. The new correlation is
- A) $0.006$
- B) $600$
- C) $-0.6$
- D) $0.6$

<details><summary>Answer</summary>

**D** — Correlation has no units. Multiplying by positive constants does not change $r$.

</details>

**Q24.** A $\chi^2$ test of independence uses a $3\times4$ table. The degrees of freedom are
- A) $6$
- B) $12$
- C) $11$
- D) $7$

<details><summary>Answer</summary>

**A** — $(r-1)(c-1)=(3-1)(4-1)=2\cdot3=6$.

</details>

# 08. Statistics

> **Official topics (Placement Test guide):** expectation, variance and higher moments; normal distribution and standardization; descriptive statistics; estimators and unbiasedness; confidence intervals; hypothesis tests, p-values; parametric and non-parametric tests.
>
> **Exam:** 7 questions on this topic, 5 options each, about 85 seconds per question. Mostly definitions (α, p-value, unbiased, which test to use) plus short calculations (z-score, CI, sample variance).
>
> **How to study this file:** every section is 🟢 (all are on the official list). Learn the definitions and the "which test when" table, then redo the worked examples. Time: about 4 hours + 1 hour MCQs.
>
> *Removed (not on the official list, or covered elsewhere):* the distribution summary table (→ [07-measure-and-probability.md](07-measure-and-probability.md), section 8), the regression-line formula (one line kept). Correlation is now part of descriptive statistics; MLE is now part of estimators.

## Contents
1. [Descriptive statistics](#1-descriptive-statistics-) 🟢
2. [Expectation, variance, higher moments](#2-expectation-variance-higher-moments-) 🟢
3. [The normal distribution and standardization](#3-the-normal-distribution-and-standardization-) 🟢
4. [Estimators and unbiasedness](#4-estimators-and-unbiasedness-) 🟢
5. [Confidence intervals](#5-confidence-intervals-) 🟢
6. [Hypothesis tests and p-values](#6-hypothesis-tests-and-p-values-) 🟢
7. [Parametric tests](#7-parametric-tests-) 🟢
8. [Non-parametric tests](#8-non-parametric-tests-) 🟢
9. [Formula sheet](#formula-sheet)
10. [Practice MCQs](#practice-mcqs) (32 questions, 5 options)

**Symbols:** data $x_1,\dots,x_n$; sample mean $\bar x$; sample variance $s^2$; population mean / SD $\mu,\sigma$; hypotheses $H_0,H_1$; significance level $\alpha$; $\Phi(z)=P(Z\le z)$ for $Z\sim N(0,1)$.

---

## 1. Descriptive statistics 🟢

**Centre**
| Measure | How | Robust to outliers? |
|---|---|---|
| mean $\bar x$ | $\frac1n\sum x_i$ | no |
| median | middle of the sorted data (even $n$: average of the two middle values) | yes |
| mode | most frequent value | — |

**Spread**
| Measure | Formula |
|---|---|
| range | max − min |
| sample variance | $s^2=\frac1{n-1}\sum(x_i-\bar x)^2$ |
| sample SD | $s=\sqrt{s^2}$ |
| quartiles, IQR | $Q_1,Q_3$ = medians of lower/upper half; $IQR=Q_3-Q_1$ |
| MAD | median of $\lvert x_i-\text{median}\rvert$ (robust) |

**Outliers (boxplot rule):** below $Q_1-1.5\,IQR$ or above $Q_3+1.5\,IQR$. A **boxplot** shows the five-number summary (min, $Q_1$, median, $Q_3$, max).

**Worked example.** $2,4,4,4,5,5,7,9$.
1. Mean $\frac{40}8=5$; median $\frac{4+5}2=4.5$; mode $4$.
2. Squared deviations $9,1,1,1,0,0,4,16$, sum $32$.
3. $s^2=\frac{32}7\approx4.57$ (dividing by $n$ would give $4$).

**Shape:** symmetric ⇒ mean ≈ median; right-skewed (long right tail, incomes) ⇒ mean > median; left-skewed ⇒ mean < median.

**Linear change** $y_i=ax_i+b$: $\bar y=a\bar x+b$, $s_y=\lvert a\rvert s_x$; median and quartiles transform the same way.

**Two variables: correlation.**
$$r=\frac{\sum(x_i-\bar x)(y_i-\bar y)}{\sqrt{\sum(x_i-\bar x)^2\sum(y_i-\bar y)^2}}\in[-1,1].$$
$r=\pm1$: points on a line; $r=0$: no **linear** relation (e.g. $y=x^2$ on symmetric data). $r$ has no units; correlation ≠ causation. Least-squares line goes through $(\bar x,\bar y)$ with slope $r\frac{s_y}{s_x}$.

> **Trap:** sample variance divides by $n-1$. One outlier moves the mean a lot but the median hardly at all.

---

## 2. Expectation, variance, higher moments 🟢

| Quantity | Formula | Meaning |
|---|---|---|
| mean | $\mu=E[X]$ | centre |
| variance | $\sigma^2=E[(X-\mu)^2]=E[X^2]-\mu^2$ | spread |
| $k$-th (raw) moment | $E[X^k]$ | |
| $k$-th central moment | $E[(X-\mu)^k]$ | |
| **skewness** | $\gamma_1=\frac{E[(X-\mu)^3]}{\sigma^3}$ | asymmetry |
| **kurtosis** | $\frac{E[(X-\mu)^4]}{\sigma^4}$ | tail weight |

**Rules:** $E[aX+b]=a\mu+b$, $\operatorname{Var}(aX+b)=a^2\sigma^2$. Shifting changes only the mean; skewness and kurtosis do not change under $aX+b$ with $a>0$ (skewness flips sign for $a<0$).

> **Must-know facts**
> 1. Symmetric distribution ⇒ all odd central moments are $0$ (skewness $0$).
> 2. Normal: skewness $0$, kurtosis $3$ (**excess kurtosis** = kurtosis − 3 = $0$). Heavy tails: excess kurtosis $>0$.
> 3. Exponential: skewness $2$ (right-skewed).
> 4. Moments may not exist: Cauchy has no mean; $t_2$ has no variance.
> 5. Sample versions: $\frac1n\sum(x_i-\bar x)^3/s^3$ etc.

**Worked example.** $P(X=0)=0.5$, $P(X=1)=0.3$, $P(X=2)=0.2$: $E[X]=0.7$, $E[X^2]=1.1$, $\operatorname{Var}=1.1-0.49=0.61$.

> **Trap:** $E[X^2]\ne(E[X])^2$; the difference is the variance.

---

## 3. The normal distribution and standardization 🟢

$X\sim N(\mu,\sigma^2)$: density $\frac1{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/(2\sigma^2)}$, symmetric bell around $\mu$. **Fully determined by mean and variance** (official example 1).

**Standardization**
$$Z=\frac{X-\mu}\sigma\sim N(0,1),\qquad P(X\le x)=\Phi\!\left(\frac{x-\mu}\sigma\right),\qquad\Phi(-z)=1-\Phi(z).$$
For data: the **z-score** $z_i=\frac{x_i-\bar x}{s}$ says how many SDs a value is from the mean.

| $z$ | 0 | 0.5 | 1 | 1.28 | 1.5 | 1.645 | 1.96 | 2 | 2.326 | 2.576 | 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $\Phi(z)$ | 0.5 | 0.6915 | 0.8413 | 0.90 | 0.9332 | 0.95 | 0.975 | 0.9772 | 0.99 | 0.995 | 0.9987 |

**Critical values:** $1.645$ (90% two-sided / 5% one-sided), $1.96$ (95% / 2.5%), $2.576$ (99% / 0.5%).
**68–95–99.7 rule:** within $1\sigma,2\sigma,3\sigma$.

> **Must-know facts**
> 1. $aX+b\sim N(a\mu+b,a^2\sigma^2)$.
> 2. Independent normals: $X+Y\sim N(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$; $\bar X\sim N(\mu,\frac{\sigma^2}n)$ exactly.
> 3. Mean = median = mode; inflection points at $\mu\pm\sigma$.
> 4. Normality can be checked with a Q–Q plot or a test (Shapiro–Wilk, Kolmogorov–Smirnov).

**Worked examples.**
- IQ $\sim N(100,15^2)$: $P(>130)=1-\Phi(2)=0.0228$.
- $X\sim N(50,16)$: $\sigma=4$, $P(46<X<54)=2\Phi(1)-1=0.6826$.

> **Trap:** $N(100,225)$ means $\sigma=15$ — the second parameter is the **variance**.

---

## 4. Estimators and unbiasedness 🟢

An **estimator** $\hat\theta=T(X_1,\dots,X_n)$ is a function of the sample used to guess a parameter $\theta$. It is itself a random variable.

| Property | Definition |
|---|---|
| **unbiased** | $E[\hat\theta]=\theta$ for every $\theta$ |
| bias | $b(\hat\theta)=E[\hat\theta]-\theta$ |
| asymptotically unbiased | $E[\hat\theta_n]\to\theta$ |
| **mean squared error** | $MSE=E[(\hat\theta-\theta)^2]=\operatorname{Var}(\hat\theta)+b^2$ |
| **consistent** | $\hat\theta_n\to\theta$ in probability as $n\to\infty$ |
| more **efficient** | smaller variance among unbiased estimators |

**Standard results**
- $\bar X$ is unbiased for $\mu$, $\operatorname{Var}\bar X=\frac{\sigma^2}n$, consistent (LLN).
- $S^2=\frac1{n-1}\sum(X_i-\bar X)^2$ is **unbiased** for $\sigma^2$. With $\frac1n$: $E=\frac{n-1}n\sigma^2$ (biased, too small). This is why we divide by $n-1$ (Bessel's correction).
- $S=\sqrt{S^2}$ is **not** unbiased for $\sigma$ (Jensen).
- Unbiased + variance $\to0$ ⇒ consistent.
- **Cramér–Rao:** the variance of an unbiased estimator is at least $\frac1{nI(\theta)}$ (Fisher information).

**Standard error:** $SE=\frac\sigma{\sqrt n}$ (or $\frac s{\sqrt n}$). 4× data ⇒ half the SE.

### How to construct estimators
- **Method of moments:** set sample moments equal to theoretical moments.
- **Maximum likelihood (MLE):** maximize $L(\theta)=\prod f(x_i;\theta)$ (usually $\log L$).

| Model | MLE |
|---|---|
| Bernoulli $(p)$ | $\hat p=\bar x$ |
| Poisson $(\lambda)$ | $\hat\lambda=\bar x$ |
| Exponential $(\lambda)$ | $\hat\lambda=\frac1{\bar x}$ |
| $N(\mu,\sigma^2)$ | $\hat\mu=\bar x$, $\hat\sigma^2=\frac1n\sum(x_i-\bar x)^2$ (biased!) |
| $U[0,\theta]$ | $\hat\theta=\max x_i$ (biased: $E=\frac n{n+1}\theta$) |

**Worked example (MLE, exponential).**
1. $\log L=n\log\lambda-\lambda\sum x_i$.
2. Derivative: $\frac n\lambda-\sum x_i=0$.
3. $\hat\lambda=\frac n{\sum x_i}=\frac1{\bar x}$.

**Worked example ($U[0,\theta]$).** Method of moments: $E[X]=\frac\theta2$ ⇒ $\hat\theta=2\bar X$ (unbiased). MLE $\max X_i$ is always $\le\theta$, so it underestimates; $\frac{n+1}n\max X_i$ is unbiased.

> **Trap:** unbiased does not mean "good": an unbiased estimator can have a huge variance; a slightly biased one can have smaller MSE.

---

## 5. Confidence intervals 🟢

A $(1-\alpha)$ **confidence interval** is a random interval that contains the true parameter with probability $1-\alpha$ **before** the data are seen.

| Case | CI at level $1-\alpha$ |
|---|---|
| mean, $\sigma$ known (or $n$ large) | $\bar x\pm z_{1-\alpha/2}\frac\sigma{\sqrt n}$ |
| mean, $\sigma$ unknown, normal data | $\bar x\pm t_{n-1,1-\alpha/2}\frac s{\sqrt n}$ |
| proportion (large $n$) | $\hat p\pm z\sqrt{\frac{\hat p(1-\hat p)}n}$ |
| variance, normal data | $\left[\frac{(n-1)s^2}{\chi^2_{n-1,1-\alpha/2}},\ \frac{(n-1)s^2}{\chi^2_{n-1,\alpha/2}}\right]$ |

**$z$-example.** $\bar x=50$, $\sigma=10$, $n=100$, 95%: $SE=1$, CI $=[48.04,\ 51.96]$.
**$t$-example.** $n=16$, $\bar x=20$, $s=4$, 95%: $SE=1$, $t_{15}=2.131$, CI $=[17.869,\ 22.131]$.
$t$-values (95%, two-sided): df 5: 2.571; 9: 2.262; 15: 2.131; 29: 2.045; $\infty$: 1.96.

| Change | Width |
|---|---|
| higher confidence | wider |
| larger $\sigma$ | wider |
| larger $n$ | narrower, $\propto\frac1{\sqrt n}$ |
| $t$ instead of $z$ | wider |

**Sample size:** $n=\left(\frac{z\sigma}E\right)^2$ rounded **up** ($\sigma=10$, $E=2$, 95% ⇒ $97$).

**Interpretation.** "In repeated sampling, 95% of such intervals contain $\mu$." Not: "$\mu$ is in this interval with probability 95%" ($\mu$ is fixed), not "95% of the data lie in it".

> **Trap:** half the width needs **4×** the sample size.

---

## 6. Hypothesis tests and p-values 🟢

**Steps**
1. $H_0$ (with "="), $H_1$ (two-sided $\mu\ne\mu_0$ or one-sided $\mu>\mu_0$ / $\mu<\mu_0$).
2. Choose $\alpha$ (e.g. $0.05$) **before** looking at the data.
3. Compute the test statistic.
4. Compare with the critical value, or the p-value with $\alpha$.
5. Reject $H_0$, or "do not reject $H_0$".

**p-value** = probability, **under $H_0$**, of a test statistic at least as extreme as the observed one. Reject $H_0$ ⇔ $p\le\alpha$.
Two-sided $z$: $p=2(1-\Phi(\lvert z\rvert))$; one-sided: $p=1-\Phi(z)$.

**Errors (official example 2)**
| | $H_0$ true | $H_0$ false |
|---|---|---|
| reject $H_0$ | **type I error**, probability $\alpha$ | correct, probability = **power** $1-\beta$ |
| do not reject | correct, probability $1-\alpha$ | **type II error**, probability $\beta$ |

$\alpha$ = significance level = $P(\text{reject }H_0\mid H_0\text{ true})$.
Power grows with larger $n$, larger effect, smaller $\sigma$, larger $\alpha$. Smaller $\alpha$ (same $n$) ⇒ larger $\beta$.

**CI–test duality:** a two-sided level-$\alpha$ test rejects $H_0:\mu=\mu_0$ ⇔ $\mu_0$ is outside the $(1-\alpha)$ CI.

**Worked example.** $H_0:\mu=50$, $\sigma=8$, $n=64$, $\bar x=52$: $SE=1$, $z=2$. Reject at 5% ($2>1.96$), not at 1% ($2<2.576$); $p\approx0.046$.

**Multiple testing:** with $m$ tests at level $\alpha$, false positives pile up; **Bonferroni** uses $\frac\alpha m$ per test.

> **Trap:** the p-value is **not** $P(H_0\text{ true})$; not rejecting $H_0$ does not prove $H_0$; $\alpha+\beta\ne1$ in general.

---

## 7. Parametric tests 🟢

**Parametric** = assumes a distribution family (usually normal) and tests its parameters.

| Test | Statistic | Use when |
|---|---|---|
| one-sample $z$-test | $\frac{\bar x-\mu_0}{\sigma/\sqrt n}$ | $\sigma$ known (or large $n$) |
| one-sample $t$-test | $\frac{\bar x-\mu_0}{s/\sqrt n}$, df $n-1$ | normal data, $\sigma$ unknown |
| paired $t$-test | $t$-test on differences $d_i$ | before/after on the same units |
| two-sample $t$-test | $\frac{\bar x_1-\bar x_2}{s_p\sqrt{1/n_1+1/n_2}}$, df $n_1+n_2-2$ | two independent normal samples, equal variances (Welch if unequal) |
| $F$-test | $\frac{s_1^2}{s_2^2}$ | compare two variances (normal data) |
| one-way ANOVA | $F$ = between / within variance | $\ge3$ group means |
| $\chi^2$ variance test | $\frac{(n-1)s^2}{\sigma_0^2}$, df $n-1$ | one variance |

**$\chi^2$ tests for counts** (large-sample, often listed with non-parametric tests): $\sum\frac{(O-E)^2}{E}$; goodness of fit df $=k-1$ (minus estimated parameters), independence in $r\times c$ table df $=(r-1)(c-1)$.

**Distributions:** $t_\nu$ symmetric with heavier tails than $N(0,1)$, $\to N(0,1)$ as $\nu\to\infty$; $\chi^2_k$ = sum of $k$ squared standard normals, mean $k$, variance $2k$; $F$ = ratio of scaled $\chi^2$.

> **Trap:** the $t$-test assumes (approximately) normal data; for small, skewed samples or outliers use a non-parametric test.

---

## 8. Non-parametric tests 🟢

**Non-parametric (distribution-free)** = no assumption of a specific distribution family. Most use **signs** or **ranks** instead of the raw values.

| Pros | Cons |
|---|---|
| valid for any continuous distribution, small samples, ordinal data | less **power** than the parametric test when its assumptions (normality) really hold |
| robust to outliers | tests medians / location shifts rather than means |

### Which test when
| Situation | Parametric | Non-parametric |
|---|---|---|
| one sample (or paired differences), location | one-sample / paired $t$ | **sign test**, **Wilcoxon signed-rank test** |
| two independent samples | two-sample $t$ | **Mann–Whitney U** (= Wilcoxon rank-sum) |
| $\ge3$ independent groups | one-way ANOVA | **Kruskal–Wallis** |
| association of two variables | Pearson correlation | **Spearman** rank correlation (monotone relations) |
| fit to a given distribution | — | **Kolmogorov–Smirnov**, $\chi^2$ goodness of fit |
| independence of categories | — | $\chi^2$ test of independence, Fisher's exact test |

### How they work
- **Sign test:** count positive differences $S$. Under $H_0$ (median difference $0$): $S\sim\text{Bin}(n,\frac12)$.
- **Wilcoxon signed-rank:** rank $\lvert d_i\rvert$, sum the ranks of the positive differences. Uses magnitude too ⇒ more power than the sign test; assumes symmetry.
- **Mann–Whitney U:** rank all observations together; compare rank sums of the two groups. $U\in[0,n_1n_2]$, mean $\frac{n_1n_2}2$ under $H_0$.
- **Spearman $\rho$:** Pearson correlation of the ranks; $\rho=1$ for every strictly increasing relation (also nonlinear).
- **Kolmogorov–Smirnov:** largest distance $\sup_x\lvert F_n(x)-F_0(x)\rvert$ between empirical and hypothesized CDF.

**Worked example (sign test).** 10 patients, blood pressure lower after treatment in 9 cases. $H_0$: no effect.
1. Under $H_0$: $S\sim\text{Bin}(10,\frac12)$.
2. One-sided $p=P(S\ge9)=\frac{\binom{10}9+\binom{10}{10}}{2^{10}}=\frac{11}{1024}\approx0.011$.
3. Reject $H_0$ at $\alpha=0.05$ (two-sided $p\approx0.021$, still $<0.05$).

> **Trap:** "non-parametric" does not mean "no assumptions" — e.g. independence of observations is still required, and Wilcoxon signed-rank assumes symmetric differences.

---

## Formula sheet

| Topic | Formula |
|---|---|
| sample variance | $s^2=\frac1{n-1}\sum(x_i-\bar x)^2$ |
| IQR / outliers | $Q_3-Q_1$; outside $[Q_1-1.5IQR,\ Q_3+1.5IQR]$ |
| variance | $E[X^2]-(EX)^2$ |
| skewness / kurtosis | $\frac{E(X-\mu)^3}{\sigma^3}$ / $\frac{E(X-\mu)^4}{\sigma^4}$ (normal: $0$ / $3$) |
| standardize | $z=\frac{x-\mu}\sigma$, $\Phi(-z)=1-\Phi(z)$ |
| unbiased | $E[\hat\theta]=\theta$; $MSE=\operatorname{Var}+\text{bias}^2$ |
| SE | $\frac\sigma{\sqrt n}$ |
| CI mean | $\bar x\pm z\frac\sigma{\sqrt n}$ or $\bar x\pm t_{n-1}\frac s{\sqrt n}$ |
| sample size | $n=(z\sigma/E)^2$, round up |
| $z$ / $t$ test | $\frac{\bar x-\mu_0}{\sigma/\sqrt n}$ / $\frac{\bar x-\mu_0}{s/\sqrt n}$ |
| decision | reject $H_0$ ⇔ $p\le\alpha$ |
| errors | type I $\alpha$; type II $\beta$; power $1-\beta$ |
| $\chi^2$ df | $k-1$ (fit), $(r-1)(c-1)$ (independence) |
| sign test | $S\sim\text{Bin}(n,\frac12)$ under $H_0$ |
| non-parametric pairs | paired $t$ ↔ Wilcoxon signed-rank; two-sample $t$ ↔ Mann–Whitney; ANOVA ↔ Kruskal–Wallis; Pearson ↔ Spearman |

---

## Practice MCQs

**Q1.** (official example 1) A normal distribution is fully determined by
A) mean only  B) variance only  C) mean and variance  D) median and mode  E) skewness

<details><summary>Answer</summary>

**C** — $N(\mu,\sigma^2)$ has exactly two parameters.

</details>

**Q2.** (official example 2) In hypothesis testing, the significance level $\alpha$ is
A) the probability of rejecting a false null hypothesis  B) the probability of retaining a true null hypothesis  C) the probability of a type I error  D) the probability that the null hypothesis is true  E) the probability of a type II error

<details><summary>Answer</summary>

**C** — Rejecting $H_0$ although it is true. A is the power, B is $1-\alpha$, E is $\beta$.

</details>

**Q3.** The median of $3,1,7,5,9$ is
A) $3$  B) $5$  C) $7$  D) $5.5$  E) $1$

<details><summary>Answer</summary>

**B** — Sorted: $1,3,5,7,9$.

</details>

**Q4.** Data $2,4,4,4,5,5,7,9$: mean, median, mode are
A) $5,4.5,4$  B) $5,5,4$  C) $4.5,5,4$  D) $5,4.5,5$  E) $4,4.5,5$

<details><summary>Answer</summary>

**A** — Mean $\frac{40}8$; median $\frac{4+5}2$; mode $4$ (three times).

</details>

**Q5.** $10$ is added to every value. Then
A) mean and SD increase by 10  B) mean unchanged, SD +10  C) mean +10, SD unchanged  D) nothing changes  E) both multiply by 10

<details><summary>Answer</summary>

**C** — A shift moves the centre, not the spread.

</details>

**Q6.** Data $3,7,8,5,12$: $s^2=$
A) $9.2$  B) $46$  C) $11.5$  D) $7$  E) $3.39$

<details><summary>Answer</summary>

**C** — $\bar x=7$, squared deviations sum to $46$, divide by $4$. ($9.2$ divides by $n$.)

</details>

**Q7.** $Q_1=20$, $Q_3=30$. Which value is an outlier ($1.5\,IQR$ rule)?
A) $6$  B) $44$  C) $35$  D) $47$  E) $15$

<details><summary>Answer</summary>

**D** — Fences $5$ and $45$.

</details>

**Q8.** Strongly right-skewed data usually have
A) mean < median  B) mean > median  C) mean = median  D) skewness < 0  E) kurtosis 0

<details><summary>Answer</summary>

**B** — The long right tail pulls the mean up.

</details>

**Q9.** The kurtosis $E[(X-\mu)^4]/\sigma^4$ of a normal distribution is
A) $0$  B) $1$  C) $2$  D) $3$  E) $4$

<details><summary>Answer</summary>

**D** — Excess kurtosis is $3-3=0$ (A is the excess).

</details>

**Q10.** $E[X]=2$, $E[X^2]=5$. $\operatorname{Var}X=$
A) $3$  B) $1$  C) $9$  D) $\sqrt5-2$  E) $4$

<details><summary>Answer</summary>

**B** — $5-2^2$.

</details>

**Q11.** IQ $\sim N(100,15^2)$. $P(\text{IQ}>130)\approx$
A) $0.0228$  B) $0.0456$  C) $0.1587$  D) $0.9772$  E) $0.05$

<details><summary>Answer</summary>

**A** — $z=2$.

</details>

**Q12.** $X\sim N(50,16)$. $P(46<X<54)\approx$
A) $0.95$  B) $0.68$  C) $0.50$  D) $0.99$  E) $0.34$

<details><summary>Answer</summary>

**B** — $\sigma=4$: $\mu\pm1\sigma$.

</details>

**Q13.** $Z\sim N(0,1)$. Then $2Z+1\sim$
A) $N(1,2)$  B) $N(1,4)$  C) $N(2,1)$  D) $N(0,4)$  E) $N(1,\sqrt2)$

<details><summary>Answer</summary>

**B** — Mean $2\cdot0+1$, variance $2^2\cdot1$.

</details>

**Q14.** An estimator $\hat\theta$ of $\theta$ is unbiased if
A) $\hat\theta=\theta$ always  B) $E[\hat\theta]=\theta$  C) $\operatorname{Var}\hat\theta=0$  D) $\hat\theta\to\theta$ almost surely  E) $\hat\theta$ is the MLE

<details><summary>Answer</summary>

**B** — D describes (strong) consistency, a different property.

</details>

**Q15.** The sample variance uses $n-1$ because
A) then $E[S^2]=\sigma^2$  B) then $S$ is robust  C) then $S^2$ is smaller  D) then $S$ is unbiased for $\sigma$  E) then $S^2$ is the MLE

<details><summary>Answer</summary>

**A** — D is false ($S$ is biased for $\sigma$); the normal MLE divides by $n$ (E false).

</details>

**Q16.** The mean squared error of an estimator equals
A) variance + bias  B) variance + bias²  C) variance × bias  D) bias²  E) variance − bias²

<details><summary>Answer</summary>

**B** — $E[(\hat\theta-\theta)^2]=\operatorname{Var}\hat\theta+(E\hat\theta-\theta)^2$.

</details>

**Q17.** The MLE of $\lambda$ for an Exponential$(\lambda)$ sample is
A) $\bar x$  B) $\frac1{\bar x}$  C) $\max x_i$  D) $s^2$  E) $\frac n{\bar x}$

<details><summary>Answer</summary>

**B** — $\frac n\lambda-\sum x_i=0$. (Mean of exponential is $\frac1\lambda$.)

</details>

**Q18.** For $X_i\sim U[0,\theta]$, the estimator $\max X_i$ is
A) unbiased  B) biased, it tends to underestimate $\theta$  C) biased, it overestimates $\theta$  D) not consistent  E) always equal to $\theta$

<details><summary>Answer</summary>

**B** — It is always $\le\theta$, $E=\frac n{n+1}\theta$. It is still consistent.

</details>

**Q19.** To halve the width of a CI (same level and $\sigma$), the sample size must be
A) doubled  B) multiplied by 4  C) halved  D) multiplied by $\sqrt2$  E) multiplied by 8

<details><summary>Answer</summary>

**B** — Width $\propto\frac1{\sqrt n}$.

</details>

**Q20.** $\bar x=50$, $\sigma=10$ known, $n=100$. The 95% CI is
A) $[48.355,51.645]$  B) $[47.424,52.576]$  C) $[30.4,69.6]$  D) $[48.04,51.96]$  E) $[49,51]$

<details><summary>Answer</summary>

**D** — $50\pm1.96\cdot1$. A: 90%; B: 99%; C forgets $\sqrt n$.

</details>

**Q21.** $n=16$ normal observations, $\bar x=20$, $s=4$, $\sigma$ unknown. The 95% CI is
A) $20\pm1.96\cdot1$  B) $20\pm2.131\cdot4$  C) $20\pm2.131\cdot1$  D) $20\pm1.96\cdot4$  E) $20\pm2.120\cdot1$

<details><summary>Answer</summary>

**C** — $t$ with $15$ df, $SE=1$. ($2.120$ is the value for 16 df.)

</details>

**Q22.** A 95% confidence interval means
A) $\mu$ lies in this interval with probability 95%  B) 95% of the data lie in the interval  C) in repeated sampling, 95% of such intervals contain $\mu$  D) the sample mean is correct with probability 95%  E) $\alpha=0.95$

<details><summary>Answer</summary>

**C** — $\mu$ is fixed; the interval is random.

</details>

**Q23.** $H_0:\mu=50$ vs $\mu\ne50$, $\sigma=8$, $n=64$, $\bar x=52$. Which is correct?
A) $z=0.25$, do not reject at 5%  B) $z=2$; reject at 5% but not at 1%  C) $z=2$; reject at 1%  D) $z=16$  E) $z=2$; do not reject at 5%

<details><summary>Answer</summary>

**B** — $1.96<2<2.576$.

</details>

**Q24.** The p-value is
A) the probability that $H_0$ is true  B) the probability of a type II error  C) the probability that $H_1$ is true  D) the probability, under $H_0$, of a result at least as extreme as observed  E) the significance level

<details><summary>Answer</summary>

**D** — The definition. A and C are the classic wrong answers.

</details>

**Q25.** $p=0.03$. Then
A) reject at $\alpha=0.01$  B) $H_0$ is true with probability 3%  C) reject at $\alpha=0.05$  D) the effect is large  E) $\beta=0.97$

<details><summary>Answer</summary>

**C** — $0.03\le0.05$ but $>0.01$.

</details>

**Q26.** Which change increases the power of a test?
A) larger sample size  B) smaller $\alpha$  C) smaller sample size  D) larger population SD  E) a two-sided instead of a one-sided test (true effect in the tested direction)

<details><summary>Answer</summary>

**A** — The others reduce power.

</details>

**Q27.** A 95% CI for $\mu$ is $[12.1,15.3]$. A two-sided 5% test rejects
A) $\mu_0=14$  B) $\mu_0=13$  C) $\mu_0=12.5$  D) $\mu_0=16$  E) $\mu_0=15$

<details><summary>Answer</summary>

**D** — Exactly the values outside the CI.

</details>

**Q28.** Two independent samples, small, clearly non-normal with outliers. Which test compares their locations?
A) two-sample $t$-test  B) Mann–Whitney U test  C) paired $t$-test  D) $F$-test  E) one-sample $z$-test

<details><summary>Answer</summary>

**B** — The rank-based alternative to the two-sample $t$-test.

</details>

**Q29.** The non-parametric alternative to the paired $t$-test is
A) Kruskal–Wallis  B) Mann–Whitney U  C) Wilcoxon signed-rank test  D) $\chi^2$ test of independence  E) ANOVA

<details><summary>Answer</summary>

**C** — (or the sign test). Kruskal–Wallis replaces one-way ANOVA.

</details>

**Q30.** Compared with parametric tests, non-parametric tests
A) always have higher power  B) need normally distributed data  C) need fewer distributional assumptions but usually have less power when the data really are normal  D) cannot be used for small samples  E) test only variances

<details><summary>Answer</summary>

**C** — They use signs/ranks, so they are robust, but they waste some information when normality holds.

</details>

**Q31.** Sign test: in 10 pairs, 9 differences are positive. The one-sided p-value is
A) $\frac9{10}$  B) $\frac{11}{1024}$  C) $\frac1{1024}$  D) $\frac{10}{1024}$  E) $0.5$

<details><summary>Answer</summary>

**B** — $P(S\ge9)$ with $S\sim\text{Bin}(10,\frac12)$: $\frac{10+1}{1024}$.

</details>

**Q32.** A $\chi^2$ test of independence uses a $3\times4$ table. Degrees of freedom:
A) $6$  B) $12$  C) $11$  D) $7$  E) $5$

<details><summary>Answer</summary>

**A** — $(3-1)(4-1)$.

</details>

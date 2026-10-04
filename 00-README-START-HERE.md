# Entrance Test Study Guide — M.Sc. Applied Mathematics in Network and Data Sciences (Hochschule Mittweida)

## The exam: what matters
- **Format: multiple choice.** You need to *recognize* the right answer fast. You do not need to write long proofs.
- **Only 2 attempts.** The first is in **November**, the second in **December/January**. Failing both means you are removed from the program.
- The test checks the Bachelor-level knowledge you **self-declared** when you applied (see the syllabus PDF).
- The official practice problems (file 12) show the level: mostly **core Bachelor material**, with short calculations and standard facts.

## Files in this folder

| File | Subject | Official syllabus items |
|---|---|---|
| [01-analysis.md](01-analysis.md) | Analysis | sequences/series in ℝⁿ, Riemann integration & differentiation in several variables, Taylor/Fourier series, Fourier/Laplace transforms, open/closed/compact sets, Hilbert/Banach spaces |
| [02-algebra.md](02-algebra.md) | Algebra | groups, rings, fields, homo-/isomorphisms, eigenvalues/eigenvectors, linear operators, Galois theory |
| [03-discrete-mathematics.md](03-discrete-mathematics.md) | Discrete Mathematics | logic, sets & relations, induction, pigeonhole, counting, generating functions |
| [04-number-theory.md](04-number-theory.md) | Number Theory | well-ordering, primality/coprimality, modular arithmetic, continued fractions, RSA |
| [05-differential-equations.md](05-differential-equations.md) | Differential Equations | ODEs, PDEs (Laplace, Poisson, heat, wave), systems of ODEs, dynamical systems, self-organization |
| [06-numerical-methods.md](06-numerical-methods.md) | Numerical Methods | linear systems, eigenvalue methods, pseudo-inverses, Taylor series |
| [07-measure-and-probability.md](07-measure-and-probability.md) | Measure & Probability | null sets, expectations, distributions/densities, independence & conditional probability, LLN & CLT |
| [08-statistics.md](08-statistics.md) | Statistics | moments, distributions, confidence intervals, descriptive statistics, hypothesis testing |
| [09-graph-theory.md](09-graph-theory.md) | Graph Theory | graphs/digraphs/hypergraphs, matrix representations, algorithms & complexity, matroids, Ramsey theory |
| [10-mathematical-modelling.md](10-mathematical-modelling.md) | Mathematical Modelling | dynamical systems, Fokker–Planck, synergetics, phase transitions, stability |
| [11-optimization.md](11-optimization.md) | Optimization | unconstrained/constrained, LP, convex optimization, gradient methods |
| [12-official-problems-solved.md](12-official-problems-solved.md) | **Official practice problems** | all 25 solved, with MCQ tricks |
| [13-mock-exam.md](13-mock-exam.md) | **Mock exam** | 40 mixed MCQs with answer key and a scoring guide |

All files are written at **Bachelor year 1–2 level**, the same level as the official practice problems. Every subject file has the same structure:
**Contents → topics from easy to harder (each one: meaning in plain words → formula → worked example step by step → trap) → Formula sheet → 20–25 practice MCQs** (answers hidden under "Answer"; click to reveal).

Each section has a level tag:
- 🟢 **core**: learn it well, because questions with calculations come from here
- 🟡 **know the basic facts only**: an advanced syllabus topic. Read the short "Must-know facts" box and move on.

> **Viewing the math:** the formulas are written in LaTeX (`$...$`). Open the files in **Obsidian**, **VS Code** (Markdown preview, or the "Markdown+Math" extension), **Typora**, or on **GitHub**. All of these render the formulas.

## Priority: where the points are likely to be
The official practice problems are heavily weighted toward core topics, so study those first.

| Priority | Topics | Why |
|---|---|---|
| 🔴 **High** | Linear algebra (determinants, rank, eigenvalues), Analysis (limits, series, integrals), Discrete math (counting, induction, sets/functions), Number theory (mod arithmetic, primes), Probability (expectation, conditional, uniform/geometric probability), ODEs (1st order, linear constant-coefficient) | About 80% of the official problems come from here |
| 🟠 **Medium** | Graph theory basics (trees, degrees, algorithms), Statistics (CIs, tests), Groups/rings/fields, Optimization (extrema, Lagrange, LP, convexity), Numerical methods (LU, Newton, least squares) | Named in the syllabus and easy to ask as MCQ |
| 🟡 **Lower: learn the key facts only** | Galois theory, Hilbert/Banach spaces, matroids, Ramsey numbers, PDE classification, Fokker–Planck, synergetics, phase transitions, measure theory details | Specialized topics. Questions here are usually "which statement is true", so the 🟡 "Must-know facts" boxes are enough |

## Study plan (today is 4 Oct; first test in November ≈ 5 weeks)

| Week | Dates | Study | Practice |
|---|---|---|---|
| 0 | Oct 4–5 | Try **all 25 official problems** without help (file 12, don't peek). Mark what you couldn't do. | — |
| 1 | Oct 6–12 | 02 Algebra (linear algebra part first) · 01 Analysis | MCQs of both files |
| 2 | Oct 13–19 | 03 Discrete Math · 04 Number Theory · 09 Graph Theory | MCQs + redo the failed official problems |
| 3 | Oct 20–26 | 07 Probability · 08 Statistics · 05 Differential Equations | MCQs |
| 4 | Oct 27–Nov 2 | 06 Numerical · 11 Optimization · 10 Modelling · Galois/Hilbert parts of 01/02 | MCQs |
| 5 | Nov 3 → exam | **Mock exam (file 13) under time pressure**, then repair weak areas using the mistake map in file 13. Last 2 days: only the *Formula sheets* | Re-do every MCQ you got wrong |

**Daily routine (about 2–3 h):** read 1 section (40 min) → close the file and write the key formulas from memory (10 min) → do the MCQs (40 min) → write every mistake into a personal "error log" (10 min).

## MCQ exam strategy
1. **Read all the options first.** They often tell you what form the answer has (e.g. $\alpha^n\delta$ vs $\alpha\delta$).
2. **Plug in small cases.** Try $n=1,2,3$, $x=0$, or a $2\times2$ matrix. This removes wrong options in seconds (see file 12, exercises 4 and 22).
3. **Check, don't solve.** For ODEs, integrals and equations, substitute each option back in.
4. **Look for the trap answer.** The usual traps: missing absolute value, $n-1$ vs $n$, $\subseteq$ vs $=$, "independent ⇒ uncorrelated" (true) vs the converse (false), forgetting the initial condition.
5. **Eliminate with extreme cases and dimensions.** A probability must lie in $[0,1]$, a variance is $\ge 0$, a volume is positive.
6. **Manage your time.** Do a first pass on all the easy questions, mark the hard ones, then come back.
7. **Never leave a question blank** unless wrong answers cost points. Ask the examiners at the start whether they do.

## Source material
- `Copy of Mathemathics-Master-Mittweida-Knowledge-Requirements_copy.pdf`: the official syllabus
- `problems-applicants-master-ma_compress.pdf`: the 25 official practice problems (solved in file 12)
- `Screenshot ….png`: the exam rules (MCQ, 2 attempts)

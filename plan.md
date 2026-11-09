# Plan: align study notes with the official Placement Test guide

Source checked: `~/Downloads/Questionaire_Mathematics_Master.pdf`
("Master's Program Placement Test – Information and Preparation Guide", 10 pages).

## 1. What the new guide changes about the exam format

| | Current notes (README, 13-mock-exam) | Official guide |
|---|---|---|
| Topics | 11 subjects incl. Number Theory | **10 topics, you choose 6** at the start. **Number Theory is NOT on the list.** |
| Questions | mock: 40 | **7 per topic → 42 total** |
| Options | A–D (4) | **a–e (5), exactly one correct** |
| Time | 90 min suggested | **60 min** (≈ 85 s per question) |
| Style | calculation + facts | "not tricky", definitions/recognition + short calculations (see 20 example Qs) |

→ README, 00-README-START-HERE and the mock exam must be updated.
→ A strategy section is needed: **which 6 topics to pick**.

## 2. Coverage check, topic by topic

Legend: ✅ covered · ⚠️ thin (one line / only mentioned) · ❌ missing

### Algebra (02)
- ✅ groups, homomorphisms, kernels, fields, determinants, eigenvalues/eigenvectors, linear maps, Galois basics, field extension degree
- ❌ **rings: ideals** (ideal, principal ideal, quotient ring, maximal ideal ⇔ quotient is a field)
- ⚠️ **characteristic polynomial** (used, not named as a topic) · ❌ **minimal polynomial** (+ Cayley–Hamilton, diagonalizable ⇔ min. poly has distinct linear factors)
- ⚠️ vector spaces (axioms, basis, dimension, subspace) – only implicit
- Official example Q1 (which is a field: ℤ/6, ℚ, ℝ[x], ℤ, ℤ/4) and Q2 (invertible ⇔ det≠0) → add as practice MCQs

### Analysis (01)
- ✅ sequences/series, open/closed/compact, Taylor, Jacobian, Fourier series, Laplace transform, Banach/Hilbert
- ❌ **convergence in metric spaces** (metric definition, xₙ→x ⇔ d(xₙ,x)→0, Cauchy, completeness, Bolzano–Weierstrass, Heine–Borel)
- ⚠️ **Lᵖ spaces** – one line; add definition of ‖f‖ₚ, Hölder/Minkowski, which are Hilbert (p=2), Lᵖ inclusions on finite measure
- ⚠️ continuity/differentiability in several variables (total vs partial derivative, differentiable ⇒ continuous)

### Differential Equations (05)
- ✅ separable, linear, Bernoulli, systems y'=Ay, e^{At}, existence/uniqueness (Picard–Lindelöf), PDE classification, heat/wave/Laplace/Poisson
- ❌ **dimension of solution spaces** (n-th order linear homogeneous ODE → n-dim space; Wronskian; general solution = particular + homogeneous)
- ⚠️ **separation of variables + Fourier series** for PDE – only a one-line fact; add one short worked heat-equation example

### Discrete Mathematics (03)
- ✅ logic, implication truth table, maps, permutations/combinations, inclusion–exclusion, pigeonhole, relations, induction, generating functions, stars & bars
- Nothing missing. Add official Q1/Q2 as MCQs.

### Graph Theory (09)
- ✅ simple/directed/hypergraphs, trees, adjacency/incidence matrices, complete & bipartite, Euler tours, Dijkstra, matroids + greedy, Ramsey
- Nothing missing. Maybe expand greedy-on-matroid to a short worked example.

### Mathematical Modelling (10)
- ✅ dynamical systems, equilibria & stability, exponential/logistic, predator–prey, SIR, units/dimensions, bifurcations, phase transitions
- ⚠️ **linearization** – used in tables, add an explicit section: f'(x*) in 1D, Jacobian at equilibrium in 2D, Hartman–Grobman in one line
- ⚠️ definition of (Lyapunov) stability vs asymptotic stability (official Q1)

### Measure & Probability (07)
- ✅ null sets, Lebesgue measure, Riemann vs Lebesgue (Dirichlet function), independence, densities/CDF, expectation, LLN (weak/strong), CLT
- ⚠️ **σ-algebras and measures** – mentioned once; add definition (contains Ω, closed under complement & countable union), measure axioms, Borel σ-algebra, probability space (Ω,𝓕,P)
- ⚠️ independence of **random variables** (joint density factorizes, E[XY]=E[X]E[Y], Var adds)

### Numerical Methods (06)
- ✅ Gaussian elimination, condition numbers, LU/Cholesky/QR/SVD, pseudo-inverse, least squares, eigenvalue methods, root finding (Newton), floating point, quadrature
- ❌ **interpolation** (Lagrange/Newton form, uniqueness of degree-≤n polynomial, error term, Runge phenomenon)
- ❌ **explicit and implicit methods** (explicit/implicit Euler, trapezoidal/Crank–Nicolson, order, stability regions, stiffness)

### Optimization (11)
- ✅ unconstrained/constrained, convex sets/functions, gradient methods, Lagrange, KKT, LP + simplex, duality, unbounded/infeasible
- Nothing missing.

### Statistics (08)
- ✅ moments, normal & standardization, descriptive stats, estimators/unbiasedness, CIs, hypothesis tests, p-values, Type I/II errors
- ❌ **parametric vs non-parametric tests** (when to use; sign test, Wilcoxon signed-rank, Mann–Whitney U, Kruskal–Wallis, χ² goodness-of-fit/independence; t-test assumptions)

### Number Theory (04)
- Not part of the official 10 topics → mark as **optional / low priority** in README (still useful for Algebra: ℤ/nℤ, units, fields).

## 3. Work items (in order)

1. **Add new file `14-official-guide-examples.md`**: all 20 example questions from the PDF with 5 options, hidden answers and the short official explanations.
2. **Fill the gaps** (each as a new section in the existing file style: meaning → formula → worked example → trap, + 2–3 new practice MCQs with 5 options):
   - [x] 02-algebra: ideals & quotient rings; characteristic & minimal polynomial (Cayley–Hamilton); vector-space basics — DONE (also: homomorphisms upgraded to core, Galois expanded, homeomorphism/constructions removed, 30 MCQs with 5 options)
   - [x] 01-analysis: metric spaces & convergence; Lᵖ spaces — DONE (also: continuity + Jacobian sections, multivariable Taylor; removed inequalities, 1D integration, multiple integrals, Fourier transform, extremum test; 28 MCQs with 5 options)
   - [x] 05-differential-equations: dimension of solution space / Wronskian; heat equation by separation of variables — DONE (also: existence/uniqueness and matrix exponential now core; removed exact equations, self-organization, 1D stability; 30 MCQs with 5 options)
   - [x] 06-numerical-methods: polynomial interpolation; explicit vs implicit methods for ODEs — DONE (also: QR + factorization overview, SVD/pseudo-inverse core, inverse iteration/QR algorithm core; removed Jacobi/Gauss–Seidel, solution-space theory; 31 MCQs with 5 options)
   - [x] 07-measure-and-probability: σ-algebras, measures, probability spaces; independence of random variables — DONE (also: Riemann vs Lebesgue + convergence theorems, CDF/density characterization, weak/strong LLN core; removed counting section, geometric probability section; 30 MCQs with 5 options)
   - [x] 08-statistics: parametric vs non-parametric tests — DONE (also: estimators section expanded with MSE/consistency/MLE, higher moments core, parametric test overview; removed distribution summary, regression formula; 32 MCQs with 5 options)
   - [x] 10-mathematical-modelling: linearization section; stability definitions — DONE (also: dynamical systems basics, units of parameters, bifurcations + phase transitions core, SIS, harvesting; removed Fokker–Planck, synergetics; 33 MCQs with 5 options)
3. **Update README.md and 00-README-START-HERE.md**: new exam format (6 of 10, 7 Qs each, 42 Qs, 5 options, 60 min), Number Theory → optional, add file 14, add "which 6 topics to choose" recommendation.
4. **Rework 13-mock-exam.md** (or add a second mock) to the real format: 10 topics × 7 questions, 5 options, so you can pick any 6 and time yourself at 60 min.
5. Final pass: re-grep each guide keyword in the notes to confirm every item is ✅.

## 4. Open question for you

- Which 6 topics do you plan to choose? If you already know, gap-filling and the mock can focus on those 6 first.

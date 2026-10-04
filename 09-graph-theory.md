# 9. Graph Theory

> **Syllabus:** Graphs, digraphs and hypergraphs · Matrix representations · Graph algorithms and complexity · Matroids · Ramsey theory
>
> **How to study this file:** Sections 1–9 are 🟢 core (degrees, trees, Euler, planar graphs, adjacency matrix, simple algorithms). They match official Exercise 23 ("$m\ge n$ edges ⇒ cycle"). Sections 10–13 are 🟡: learn only the fact boxes. Time: about 3–4 hours, plus 1 hour for the MCQs.

## Contents
1. [Basic words](#1-basic-words-) 🟢
2. [Degrees and the handshake lemma](#2-degrees-and-the-handshake-lemma-) 🟢
3. [Special graphs](#3-special-graphs-) 🟢
4. [Trees](#4-trees-) 🟢
5. [Bipartite graphs](#5-bipartite-graphs-) 🟢
6. [Euler and Hamilton](#6-euler-and-hamilton-) 🟢
7. [Planar graphs](#7-planar-graphs-) 🟢
8. [Digraphs](#8-digraphs-directed-graphs-) 🟢
9. [Matrix representations](#9-matrix-representations-) 🟢
10. [Colouring](#10-colouring-) 🟡
11. [Graph algorithms and complexity](#11-graph-algorithms-and-complexity-) 🟡
12. [Hypergraphs and matroids](#12-hypergraphs-and-matroids-) 🟡
13. [Ramsey theory](#13-ramsey-theory-) 🟡
14. [Formula sheet](#formula-sheet)
15. [Practice MCQs](#practice-mcqs)

---

## 1. Basic words 🟢

A **graph** $G=(V,E)$ has **vertices** $V$ (points) and **edges** $E$ (lines between two points).
We write $n=|V|$ (number of vertices) and $m=|E|$ (number of edges).

| Word | Meaning |
|---|---|
| simple graph | no loops (edge from $v$ to $v$) and no double edges |
| adjacent | $u$ and $v$ are joined by an edge |
| degree $\deg v$ | number of edges at $v$ (a loop counts 2) |
| walk | a sequence of vertices, each joined to the next (repeats allowed) |
| path | a walk with no repeated vertex |
| cycle | a closed path with at least 3 vertices |
| connected | there is a path between any two vertices |
| component | a maximal connected piece |
| complement $\bar G$ | same vertices; $uv$ is an edge in $\bar G$ iff it is **not** an edge in $G$ |

In this file "graph" means **simple graph** unless we say otherwise.

> **Trap:** a walk may repeat vertices; a path may not. Matrix powers count **walks** (Section 9).

---

## 2. Degrees and the handshake lemma 🟢

**Plain words.** Every edge has two ends. So when you add all degrees, you count every edge twice.

**Formula (handshake lemma).**
$$\sum_{v\in V}\deg v=2m$$
**Consequence:** the number of vertices with **odd** degree is **even**.

**Worked example.** A graph has degrees $3,3,2,2,2$. How many edges?
1. Sum of degrees: $3+3+2+2+2=12$.
2. $m=12/2=6$.

**Regular graphs.** $k$-regular = every vertex has degree $k$. Then $m=\frac{nk}2$.
Example: a 3-regular graph on 8 vertices has $\frac{8\cdot3}2=12$ edges.

**Does a graph exist?** Degrees $3,3,3,3,3$ (5 vertices): sum $=15$ is odd ⇒ **impossible**.

> **Trap:** an even sum is necessary, but not enough. Degrees $3,3,1,1$ have sum 8, but no simple graph has them: each degree-3 vertex would need 3 neighbours, so both would be joined to both leaves, which then have degree 2.

---

## 3. Special graphs 🟢

| Graph | Description | $n$ | $m$ |
|---|---|---|---|
| $K_n$ | complete: every pair joined | $n$ | $\binom n2=\frac{n(n-1)}2$ |
| $K_{a,b}$ | complete bipartite: two groups, all edges between them | $a+b$ | $ab$ |
| $C_n$ | cycle | $n$ | $n$ |
| $P_n$ | path with $n$ vertices | $n$ | $n-1$ |
| tree | connected, no cycle | $n$ | $n-1$ |
| $Q_d$ | hypercube (0-1 strings of length $d$) | $2^d$ | $d\,2^{d-1}$ |

**Complement.** $m(G)+m(\bar G)=\binom n2$.

**Worked example.** $G$ has 7 vertices and 12 edges. How many edges has $\bar G$?
1. $K_7$ has $\binom72=21$ edges.
2. $\bar G$ has $21-12=9$ edges.

**Isomorphic** graphs are "the same graph with different names". They must have the same $n$, $m$ and degree list.

> **Trap:** the same degree list does **not** prove isomorphism. $C_6$ and two separate triangles are both 2-regular with 6 vertices.

---

## 4. Trees 🟢

**Plain words.** A tree is a connected graph with no cycle. A **forest** is a graph with no cycle (its pieces are trees). A **leaf** is a vertex of degree 1.

**Key facts.** For a graph with $n$ vertices, these all mean "tree":
1. connected and no cycle;
2. connected with $n-1$ edges;
3. no cycle and $n-1$ edges;
4. exactly one path between any two vertices.

**More facts.**
- A forest with $c$ components has $m=n-c$ edges.
- Every tree with $n\ge2$ vertices has at least 2 leaves.
- Adding any edge to a tree creates exactly one cycle.
- **Cayley:** there are $n^{n-2}$ labelled trees on $n$ vertices ($n=4$: 16 trees).

**Official Exercise 23.** A graph with $m\ge n$ edges has a cycle.
*Proof:* if it had no cycle, it would be a forest, so $m=n-c\le n-1<n$. Contradiction.

**Worked example (count leaves).** A tree has 2 vertices of degree 3, 1 vertex of degree 4, and all others are leaves. How many leaves $L$?
1. Number of vertices: $n=3+L$, so $m=n-1=2+L$.
2. Handshake: $3+3+4+L=2m=4+2L$.
3. $10+L=4+2L\Rightarrow L=6$.

> **Trap:** $n-1$ edges alone does **not** make a tree. You also need "connected" or "no cycle".

---

## 5. Bipartite graphs 🟢

**Plain words.** The vertices split into two groups $X,Y$, and every edge goes between the groups (none inside a group).

**Key fact.**
$$G\text{ is bipartite}\iff G\text{ has no cycle of odd length}\iff G\text{ can be coloured with 2 colours}$$

**Worked example.** Is $C_5$ bipartite? Colour around the cycle: red, blue, red, blue, red. The 5th vertex is next to the 1st, both red. Odd cycle ⇒ **not bipartite**. $C_6$ works fine ⇒ bipartite.

**Facts.** Every tree is bipartite. $K_{a,b}$ is bipartite. $K_3$ (a triangle) is not.

**Matchings (short).** A **matching** is a set of edges with no common vertex. In a bipartite graph: maximum matching size = minimum vertex cover size (**König**). **Hall:** $X$ can be fully matched iff every set $S\subseteq X$ has at least $|S|$ neighbours.

> **Trap:** $K_{a,b}$ has **no** edges inside a group, so $m=ab$, not $\binom{a+b}2$.

---

## 6. Euler and Hamilton 🟢

| | uses every … once | test |
|---|---|---|
| **Euler** circuit/trail | **edge** | easy degree test |
| **Hamilton** cycle/path | **vertex** | no simple test (hard) |

**Euler rule** (connected graph):
- **Euler circuit** (closed) ⇔ **every** degree is even.
- **Euler trail** (open) ⇔ exactly **0 or 2** vertices of odd degree. With 2, the trail starts at one and ends at the other.

**Worked example.** Degrees $2,2,3,3,4$ (connected).
1. Odd-degree vertices: two (the 3s).
2. So an Euler trail exists, from one degree-3 vertex to the other, but no Euler circuit.

**Standard results.**
- $K_n$ has an Euler circuit ⇔ $n$ is odd (degree $n-1$ must be even).
- $K_{a,b}$ has an Euler circuit ⇔ $a$ and $b$ are both even.

**Hamilton facts.**
- **Dirac:** if $n\ge3$ and every degree is $\ge n/2$, the graph has a Hamilton cycle.
- $K_n$ ($n\ge3$) has a Hamilton cycle. $K_{a,b}$ has one ⇔ $a=b\ge2$.
- The Petersen graph (10 vertices, 3-regular) has **no** Hamilton cycle.

> **Trap:** Euler = **E**dges, Hamilton = vertices. Don't mix them up.

---

## 7. Planar graphs 🟢

**Plain words.** A graph is **planar** if you can draw it with no crossing edges. The drawing cuts the plane into **faces** (regions), including the outside region.

**Euler's formula** (connected planar graph):
$$V-E+F=2$$

**Edge bounds** (simple planar graph, $V\ge3$):
$$E\le3V-6,\qquad E\le 2V-4\ \text{ if there is no triangle (e.g. bipartite)}$$

**Worked example 1.** A connected planar graph has 6 vertices and 9 edges. Faces?
$F=2-V+E=2-6+9=5$.

**Worked example 2.** Is $K_5$ planar? $V=5$, $E=10$. Bound: $3\cdot5-6=9<10$ ⇒ **not planar**.

**Worked example 3.** Is $K_{3,3}$ planar? $V=6$, $E=9$. It has no triangle, so $E\le2\cdot6-4=8<9$ ⇒ **not planar**.

**Facts.**
- $K_n$ is planar ⇔ $n\le4$. $K_{a,b}$ is planar ⇔ $\min(a,b)\le2$.
- **Kuratowski:** planar ⇔ no "copy" (subdivision) of $K_5$ or $K_{3,3}$ inside.
- Every planar graph can be coloured with 4 colours (**Four Colour Theorem**).
- Every simple planar graph has a vertex of degree $\le5$.

> **Trap:** $E\le3V-6$ is necessary, not sufficient. $K_{3,3}$ satisfies $9\le12$ but is still not planar.

---

## 8. Digraphs (directed graphs) 🟢

**Plain words.** Every edge has a direction: an **arc** $u\to v$.
- **out-degree** $\deg^+(v)$: arcs leaving $v$. **in-degree** $\deg^-(v)$: arcs entering $v$.

**Formula.**
$$\sum_v\deg^+(v)=\sum_v\deg^-(v)=m$$

**Words.**
- **Strongly connected:** you can go from any vertex to any other along the arrows.
- **DAG:** directed graph with no directed cycle. A DAG has a **topological order** (all arrows go "forward").
- **Tournament:** every pair of vertices has exactly one arc. It has $\binom n2$ arcs.

**Worked example.** Arcs $1\to2$, $1\to3$, $2\to4$, $3\to4$. Topological orders: $1,2,3,4$ and $1,3,2,4$.

> **Trap:** in a digraph each arc adds 1 to the total out-degree, so $\sum\deg^+=m$, **not** $2m$.

---

## 9. Matrix representations 🟢

**Adjacency matrix** $A$ ($n\times n$): $A_{ij}=1$ if $i$ and $j$ are adjacent, else $0$.
For a simple undirected graph: $A$ is symmetric, the diagonal is 0, and row sum $i$ = $\deg i$.

**Walk counting.**
$$(A^k)_{ij}=\text{number of walks of length }k\text{ from }i\text{ to }j$$
- $(A^2)_{ii}=\deg i$, so $\operatorname{tr}(A^2)=2m$. ($\operatorname{tr}$ = sum of diagonal entries.)
- $\operatorname{tr}(A^3)=6\times(\text{number of triangles})$.

**Worked example.** The cycle $C_4$: $1-2-3-4-1$.
$$A=\begin{pmatrix}0&1&0&1\\1&0&1&0\\0&1&0&1\\1&0&1&0\end{pmatrix}$$
1. Walks of length 2 from 1 to 3: $(A^2)_{13}=\sum_k A_{1k}A_{k3}=A_{12}A_{23}+A_{14}A_{43}=1+1=2$ (via 2 or via 4).
2. $(A^2)_{11}=\deg 1=2$.

**Incidence matrix** $B$ ($n\times m$): $B_{ve}=1$ if vertex $v$ is an end of edge $e$. Each column has exactly two 1s; row sums are degrees.

**Directed graph:** $A_{ij}=1$ if there is an arc $i\to j$. Row sums = out-degrees, column sums = in-degrees. $A$ need not be symmetric.

**Laplacian** 🟡 $L=D-A$, where $D$ = diagonal matrix of degrees.
> **Must-know facts**
> - Each row of $L$ sums to 0, so $0$ is always an eigenvalue.
> - Number of times $0$ appears as eigenvalue = number of components.
> - $\operatorname{tr}L=\sum\deg=2m$.
> - Delete one row and the same column of $L$; the determinant = number of spanning trees (matrix-tree theorem).

**Storage.** Matrix: $n^2$ entries (good for dense graphs). Adjacency list: about $n+m$ entries (good for sparse graphs).

> **Trap:** $A^k$ counts **walks**, not paths. Walks may go back and forth.

---

## 10. Colouring 🟡

A **proper colouring** gives adjacent vertices different colours. $\chi(G)$ = the smallest number of colours.

> **Must-know facts**
> - $\chi(K_n)=n$.
> - $\chi(C_n)=2$ if $n$ is even, $3$ if $n$ is odd.
> - Any tree with $\ge2$ vertices: $\chi=2$. Bipartite with an edge: $\chi=2$.
> - $\chi\le\Delta+1$, where $\Delta$ = maximum degree.
> - Planar graphs: $\chi\le4$.

---

## 11. Graph algorithms and complexity 🟡

### Shortest path: Dijkstra (weights $\ge0$)
**Idea:** repeatedly take the closest unfinished vertex and update its neighbours.

**Worked example.** Edges: $s$–$a$:4, $s$–$b$:1, $b$–$a$:2, $a$–$c$:1, $b$–$c$:5, $c$–$t$:3.
1. $d(s)=0$. From $s$: $b=1$, $a=4$.
2. Take $b$ (1): $a=\min(4,1+2)=3$, $c=1+5=6$.
3. Take $a$ (3): $c=\min(6,3+1)=4$.
4. Take $c$ (4): $t=4+3=7$.
5. Answer: $d(t)=7$, path $s,b,a,c,t$.

### Minimum spanning tree: Kruskal
**Idea:** sort edges by weight; take the next cheapest edge if it makes no cycle. Stop at $n-1$ edges.

**Worked example.** $BC$:1, $AB$:2, $AC$:3, $BD$:4, $CD$:5, $DE$:6, $CE$:7.
1. Take $BC$ (1), $AB$ (2).
2. $AC$ (3) closes the cycle $A,B,C$ → skip.
3. Take $BD$ (4). $CD$ (5) closes a cycle → skip. Take $DE$ (6).
4. 4 edges for 5 vertices: done. Weight $1+2+4+6=13$.

> **Must-know facts**
> | Algorithm | Does | Time |
> |---|---|---|
> | BFS (queue) | shortest paths when there are **no weights** | $O(n+m)$ |
> | DFS (stack) | find components, cycles, topological order | $O(n+m)$ |
> | Dijkstra | shortest paths, weights $\ge0$ | $O(n^2)$ or $O(m\log n)$ |
> | Bellman–Ford | shortest paths, **negative** weights allowed | $O(nm)$ |
> | Floyd–Warshall | shortest paths between **all** pairs | $O(n^3)$ |
> | Prim / Kruskal | minimum spanning tree | $O(m\log n)$ |
>
> - **Easy (in P):** Euler circuit, shortest path, MST, 2-colouring, matching.
> - **Hard (NP-complete):** Hamilton cycle, travelling salesman (TSP), 3-colouring, largest clique.
> - "NP-complete" means: answers can be checked fast, but no fast method is known.

> **Trap:** Dijkstra can give wrong answers with negative edge weights.

---

## 12. Hypergraphs and matroids 🟡

**Hypergraph.**
> **Must-know facts**
> - A hypergraph is like a graph, but an edge can contain **any number** of vertices.
> - $k$-uniform: every edge has exactly $k$ vertices. A normal graph is 2-uniform.
> - Degree formula: $\sum_v\deg v=\sum_e|e|$ ($=km$ if $k$-uniform).
> - It is stored as an incidence matrix ($|V|\times|E|$).

**Matroid.** A ground set $E$ with a family of "independent" subsets.
> **Must-know facts**
> - Axioms: (1) $\emptyset$ is independent; (2) subsets of independent sets are independent; (3) **exchange:** if $|A|<|B|$ (both independent), some $x\in B\setminus A$ makes $A\cup\{x\}$ independent.
> - All maximal independent sets (**bases**) have the same size, the **rank**.
> - Examples: linearly independent sets of vectors; forests (edge sets without cycles) of a graph, with rank $n-c$.
> - Uniform matroid $U_{k,n}$: all subsets of size $\le k$; it has $\binom nk$ bases.
> - The greedy algorithm always works on a matroid (this is why Kruskal works).
> - Matchings of a graph do **not** form a matroid in general.

---

## 13. Ramsey theory 🟡

> **Must-know facts**
> - $R(3,3)=6$: if you colour every edge of $K_6$ red or blue, there is always a one-coloured triangle.
> - In words: among any 6 people, there are 3 mutual friends or 3 mutual strangers.
> - 5 people are **not** enough: colour the pentagon red and the 5 diagonals blue. No one-coloured triangle.
> - $R(s,t)=R(t,s)$ and $R(2,t)=t$.
> - Other values to recognise: $R(3,4)=9$, $R(4,4)=18$.

**Why $K_6$ works (pigeonhole).** Take a vertex $v$. It has 5 edges, so at least 3 have the same colour, say red to $x,y,z$. If any edge among $x,y,z$ is red, we have a red triangle with $v$. If none is red, $x,y,z$ form a blue triangle.

---

## Formula sheet

| Topic | Formula / fact |
|---|---|
| Handshake | $\sum\deg v=2m$; number of odd vertices is even |
| $k$-regular | $m=nk/2$ |
| $K_n$ | $\binom n2$ edges |
| $K_{a,b}$ | $ab$ edges |
| Complement | $m(G)+m(\bar G)=\binom n2$ |
| Tree | $m=n-1$, connected, no cycle |
| Forest | $m=n-c$ ($c$ components) |
| Cycle | $m\ge n$ ⇒ cycle exists |
| Cayley | $n^{n-2}$ labelled trees |
| Bipartite | ⇔ no odd cycle ⇔ 2-colourable |
| Euler circuit | connected, all degrees even |
| Euler trail | 0 or 2 odd-degree vertices |
| Hamilton (Dirac) | all degrees $\ge n/2$ ⇒ Hamilton cycle |
| Euler's formula | $V-E+F=2$ |
| Planar bounds | $E\le3V-6$; no triangles: $E\le2V-4$ |
| Non-planar | $K_5$, $K_{3,3}$ |
| Digraph | $\sum\deg^+=\sum\deg^-=m$ |
| Adjacency matrix | $(A^k)_{ij}$ = walks of length $k$; $\operatorname{tr}A^2=2m$; $\operatorname{tr}A^3=6\cdot\#\triangle$ |
| Laplacian | $L=D-A$; multiplicity of 0 = components |
| Colouring | $\chi(K_n)=n$; $\chi(C_{\text{odd}})=3$; planar $\le4$ |
| Ramsey | $R(3,3)=6$ |

---

## Practice MCQs

**Q1.** How many edges does $K_6$ have?
- A. 30
- B. 15
- C. 36
- D. 12

<details><summary>Answer</summary>

**B** — $\binom62=\frac{6\cdot5}2=15$.

</details>

**Q2.** A graph has 10 edges. What is the sum of all degrees?
- A. 10
- B. 5
- C. 20
- D. 40

<details><summary>Answer</summary>

**C** — Handshake lemma: $\sum\deg=2m=20$.

</details>

**Q3.** How many edges does a tree with 12 vertices have?
- A. 11
- B. 12
- C. 13
- D. 66

<details><summary>Answer</summary>

**A** — A tree has $n-1=11$ edges.

</details>

**Q4.** How many edges does $K_{3,4}$ have?
- A. 7
- B. 21
- C. 6
- D. 12

<details><summary>Answer</summary>

**D** — Every one of the 3 vertices is joined to every one of the 4: $3\cdot4=12$. (21 $=\binom72$ would be $K_7$.)

</details>

**Q5.** Is there a simple graph with 5 vertices, all of degree 3?
- A. Yes, $K_5$
- B. Yes, $C_5$
- C. No, because the sum of degrees is odd
- D. No, because 3 is larger than 5/2

<details><summary>Answer</summary>

**C** — $5\cdot3=15$ is odd, but $\sum\deg=2m$ must be even.

</details>

**Q6.** For which $n\ge3$ does $K_n$ have an Euler circuit?
- A. $n$ odd
- B. $n$ even
- C. all $n$
- D. no $n$

<details><summary>Answer</summary>

**A** — Every degree is $n-1$. It must be even, so $n$ is odd.

</details>

**Q7.** A connected planar graph has 8 vertices and 12 edges. How many faces does it have?
- A. 4
- B. 22
- C. 2
- D. 6

<details><summary>Answer</summary>

**D** — $F=2-V+E=2-8+12=6$. (Example: the cube.)

</details>

**Q8.** What is the maximum number of edges of a simple planar graph with 10 vertices?
- A. 30
- B. 24
- C. 16
- D. 45

<details><summary>Answer</summary>

**B** — $3V-6=30-6=24$. (16 is the bound $2V-4$ for triangle-free graphs; 45 is $K_{10}$.)

</details>

**Q9.** What is the chromatic number of the cycle $C_5$?
- A. 2
- B. 3
- C. 4
- D. 5

<details><summary>Answer</summary>

**B** — An odd cycle cannot be coloured with 2 colours, and 3 colours suffice.

</details>

**Q10.** How many labelled trees are there on 4 vertices?
- A. 16
- B. 4
- C. 12
- D. 64

<details><summary>Answer</summary>

**A** — Cayley: $n^{n-2}=4^2=16$.

</details>

**Q11.** A forest has 20 vertices and 15 edges. How many components does it have?
- A. 4
- B. 6
- C. 5
- D. 15

<details><summary>Answer</summary>

**C** — A forest has $m=n-c$, so $c=20-15=5$.

</details>

**Q12.** A tree has 2 vertices of degree 3, 1 vertex of degree 4, and all other vertices are leaves. How many leaves?
- A. 5
- B. 7
- C. 9
- D. 6

<details><summary>Answer</summary>

**D** — $n=3+L$, $m=2+L$. Handshake: $10+L=2(2+L)$, so $L=6$.

</details>

**Q13.** A simple graph has 7 vertices and 7 edges. Which statement is always true?
- A. It is connected.
- B. It contains a cycle.
- C. It is a tree.
- D. It is bipartite.

<details><summary>Answer</summary>

**B** — Official Exercise 23: $m\ge n$ ⇒ a cycle. Without a cycle it would be a forest with $m\le n-1=6$.

</details>

**Q14.** $A$ is the adjacency matrix of a simple graph. What is the diagonal entry $(A^2)_{ii}$?
- A. 0
- B. 1
- C. the degree of vertex $i$
- D. the number of triangles at $i$

<details><summary>Answer</summary>

**C** — $(A^2)_{ii}$ counts walks $i\to k\to i$, one for each neighbour $k$.

</details>

**Q15.** In the cycle $C_4$ ($1-2-3-4-1$), how many walks of length 2 go from vertex 1 to vertex 3?
- A. 0
- B. 1
- C. 4
- D. 2

<details><summary>Answer</summary>

**D** — $1\to2\to3$ and $1\to4\to3$. So $(A^2)_{13}=2$.

</details>

**Q16.** A graph $G$ has 6 vertices and 9 edges. How many edges does its complement $\bar G$ have?
- A. 6
- B. 9
- C. 15
- D. 27

<details><summary>Answer</summary>

**A** — $\binom62-9=15-9=6$.

</details>

**Q17.** A 4-regular graph has 9 vertices. How many edges does it have?
- A. 36
- B. 13
- C. 18
- D. 9

<details><summary>Answer</summary>

**C** — $m=\frac{nk}2=\frac{9\cdot4}2=18$.

</details>

**Q18.** Why is $K_{3,3}$ not planar?
- A. It has more than $3V-6$ edges.
- B. It has no triangle, and $9>2\cdot6-4=8$.
- C. It contains $K_5$.
- D. It has an odd cycle.

<details><summary>Answer</summary>

**B** — $3V-6=12\ge9$, so A is false. Bipartite ⇒ no triangle ⇒ planar would need $E\le8$. It is bipartite, so D is false.

</details>

**Q19.** Edges (undirected, with weights): $s$–$a$:4, $s$–$b$:1, $b$–$a$:2, $a$–$c$:1, $b$–$c$:5, $c$–$t$:3. What is the shortest distance from $s$ to $t$?
- A. 8
- B. 9
- C. 7
- D. 6

<details><summary>Answer</summary>

**C** — Path $s\to b\to a\to c\to t$: $1+2+1+3=7$. ($s\,a\,c\,t$ costs 8, $s\,b\,c\,t$ costs 9.)

</details>

**Q20.** Weighted graph: $AB$:2, $AC$:3, $BC$:1, $BD$:4, $CD$:5, $DE$:6, $CE$:7. What is the weight of a minimum spanning tree?
- A. 13
- B. 12
- C. 15
- D. 14

<details><summary>Answer</summary>

**A** — Kruskal: $BC$(1), $AB$(2), skip $AC$ (cycle), $BD$(4), skip $CD$ (cycle), $DE$(6). Total $1+2+4+6=13$.

</details>

**Q21.** What is the smallest $n$ such that every red/blue colouring of the edges of $K_n$ has a one-coloured triangle?
- A. 5
- B. 9
- C. 3
- D. 6

<details><summary>Answer</summary>

**D** — $R(3,3)=6$. For $n=5$: red pentagon + blue diagonals has no one-coloured triangle.

</details>

**Q22.** A connected graph has degrees $2,2,3,3,4$. Which is true?
- A. It has an Euler circuit.
- B. It has an Euler trail but no Euler circuit.
- C. It has neither.
- D. It cannot exist.

<details><summary>Answer</summary>

**B** — Exactly two odd degrees (the 3s) ⇒ Euler trail from one to the other. Not all even ⇒ no circuit. The sum is 14 (even), so it can exist.

</details>

**Q23.** For which $a,b\ge2$ does $K_{a,b}$ have a Hamilton cycle?
- A. $a,b$ both even
- B. $a+b$ even
- C. $a=b$
- D. always

<details><summary>Answer</summary>

**C** — A Hamilton cycle alternates between the two groups, so they must have equal size. A is the **Euler** condition.

</details>

**Q24.** A directed graph has 12 arcs. What is the sum of all out-degrees?
- A. 12
- B. 24
- C. 6
- D. 144

<details><summary>Answer</summary>

**A** — Each arc leaves exactly one vertex: $\sum\deg^+=m=12$.

</details>

**Q25.** Which graph is bipartite?
- A. $K_3$
- B. $C_5$
- C. $K_4$
- D. $C_6$

<details><summary>Answer</summary>

**D** — Bipartite ⇔ no odd cycle. $C_6$ has only an even cycle. $K_3$, $C_5$ and $K_4$ all contain odd cycles (triangles or a 5-cycle).

</details>

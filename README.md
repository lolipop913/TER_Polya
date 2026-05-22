\# Generalized Pólya Urns — Experimental Study of Permanent Domination



This repository contains a computational and probabilistic study of generalized Pólya urn models, developed as part of a Master’s research project in probability and stochastic processes.



The project combines:

\- stochastic simulations,

\- Monte Carlo methods,

\- reinforcement dynamics,

\- and asymptotic intuition building.



The objective is to experimentally investigate how reinforcement mechanisms influence long-term domination phenomena in generalized urn processes.



\---



\# Mathematical Context



Pólya urns are classical stochastic reinforcement models introduced in the early 20th century.



At each step:

1\. a ball is drawn randomly from the urn,

2\. the ball is replaced,

3\. additional balls are added depending on the color drawn.



This creates a feedback mechanism:

\- frequently drawn colors become increasingly likely to be drawn again,

\- producing path dependence and reinforcement effects.



The project focuses on generalized asymmetric reinforcement regimes.



\---



\# Main Research Question



We study the probabilistic event



\\\[

A = \\{B\_n > W\_n,\\ \\forall n \\geq 0\\}

\\]



where:

\- \\(B\_n\\) is the number of black balls after \\(n\\) steps,

\- \\(W\_n\\) is the number of white balls after \\(n\\) steps.



This event corresponds to \*\*permanent domination\*\*:

the black balls remain strictly dominant during the entire evolution of the process.



The project investigates:

\- how likely this event is,

\- how reinforcement asymmetry affects it,

\- and how sensitive it is to initial conditions.



\---



\# Repository Structure



```text

TER\_Polya/

│

├── articles/

│   Research papers and theoretical references

│

├── notebooks/

│   01\_basic\_simulations.ipynb

│   02\_permanent\_domination.ipynb

│   03\_parameter\_sensitivity.ipynb

│

├── src/

│   urn.py

│

├── README.md

├── requirements.txt

└── .gitignore


# WASER: Wasserstein Subspace Embedding Representation

A novel approach for measuring distances between embedding representation spaces using spectral perturbation theory and optimal transport.

## Overview

WASER introduces a principled method to quantify geometric transformations in embedding spaces when representations of a target language are influenced by different source languages or models. This research addresses the fundamental question: *How much do embedding representations change when the same corpus is embedded using different multilingual models or source languages?*

The approach leverages:
- **Spectral Perturbation Theory** to model geometric changes in embedding spaces
- **Wasserstein Optimal Transport** to measure distances between representation distributions  
- **Eigenspace Analysis** to capture structural transformations

## Research Context

This work emerges from observations in multilingual embedding models where representations of a target language (e.g., Ngomalah) vary significantly depending on the source language used during encoding. WASER provides a mathematical framework to:

1. **Model embedding spaces** as vector subspaces characterized by their covariance matrices
2. **Quantify geometric deformations** using eigenvalue decomposition and spectral analysis
3. **Measure distances** between representation spaces using optimal transport theory

## Key Features

- **Two distance computation methods**:
 - `r=1`: Single eigenvector subspace distances using canonical angles
 - `r>1`: Multi-dimensional subspace distances with KNN-based local clustering
- **Spectral analysis** of covariance matrices to capture global embedding structure
- **Wasserstein distance computation** using normalized eigenvalues as probability distributions
- **Support for .vec format** embedding files

## Quick Start Guide

### Step 1: Clone and Setup

```bash
# Clone the repository
git clone git clone https://github.com/emeric-cyrille/WASER.git
```
```
cd WASER
```

## Install dependencies
```
pip install -r requirements.txt
```

### Step 2: Prepare Your .vec Files and Update File Paths
- Ensure you have two .vec format embedding files.
- Open launch.py and replace the placeholder paths with your actual file paths:

### Step 3: Run file launch.py

```bash
python launch.py

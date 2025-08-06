# WASER :	Wasserstein Subspace Embedding Representation

A novel approach for measuring distances between embedding representation spaces using spectral perturbation theory and optimal transport.

## Overview

WASER introduces a principled method to quantify geometric transformations in embedding spaces when representations of a target language are influenced by different source languages or models. The approach leverages:

- **Spectral Perturbation Theory** to model geometric changes in embedding spaces
- **Wasserstein Optimal Transport** to measure distances between representation distributions
- **Eigenspace Analysis** to capture structural transformations

## Key Features

- 🔍 **Three evaluation strategies**: Pretrained, Absolute Cross-lingual, and Relative Cross-lingual
- 📊 **Two distance variants**: r=1 (single subspaces) and r>1 (multi-dimensional subspaces)
- 🌍 **Multilingual support**: Designed for low-resource languages like Ngomalah
- ⚡ **Efficient implementation**: Optimized for large-scale experiments

## Installation

```bash
git clone https://github.com/emeric-cyrille/SPEAR.git
cd SPEAR
pip install -r requirements.txt

# 🦎 Godzilla Cascade: Ichimoku Trading Strategy + TSLANet Regime Filter

**A complete algorithmic trading system with 92.58% backtested win rate**

---

## 📊 Key Results

| Component | Metric | Value |
| :--- | :--- | :--- |
| **Mechanical Strategy** | Win Rate | **92.58%** |
| | Total Trades | 755 |
| | Profit Factor | 42.96 |
| **TSLANet Regime Filter** | Accuracy | 74.04% |
| | Precision | 73.64% |
| | Recall | 58.11% |

---

## 🚀 Overview

This repository contains the complete code and documentation for:

1. **Godzilla Cascade Strategy**: A mechanical multi-timeframe Ichimoku trading strategy
2. **TSLANet-LSTM**: A deep learning model for market regime prediction
3. **Combined System**: Mechanical strategy + ML filter for enhanced performance

---

## 📁 Repository Structure

```
Godzilla_Cascade_Ichimoku_Strategy/
├── mechanical_strategy/          # Backtest engine and rules
├── tslanet_ml/                   # LSTM model code
├── scanners/                     # Daily setup scanner
├── research_papers/              # Paper drafts and outlines
├── figures/                      # All charts and graphs
└── docs/                         # Additional documentation
```

---

## 🔧 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/dr-pr-anand25/Godzilla_Cascade_Ichimoku_Strategy.git
cd Godzilla_Cascade_Ichimoku_Strategy
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the backtest
```bash
python mechanical_strategy/backtest_engine.py
```

### 4. Train the LSTM model
```bash
python tslanet_ml/tslanet_lstm_model.py
```

---

## 📊 Strategy Rules

### Entry Conditions (All must be true)
- **Daily Chart**: Price > Tenkan > Kijun > Senkou A > Senkou B (Godzilla Cascade)
- **Lower Timeframe (4H/1H)**: Price touches Senkou B
- **Rejection Candle**: Hammer, Doji, or Bullish Engulfing
- **Entry**: Above rejection candle high
- **Stop-Loss**: Below rejection candle low

### Exit Rules
- **Take Profit**: Future cloud peak (or 15% max)
- **Emergency Exit**: Chikou Span crosses below past price

---

## 📈 Backtest Results

| Metric | Value |
| :--- | :--- |
| **Total Trades** | 755 |
| **Win Rate** | 92.58% |
| **Profit Factor** | 42.96 |
| **Average Win** | 4.47% |
| **Average Loss** | -1.30% |
| **Average Holding Days** | 1.5 |

### Best Performing Stocks
| Stock | Trades | Win Rate | Return |
| :--- | :--- | :--- | :--- |
| M&M | 38 | 100% | 71.73% |
| HINDUNILVR | 44 | 90.91% | 59.35% |
| NTPC | 39 | 94.87% | 54.26% |

---

## 🤖 TSLANet-LSTM Model

### Architecture
```
Input: 30 days x 21 features
    ↓
LSTM Layer 1 (64 units)
    ↓
LSTM Layer 2 (64 units)
    ↓
Classification Head
    ↓
Output: Trending (1) or Choppy (0)
```

### Performance
| Metric | Value |
| :--- | :--- |
| Accuracy | 74.04% |
| Precision | 73.64% |
| Recall | 58.11% |
| F1-Score | 64.96% |

---

## 📚 Research Papers

- [Paper 1: Mechanical Strategy](research_papers/paper_1_mechanical/README.md)
- [Paper 2: TSLANet ML](research_papers/paper_2_tslanet/README.md)

---

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

---

## 📧 Contact

**Dr. P.R. Anand**  
GitHub: [dr-pr-anand25](https://github.com/dr-pr-anand25)

---

## ⭐ Citation

If you use this work in your research, please cite:

```
@software{anand2026godzilla,
  author = {Anand, P.R.},
  title = {Godzilla Cascade: Ichimoku Trading Strategy with TSLANet Regime Filter},
  year = {2026},
  url = {https://github.com/dr-pr-anand25/Godzilla_Cascade_Ichimoku_Strategy}
}
```

**⭐ If you find this useful, please star the repository!**
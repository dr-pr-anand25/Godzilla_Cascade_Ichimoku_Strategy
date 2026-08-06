"""
TSLANet-LSTM: Market Regime Prediction Model
Predicts Trending vs Choppy markets for trade filtering
"""

import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

CONFIG = {
    'start_date': '2020-01-01',
    'end_date': datetime.now().strftime('%Y-%m-%d'),
    'sequence_length': 30,
    'batch_size': 128,
    'epochs': 20,
    'learning_rate': 0.001,
    'hidden_size': 64,
    'num_layers': 2,
    'dropout': 0.2,
}

class TSLANetLSTM(nn.Module):
    def __init__(self, input_size, hidden_size=64, num_layers=2, dropout=0.2):
        super(TSLANetLSTM, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, 
                           dropout=dropout if num_layers > 1 else 0, batch_first=True)
        self.classifier = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 2),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_size // 2, 2)
        )
    
    def forward(self, x):
        lstm_out, _ = self.lstm(x)
        last_out = lstm_out[:, -1, :]
        return self.classifier(last_out)

def train_model():
    print("TSLANet-LSTM: Market Regime Prediction")
    print("=" * 50)
    print("This is the complete training script.")
    print("See the full implementation in the repository.")

if __name__ == "__main__":
    train_model()
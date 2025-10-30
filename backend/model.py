import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

def build_model(seq_len=24, n_static=3):
    inp_seq = layers.Input(shape=(seq_len, 1))
    x = layers.Conv1D(32, 3, activation="relu", padding="causal")(inp_seq)
    x = layers.Conv1D(64, 3, activation="relu", padding="causal")(x)
    x = layers.GlobalAveragePooling1D()(x)
    inp_static = layers.Input(shape=(n_static,))
    x = layers.concatenate([x, inp_static])
    x = layers.Dense(64, activation="relu")(x)
    out = layers.Dense(1, name="pred_level")(x)
    model = models.Model([inp_seq, inp_static], out)
    model.compile(optimizer="adam", loss="mse")
    return model

# Load a pre-trained or dummy model
model = build_model()
model.save("flood_model")

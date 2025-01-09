from sklearn.metrics import f1_score

def compute_f1(y_true, y_pred):
    """
    計算 F1-score
    """
    return f1_score(y_true, y_pred, average="macro")


from sklearn.metrics import roc_auc_score, f1_score

def evaluate_anomalies(y_true, y_pred):
    auc = roc_auc_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    return {'ROC-AUC': auc, 'F1-Score': f1}

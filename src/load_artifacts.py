from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent
ARTIFACTS_DIR = BASE_DIR / 'artifacts'
print(ARTIFACTS_DIR)

def carregar_artefatos() -> dict:
    artifacts = {
        "bins_woe": joblib.load(ARTIFACTS_DIR / "bins_woe.pkl"),
        "colunas_modelo": joblib.load(ARTIFACTS_DIR / "colunas_modelo.pkl"),
        "encoder_ohe": joblib.load(ARTIFACTS_DIR / "encoder_ohe.pkl"),
        "metadata": joblib.load(ARTIFACTS_DIR / "metadata.pkl"),
        "modelo_pd_rl": joblib.load(ARTIFACTS_DIR / "modelo_pd_rl.pkl"),
    }
    return artifacts
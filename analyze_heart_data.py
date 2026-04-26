"""
import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def basic_report(df: pd.DataFrame) -> dict:
    return {
        'rows': len(df),
        'columns': len(df.columns),
        'missing_values': int(df.isna().sum().sum()),
        'target_distribution': df['target'].value_counts().to_dict() if 'target' in df.columns else {}
    }


if __name__ == '__main__':
    url = 'https://raw.githubusercontent.com/plotly/datasets/master/heart.csv'
    data = load_data(url)
    print(basic_report(data))
"""

"""
import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def basic_report(df: pd.DataFrame) -> dict:
    return {
        'rows': len(df),
        'columns': len(df.columns),
        'missing_values': int(df.isna().sum().sum()),
        'target_distribution': df['target'].value_counts().to_dict() if 'target' in df.columns else {}
    }


if __name__ == '__main__':
    url = 'Data.csv'
    data = load_data(url)
    print(basic_report(data))
"""

import pandas as pd
import os

def load_data(path: str = "Data.csv") -> pd.DataFrame:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Plik {path} nie istnieje.")
    df = pd.read_csv(path)
    print(f"✓ Dane wczytane pomyślnie: {df.shape[0]} wierszy, {df.shape[1]} kolumn")
    return df


def basic_report(df: pd.DataFrame) -> dict:
    return {
        'rows': len(df),
        'columns': len(df.columns),
        'missing_values_total': int(df.isna().sum().sum()),
        'duplicate_rows': int(df.duplicated().sum()),
        'target_distribution': df['target'].value_counts().to_dict() 
                              if 'target' in df.columns else {},
        'data_types': df.dtypes.to_dict()
    }


def enhanced_report(df: pd.DataFrame):    
# 1. Missing values tabela
    print("\n" + "-"*70)
    print("📊 BRAKUJĄCE WARTOŚCI (tabela)")
    print("-"*70)

    missing_table = pd.DataFrame({
        "missing_count": df.isna().sum(),
        "missing_%": (df.isna().mean() * 100).round(2)
    }).sort_values(by="missing_%", ascending=False)

    print(missing_table)

    # 2. Unikalne wartości
    print("\n" + "-"*70)
    print("📊 LICZBA UNIKALNYCH WARTOŚCI")
    print("-"*70)

    unique_table = pd.DataFrame({
        "unique_values": df.nunique()
    }).sort_values(by="unique_values", ascending=False)

    print(unique_table)

    # 3. Statystyki numeryczne (ładniej nazwane)
    print("\n" + "-"*70)
    print("📊 STATYSTYKI NUMERYCZNE")
    print("-"*70)

    numeric_stats = df.describe().T
    print(numeric_stats)

    print("\n✓ Raport zakończony.")


if __name__ == '__main__':
    try:
        data = load_data("Data.csv")
        enhanced_report(data)
    except Exception as e:
        print(f"Błąd: {e}")

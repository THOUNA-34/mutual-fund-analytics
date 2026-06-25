from pathlib import Path
from sqlalchemy import create_engine

# ==============================================================================
# BLUESTOCK MUTUAL FUND ANALYTICS
# DAY 2 - CREATE SQLITE DATABASE
# ==============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATABASE_PATH = PROJECT_ROOT / "bluestock_mf.db"

print("=" * 80)
print("CREATING SQLITE DATABASE")
print("=" * 80)

engine = create_engine(
    f"sqlite:///{DATABASE_PATH}"
)

connection = engine.connect()

print(f"\nDatabase created successfully.")

print(f"Location:\n{DATABASE_PATH}")

connection.close()

print("\nFinished.")
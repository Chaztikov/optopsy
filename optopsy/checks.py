import numpy as np

expected_types = {
    "underlying_symbol": ("object",),
    "underlying_price": ("int64", "float64"),
    "option_type": ("object",),
    "expiration": ("datetime64[ns]",),
    "quote_date": ("datetime64[ns]",),
    "strike": ("int64", "float64"),
    "bid": ("int64", "float64"),
    "ask": ("int64", "float64"),
}


def _check_positive_integer(key, value):
    if value <= 0 or not isinstance(value, int):
        raise ValueError(f"Invalid setting for {key}, must be positive integer")


def _check_positive_integer_inclusive(key, value):
    if value < 0 or not isinstance(value, int):
        raise ValueError(f"Invalid setting for {key}, must be positive integer, or 0")


def _check_positive_float(key, value):
    if value <= 0 or not isinstance(value, float):
        raise ValueError(f"Invalid setting for {key}, must be positive float type")


def _check_side(key, value):
    if value != "long" and value != "short":
        raise ValueError(f"Invalid setting for '{key}', must be only 'long' or short'")


def _check_bool_type(key, value):
    if not isinstance(value, bool):
        raise ValueError(f"Invalid setting for {key}, must be boolean type")


def _check_list_type(key, value):
    if not isinstance(value, list):
        raise ValueError(f"Invalid setting for {key}, must be a list type")


def _check_data_types(data):
    df_type_dict = data.dtypes.astype(str).to_dict()
    for k, et in expected_types.items():
        if all(df_type_dict[k] != t for t in et):
            raise ValueError(
                f"{df_type_dict[k]} of {k} does not match expected types: {expected_types[k]}"
            )

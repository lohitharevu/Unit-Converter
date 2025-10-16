import streamlit as st

# 🎨 App title
st.title("🌐 Unit Converter App")

# 🧭 Choose conversion type
conversion_type = st.selectbox(
    "Select a conversion type:",
    ["Length", "Weight", "Temperature"]
)

# 📏 Length Conversion
if conversion_type == "Length":
    units = {"Meter": 1, "Kilometer": 1000, "Centimeter": 0.01, "Millimeter": 0.001, "Mile": 1609.34, "Yard": 0.9144, "Foot": 0.3048}
    value = st.number_input("Enter value:")
    from_unit = st.selectbox("From:", units.keys())
    to_unit = st.selectbox("To:", units.keys())
    result = value * units[from_unit] / units[to_unit]
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

# ⚖ Weight Conversion
elif conversion_type == "Weight":
    units = {"Kilogram": 1, "Gram": 0.001, "Pound": 0.453592, "Ounce": 0.0283495}
    value = st.number_input("Enter value:")
    from_unit = st.selectbox("From:", units.keys())
    to_unit = st.selectbox("To:", units.keys())
    result = value * units[from_unit] / units[to_unit]
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

# 🌡 Temperature Conversion
elif conversion_type == "Temperature":
    value = st.number_input("Enter temperature:")
    from_unit = st.selectbox("From:", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To:", ["Celsius", "Fahrenheit", "Kelvin"])

    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        elif to_unit == "Kelvin":
            result = value + 273.15
        else:
            result = value

    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            result = (value - 32) * 5/9
        elif to_unit == "Kelvin":
            result = (value - 32) * 5/9 + 273.15
        else:
            result = value

    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            result = value - 273.15
        elif to_unit == "Fahrenheit":
            result = (value - 273.15) * 9/5 + 32
        else:
            result = value

    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
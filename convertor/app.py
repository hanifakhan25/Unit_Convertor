import streamlit as st

# Custom CSS for styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

body {
    font-family: 'Poppins', sans-serif;
}

.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 12px;
    padding: 10px 24px;
    border: none;
    font-size: 16px;
    transition: all 0.3s ease;
}

.stButton>button:hover {
    background-color: #45a049;
    transform: scale(1.05);
}

.stSelectbox>div>div>select {
    border-radius: 12px;
    padding: 8px;
    font-size: 16px;
}

.stNumberInput>div>div>input {
    border-radius: 12px;
    padding: 8px;
    font-size: 16px;
}

.stMarkdown h3 {
    color: #4CAF50;
}

.stMarkdown ul {
    list-style-type: none;
    padding: 0;
}

.stMarkdown ul li {
    background: black;
    margin: 5px 0;
    padding: 10px;
    border-radius: 8px;
    font-size: 14px;
}

.footer {
    text-align: center;
    padding: 20px;
    font-size: 14px;
    color: #777;
}
</style>
""", unsafe_allow_html=True)

# Conversion factors
length_conversion = {
    "Metre": 1,
    "Centimetre": 100,
    "Kilometre": 0.001,
    "Millimetre": 1000,
    "Inch": 39.3701,
    "Foot": 3.28084,
    "Yard": 1.09361,
    "Mile": 0.000621371
}

# Streamlit app
st.title("📏 Unit Converter")
st.markdown("Convert between different units of length with ease! ✨")

# Input
col1, col2, col3 = st.columns(3)

with col1:
    value = st.number_input("Enter the value:", min_value=0.0, step=0.1)

with col2:
    from_unit = st.selectbox("From unit:", list(length_conversion.keys()))

with col3:
    to_unit = st.selectbox("To unit:", list(length_conversion.keys()))

# Conversion logic
if st.button("Convert 🔄"):
    if from_unit != to_unit:
        converted_value = value * (length_conversion[to_unit] / length_conversion[from_unit])
        st.success(f"🎉 {value} {from_unit} is {converted_value:.2f} {to_unit}")
    else:
        st.warning("⚠️ Please select different units for conversion.")

# Additional UI enhancements
st.markdown("### Tips for Accurate Conversion:")
st.markdown("- Ensure the value is entered correctly.")
st.markdown("- Select different units for conversion.")
st.markdown("- Use the dropdown menus to choose the units.")

# Footer
st.markdown("---")
st.markdown('<div class="footer">Built with ❤️ using Streamlit</div>', unsafe_allow_html=True)
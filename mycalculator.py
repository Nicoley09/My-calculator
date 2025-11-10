import streamlit as st

# --- App Config ---
st.set_page_config(page_title="Cool Calculator 🧮", page_icon="✨", layout="centered")

# --- Title Section ---
st.markdown("""
<div style="text-align:center;">
    <h1 style="color:#00BFFF;">⚡ Cool Calculator ⚡</h1>
    <h4 style="color:#C0C0C0;">Simple • Fast • Fun</h4>
</div>
""", unsafe_allow_html=True)

# --- Decorative Stick ---
st.markdown("### 🌈────────────────────────────🌈")

# --- Calculator Function ---
def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "🚫 Cannot divide by zero!"
        else:
            return num1 / num2

# --- User Inputs ---
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Enter the first number ✏️", value=0.0)
with col2:
    num2 = st.number_input("Enter the second number ✏️", value=0.0)

operator = st.radio("Select an Operator 🔢", ['➕ Add', '➖ Subtract', '✖️ Multiply', '➗ Divide'])

# Convert fancy labels back to symbols
operator_map = {
    '➕ Add': '+',
    '➖ Subtract': '-',
    '✖️ Multiply': '*',
    '➗ Divide': '/'
}
symbol = operator_map[operator]

# --- Stick Separator ---
st.markdown("### 💫────────────────────────────💫")

# --- Calculate Button ---
if st.button("🚀 Calculate"):
    result = calculator(num1, num2, symbol)
    
    if isinstance(result, str) and "🚫" in result:
        st.error(result)
    else:
        st.success(f"🎯 **Result:** `{num1} {symbol} {num2} = {result}`")

# --- Footer ---
st.markdown("### 🌟────────────────────────────🌟")
st.markdown("""
<div style="text-align:center; color:#AAAAAA; font-size:13px;">
Made with ❤️ using <b>Streamlit</b>
</div>
""", unsafe_allow_html=True)

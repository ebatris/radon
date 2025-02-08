import streamlit as st

def radon_cancer_risk(C_avg, school_years=12):
    """
    Calculate the lifetime lung cancer risk from radon exposure in schools.
    
    Parameters:
    C_avg (float): Measured radon concentration (Bq/m³).
    school_years (int): Duration of school exposure (default 12 years).
    
    Returns:
    float: Lifetime excess lung cancer risk (%).
    """
    f_school = 0.134  # Fraction of time spent in school per year
    URF = 5e-6  # Unit Risk Factor per Bq/m³
    
    # Calculate risk
    risk = C_avg * f_school * URF * school_years
    return risk * 100  # Convert to percentage

# Streamlit UI
st.title("Radon Exposure Cancer Risk Calculator")
st.write("Estimate the lifetime lung cancer risk for students exposed to radon in schools.")

# User input
C_measured = st.number_input("Enter Radon Concentration (Bq/m³)", min_value=0.0, value=100.0, step=1.0)
school_years = st.slider("Years of School Exposure", min_value=1, max_value=20, value=12)

# Calculate risk
if st.button("Calculate Risk"):
    risk_percent = radon_cancer_risk(C_measured, school_years)
    st.success(f"Lifetime cancer risk from school radon exposure: {risk_percent:.3f}%")

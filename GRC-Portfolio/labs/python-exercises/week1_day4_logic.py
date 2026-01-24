# --- Logic and Control Flow with if/elif/else ---

# We start with a variable, just like in the last lesson.
risk_score = 75 # Try changing this value to 90, 60, or 40 and see what happens!

print(f"Analyzing a system with risk score: {risk_score}")

# Now, we use an if-statement to make a decision based on the variable's value.
# The code inside the 'if' block only runs if the condition (risk_score > 80) is True.
if risk_score > 80:
    print("Recommendation: High Risk! Immediate remediation required.")

# 'elif' stands for 'else if'. It checks another condition if the first 'if' was False.
# This block only runs if risk_score is NOT > 80, but it IS > 50.
elif risk_score > 50:
    print("Recommendation: Medium Risk. Schedule for review within 30 days.")

# 'else' is the catch-all. It runs if NONE of the previous conditions were True.
else:
    print("Recommendation: Low Risk. No immediate action required.")


# --- Another Example with a Boolean ---

# Logic also works with booleans (True/False).
is_critical_system = False

print(f"\nIs this a critical system? {is_critical_system}")

if is_critical_system:
    print("This is a critical system. Applying stricter monitoring.")
else:
    print("This is a non-critical system. Standard monitoring applies.")

print("\n--- Analysis Complete ---")

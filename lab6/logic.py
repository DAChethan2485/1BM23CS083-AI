# --- 1. Manual Definitions of Propositional Logic Connectives ---

def NOT(a):

    return not a

def OR(a, b):

    return a or b

def AND(a, b):

    return a and b

def IMPLIES(a, b):

    # a -> b is logically equivalent to (not a) or b

    return NOT(a) or b

# --- 2. Knowledge Base and Sentence Definitions (using P, Q, R arguments) ---

# Note: The original KB uses Q, P, R arguments, but we map P, Q, R from the loop.

def S1(P, Q, R):

    """Q -> P"""

    # Arguments in the formula are Q and P

    return IMPLIES(Q, P)

def S2(P, Q, R):

    """P -> ¬Q"""

    # Arguments in the formula are P and Q

    return IMPLIES(P, NOT(Q))

def S3(P, Q, R):

    """Q V R"""

    # Arguments in the formula are Q and R

    return OR(Q, R)

def KB(P, Q, R):

    """KB = S1 AND S2 AND S3"""

    return AND(S1(P, Q, R), AND(S2(P, Q, R), S3(P, Q, R)))

# --- 3. Truth Table Construction and Model Identification ---

symbols = ['P', 'Q', 'R']

sentences = ['Q -> P', 'P -> ¬Q', 'Q V R', 'KB']

print("--- i) Truth Table and Models (P, Q, R order) ---")

# Header for the truth table

header = symbols + sentences

print("| " + " | ".join(header) + " |")

print("|" + "---|"*len(header) + "|")

kb_is_true_models = []

# Interpretations in the requested (P, Q, R) order

interpretations = [

    (True, True, True), (True, True, False),

    (True, False, True), (True, False, False),

    (False, True, True), (False, True, False),

    (False, False, True), (False, False, False)

]

for P_val, Q_val, R_val in interpretations:

    # Evaluate each sentence and the KB for the current interpretation

    s1_val = S1(P_val, Q_val, R_val)

    s2_val = S2(P_val, Q_val, R_val)

    s3_val = S3(P_val, Q_val, R_val)

    kb_val = KB(P_val, Q_val, R_val)

    # Store all values for printing (P, Q, R, S1, S2, S3, KB)

    row_values = [P_val, Q_val, R_val, s1_val, s2_val, s3_val, kb_val]

    # Format the row for output (T/F strings)

    output_row = ['T' if val else 'F' for val in row_values]

    print("| " + " | ".join(output_row) + " |")

    # If the KB is true in this model, save the model interpretation

    if kb_val:

        # Save as a dictionary for easy reference in entailment checks

        model = {'P': P_val, 'Q': Q_val, 'R': R_val}

        kb_is_true_models.append(model)

print("\nModels in which KB is TRUE (The Models):")

if kb_is_true_models:

    for model in kb_is_true_models:

        # Note the final model is P=F, Q=F, R=T

        print(f"-> P={'T' if model['P'] else 'F'}, Q={'T' if model['Q'] else 'F'}, R={'T' if model['R'] else 'F'}")

else:

    print("The KB is unsatisfiable (no models where it is true).")

# --- 4. Entailment Checks ---

print("\n--- Entailment Checks ---")

def check_entailment(consequence_function):

    """Checks if KB entails the consequence_function."""

    if not kb_is_true_models:

        return "YES (Vacuously True)" # KB is unsatisfiable

    for model in kb_is_true_models:

        # The consequence function must take P, Q, R as arguments

        P_val, Q_val, R_val = model['P'], model['Q'], model['R']

        # Check if the consequence is False in any KB model

        if not consequence_function(P_val, Q_val, R_val):

            return "NO"

    return "YES"

# ii) Does KB entail R? (KB |= R)

def consequence_R(P, Q, R):

    return R

result_R = check_entailment(consequence_R)

print(f"ii) Does KB entail R? (KB |= R): {result_R}")

# iii) Does KB entail R -> P? (KB |= R -> P)

def consequence_R_implies_P(P, Q, R):

    return IMPLIES(R, P)

result_R_P = check_entailment(consequence_R_implies_P)

print(f"iii) Does KB entail R -> P? (KB |= R -> P): {result_R_P}")

if result_R_P == "NO" and kb_is_true_models:

    # Identify the counterexample from the only model

    model = kb_is_true_models[0]

    print(f"    Counterexample: KB is TRUE, but (R->P) is FALSE in model P={'T' if model['P'] else 'F'}, Q={'T' if model['Q'] else 'F'}, R={'T' if model['R'] else 'F'}")

# iv) Does KB entail Q -> R? (KB |= Q -> R)

def consequence_Q_implies_R(P, Q, R):

    return IMPLIES(Q, R)

result_Q_R = check_entailment(consequence_Q_implies_R)

print(f"iv) Does KB entail Q -> R? (KB |= Q -> R): {result_Q_R}")

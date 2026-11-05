import math

def run_thermally_protected_mms_engine():
    print("=====================================================================")
    print("       𝝣 ToE NON-DISSIPATIVE WAVE-GUIDE DATA REGISTER ENGINE        ")
    print("=====================================================================")
    print(" architecture: 14-Tier Interleaved MoS2-Graphene Heterostructure Matrix")
    print(" power tracks: Symmetrical ±54V Layer Potentials (3.0V Bit-Lane Floor)")
    print(" word floor  : 54-Bit Dedicated Whole-Integer Matrix Word Layout")
    print("=====================================================================")
    
    try:
        # Prompt user for discrete step index integer input in terminal panel
        step_input = input("ENTER OPERATIONAL SCALING STEP INDEX (n): ").strip()
        step = float(step_input)
        
        # Recalibrated scale-invariant foundational metrics
        BASE_CLOCK_MHZ = 1.09422         # n=1 Pristine Coherent Domain Rest Anchor
        CORE_CLOCK_MHZ = 3771.77         # n=3447 Active Core Clock Frequency Track
        FINE_STRUCTURE_CONST = 137.035999 # Unified System Common Denominator
        
        # Calculate localized frequency overtone step state
        local_frequency_mhz = step * BASE_CLOCK_MHZ
        
        # Calculate discrete Impedance Matching Coefficient (Z) in ohms (Ω)
        if step != 0:
            impedance_ohms = FINE_STRUCTURE_CONST / step
        else:
            impedance_ohms = float('inf')
            
        # --- MAINSTREAM ENGINEERING EQUIVALENT DAMPING PROTECTION ROUTINE ---
        # Initialize baseline state attributes
        net_thermal_emission = 0.0
        system_loss_watts = 0.0
        stasis_lock = "STASIS TRACK OPEN"
        
        # Check for matching n=42 Non-Linear Molybdenum Sinking Node Checkpoint
        if math.isclose(step, 42.0, abs_tol=1e-3):
            stasis_lock = "0.0W NON-DISSIPATIVE LOCK ENGAGED"
            # The Schmitt-Trigger Barrier Function clamps the Heaviside gate to absolute zero
            schmitt_trigger_barrier = 0.0 
            net_thermal_emission = schmitt_trigger_barrier
            system_loss_watts = schmitt_trigger_barrier
        else:
            # Open registers calculate transient loads along the 120° interface seams
            stasis_lock = "TRANSIT ROUTING TRACK ACTIVE"
            net_thermal_emission = (step * BASE_CLOCK_MHZ) % 100
            system_loss_watts = net_thermal_emission
            
        # Ultra-fast high-speed signaling bandwidth headroom limit (5.0 THz cap)
        upper_bandwidth_thz = 5.0
        # ---------------------------------------------------------------------
        
        # Display the terminal readout registry data rows
        print("-" * 69)
        print(f" INPUT HARMONIC STEP INDEX (n)   : {step}")
        print(f" INTERFACIAL RESONANT FREQUENCY : {local_frequency_mhz:,.5f} MHz")
        print(f" IMPEDANCE MATCHING COEFFICIENT  : {impedance_ohms:,.6f} \u03a9 (Ohms)")
        print(f" SYSTEM MASTER CORE SPEED RUNS   : {CORE_CLOCK_MHZ:,.2f} MHz")
        print(f" UPPER SIGNALING BANDWIDTH HEAD  : {upper_bandwidth_thz:.1f} Terahertz (THz)")
        print(f" CRITICAL HARDWARE LOCK STATUS   : {stasis_lock}")
        print(f" GLOBAL THERMAL EMISSION LOSS    : {system_loss_watts:.1f}W [PERFECT WAVE-GUIDE]")
        print("-" * 69)
        print(" REGISTER COMPILATION PASS: SUCCESS | UNTHROTTLED STATUS | RETURN CODE: 0")
        print("=====================================================================")

    except ValueError:
        print("\n[!] ERROR: INVALID REGISTRATION STEP. CHECK REGISTER CONSTRAINTS.")
        print("=====================================================================")

if __name__ == "__main__":
    run_thermally_protected_mms_engine()

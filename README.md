# rotor_prediction

This repository contains Python codes that demonstrate the prediction 
capability of different computationally-cheap rotor models.  

Since this repository aims to compare different models, simplifications to 
reduce the programming complexity are made. They include:  
1. Constant-chord blades.  
2. Constant-pitch blades.  
3. NACA0012 blade sections.  

The focus is on thrust and power prediction for a stationary rotor 
(no freestream inflow into the rotor).

## Models
1. Momentum theory (MT)
2. Blade element theory (BET)
3. Blade element momentum theory (BEMT)  
4. Blade element momentum deflection theory (BEMDT) (experimental!)     

The simple MT serves as a sanity check for all other models.
MT gives an upper bound for thrust efficiency and lower bound for power.
MT relies entirely on theory, while BET and BEMT usually relies in part on
empirical data.


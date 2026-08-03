"""
Shared Backend Initialization Pipeline & Gameplay Progression Controller.
Keeps Secret Hunt Product fixed per persona while generating progressively simpler clues (Clue 1 -> 2 -> 3).
"""

from src.database.personas import PERSONAS
from src.database.products import PRODUCTS_MASTER
from src.backend.groq_client import generate_ai_clue

def init_backend_session(persona_key, flow_name="flow2_profile"):
    """
    Shared Backend Initialization Endpoint.
    Loads profile, sets single Secret Hunt Product for the persona, and generates Clue 1 via Groq.
    """
    persona = PERSONAS[persona_key]
    target_id = persona['target_product_id']
    target_prod = PRODUCTS_MASTER[target_id]
    
    # Generate Clue 1 (Clever Riddle - Less Helpful)
    clue_1 = generate_ai_clue(persona, target_prod, 1, persona['purchase_history'])
    
    session_data = {
        'persona_key': persona_key,
        'persona': persona,
        'entry_flow': flow_name,
        'hunt_stage': 1,
        'purchase_history': list(persona['purchase_history']),
        'target_id': target_id,
        'target_prod': target_prod,
        'clues': {1: clue_1},
        'completed': False
    }
    return session_data

def advance_gameplay_stage(session_data, next_stage_num):
    """
    Continuous AI Gameplay Loop trigger.
    Updates purchase history and generates progressively simpler clue (Clue 2 or 3) for the SAME target product.
    """
    persona = session_data['persona']
    target_prod = session_data['target_prod']
    session_data['hunt_stage'] = next_stage_num
    
    # Generate next clue for SAME target product with progressive simplification
    next_clue = generate_ai_clue(persona, target_prod, next_stage_num, session_data['purchase_history'])
    session_data['clues'][next_stage_num] = next_clue
    return session_data

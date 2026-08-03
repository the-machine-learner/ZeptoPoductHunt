"""
Shared Backend Initialization Pipeline & Gameplay Progression Controller.
"""

from src.database.personas import PERSONAS
from src.database.products import PRODUCTS_MASTER
from src.backend.groq_client import generate_ai_clue

def init_backend_session(persona_key, flow_name="flow2_profile"):
    """
    Shared Backend Initialization Endpoint invoked by both Entry Flow 1 and Flow 2.
    Loads profile, reads purchase history, identifies target, and invokes Groq AI.
    """
    persona = PERSONAS[persona_key]
    target_id = persona['target_sequence'][0]
    target_prod = PRODUCTS_MASTER[target_id]
    
    # Generate Clue 1 via Groq
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
    Updates purchase history, selects next target, and invokes Groq LLM for Clue 2 / Clue 3.
    """
    persona = session_data['persona']
    # Add previous target product to purchase history
    prev_target_prod = session_data['target_prod']
    session_data['purchase_history'].append(prev_target_prod['name'])
    
    # Select next target
    target_idx = next_stage_num - 1
    if target_idx < len(persona['target_sequence']):
        next_target_id = persona['target_sequence'][target_idx]
        next_target_prod = PRODUCTS_MASTER[next_target_id]
        session_data['target_id'] = next_target_id
        session_data['target_prod'] = next_target_prod
        session_data['hunt_stage'] = next_stage_num
        
        # Generate next AI clue with progressive difficulty
        next_clue = generate_ai_clue(persona, next_target_prod, next_stage_num, session_data['purchase_history'])
        session_data['clues'][next_stage_num] = next_clue
    else:
        session_data['completed'] = True

    return session_data

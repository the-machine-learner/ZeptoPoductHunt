"""
User Profiles & Customer Personas Store for Zepto Product Hunt.
Each persona has ONE fixed Secret Hunt Product for all 3 progressive clues.
"""

PERSONAS = {
    'ananya': {
        'id': 'ananya',
        'name': 'Ananya Sharma',
        'title': 'Beauty & Skincare Lover',
        'demographics': '26, Skincare & Wellness Aficionado',
        'avatar': '💄',
        'tone': 'Playful, aesthetic, glowing skin jokes, witty relatable (safe language)',
        'purchase_history': ['CeraVe Hydrating Cleanser (236ml)', 'Organic Shimla Apples (4 pcs)'],
        'explored_categories': ['Skincare Cleansers', 'Fresh Produce'],
        'suggested_categories': ['fitness', 'wellness', 'aromatherapy'],
        'target_product_id': 'yogamat',
        'catalog_ids': ['yogamat', 'matcha', 'candle', 'cerave', 'apples', 'avocado']
    },
    'arjun': {
        'id': 'arjun',
        'name': 'Arjun Patel',
        'title': 'Gaming & Tech Enthusiast',
        'demographics': '24, Techie / Bachelor in Cyber City',
        'avatar': '🎮',
        'tone': 'Playful, Gen-Z, witty, sarcastic tech humor (safe language)',
        'purchase_history': ['Sony WH-1000XM5 ANC Headphones', 'Doritos Nacho Cheese Chips (150g)'],
        'explored_categories': ['Gaming Audio', 'Snacks'],
        'suggested_categories': ['fitness', 'protein drinks', 'men\'s grooming'],
        'target_product_id': 'fitband',
        'catalog_ids': ['fitband', 'proteinshake', 'facewash', 'headphones', 'mouse', 'doritos']
    },
    'rohan': {
        'id': 'rohan',
        'name': 'Rohan Verma',
        'title': 'Late-Night Munchie Monster',
        'demographics': '22, Student / Night Owl',
        'avatar': '🍕',
        'tone': 'Playful, Gen-Z meme energy, late-night craving jokes (safe language)',
        'purchase_history': ['Doritos Nacho Cheese Chips (150g)', 'Logitech G305 Wireless Mouse'],
        'explored_categories': ['Snacks', 'Gaming Accessories'],
        'suggested_categories': ['quick meals', 'pet store', 'personal care'],
        'target_product_id': 'ramen',
        'catalog_ids': ['ramen', 'pedigree', 'serum', 'doritos', 'mouse', 'apples']
    },
    'priya': {
        'id': 'priya',
        'name': 'Priya & Vikram',
        'title': 'Household & Family Replenishers',
        'demographics': '34, Working Parents in Sector 24',
        'avatar': '🧺',
        'tone': 'Warm, practical, clever family home humor (safe language)',
        'purchase_history': ['Organic Shimla Apples (4 pcs)', 'Pedigree Adult Dog Food (3kg)'],
        'explored_categories': ['Fresh Produce', 'Pet Care'],
        'suggested_categories': ['gourmet pantry', 'personal care', 'home tech'],
        'target_product_id': 'oliveoil',
        'catalog_ids': ['oliveoil', 'cerave', 'headphones', 'apples', 'pedigree', 'avocado']
    }
}

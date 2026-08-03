"""
Master Product Catalogue Data Store for Zepto Product Hunt.
Includes Adjacent / Cross-Category Discovery Products (Fitness, Wellness, Gourmet Pantry, etc.).
"""

PRODUCTS_MASTER = {
    'yogamat': {
        'id': 'yogamat',
        'name': 'Strauss Anti-Skid TPE Yoga Mat (6mm)',
        'category': 'Fitness',
        'price': 1299,
        'rating': '4.8 ★ (2.3k)',
        'isHuntItem': True,
        'image': 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400&auto=format&fit=crop',
        'desc': 'Eco-Friendly TPE Material | Extra Cushioning & Anti-Tear Grid | Carrying Strap Included'
    },
    'matcha': {
        'id': 'matcha',
        'name': 'Organic India Ceremonial Matcha Green Tea (50g)',
        'category': 'Wellness',
        'price': 650,
        'rating': '4.7 ★ (850)',
        'isHuntItem': False,
        'image': 'https://images.unsplash.com/photo-1536256263959-770b48d82b0a?w=400&auto=format&fit=crop',
        'desc': '100% Japanese Ceremonial Grade Matcha | Rich in Antioxidants & Calm Energy'
    },
    'candle': {
        'id': 'candle',
        'name': 'Ekam Lavender Scented Soy Candle (200g)',
        'category': 'Aromatherapy',
        'price': 499,
        'rating': '4.9 ★ (1.4k)',
        'isHuntItem': False,
        'image': 'https://images.unsplash.com/photo-1603006905003-be475563bc59?w=400&auto=format&fit=crop',
        'desc': 'Pure Essential Oils Soy Wax Candle | 35 Hours Clean Burn Time | Stress Relief'
    },
    'fitband': {
        'id': 'fitband',
        'name': 'Noise ColorFit Pulse Smart Fitness Band',
        'category': 'Fitness',
        'price': 1799,
        'rating': '4.6 ★ (3.8k)',
        'isHuntItem': True,
        'image': 'https://images.unsplash.com/photo-1575311373937-040b8e1fd5b6?w=400&auto=format&fit=crop',
        'desc': '1.4" HD Display | 24/7 Heart Rate & SpO2 Monitor | 10-Day Battery'
    },
    'proteinshake': {
        'id': 'proteinshake',
        'name': 'Raw Pressery Protein Coffee Shake (250ml)',
        'category': 'Gourmet Drinks',
        'price': 120,
        'rating': '4.8 ★ (1.9k)',
        'isHuntItem': False,
        'image': 'https://images.unsplash.com/photo-1517256064527-09c73fc73e38?w=400&auto=format&fit=crop',
        'desc': '18g Whey Protein | Cold Brewed Espresso Flavor | Zero Added Sugar'
    },
    'facewash': {
        'id': 'facewash',
        'name': 'Garnier Men TurboLight Anti-Pollution Face Wash',
        'category': 'Men\'s Grooming',
        'price': 249,
        'rating': '4.7 ★ (4.2k)',
        'isHuntItem': False,
        'image': 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400&auto=format&fit=crop',
        'desc': 'Charcoal & Clay Deep Cleansing Formula for Urban Dirt & Oil Control'
    },
    'ramen': {
        'id': 'ramen',
        'name': 'Buldak 2x Spicy Korean Instant Ramen (5-pack)',
        'category': 'Quick Meals',
        'price': 575,
        'rating': '4.9 ★ (6.1k)',
        'isHuntItem': True,
        'image': 'https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=400&auto=format&fit=crop',
        'desc': 'Fiery Hot Chicken Flavor Korean Stir-Fried Noodles | Extreme Spice Craving'
    },
    'oliveoil': {
        'id': 'oliveoil',
        'name': 'Borges Extra Virgin Olive Oil (1L)',
        'category': 'Gourmet Pantry',
        'price': 1150,
        'rating': '4.8 ★ (2.1k)',
        'isHuntItem': True,
        'image': 'https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=400&auto=format&fit=crop',
        'desc': 'Cold Pressed First Cold Extraction Spanish Olive Oil for Healthy Cooking'
    },
    'gamepad': {
        'id': 'gamepad',
        'name': 'Zebronics MAX FURY RGB Gamepad',
        'category': 'Gaming',
        'price': 1999,
        'rating': '4.8 ★ (1.2k)',
        'isHuntItem': False,
        'image': 'https://images.unsplash.com/photo-1600080972464-8e5f35f63d08?w=400&auto=format&fit=crop',
        'desc': 'Transparent RGB LED Wired Gamepad | Dual Motor Force Feedback | Ultra-low Latency 1.8m Cable'
    },
    'headphones': {
        'id': 'headphones',
        'name': 'Sony WH-1000XM5 ANC Headphones',
        'category': 'Gaming',
        'price': 29990,
        'rating': '4.9 ★ (3.1k)',
        'isHuntItem': False,
        'image': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400&auto=format&fit=crop',
        'desc': 'Industry Leading Noise Cancellation | 30hr Battery Life | Crystal Clear Hands-free Calls'
    },
    'mouse': {
        'id': 'mouse',
        'name': 'Logitech G305 Wireless Mouse',
        'category': 'Gaming',
        'price': 4295,
        'rating': '4.7 ★ (890)',
        'isHuntItem': False,
        'image': 'https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=400&auto=format&fit=crop',
        'desc': 'LIGHTSPEED Wireless Technology | HERO Sensor 12,000 DPI | 250 Hours Battery Life'
    },
    'apples': {
        'id': 'apples',
        'name': 'Organic Shimla Apples (4 pcs)',
        'category': 'Fresh',
        'price': 189,
        'rating': '4.7 ★ (4.1k)',
        'isHuntItem': False,
        'image': 'https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=400&auto=format&fit=crop',
        'desc': 'Crisp, Juicy, Farm-Fresh High Mountain Shimla Apples (~500g)'
    },
    'avocado': {
        'id': 'avocado',
        'name': 'Fresh Imported Hass Avocado (2 pcs)',
        'category': 'Fresh',
        'price': 260,
        'rating': '4.5 ★ (920)',
        'isHuntItem': False,
        'image': 'https://images.unsplash.com/photo-1523049673857-eb18f1d7b578?w=400&auto=format&fit=crop',
        'desc': 'Nutrient Rich Ready-to-Eat Premium Imported Hass Avocados'
    },
    'cerave': {
        'id': 'cerave',
        'name': 'CeraVe Hydrating Cleanser (236ml)',
        'category': 'Personal',
        'price': 550,
        'rating': '4.8 ★ (2.8k)',
        'isHuntItem': False,
        'image': 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400&auto=format&fit=crop',
        'desc': 'Non-Foaming Face Wash with Essential Ceramides & Hyaluronic Acid'
    },
    'serum': {
        'id': 'serum',
        'name': 'Minimalist 10% Vitamin C Serum',
        'category': 'Personal',
        'price': 699,
        'rating': '4.7 ★ (1.5k)',
        'isHuntItem': False,
        'image': 'https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400&auto=format&fit=crop',
        'desc': 'Glow Boosting Formula with Centella Water & Acetyl Glucosamine (30ml)'
    },
    'pedigree': {
        'id': 'pedigree',
        'name': 'Pedigree Adult Dog Food (3kg)',
        'category': 'Pet Store',
        'price': 920,
        'rating': '4.8 ★ (1.1k)',
        'isHuntItem': False,
        'image': 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=400&auto=format&fit=crop',
        'desc': '100% Complete Nutrition for Adult Dogs | Healthy Coat & Digestion'
    },
    'doritos': {
        'id': 'doritos',
        'name': 'Doritos Nacho Cheese Chips (150g)',
        'category': 'Snacks',
        'price': 90,
        'rating': '4.9 ★ (8.9k)',
        'isHuntItem': False,
        'image': 'https://images.unsplash.com/photo-1566478989037-eec170784d0b?w=400&auto=format&fit=crop',
        'desc': 'Crunchy Tortilla Chips with Bold & Cheesy Nacho Flavor'
    }
}

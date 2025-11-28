"""
Seed data for Hemp Advocacy Dashboard
Sources: USDA NASS, Whitney Economics, Vangst, Census Bureau, MultiState
"""

# National Production Data (USDA NASS National Hemp Report)
PRODUCTION_NATIONAL = [
    # (year, planted_acres, harvested_acres, production_value_usd, hemp_type, source)
    (2023, 27619, 21093, 285000000, 'all', 'USDA NASS'),
    (2024, 45294, 32694, 445000000, 'all', 'USDA NASS'),
    # Floral hemp specifically
    (2023, 7392, 7392, 270000000, 'floral', 'USDA NASS'),
    (2024, 11827, 11827, 386000000, 'floral', 'USDA NASS'),
    # Grain hemp
    (2023, 5500, 5500, 2320000, 'grain', 'USDA NASS'),
    (2024, 4863, 4863, 2620000, 'grain', 'USDA NASS'),
]

# Market Size Metrics
MARKET_METRICS = [
    # (metric_name, year, value, unit, category, source, notes)
    ('US Industrial Hemp Market', 2023, 1630000000, 'USD', 'market_size', 'Grand View Research', None),
    ('US Industrial Hemp Market', 2024, 1960000000, 'USD', 'market_size', 'Grand View Research', 'Projected'),
    ('US Industrial Hemp Market', 2030, 7800000000, 'USD', 'projection', 'Grand View Research', '21.1% CAGR'),
    ('Cannabis Beverages Market', 2023, 1160000000, 'USD', 'market_size', 'Grand View Research', 'Global'),
    ('Cannabis Beverages Market', 2024, 2040000000, 'USD', 'market_size', 'Fortune Business Insights', 'Global'),
    ('Cannabis Beverages Market', 2030, 3860000000, 'USD', 'projection', 'Grand View Research', 'Global, 19.2% CAGR'),
    ('CBD Beverages Market', 2024, 7130000000, 'USD', 'market_size', 'Straits Research', 'Global'),
    ('CBD Beverages Market', 2033, 55470000000, 'USD', 'projection', 'Straits Research', 'Global, 25.6% CAGR'),
    ('US Hemp Production Value', 2023, 318000000, 'USD', 'market_size', 'USDA NASS', None),
    ('US Hemp Production Value', 2024, 445000000, 'USD', 'market_size', 'USDA NASS', '40% YoY growth'),
    ('US Hemp Acreage Growth', 2024, 64, 'percent', 'growth_rate', 'USDA NASS', 'YoY planted acres'),
    ('Floral Hemp Production Growth', 2024, 159, 'percent', 'growth_rate', 'USDA NASS', 'YoY pounds produced'),
    ('North America Market Share', 2024, 55.95, 'percent', 'market_size', 'Grand View Research', 'Of global hemp market'),
]

# Employment Statistics
EMPLOYMENT_STATS = [
    # (geography, year, total_jobs, job_growth_pct, total_wages_usd, sector, source)
    ('US', 2023, 417493, None, None, 'cannabis_all', 'Vangst'),
    ('US', 2024, 440445, 5.4, None, 'cannabis_all', 'Vangst'),
    ('TX', 2023, 50100, None, 1600000000, 'hemp_all', 'Texas Hemp Economic Report'),
    ('TX', 2025, 53300, 6.4, 2100000000, 'hemp_all', 'Texas Hemp Economic Report'),
    ('MI', 2023, None, None, None, 'cannabis_all', 'Vangst'),  # +10,000 jobs added
    ('MO', 2023, None, None, None, 'cannabis_all', 'Vangst'),  # +10,000 jobs added
    ('NY', 2023, None, 2050, None, 'cannabis_all', 'Vangst'),  # Jobs added
    ('NJ', 2023, None, 4870, None, 'cannabis_all', 'Vangst'),  # Jobs added
]

# State Regulatory Status (as of late 2024/2025)
REGULATORY_STATUS = [
    # (state, status, max_thc_serving, max_thc_package, age, notes, source)
    ('AL', 'banned', None, None, None, None, 'MultiState'),
    ('AK', 'legal', 10, None, 21, None, 'MultiState'),
    ('AZ', 'legal_restricted', 10, None, 21, 'No powder or concentrated tinctures', 'MultiState'),
    ('AR', 'banned', None, None, None, 'Court upheld state ban', 'MultiState'),
    ('CA', 'dispensary_only', None, None, 21, 'AB 8 requires dispensary sales', 'MultiState'),
    ('CO', 'legal', 10, 100, 21, None, 'MultiState'),
    ('CT', 'legal_restricted', 5, 50, 21, None, 'MultiState'),
    ('DE', 'legal', 10, None, 21, None, 'MultiState'),
    ('FL', 'legal', 10, None, 21, 'Remote sales regulated', 'MultiState'),
    ('GA', 'legal', 10, None, 21, None, 'MultiState'),
    ('HI', 'legal_restricted', 2.5, None, 21, 'Lower THC limit', 'MultiState'),
    ('ID', 'banned', None, None, None, None, 'MultiState'),
    ('IL', 'pending', None, None, 21, 'Pritzker considering regulation', 'MultiState'),
    ('IN', 'legal', 10, None, 21, None, 'MultiState'),
    ('IA', 'legal_restricted', 4, 10, 21, 'HF-2605 effective July 2024', 'MultiState'),
    ('KS', 'banned', None, None, None, None, 'MultiState'),
    ('KY', 'legal_restricted', 5, None, 21, '2025 legislation enacted', 'MultiState'),
    ('LA', 'legal', 8, None, 21, None, 'MultiState'),
    ('ME', 'legal', 10, None, 21, None, 'MultiState'),
    ('MD', 'legal_restricted', 10, None, 21, '2025 legislation enacted', 'MultiState'),
    ('MA', 'legal', 5, 50, 21, None, 'MultiState'),
    ('MI', 'legal', 10, None, 21, None, 'MultiState'),
    ('MN', 'legal', 5, 50, 21, 'State regulated market', 'MultiState'),
    ('MS', 'legal', 10, None, 21, None, 'MultiState'),
    ('MO', 'legal', 100, None, 21, 'Higher limits allowed', 'MultiState'),
    ('MT', 'legal', 10, None, 21, None, 'MultiState'),
    ('NE', 'legal', 10, None, 21, None, 'MultiState'),
    ('NV', 'legal', 10, 100, 21, None, 'MultiState'),
    ('NH', 'legal', 10, None, 21, None, 'MultiState'),
    ('NJ', 'legal', 10, None, 21, None, 'MultiState'),
    ('NM', 'legal', 10, None, 21, None, 'MultiState'),
    ('NY', 'legal_restricted', 10, None, 21, None, 'MultiState'),
    ('NC', 'legal', 10, None, 21, None, 'MultiState'),
    ('ND', 'legal', 10, None, 21, None, 'MultiState'),
    ('OH', 'pending', 0.42, None, 21, 'Per fluid ounce limit proposed', 'MultiState'),
    ('OK', 'legal', 10, None, 21, None, 'MultiState'),
    ('OR', 'legal', 10, 50, 21, None, 'MultiState'),
    ('PA', 'legal', 10, None, 21, None, 'MultiState'),
    ('RI', 'legal', 10, None, 21, None, 'MultiState'),
    ('SC', 'legal', 10, None, 21, None, 'MultiState'),
    ('SD', 'legal', 10, None, 21, None, 'MultiState'),
    ('TN', 'legal_restricted', 10, None, 21, 'HB 1376 overhaul Jan 2026', 'MultiState'),
    ('TX', 'legal', 10, None, 21, 'TABC regulations proceeding', 'MultiState'),
    ('UT', 'banned', None, None, None, None, 'MultiState'),
    ('VT', 'legal', 5, 50, 21, None, 'MultiState'),
    ('VA', 'legal', 10, None, 21, None, 'MultiState'),
    ('WA', 'legal', 10, 50, 21, None, 'MultiState'),
    ('WV', 'legal', 10, None, 21, None, 'MultiState'),
    ('WI', 'legal', 10, None, 21, None, 'MultiState'),
    ('WY', 'legal', 100, None, 21, 'Higher limits allowed', 'MultiState'),
    ('DC', 'legal', 10, None, 21, None, 'MultiState'),
]

# Tax Revenue by State (Q4 2023/Q1 2024 data from Census Bureau)
TAX_REVENUE = [
    # (state, year, quarter, tax_revenue_usd, pct_of_state_revenue, source)
    ('CA', 2023, 4, 161000000, None, 'Census Bureau'),
    ('WA', 2023, 4, 113400000, 1.37, 'Census Bureau'),
    ('CO', 2023, 4, 61000000, 1.23, 'Census Bureau'),
    ('AK', 2023, 4, 7000000, 1.32, 'Census Bureau'),
    ('MI', 2023, 4, 95000000, None, 'Census Bureau'),
    ('IL', 2023, 4, 85000000, None, 'Census Bureau'),
    ('AZ', 2023, 4, 70000000, None, 'Census Bureau'),
    ('MA', 2023, 4, 65000000, None, 'Census Bureau'),
    ('NV', 2023, 4, 45000000, None, 'Census Bureau'),
    ('OR', 2023, 4, 35000000, None, 'Census Bureau'),
    # National totals
    ('US', 2024, None, 4400000000, None, 'MPP'),
    ('US', 2014, None, 0, None, 'MPP'),
    ('US', 2023, None, 4100000000, None, 'MPP'),
]

# Consumer Trends
CONSUMER_TRENDS = [
    # (metric_name, year, value, unit, demographic, source)
    ('CBD Awareness Rate', 2024, 64, 'percent', 'all_americans', 'Mastermind Behavior'),
    ('CBD Beverage Sales Growth', 2023, 36.5, 'percent', 'all', 'Industry Report'),
    ('Willingness to Pay Premium for Traceable Products', 2024, 70, 'percent', 'millennials_genz', 'Euromonitor'),
    ('Preference for Natural/Organic Products', 2024, 71, 'percent', 'all', 'Euromonitor'),
    ('Gummies Popularity Increase', 2024, 25, 'percent', 'all', 'Brightfield Group'),
    ('Beverage Popularity Increase', 2024, 20, 'percent', 'all', 'Brightfield Group'),
]

# Industry Timeline
INDUSTRY_TIMELINE = [
    # (date, event_type, title, description, impact, source)
    ('2018-12-20', 'legislation', '2018 Farm Bill Signed', 'Hemp legalized federally with <0.3% THC', 'positive', 'Congress.gov'),
    ('2020-03-22', 'regulatory', 'USDA Final Hemp Rule', 'Established federal hemp production framework', 'positive', 'USDA'),
    ('2023-01-01', 'market', 'Hemp THC Beverages Boom', 'THC drinks expand to non-marijuana states', 'positive', 'MJBizDaily'),
    ('2024-04-17', 'market', 'USDA Reports 40% Growth', 'US hemp production value reaches $445M', 'positive', 'USDA NASS'),
    ('2024-06-01', 'market', 'Major Brands Enter Market', 'Snoop Dogg, Death Row Records launch THC beverages', 'positive', 'Industry Press'),
    ('2024-09-01', 'regulatory', 'California Emergency Rules', 'CA bans hemp THC in food/beverage outside dispensaries', 'negative', 'CA DPH'),
    ('2024-12-01', 'legislation', 'Germany Legalizes Hemp', 'Consumer Cannabis Act creates regulated hemp market', 'positive', 'German Government'),
    ('2025-05-22', 'regulatory', 'Tennessee Overhaul', 'HB 1376 moves hemp to Alcoholic Beverage Commission', 'neutral', 'TN Legislature'),
    ('2025-06-01', 'legislation', 'Texas SB 3 Vetoed', 'Governor Abbott vetoes hemp THC ban', 'positive', 'TX Tribune'),
    ('2025-11-01', 'legislation', 'Federal Hemp Restriction', 'New law caps THC at 0.4mg/serving by Nov 2026', 'negative', 'NPR'),
]

# Summary stats for hero metrics
HERO_METRICS = {
    'production_value_2024': 445000000,
    'production_growth_yoy': 40,
    'planted_acres_2024': 45294,
    'acres_growth_yoy': 64,
    'total_jobs': 440445,
    'job_growth_yoy': 5.4,
    'state_tax_revenue_2024': 4400000000,
    'states_legal': 28,
    'states_restricted': 9,
    'states_banned': 6,
}

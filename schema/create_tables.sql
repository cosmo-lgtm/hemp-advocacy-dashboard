-- Hemp Advocacy Dashboard - BigQuery Schema
-- Dataset: hemp_advocacy (isolated for potential public sharing)

-- 1. USDA Hemp Production by State and Year
CREATE TABLE IF NOT EXISTS `artful-logic-475116-p1.hemp_advocacy.production_by_state` (
  state STRING NOT NULL,
  year INT64 NOT NULL,
  planted_acres INT64,
  harvested_acres INT64,
  production_lbs INT64,
  yield_lbs_per_acre FLOAT64,
  production_value_usd INT64,
  num_operations INT64,
  hemp_type STRING,  -- 'floral', 'grain', 'fiber', 'seed'
  source STRING,
  last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

-- 2. National Market Metrics Over Time
CREATE TABLE IF NOT EXISTS `artful-logic-475116-p1.hemp_advocacy.market_metrics` (
  metric_name STRING NOT NULL,
  year INT64 NOT NULL,
  value FLOAT64 NOT NULL,
  unit STRING,
  category STRING,  -- 'market_size', 'growth_rate', 'projection'
  source STRING,
  notes STRING,
  last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

-- 3. Employment Statistics
CREATE TABLE IF NOT EXISTS `artful-logic-475116-p1.hemp_advocacy.employment_stats` (
  geography STRING NOT NULL,  -- 'US', state code, or region
  year INT64 NOT NULL,
  total_jobs INT64,
  job_growth_pct FLOAT64,
  total_wages_usd INT64,
  sector STRING,  -- 'cultivation', 'processing', 'retail', 'all'
  source STRING,
  last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

-- 4. State Regulatory Status
CREATE TABLE IF NOT EXISTS `artful-logic-475116-p1.hemp_advocacy.regulatory_status` (
  state STRING NOT NULL,
  thc_beverage_status STRING,  -- 'legal', 'legal_restricted', 'dispensary_only', 'banned', 'pending'
  max_thc_mg_per_serving FLOAT64,
  max_thc_mg_per_package FLOAT64,
  age_restriction INT64,
  effective_date DATE,
  notes STRING,
  source STRING,
  last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

-- 5. Consumer Trends & Demand Indicators
CREATE TABLE IF NOT EXISTS `artful-logic-475116-p1.hemp_advocacy.consumer_trends` (
  metric_name STRING NOT NULL,
  year INT64 NOT NULL,
  value FLOAT64 NOT NULL,
  unit STRING,
  demographic STRING,  -- 'all', 'millennials', 'gen_z', etc.
  source STRING,
  last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

-- 6. Tax Revenue by State (Cannabis/Hemp Combined where available)
CREATE TABLE IF NOT EXISTS `artful-logic-475116-p1.hemp_advocacy.tax_revenue` (
  state STRING NOT NULL,
  year INT64 NOT NULL,
  quarter INT64,
  tax_revenue_usd INT64,
  pct_of_state_revenue FLOAT64,
  source STRING,
  last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

-- 7. Timeline / Milestones
CREATE TABLE IF NOT EXISTS `artful-logic-475116-p1.hemp_advocacy.industry_timeline` (
  event_date DATE NOT NULL,
  event_type STRING,  -- 'legislation', 'regulatory', 'market', 'milestone'
  title STRING NOT NULL,
  description STRING,
  impact STRING,  -- 'positive', 'negative', 'neutral'
  source STRING
);

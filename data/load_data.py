#!/usr/bin/env python3
"""
Load seed data into BigQuery hemp_advocacy dataset
"""
from google.cloud import bigquery
from datetime import datetime
from seed_data import (
    PRODUCTION_NATIONAL,
    MARKET_METRICS,
    EMPLOYMENT_STATS,
    REGULATORY_STATUS,
    TAX_REVENUE,
    CONSUMER_TRENDS,
    INDUSTRY_TIMELINE
)

PROJECT_ID = "artful-logic-475116-p1"
DATASET_ID = "hemp_advocacy"

client = bigquery.Client(project=PROJECT_ID)

def load_production_data():
    """Load national production data"""
    table_id = f"{PROJECT_ID}.{DATASET_ID}.production_by_state"
    rows = []
    for year, planted, harvested, value, hemp_type, source in PRODUCTION_NATIONAL:
        rows.append({
            "state": "US",
            "year": year,
            "planted_acres": planted,
            "harvested_acres": harvested,
            "production_value_usd": value,
            "hemp_type": hemp_type,
            "source": source,
        })

    errors = client.insert_rows_json(table_id, rows)
    if errors:
        print(f"Errors loading production data: {errors}")
    else:
        print(f"Loaded {len(rows)} production records")

def load_market_metrics():
    """Load market metrics"""
    table_id = f"{PROJECT_ID}.{DATASET_ID}.market_metrics"
    rows = []
    for name, year, value, unit, category, source, notes in MARKET_METRICS:
        rows.append({
            "metric_name": name,
            "year": year,
            "value": float(value),
            "unit": unit,
            "category": category,
            "source": source,
            "notes": notes,
        })

    errors = client.insert_rows_json(table_id, rows)
    if errors:
        print(f"Errors loading market metrics: {errors}")
    else:
        print(f"Loaded {len(rows)} market metric records")

def load_employment_stats():
    """Load employment statistics"""
    table_id = f"{PROJECT_ID}.{DATASET_ID}.employment_stats"
    rows = []
    for geo, year, jobs, growth, wages, sector, source in EMPLOYMENT_STATS:
        rows.append({
            "geography": geo,
            "year": year,
            "total_jobs": jobs,
            "job_growth_pct": growth,
            "total_wages_usd": wages,
            "sector": sector,
            "source": source,
        })

    errors = client.insert_rows_json(table_id, rows)
    if errors:
        print(f"Errors loading employment stats: {errors}")
    else:
        print(f"Loaded {len(rows)} employment records")

def load_regulatory_status():
    """Load state regulatory status"""
    table_id = f"{PROJECT_ID}.{DATASET_ID}.regulatory_status"
    rows = []
    for state, status, max_serv, max_pkg, age, notes, source in REGULATORY_STATUS:
        rows.append({
            "state": state,
            "thc_beverage_status": status,
            "max_thc_mg_per_serving": max_serv,
            "max_thc_mg_per_package": max_pkg,
            "age_restriction": age,
            "notes": notes,
            "source": source,
        })

    errors = client.insert_rows_json(table_id, rows)
    if errors:
        print(f"Errors loading regulatory status: {errors}")
    else:
        print(f"Loaded {len(rows)} regulatory records")

def load_tax_revenue():
    """Load tax revenue data"""
    table_id = f"{PROJECT_ID}.{DATASET_ID}.tax_revenue"
    rows = []
    for state, year, quarter, revenue, pct, source in TAX_REVENUE:
        rows.append({
            "state": state,
            "year": year,
            "quarter": quarter,
            "tax_revenue_usd": revenue,
            "pct_of_state_revenue": pct,
            "source": source,
        })

    errors = client.insert_rows_json(table_id, rows)
    if errors:
        print(f"Errors loading tax revenue: {errors}")
    else:
        print(f"Loaded {len(rows)} tax revenue records")

def load_consumer_trends():
    """Load consumer trends data"""
    table_id = f"{PROJECT_ID}.{DATASET_ID}.consumer_trends"
    rows = []
    for name, year, value, unit, demo, source in CONSUMER_TRENDS:
        rows.append({
            "metric_name": name,
            "year": year,
            "value": float(value),
            "unit": unit,
            "demographic": demo,
            "source": source,
        })

    errors = client.insert_rows_json(table_id, rows)
    if errors:
        print(f"Errors loading consumer trends: {errors}")
    else:
        print(f"Loaded {len(rows)} consumer trend records")

def load_industry_timeline():
    """Load industry timeline events"""
    table_id = f"{PROJECT_ID}.{DATASET_ID}.industry_timeline"
    rows = []
    for date, event_type, title, desc, impact, source in INDUSTRY_TIMELINE:
        rows.append({
            "event_date": date,
            "event_type": event_type,
            "title": title,
            "description": desc,
            "impact": impact,
            "source": source,
        })

    errors = client.insert_rows_json(table_id, rows)
    if errors:
        print(f"Errors loading timeline: {errors}")
    else:
        print(f"Loaded {len(rows)} timeline records")

if __name__ == "__main__":
    print("Loading hemp advocacy data into BigQuery...")
    load_production_data()
    load_market_metrics()
    load_employment_stats()
    load_regulatory_status()
    load_tax_revenue()
    load_consumer_trends()
    load_industry_timeline()
    print("Done!")

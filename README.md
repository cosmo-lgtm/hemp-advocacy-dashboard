# Hemp Industry Economic Impact Dashboard

A professional, data-driven Streamlit dashboard showcasing the economic impact of the hemp-derived THC beverage industry. Designed for stakeholders and policymakers.

## Purpose

Present factual, publicly-sourced data demonstrating:
- Economic contributions (jobs, wages, tax revenue)
- Market growth and consumer demand
- Agricultural benefits (acreage, farmers, rural economy)
- State regulatory landscape
- Industry trajectory since 2018 Farm Bill

## Data Sources

All data is publicly available and cited:
- **USDA NASS** - National Hemp Report (production, acreage, values)
- **Census Bureau** - Cannabis excise tax collections
- **Industry Reports** - Brightfield Group, Whitney Economics, Vangst
- **Legislative Trackers** - MultiState, Vicente LLP

## Architecture

```
BigQuery Dataset: hemp_advocacy (isolated for potential public sharing)
├── production_by_state      # USDA acreage, yield, value by state/year
├── market_metrics           # Market size, growth rates, projections
├── employment_stats         # Jobs, wages, employment by sector
├── regulatory_status        # State-by-state legal status
└── consumer_trends          # Demand indicators, survey data
```

## Deployment

- **Streamlit Cloud** for public access
- **BigQuery** backend (read-only service account for dashboard)
- **Scheduled refresh** via Cloud Scheduler

## Key Metrics Highlighted

1. **$445M** - 2024 U.S. hemp production value (+40% YoY)
2. **45,294 acres** - 2024 planted acreage (+64% YoY)
3. **440,000+** jobs in cannabis/hemp sector
4. **$4.4B** - 2024 state cannabis tax revenue
5. **28 states** - Legal THC beverage sales

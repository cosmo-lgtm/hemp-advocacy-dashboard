# Hemp Industry Economic Impact Dashboard

A data-driven advocacy tool presenting economic impact data on the hemp-derived THC beverage industry for policymakers and stakeholders.

**Live URL:** https://hemp-advocacy-dashboard.streamlit.app (private access)

## Purpose

This dashboard consolidates publicly available data to demonstrate:
- Economic contribution of the hemp industry (jobs, tax revenue, production value)
- Market growth trajectory and segment breakdown
- State-by-state regulatory landscape for THC beverages
- Consumer demand patterns across demographics

Intended audience: Lawmakers, regulators, and stakeholders evaluating hemp industry policy.

## Data Sources

| Source | Data Type | Update Frequency |
|--------|-----------|------------------|
| USDA NASS | Hemp production, acreage, farm operations | Annual |
| U.S. Census Bureau | Employment statistics | Annual |
| Vangst Jobs Report | Cannabis/hemp industry employment | Annual |
| Grand View Research | Market projections, CAGR | Periodic |
| MultiState Insider | State regulatory status | Quarterly |
| Vicente LLP | THC beverage legal status by state | Quarterly |
| MPP (Marijuana Policy Project) | State tax revenue data | Quarterly |
| Mastermind Behavior | Consumer awareness surveys | Annual |
| Euromonitor | Beverage market trends | Annual |

## Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Streamlit App  │────▶│    BigQuery     │────▶│   Data Tables   │
│  (Frontend)     │     │   (Warehouse)   │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
        │                                               │
        ▼                                               ▼
┌─────────────────┐                           ┌─────────────────┐
│ Streamlit Cloud │                           │  hemp_advocacy  │
│   (Hosting)     │                           │    dataset      │
└─────────────────┘                           └─────────────────┘
```

### BigQuery Dataset

**Project:** `artful-logic-475116-p1`  
**Dataset:** `hemp_advocacy`

#### Tables

| Table | Description | Key Fields |
|-------|-------------|------------|
| `production_by_state` | USDA hemp production data | year, state, hemp_type, acres_planted, production_value_usd |
| `market_metrics` | Market size and projections | year, metric_name, value, cagr |
| `employment_stats` | Industry job numbers | year, geography, total_jobs, yoy_growth |
| `regulatory_status` | State THC beverage laws | state, thc_beverage_status, max_thc_mg, age_requirement |
| `tax_revenue` | State cannabis/hemp tax data | year, quarter, state, tax_revenue_usd |
| `consumer_trends` | Awareness and preference data | year, metric_name, value, demographic |
| `industry_timeline` | Key legislative/industry events | event_date, title, description, impact |

## Visualizations

### Chart Types Used

1. **Sankey Diagram** - Industry value chain flow (Production → Processing → Products → Retail)
2. **Donut Chart** - Market segment breakdown with center annotation
3. **Area Chart** - Market growth trajectory 2023-2030
4. **Choropleth Map** - State regulatory status (color-coded by legal status)
5. **Funnel Chart** - Employment breakdown by category
6. **Treemap** - State tax revenue distribution
7. **Radar Chart** - Consumer segment analysis (Gen Z vs Millennials vs Gen X)
8. **Timeline** - Key industry events with impact indicators

### Design System

- **Theme:** Dark mode with glassmorphism effects
- **Primary Color:** Emerald green (`#10b981`)
- **Font:** Space Grotesk
- **Background:** Gradient (`#0a0a0a` → `#1a1a2e`)

## Local Development

### Prerequisites

- Python 3.11
- Google Cloud service account with BigQuery access

### Setup

```bash
cd dashboards/hemp-advocacy

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up credentials (for local dev)
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json

# Run locally
streamlit run app.py
```

### Project Structure

```
hemp-advocacy/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── runtime.txt            # Python version for deployment
├── .python-version        # pyenv version
├── .streamlit/
│   └── config.toml        # Streamlit configuration
├── data/
│   ├── seed_data.py       # Research data with source citations
│   └── load_data.py       # BigQuery data loader script
└── README.md              # This file
```

## Deployment

### Streamlit Cloud

1. Repository: https://github.com/cosmo-lgtm/hemp-advocacy-dashboard
2. Branch: `main`
3. Main file: `app.py`

### Secrets Configuration

In Streamlit Cloud (Settings → Secrets), add:

```toml
[gcp_service_account]
type = "service_account"
project_id = "artful-logic-475116-p1"
private_key_id = "..."
private_key = """-----BEGIN PRIVATE KEY-----
...actual key with real newlines...
-----END PRIVATE KEY-----
"""
client_email = "..."
client_id = "..."
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "..."
```

**Important:** The `private_key` must use triple quotes with actual newlines, not `\n` escape sequences.

## Data Refresh

Data is currently static (seeded from research). To update:

1. Update `data/seed_data.py` with new research
2. Run `python data/load_data.py` to reload BigQuery tables
3. Dashboard auto-refreshes (1-hour cache TTL)

## Key Metrics Displayed

| Metric | Value | Source |
|--------|-------|--------|
| U.S. Hemp Production Value | $445M (2024) | USDA NASS |
| Industry Jobs | 440,000+ | Vangst 2024 |
| State Tax Revenue | $4.4B (2024) | MPP Analysis |
| Acres Planted | 45,294 | USDA NASS |
| Market CAGR | 21.1% | Grand View Research |
| Projected Market (2030) | $7.8B | Grand View Research |
| States with Legal THC Beverages | 28 | Vicente LLP |

## Regulatory Status Categories

| Status | Color | Description |
|--------|-------|-------------|
| Legal | Green | THC beverages permitted with standard regulations |
| Legal Restricted | Light Green | Legal with additional restrictions |
| Pending | Yellow | Legislation in progress |
| Dispensary Only | Orange | Only available through licensed dispensaries |
| Banned | Red | THC beverages prohibited |

## Future Enhancements

- [ ] Add real-time data feeds from public APIs
- [ ] Include state-level drill-down views
- [ ] Add comparison tools (state vs state)
- [ ] Export functionality for presentations
- [ ] Embed capability for external sites

## Contact

Dashboard maintained by Disruptive Beverages team.

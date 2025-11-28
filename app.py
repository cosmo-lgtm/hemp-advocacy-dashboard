"""
Hemp Industry Economic Impact Dashboard
A data-driven resource for stakeholders and policymakers
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from google.cloud import bigquery
from google.oauth2 import service_account

# Page config
st.set_page_config(
    page_title="Hemp Industry Economic Impact",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional, infographic-style design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .metric-card {
        background: linear-gradient(135deg, #1a472a 0%, #2d5a3d 100%);
        border-radius: 12px;
        padding: 24px;
        text-align: center;
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .metric-value { font-size: 2.5rem; font-weight: 700; margin-bottom: 4px; }
    .metric-label { font-size: 0.9rem; opacity: 0.9; text-transform: uppercase; letter-spacing: 0.5px; }
    .metric-change { font-size: 0.85rem; color: #90EE90; margin-top: 8px; }
    .section-header {
        font-size: 1.5rem; font-weight: 600; color: #1a472a;
        border-bottom: 3px solid #2d5a3d; padding-bottom: 8px; margin: 32px 0 16px 0;
    }
    .source-citation { font-size: 0.75rem; color: #666; font-style: italic; margin-top: 8px; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Initialize BigQuery client
@st.cache_resource
def get_bq_client():
    credentials = service_account.Credentials.from_service_account_info(
        dict(st.secrets["gcp_service_account"])
    )
    return bigquery.Client(credentials=credentials, project="artful-logic-475116-p1")

@st.cache_data(ttl=3600)
def load_data(query):
    client = get_bq_client()
    return client.query(query).to_dataframe()

# Load all data
@st.cache_data(ttl=3600)
def load_all_data():
    data = {}
    data['production'] = load_data("SELECT * FROM `artful-logic-475116-p1.hemp_advocacy.production_by_state` ORDER BY year, hemp_type")
    data['market'] = load_data("SELECT * FROM `artful-logic-475116-p1.hemp_advocacy.market_metrics` ORDER BY year")
    data['employment'] = load_data("SELECT * FROM `artful-logic-475116-p1.hemp_advocacy.employment_stats` ORDER BY year")
    data['regulatory'] = load_data("SELECT * FROM `artful-logic-475116-p1.hemp_advocacy.regulatory_status` ORDER BY state")
    data['tax'] = load_data("SELECT * FROM `artful-logic-475116-p1.hemp_advocacy.tax_revenue` ORDER BY year, state")
    data['timeline'] = load_data("SELECT * FROM `artful-logic-475116-p1.hemp_advocacy.industry_timeline` ORDER BY event_date")
    return data

data = load_all_data()

# HEADER
st.markdown("""
<div style="text-align: center; padding: 20px 0 30px 0;">
    <h1 style="color: #1a472a; font-size: 2.5rem; margin-bottom: 8px;">Hemp Industry Economic Impact</h1>
    <p style="color: #666; font-size: 1.1rem; max-width: 800px; margin: 0 auto;">
        Data-driven insights on jobs, economic growth, and consumer choice in the hemp-derived products sector
    </p>
</div>
""", unsafe_allow_html=True)

# HERO METRICS
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="metric-card"><div class="metric-value">$445M</div><div class="metric-label">2024 Production Value</div><div class="metric-change">↑ 40% from 2023</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><div class="metric-value">440K+</div><div class="metric-label">Jobs Supported</div><div class="metric-change">↑ 5.4% YoY growth</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card"><div class="metric-value">$4.4B</div><div class="metric-label">State Tax Revenue</div><div class="metric-change">2024 Collections</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="metric-card"><div class="metric-value">45,294</div><div class="metric-label">Acres Planted</div><div class="metric-change">↑ 64% from 2023</div></div>', unsafe_allow_html=True)

st.markdown("<p class='source-citation'>Sources: USDA NASS National Hemp Report 2025, Vangst Jobs Report 2024, MPP Tax Revenue Analysis</p>", unsafe_allow_html=True)

# MARKET GROWTH
st.markdown("<div class='section-header'>Market Growth & Projections</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    prod_df = data['production'][data['production']['hemp_type'] == 'all'].copy()
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=prod_df['year'], y=prod_df['production_value_usd'] / 1_000_000,
        marker_color=['#2d5a3d', '#1a472a'],
        text=[f"${v/1_000_000:.0f}M" for v in prod_df['production_value_usd']],
        textposition='outside', textfont=dict(size=14, color='#1a472a')
    ))
    fig.update_layout(title="U.S. Hemp Production Value", xaxis_title="Year", yaxis_title="Value ($ Millions)",
                      showlegend=False, plot_bgcolor='white', height=350, yaxis=dict(gridcolor='#eee'))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("<p class='source-citation'>Source: USDA NASS National Hemp Report</p>", unsafe_allow_html=True)

with col2:
    hemp_market = data['market'][data['market']['metric_name'] == 'US Industrial Hemp Market']
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=hemp_market['year'], y=hemp_market['value'] / 1_000_000_000,
        mode='lines+markers', name='US Hemp Market',
        line=dict(color='#1a472a', width=3), marker=dict(size=10)
    ))
    fig.update_layout(title="U.S. Industrial Hemp Market Trajectory", xaxis_title="Year", yaxis_title="Market Size ($ Billions)",
                      showlegend=True, plot_bgcolor='white', height=350, yaxis=dict(gridcolor='#eee'))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("<p class='source-citation'>Source: Grand View Research, CAGR 21.1%</p>", unsafe_allow_html=True)

# REGULATORY MAP
st.markdown("<div class='section-header'>State Regulatory Landscape</div>", unsafe_allow_html=True)
status_counts = data['regulatory']['thc_beverage_status'].value_counts()
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.markdown("### Status Summary")
    status_colors = {'legal': '#2d5a3d', 'legal_restricted': '#6b8e23', 'pending': '#daa520', 'dispensary_only': '#cd853f', 'banned': '#8b0000'}
    for status, count in status_counts.items():
        color = status_colors.get(status, '#666')
        label = status.replace('_', ' ').title()
        st.markdown(f'<div style="display: flex; align-items: center; margin: 8px 0;"><div style="width: 16px; height: 16px; background: {color}; border-radius: 4px; margin-right: 8px;"></div><span><strong>{count}</strong> states - {label}</span></div>', unsafe_allow_html=True)

with col2:
    reg_df = data['regulatory'].copy()
    status_map = {'legal': 4, 'legal_restricted': 3, 'pending': 2, 'dispensary_only': 1, 'banned': 0}
    reg_df['status_num'] = reg_df['thc_beverage_status'].map(status_map)
    fig = go.Figure(data=go.Choropleth(
        locations=reg_df['state'], z=reg_df['status_num'], locationmode='USA-states',
        colorscale=[[0, '#8b0000'], [0.25, '#cd853f'], [0.5, '#daa520'], [0.75, '#6b8e23'], [1, '#2d5a3d']],
        showscale=False, hovertemplate="<b>%{location}</b><br>%{text}<extra></extra>",
        text=reg_df['thc_beverage_status'].str.replace('_', ' ').str.title()
    ))
    fig.update_layout(geo=dict(scope='usa', projection=dict(type='albers usa'), showlakes=False, bgcolor='rgba(0,0,0,0)'),
                      margin=dict(l=0, r=0, t=0, b=0), height=400)
    st.plotly_chart(fig, use_container_width=True)

with col3:
    st.markdown("### Key Observations")
    st.markdown("- **28 states** have legal THC beverage sales\n- **Age 21+** requirement universal\n- **5-10mg** typical serving limit\n- Active regulation in **27+ states**")

st.markdown("<p class='source-citation'>Source: MultiState Insider, Vicente LLP (as of November 2025)</p>", unsafe_allow_html=True)

# JOBS & ECONOMIC IMPACT
st.markdown("<div class='section-header'>Employment & Economic Contribution</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    emp_us = data['employment'][data['employment']['geography'] == 'US'].copy()
    fig = go.Figure()
    fig.add_trace(go.Bar(x=emp_us['year'], y=emp_us['total_jobs'] / 1000, marker_color='#2d5a3d',
                         text=[f"{v/1000:.0f}K" for v in emp_us['total_jobs']], textposition='outside'))
    fig.update_layout(title="U.S. Cannabis/Hemp Industry Employment", xaxis_title="Year", yaxis_title="Jobs (Thousands)",
                      showlegend=False, plot_bgcolor='white', height=350, yaxis=dict(gridcolor='#eee'))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("<p class='source-citation'>Source: Vangst 2024 Jobs Report</p>", unsafe_allow_html=True)

with col2:
    tax_states = data['tax'][(data['tax']['state'] != 'US') & (data['tax']['year'] == 2023) & (data['tax']['quarter'] == 4)].nlargest(8, 'tax_revenue_usd')
    fig = go.Figure()
    fig.add_trace(go.Bar(y=tax_states['state'], x=tax_states['tax_revenue_usd'] / 1_000_000, orientation='h',
                         marker_color='#1a472a', text=[f"${v/1_000_000:.0f}M" for v in tax_states['tax_revenue_usd']], textposition='outside'))
    fig.update_layout(title="Quarterly State Tax Revenue (Q4 2023)", xaxis_title="Tax Revenue ($ Millions)", yaxis_title="",
                      showlegend=False, plot_bgcolor='white', height=350, yaxis=dict(autorange="reversed"), xaxis=dict(gridcolor='#eee'))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("<p class='source-citation'>Source: U.S. Census Bureau</p>", unsafe_allow_html=True)

# CONSUMER DEMAND
st.markdown("<div class='section-header'>Consumer Demand Indicators</div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div style="background: #f8f9fa; padding: 24px; border-radius: 12px; text-align: center;"><div style="font-size: 3rem; font-weight: 700; color: #1a472a;">64%</div><div style="color: #666;">of Americans are familiar with CBD products</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div style="background: #f8f9fa; padding: 24px; border-radius: 12px; text-align: center;"><div style="font-size: 3rem; font-weight: 700; color: #1a472a;">36.5%</div><div style="color: #666;">CBD beverage sales growth in 2023</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div style="background: #f8f9fa; padding: 24px; border-radius: 12px; text-align: center;"><div style="font-size: 3rem; font-weight: 700; color: #1a472a;">70%</div><div style="color: #666;">Millennials/Gen Z willing to pay premium for traceable products</div></div>', unsafe_allow_html=True)
st.markdown("<p class='source-citation'>Sources: Mastermind Behavior, Euromonitor, Industry Reports</p>", unsafe_allow_html=True)

# TIMELINE
st.markdown("<div class='section-header'>Industry Milestones</div>", unsafe_allow_html=True)
timeline_df = data['timeline'].sort_values('event_date')
for _, row in timeline_df.iterrows():
    impact_color = {'positive': '#2d5a3d', 'negative': '#8b0000', 'neutral': '#666'}.get(row['impact'], '#666')
    st.markdown(f'<div style="display: flex; margin: 12px 0; padding: 12px; background: #f8f9fa; border-radius: 8px; border-left: 4px solid {impact_color};"><div style="min-width: 100px; font-weight: 600; color: #666;">{row["event_date"].strftime("%b %Y")}</div><div><div style="font-weight: 600; color: #1a472a;">{row["title"]}</div><div style="color: #666; font-size: 0.9rem;">{row["description"]}</div></div></div>', unsafe_allow_html=True)

# KEY TAKEAWAYS
st.markdown("<div class='section-header'>Key Takeaways for Policymakers</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
### Economic Impact
- **$445 million** in U.S. hemp production value (2024)
- **$4.4 billion** in state tax revenue generated
- **440,000+ jobs** supported across the industry
- **40%+ annual growth** in production value

### Agricultural Benefits
- **45,294 acres** under cultivation
- **8,153 farming operations** surveyed
- Diversification opportunity for rural economies
- Crop insurance and USDA programs accessible
""")
with col2:
    st.markdown("""
### Consumer Choice
- **28 states** with legal THC beverage markets
- Strong consumer demand and awareness
- Preference for regulated, traceable products
- Age-restricted (21+) across all legal markets

### Regulatory Considerations
- Responsible state frameworks emerging
- Serving limits (typically 5-10mg) protect consumers
- Industry supports sensible regulation
- Clear labeling and testing requirements in place
""")

# FOOTER
st.markdown("---")
st.markdown('<div style="text-align: center; color: #666; padding: 20px;"><p><strong>Data Sources:</strong> USDA NASS, U.S. Census Bureau, Vangst, Grand View Research, MultiState, Vicente LLP, Whitney Economics</p><p style="font-size: 0.8rem;">Last updated: November 2025 | Data refreshed quarterly from public sources</p></div>', unsafe_allow_html=True)

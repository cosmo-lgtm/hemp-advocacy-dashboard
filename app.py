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

# Modern dark mode CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap');

    /* Global dark theme */
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #0f0f1a 100%);
    }

    html, body, [class*="css"] {
        font-family: 'Space Grotesk', sans-serif;
        color: #e0e0e0;
    }

    /* Glassmorphism metric cards */
    .metric-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 28px;
        text-align: center;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, #10b981, #34d399, #6ee7b7);
    }
    .metric-card:hover {
        transform: translateY(-4px);
        border-color: rgba(16, 185, 129, 0.3);
        box-shadow: 0 20px 40px rgba(16, 185, 129, 0.1);
    }
    .metric-value {
        font-size: 2.8rem;
        font-weight: 700;
        background: linear-gradient(135deg, #10b981 0%, #34d399 50%, #6ee7b7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 8px;
    }
    .metric-label {
        font-size: 0.85rem;
        color: #9ca3af;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-weight: 500;
    }
    .metric-change {
        font-size: 0.8rem;
        color: #10b981;
        margin-top: 12px;
        display: inline-flex;
        align-items: center;
        gap: 4px;
        background: rgba(16, 185, 129, 0.1);
        padding: 4px 12px;
        border-radius: 20px;
    }

    /* Section headers */
    .section-header {
        font-size: 1.4rem;
        font-weight: 600;
        color: #f3f4f6;
        padding-bottom: 12px;
        margin: 48px 0 24px 0;
        position: relative;
        display: inline-block;
    }
    .section-header::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 60px;
        height: 3px;
        background: linear-gradient(90deg, #10b981, transparent);
        border-radius: 2px;
    }

    /* Source citations */
    .source-citation {
        font-size: 0.7rem;
        color: #6b7280;
        margin-top: 12px;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Stat cards */
    .stat-card {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 32px;
        text-align: center;
    }
    .stat-value {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #10b981, #34d399);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .stat-label {
        color: #9ca3af;
        font-size: 0.9rem;
        margin-top: 8px;
        line-height: 1.5;
    }

    /* Timeline items */
    .timeline-item {
        display: flex;
        margin: 16px 0;
        padding: 20px;
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        transition: all 0.2s ease;
    }
    .timeline-item:hover {
        background: rgba(255, 255, 255, 0.04);
        border-color: rgba(16, 185, 129, 0.2);
    }
    .timeline-date {
        min-width: 100px;
        font-weight: 600;
        color: #6b7280;
        font-size: 0.85rem;
    }
    .timeline-title {
        font-weight: 600;
        color: #f3f4f6;
        margin-bottom: 4px;
    }
    .timeline-desc {
        color: #9ca3af;
        font-size: 0.85rem;
    }

    /* Key points */
    .key-section h3 {
        color: #10b981;
        font-size: 1.1rem;
        margin-bottom: 16px;
    }
    .key-section ul {
        list-style: none;
        padding: 0;
    }
    .key-section li {
        padding: 8px 0;
        color: #d1d5db;
        border-bottom: 1px solid rgba(255,255,255,0.05);
    }
    .key-section li:last-child {
        border-bottom: none;
    }

    /* Status legend */
    .status-item {
        display: flex;
        align-items: center;
        margin: 10px 0;
        padding: 8px 12px;
        background: rgba(255,255,255,0.02);
        border-radius: 8px;
    }
    .status-dot {
        width: 12px;
        height: 12px;
        border-radius: 50%;
        margin-right: 12px;
    }
    .status-text {
        color: #d1d5db;
        font-size: 0.9rem;
    }
    .status-count {
        font-weight: 700;
        color: #f3f4f6;
    }

    /* Observations */
    .obs-card {
        background: rgba(16, 185, 129, 0.05);
        border: 1px solid rgba(16, 185, 129, 0.1);
        border-radius: 12px;
        padding: 20px;
    }
    .obs-card h3 {
        color: #10b981;
        font-size: 1rem;
        margin-bottom: 12px;
    }
    .obs-card ul {
        margin: 0;
        padding-left: 20px;
    }
    .obs-card li {
        color: #d1d5db;
        padding: 4px 0;
        font-size: 0.9rem;
    }
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

# Dark theme for plotly
dark_template = dict(
    layout=dict(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#9ca3af', family='Space Grotesk'),
        title=dict(font=dict(color='#f3f4f6', size=16)),
        xaxis=dict(gridcolor='rgba(255,255,255,0.05)', zerolinecolor='rgba(255,255,255,0.05)'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.05)', zerolinecolor='rgba(255,255,255,0.05)'),
    )
)

# HEADER
st.markdown("""
<div style="text-align: center; padding: 40px 0 50px 0;">
    <p style="color: #10b981; font-size: 0.85rem; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 16px;">Economic Impact Report</p>
    <h1 style="color: #f3f4f6; font-size: 3rem; font-weight: 700; margin-bottom: 16px; line-height: 1.2;">
        Hemp Industry<br/><span style="background: linear-gradient(135deg, #10b981, #34d399); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">by the Numbers</span>
    </h1>
    <p style="color: #6b7280; font-size: 1rem; max-width: 600px; margin: 0 auto;">
        Data-driven insights on jobs, growth, and consumer choice in the hemp-derived products sector
    </p>
</div>
""", unsafe_allow_html=True)

# HERO METRICS
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="metric-card"><div class="metric-value">$445M</div><div class="metric-label">Production Value</div><div class="metric-change">↑ 40% YoY</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><div class="metric-value">440K+</div><div class="metric-label">Jobs Created</div><div class="metric-change">↑ 5.4% YoY</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card"><div class="metric-value">$4.4B</div><div class="metric-label">Tax Revenue</div><div class="metric-change">2024 Total</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="metric-card"><div class="metric-value">45.3K</div><div class="metric-label">Acres Planted</div><div class="metric-change">↑ 64% YoY</div></div>', unsafe_allow_html=True)

st.markdown("<p class='source-citation' style='text-align:center; margin-top: 24px;'>Sources: USDA NASS 2025, Vangst Jobs Report, MPP Tax Revenue Analysis</p>", unsafe_allow_html=True)

# MARKET GROWTH
st.markdown("<div class='section-header'>Market Growth</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    prod_df = data['production'][data['production']['hemp_type'] == 'all'].copy()
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=prod_df['year'],
        y=prod_df['production_value_usd'] / 1_000_000,
        marker=dict(
            color=['#059669', '#10b981'],
            line=dict(width=0)
        ),
        text=[f"${v/1_000_000:.0f}M" for v in prod_df['production_value_usd']],
        textposition='outside',
        textfont=dict(size=14, color='#10b981')
    ))
    fig.update_layout(
        title="U.S. Hemp Production Value",
        xaxis_title="", yaxis_title="",
        showlegend=False, height=380,
        **dark_template['layout'],
        yaxis=dict(gridcolor='rgba(255,255,255,0.03)', tickformat='$,.0f', ticksuffix='M'),
        xaxis=dict(tickmode='array', tickvals=[2023, 2024])
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    hemp_market = data['market'][data['market']['metric_name'] == 'US Industrial Hemp Market']
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=hemp_market['year'],
        y=hemp_market['value'] / 1_000_000_000,
        mode='lines+markers',
        line=dict(color='#10b981', width=3),
        marker=dict(size=10, color='#10b981', line=dict(width=2, color='#0a0a0a')),
        fill='tozeroy',
        fillcolor='rgba(16, 185, 129, 0.1)'
    ))
    fig.update_layout(
        title="Market Trajectory → $7.8B by 2030",
        xaxis_title="", yaxis_title="",
        showlegend=False, height=380,
        **dark_template['layout'],
        yaxis=dict(gridcolor='rgba(255,255,255,0.03)', tickformat='$,.1f', ticksuffix='B'),
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("<p class='source-citation'>Sources: USDA NASS, Grand View Research (21.1% CAGR)</p>", unsafe_allow_html=True)

# REGULATORY MAP
st.markdown("<div class='section-header'>Regulatory Landscape</div>", unsafe_allow_html=True)
status_counts = data['regulatory']['thc_beverage_status'].value_counts()
col1, col2, col3 = st.columns([1, 2.5, 1])

with col1:
    st.markdown("#### By Status")
    status_colors = {
        'legal': '#10b981',
        'legal_restricted': '#34d399',
        'pending': '#fbbf24',
        'dispensary_only': '#f97316',
        'banned': '#ef4444'
    }
    for status, count in status_counts.items():
        color = status_colors.get(status, '#6b7280')
        label = status.replace('_', ' ').title()
        st.markdown(f'''
        <div class="status-item">
            <div class="status-dot" style="background: {color};"></div>
            <span class="status-text"><span class="status-count">{count}</span> — {label}</span>
        </div>
        ''', unsafe_allow_html=True)

with col2:
    reg_df = data['regulatory'].copy()
    status_map = {'legal': 4, 'legal_restricted': 3, 'pending': 2, 'dispensary_only': 1, 'banned': 0}
    reg_df['status_num'] = reg_df['thc_beverage_status'].map(status_map)
    fig = go.Figure(data=go.Choropleth(
        locations=reg_df['state'],
        z=reg_df['status_num'],
        locationmode='USA-states',
        colorscale=[
            [0, '#ef4444'],
            [0.25, '#f97316'],
            [0.5, '#fbbf24'],
            [0.75, '#34d399'],
            [1, '#10b981']
        ],
        showscale=False,
        hovertemplate="<b>%{location}</b><br>%{text}<extra></extra>",
        text=reg_df['thc_beverage_status'].str.replace('_', ' ').str.title(),
        marker_line_color='#1a1a2e',
        marker_line_width=1
    ))
    fig.update_layout(
        geo=dict(
            scope='usa',
            projection=dict(type='albers usa'),
            showlakes=False,
            bgcolor='rgba(0,0,0,0)',
            landcolor='rgba(255,255,255,0.02)',
        ),
        margin=dict(l=0, r=0, t=0, b=0),
        height=420,
        paper_bgcolor='rgba(0,0,0,0)',
    )
    st.plotly_chart(fig, use_container_width=True)

with col3:
    st.markdown('''
    <div class="obs-card">
        <h3>Key Stats</h3>
        <ul>
            <li><strong>28</strong> states legal</li>
            <li><strong>21+</strong> age required</li>
            <li><strong>5-10mg</strong> THC limits</li>
            <li><strong>27+</strong> active bills</li>
        </ul>
    </div>
    ''', unsafe_allow_html=True)

st.markdown("<p class='source-citation'>Source: MultiState Insider, Vicente LLP (Nov 2025)</p>", unsafe_allow_html=True)

# JOBS & TAX
st.markdown("<div class='section-header'>Economic Contribution</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    emp_us = data['employment'][data['employment']['geography'] == 'US'].copy()
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=emp_us['year'],
        y=emp_us['total_jobs'] / 1000,
        marker=dict(color='#10b981'),
        text=[f"{v/1000:.0f}K" for v in emp_us['total_jobs']],
        textposition='outside',
        textfont=dict(color='#10b981')
    ))
    fig.update_layout(
        title="Industry Employment",
        xaxis_title="", yaxis_title="",
        showlegend=False, height=350,
        **dark_template['layout'],
        yaxis=dict(gridcolor='rgba(255,255,255,0.03)'),
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    tax_states = data['tax'][(data['tax']['state'] != 'US') & (data['tax']['year'] == 2023) & (data['tax']['quarter'] == 4)].nlargest(6, 'tax_revenue_usd')
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=tax_states['state'],
        x=tax_states['tax_revenue_usd'] / 1_000_000,
        orientation='h',
        marker=dict(
            color=tax_states['tax_revenue_usd'],
            colorscale=[[0, '#059669'], [1, '#34d399']],
        ),
        text=[f"${v/1_000_000:.0f}M" for v in tax_states['tax_revenue_usd']],
        textposition='outside',
        textfont=dict(color='#10b981')
    ))
    fig.update_layout(
        title="State Tax Revenue (Q4 2023)",
        xaxis_title="", yaxis_title="",
        showlegend=False, height=350,
        **dark_template['layout'],
        yaxis=dict(autorange="reversed"),
        xaxis=dict(gridcolor='rgba(255,255,255,0.03)'),
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("<p class='source-citation'>Sources: Vangst 2024, U.S. Census Bureau</p>", unsafe_allow_html=True)

# CONSUMER DEMAND
st.markdown("<div class='section-header'>Consumer Demand</div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="stat-card"><div class="stat-value">64%</div><div class="stat-label">of Americans familiar<br/>with CBD products</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="stat-card"><div class="stat-value">36.5%</div><div class="stat-label">CBD beverage sales<br/>growth in 2023</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="stat-card"><div class="stat-value">70%</div><div class="stat-label">Gen Z/Millennials pay<br/>premium for traceable</div></div>', unsafe_allow_html=True)

st.markdown("<p class='source-citation' style='margin-top: 24px;'>Sources: Mastermind Behavior, Euromonitor</p>", unsafe_allow_html=True)

# TIMELINE
st.markdown("<div class='section-header'>Industry Timeline</div>", unsafe_allow_html=True)
timeline_df = data['timeline'].sort_values('event_date')
for _, row in timeline_df.iterrows():
    impact_color = {'positive': '#10b981', 'negative': '#ef4444', 'neutral': '#6b7280'}.get(row['impact'], '#6b7280')
    st.markdown(f'''
    <div class="timeline-item" style="border-left: 3px solid {impact_color};">
        <div class="timeline-date">{row["event_date"].strftime("%b %Y")}</div>
        <div>
            <div class="timeline-title">{row["title"]}</div>
            <div class="timeline-desc">{row["description"]}</div>
        </div>
    </div>
    ''', unsafe_allow_html=True)

# KEY TAKEAWAYS
st.markdown("<div class='section-header'>Key Takeaways</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
<div class="key-section">

### Economic Impact
- **$445M** U.S. hemp production value (2024)
- **$4.4B** state tax revenue generated
- **440K+** jobs across the industry
- **40%+** annual production growth

### Agricultural Benefits
- **45,294** acres under cultivation
- **8,153** farming operations
- Rural economic diversification
- Federal crop insurance eligible

</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="key-section">

### Consumer Choice
- **28 states** with legal THC beverages
- Strong demand & awareness
- Preference for regulated products
- Universal 21+ age restriction

### Regulatory Landscape
- Responsible state frameworks emerging
- 5-10mg serving limits standard
- Industry supports sensible regulation
- Clear labeling requirements in place

</div>
""", unsafe_allow_html=True)

# FOOTER
st.markdown("---")
st.markdown('''
<div style="text-align: center; color: #4b5563; padding: 30px 0;">
    <p style="font-size: 0.75rem; margin-bottom: 8px;">
        <strong style="color: #6b7280;">Data Sources:</strong> USDA NASS • Census Bureau • Vangst • Grand View Research • MultiState • Vicente LLP
    </p>
    <p style="font-size: 0.7rem; color: #4b5563;">
        Last updated November 2025 • Data refreshed quarterly
    </p>
</div>
''', unsafe_allow_html=True)

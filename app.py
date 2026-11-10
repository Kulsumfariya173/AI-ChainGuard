import streamlit as st
import pandas as pd
from datetime import datetime

from ai_model.threat_detection import detect_threat
from blockchain.blockchain import Blockchain


# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI-ChainGuard",
    page_icon="🛡️",
    layout="wide"
)


# ==========================================
# 2. SESSION STATE
# ==========================================

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "blockchain" not in st.session_state:
    st.session_state.blockchain = Blockchain()

if "threat_history" not in st.session_state:
    st.session_state.threat_history = []

chain = st.session_state.blockchain


# ==========================================
# 3. CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.stApp {
    background-color: #101827;
    color: white;
}

.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #60a5fa;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 16px;
}

div.stButton > button {
    background-color: #2563eb;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 10px 20px;
}

div.stButton > button:hover {
    background-color: #1d4ed8;
    color: white;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# 4. LOGIN PAGE
# ==========================================

if not st.session_state.authenticated:

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="main-title">🛡️ AI-ChainGuard</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Intelligent Cyber Threat Detection & Blockchain Security'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    left, center, right = st.columns([1, 1.5, 1])

    with center:

        st.subheader("Welcome Back")
        st.write("Login to access your security dashboard.")

        with st.form("login_form"):

            username = st.text_input(
                "Username",
                placeholder="Enter your username"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password"
            )

            submitted = st.form_submit_button(
                "🔐 Login Securely",
                use_container_width=True
            )

            if submitted:

                if username == "admin" and password == "chainguard123":

                    st.session_state.authenticated = True
                    st.rerun()

                else:
                    st.error("Invalid username or password.")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="subtitle">'
        '🔒 AI-Powered Threat Detection | Blockchain Security'
        '</div>',
        unsafe_allow_html=True
    )

    st.stop()


# ==========================================
# 5. MAIN DASHBOARD HEADER
# ==========================================

header1, header2 = st.columns([5, 1])

with header1:

    st.title("🛡️ AI-ChainGuard")

    st.subheader(
        "Intelligent Cyber Threat Detection & Blockchain Security"
    )

with header2:

    st.write("")

    if st.button("Logout"):

        st.session_state.authenticated = False
        st.rerun()

st.markdown("---")


# ==========================================
# 6. SIDEBAR
# ==========================================

st.sidebar.title("🛡️ AI-ChainGuard")

st.sidebar.write("Security Management")

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Threat Detection",
        "Threat History",
        "Blockchain Records"
    ]
)


# ==========================================
# 7. OVERVIEW PAGE
# ==========================================

if page == "Overview":

    st.header("📊 Security Overview")

    total_events = len(st.session_state.threat_history)

    suspicious_events = sum(
        1 for event in st.session_state.threat_history
        if event["Status"] == "Suspicious"
    )

    normal_events = total_events - suspicious_events

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Events", total_events)

    col2.metric("Threats Detected", suspicious_events)

    col3.metric("Normal Events", normal_events)

    col4.metric("Blockchain Blocks", len(chain.chain))

    st.markdown("---")

    st.subheader("System Status")

    if chain.is_chain_valid():
        st.success("Blockchain Integrity: Valid")
    else:
        st.error("Blockchain Integrity: Invalid")

    st.info("AI Threat Detection: Ready")

    st.info("Blockchain Security: Active")


# ==========================================
# 8. THREAT DETECTION PAGE
# ==========================================

elif page == "Threat Detection":

    st.header("🌐 Network Traffic Analysis")

    st.write(
        "Enter network traffic details to identify suspicious activity."
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        duration = st.number_input(
            "Duration",
            min_value=0,
            value=3
        )

        src_bytes = st.number_input(
            "Source Bytes",
            min_value=0,
            value=100
        )

    with col2:

        dst_bytes = st.number_input(
            "Destination Bytes",
            min_value=0,
            value=50
        )

        failed_logins = st.number_input(
            "Failed Logins",
            min_value=0,
            value=8
        )

    with col3:

        connection_count = st.number_input(
            "Connection Count",
            min_value=0,
            value=30
        )

        login_success = st.selectbox(
            "Login Success",
            [0, 1]
        )

    if st.button("🔍 Detect Threat", type="primary"):

        network_data = {
            "duration": duration,
            "src_bytes": src_bytes,
            "dst_bytes": dst_bytes,
            "failed_logins": failed_logins,
            "connection_count": connection_count,
            "login_success": login_success
        }

        detection = detect_threat(network_data)

        current_time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        # Record suspicious activity in blockchain

        if detection["status"] == "Suspicious":

            chain.add_block({
                "event": "Suspicious Network Activity",
                "status": detection["status"],
                "risk": detection["risk"],
                "confidence": detection["confidence"],
                "timestamp": current_time
            })

            blockchain_status = "Recorded"

            st.warning(
                "⚠️ Suspicious activity detected and recorded in blockchain!"
            )

        else:

            blockchain_status = "Not Required"

            st.success("✅ Normal network activity detected.")

        # Save detection in history

        history_record = {
            "Time": current_time,
            "Status": detection["status"],
            "Confidence": detection["confidence"],
            "Risk": detection["risk"],
            "Failed Logins": failed_logins,
            "Connections": connection_count,
            "Blockchain": blockchain_status
        }

        st.session_state.threat_history.append(history_record)

        # Display results

        st.markdown("---")

        st.subheader("📊 Detection Results")

        result1, result2, result3 = st.columns(3)

        result1.metric(
            "Status",
            detection["status"]
        )

        result2.metric(
            "Confidence",
            f'{detection["confidence"]}%'
        )

        result3.metric(
            "Risk Level",
            detection["risk"]
        )

        st.write(
            "Blockchain:",
            blockchain_status
        )


# ==========================================
# 9. THREAT HISTORY PAGE
# ==========================================

elif page == "Threat History":

    st.header("📋 Threat Detection History")

    st.write(
        "View previously analysed network activities and their results."
    )

    history = st.session_state.threat_history

    if history:

        history_df = pd.DataFrame(history)

        st.metric(
            "Total Analysed Events",
            len(history)
        )

        st.dataframe(
            history_df,
            use_container_width=True,
            hide_index=True
        )

        csv_data = history_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Download Detection History",
            data=csv_data,
            file_name="threat_detection_history.csv",
            mime="text/csv"
        )

    else:

        st.info(
            "No detection history available. "
            "Run a threat detection first."
        )


# ==========================================
# 10. BLOCKCHAIN RECORDS PAGE
# ==========================================

elif page == "Blockchain Records":

    st.header("⛓️ Blockchain Security")

    st.write(
        "View blockchain records and verify their integrity."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Total Blocks",
            len(chain.chain)
        )

    with col2:

        valid = chain.is_chain_valid()

        st.metric(
            "Blockchain Integrity",
            "Valid" if valid else "Invalid"
        )

    if valid:

        st.success("✅ Blockchain integrity verified.")

    else:

        st.error("❌ Blockchain integrity check failed.")

    st.markdown("---")

    # Blockchain verification button

    st.subheader("🔐 Integrity Verification")

    if st.button(
        "🔍 Verify Blockchain Integrity",
        type="primary",
        use_container_width=True
    ):

        if chain.is_chain_valid():

            st.success(
                "✅ Blockchain integrity verified! "
                "No tampering detected."
            )

        else:

            st.error(
                "🚨 Warning! Blockchain tampering detected. "
                "The stored data may have been modified."
            )

    st.markdown("---")

    # Display blockchain records

    st.subheader("Blockchain Records")

    for block in chain.chain:

        with st.expander(f"Block {block.index}"):

            st.write("Block Index:", block.index)

            st.write("Timestamp:", block.timestamp)

            st.write("Data:", block.data)

            st.write("Current Hash:")

            st.code(block.hash)

            st.write("Previous Hash:")

            st.code(block.previous_hash)


# ==========================================
# 11. FOOTER
# ==========================================

st.markdown("---")

st.markdown(
    "<center>AI-ChainGuard | "
    "AI-Based Cybersecurity and Blockchain Integrity System"
    "</center>",
    unsafe_allow_html=True
)
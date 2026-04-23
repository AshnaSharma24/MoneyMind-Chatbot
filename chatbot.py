# import streamlit as st
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# # -----------------------------
# # 🎨 PAGE CONFIG
# # -----------------------------
# st.set_page_config(page_title="MoneyMind", page_icon="💰", layout="wide")

# # -----------------------------
# # 🎨 CUSTOM CSS (UI BOOST)
# # -----------------------------
# st.markdown("""
#     <style>
#     .main {
#         background-color: #0f172a;
#         color: white;
#     }
#     .stTextInput>div>div>input {
#         background-color: #1e293b;
#         color: white;
#     }
#     # .chat-user {
#     #     background-color: #2563eb;
#     #     padding: 10px;
#     #     border-radius: 10px;
#     #     margin: 5px;
#     # }
#     # .chat-bot {
#     #     background-color: #334155;
#     #     padding: 10px;
#     #     border-radius: 10px;
#     #     margin: 5px;
#     # }
#     </style>
# """, unsafe_allow_html=True)

# # -----------------------------
# # 📌 TITLE
# # -----------------------------
# st.title("💰 MoneyMind AI Chatbot")
# st.caption("Your Personal Finance Assistant")

# # -----------------------------
# # 📌 FAQ DATA
# # -----------------------------
# questions = [
#     "What is EMI?", "How is EMI calculated?", "What is SIP?",
#     "How to improve credit score?", "What is an emergency fund?",
#     "How much should I save monthly?", "What is tax saving investment?",
#     "What is compound interest?", "What is diversification?",
#     "What is inflation?", "What is mutual fund?",
#     "What is credit utilization?", "What is savings goal?",
#     "What is FD?", "What is risk in investment?"
# ]

# answers = [
#     "EMI is Equated Monthly Installment used to repay loans.",
#     "EMI depends on principal, rate, and tenure.",
#     "SIP is Systematic Investment Plan.",
#     "Pay bills on time and reduce credit usage.",
#     "Emergency fund = 3-6 months expenses.",
#     "Save at least 20% income.",
#     "ELSS, PPF, NPS help save tax.",
#     "Interest on interest over time.",
#     "Investing in multiple assets.",
#     "Increase in prices over time.",
#     "Professionally managed fund.",
#     "Used credit percentage.",
#     "Target saving amount.",
#     "Fixed deposit with interest.",
#     "Chance of financial loss."
# ]

# # -----------------------------
# # 📌 ML MODEL
# # -----------------------------
# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(questions)

# def get_response(user_input):
#     user_vec = vectorizer.transform([user_input])
#     similarity = cosine_similarity(user_vec, X)
#     idx = similarity.argmax()
#     score = similarity[0][idx]

#     # 🔥 IMPORTANT FIX
#     if score < 0.4:
#         return "❌ Sorry, I didn’t understand. Please ask finance-related questions."

#     return answers[idx]

# # -----------------------------
# # 📊 SIDEBAR CALCULATORS
# # -----------------------------
# st.sidebar.header("📊 Financial Tools")

# calc_type = st.sidebar.selectbox(
#     "Choose Calculator",
#     ["None", "EMI Calculator", "SIP Calculator", "Savings Goal"]
# )

# # EMI
# if calc_type == "EMI Calculator":
#     st.sidebar.subheader("EMI Calculator")
#     P = st.sidebar.number_input("Loan Amount")
#     R = st.sidebar.number_input("Interest Rate (%)")
#     N = st.sidebar.number_input("Months")

#     if st.sidebar.button("Calculate EMI"):
#         R = R / (12 * 100)
#         emi = (P * R * (1 + R)**N) / ((1 + R)**N - 1)
#         st.sidebar.success(f"EMI: {round(emi,2)}")

# # SIP
# elif calc_type == "SIP Calculator":
#     st.sidebar.subheader("SIP Calculator")
#     monthly = st.sidebar.number_input("Monthly Investment")
#     rate = st.sidebar.number_input("Return Rate (%)")
#     years = st.sidebar.number_input("Years")

#     if st.sidebar.button("Calculate SIP"):
#         rate = rate / (12 * 100)
#         months = years * 12
#         fv = monthly * (((1 + rate)**months - 1) / rate) * (1 + rate)
#         st.sidebar.success(f"Future Value: {round(fv,2)}")

# # Savings Goal
# elif calc_type == "Savings Goal":
#     st.sidebar.subheader("Savings Goal")
#     goal = st.sidebar.number_input("Target Amount")
#     rate = st.sidebar.number_input("Return (%)")
#     years = st.sidebar.number_input("Years")

#     if st.sidebar.button("Calculate"):
#         pv = goal / ((1 + rate/100)**years)
#         st.sidebar.success(f"Required Today: {round(pv,2)}")

# # -----------------------------
# # 💬 CHAT HISTORY
# # -----------------------------
# if "chat" not in st.session_state:
#     st.session_state.chat = []

# # -----------------------------
# # 💬 INPUT
# # -----------------------------
# user_input = st.text_input("Ask your question...")

# if user_input:
#     response = get_response(user_input)

#     st.session_state.chat.append(("user", user_input))
#     st.session_state.chat.append(("bot", response))

# # -----------------------------
# # 💬 DISPLAY CHAT
# # -----------------------------
# for role, msg in st.session_state.chat:
#     if role == "user":
#         st.markdown(f'<div class="chat-user">🧑 {msg}</div>', unsafe_allow_html=True)
#     else:
#         st.markdown(f'<div class="chat-bot">🤖 {msg}</div>', unsafe_allow_html=True)





# import streamlit as st
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# # -----------------------------
# # 🎨 PAGE CONFIG
# # -----------------------------
# st.set_page_config(page_title="MoneyMind", page_icon="💰")

# st.title("💰 MoneyMind AI Chatbot")
# st.caption("Ask finance-related questions or use tools from sidebar")

# # -----------------------------
# # 📌 FAQ DATA
# # -----------------------------
# questions = [
#     "What is EMI?", "How is EMI calculated?", "What is SIP?",
#     "How to improve credit score?", "What is an emergency fund?",
#     "How much should I save monthly?", "What is tax saving investment?",
#     "What is compound interest?", "What is diversification?",
#     "What is inflation?", "What is mutual fund?",
#     "What is credit utilization?", "What is savings goal?",
#     "What is FD?", "What is risk in investment?"
# ]

# answers = [
#     "EMI is Equated Monthly Installment used to repay loans.",
#     "EMI depends on principal, rate, and tenure.",
#     "SIP is Systematic Investment Plan.",
#     "Pay bills on time and reduce credit usage.",
#     "Emergency fund = 3-6 months expenses.",
#     "Save at least 20% income.",
#     "ELSS, PPF, NPS help save tax.",
#     "Interest on interest over time.",
#     "Investing in multiple assets.",
#     "Increase in prices over time.",
#     "Professionally managed fund.",
#     "Used credit percentage.",
#     "Target saving amount.",
#     "Fixed deposit with interest.",
#     "Chance of financial loss."
# ]

# # -----------------------------
# # 📌 ML MODEL
# # -----------------------------
# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(questions)

# def get_response(user_input):
#     user_vec = vectorizer.transform([user_input])
#     similarity = cosine_similarity(user_vec, X)
#     idx = similarity.argmax()
#     score = similarity[0][idx]

#     if score < 0.4:
#         return "❌ Please ask finance-related questions."

#     return answers[idx]

# # -----------------------------
# # 📊 SIDEBAR CALCULATORS
# # -----------------------------
# st.sidebar.header("📊 Financial Tools")

# calc = st.sidebar.selectbox("Select Tool", ["None", "EMI", "SIP", "Savings Goal"])

# # EMI
# if calc == "EMI":
#     st.sidebar.subheader("EMI Calculator")
#     P = st.sidebar.number_input("Loan Amount")
#     R = st.sidebar.number_input("Interest Rate (%)")
#     N = st.sidebar.number_input("Months")

#     if st.sidebar.button("Calculate EMI"):
#         R = R / (12 * 100)
#         emi = (P * R * (1 + R)**N) / ((1 + R)**N - 1)
#         st.sidebar.success(f"EMI: {round(emi,2)}")

# # SIP
# elif calc == "SIP":
#     st.sidebar.subheader("SIP Calculator")
#     monthly = st.sidebar.number_input("Monthly Investment")
#     rate = st.sidebar.number_input("Return Rate (%)")
#     years = st.sidebar.number_input("Years")

#     if st.sidebar.button("Calculate SIP"):
#         rate = rate / (12 * 100)
#         months = years * 12
#         fv = monthly * (((1 + rate)**months - 1) / rate) * (1 + rate)
#         st.sidebar.success(f"Future Value: {round(fv,2)}")

# # Savings Goal
# elif calc == "Savings Goal":
#     st.sidebar.subheader("Savings Goal")
#     goal = st.sidebar.number_input("Target Amount")
#     rate = st.sidebar.number_input("Return (%)")
#     years = st.sidebar.number_input("Years")

#     if st.sidebar.button("Calculate"):
#         pv = goal / ((1 + rate/100)**years)
#         st.sidebar.success(f"Required Today: {round(pv,2)}")

# # -----------------------------
# # 💬 SINGLE QUERY INPUT
# # -----------------------------
# user_input = st.text_input("Ask your question:")

# if user_input:
#     response = get_response(user_input)
    
#     # st.info(user_input)

#     # st.markdown("### 🤖 Bot:")
#     st.success(response)


# import streamlit as st
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# # -----------------------------
# # 🎨 PAGE CONFIG
# # -----------------------------
# st.set_page_config(page_title="MoneyMind", layout="wide")

# # -----------------------------
# # 🎨 CUSTOM CSS
# # -----------------------------
# st.markdown("""
#     <style>
#     .main {
#         background-color: #0f172a;
#         color: white;
#     }
#     .stTextInput>div>div>input {
#         background-color: #1e293b;
#         color: white;
#     }
#     .chat-user {
#         background-color: #2563eb;
#         padding: 10px;
#         border-radius: 10px;
#         margin: 5px;
#     }
#     .chat-bot {
#         background-color: #334155;
#         padding: 10px;
#         border-radius: 10px;
#         margin: 5px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# st.markdown("""
# <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
# """, unsafe_allow_html=True)



# # -----------------------------
# # 📌 TITLE
# # -----------------------------
# st.markdown("""
# <h1>
# <i class="fa-brands fa-discourse" style="color: rgb(177, 151, 252);"></i>
# MoneyMind AI Chatbot
# </h1>
# """, unsafe_allow_html=True)
# st.caption("Your Personal Finance Assistant")

# # -----------------------------
# # 📌 LOAD CSV DATA
# # -----------------------------
# df = pd.read_csv("P8_Chatbot_FAQ_Bank.csv")

# # Clean + normalize
# df["Question"] = df["Question"].str.lower()

# questions = df["Question"].tolist()
# answers = df["Answer"].tolist()

# # -----------------------------
# # 📌 ML MODEL
# # -----------------------------
# vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2))
# X = vectorizer.fit_transform(questions)

# def get_response(user_input):
#     user_input = user_input.lower()

#     user_vec = vectorizer.transform([user_input])
#     similarity = cosine_similarity(user_vec, X)
#     idx = similarity.argmax()
#     score = similarity[0][idx]

#     if score < 0.25:
#         return "❌ Sorry, I didn’t understand. Please ask finance-related questions."

#     return answers[idx]

# # -----------------------------
# #  SIDEBAR CALCULATORS
# # -----------------------------
# st.sidebar.markdown("""
# <h3 style="display:flex; align-items:center; gap:8px;">
# <i class="fa-solid fa-calculator" style="color: rgb(177, 151, 252);"></i>
# <span>Financial Tools</span>
# </h3>
# """, unsafe_allow_html=True)

# calc_type = st.sidebar.selectbox(
#     "Choose Calculator",
#     ["None", "EMI Calculator", "SIP Calculator", "Savings Goal"]
# )

# # EMI
# if calc_type == "EMI Calculator":
#     st.sidebar.subheader("EMI Calculator")
#     P = st.sidebar.number_input("Loan Amount")
#     R = st.sidebar.number_input("Interest Rate (%)")
#     N = st.sidebar.number_input("Months")

#     if st.sidebar.button("Calculate EMI"):
#         R = R / (12 * 100)
#         emi = (P * R * (1 + R)**N) / ((1 + R)**N - 1)
#         st.sidebar.success(f"EMI: {round(emi,2)}")

# # SIP
# elif calc_type == "SIP Calculator":
#     st.sidebar.subheader("SIP Calculator")
#     monthly = st.sidebar.number_input("Monthly Investment")
#     rate = st.sidebar.number_input("Return Rate (%)")
#     years = st.sidebar.number_input("Years")

#     if st.sidebar.button("Calculate SIP"):
#         rate = rate / (12 * 100)
#         months = years * 12
#         fv = monthly * (((1 + rate)**months - 1) / rate) * (1 + rate)
#         st.sidebar.success(f"Future Value: {round(fv,2)}")

# # Savings Goal
# elif calc_type == "Savings Goal":
#     st.sidebar.subheader("Savings Goal")
#     goal = st.sidebar.number_input("Target Amount")
#     rate = st.sidebar.number_input("Return (%)")
#     years = st.sidebar.number_input("Years")

#     if st.sidebar.button("Calculate"):
#         pv = goal / ((1 + rate/100)**years)
#         st.sidebar.success(f"Required Today: {round(pv,2)}")

# # -----------------------------
# # 💬 CHAT HISTORY
# # -----------------------------
# if "chat" not in st.session_state:
#     st.session_state.chat = []

# # -----------------------------
# # 💬 INPUT
# # -----------------------------
# user_input = st.text_input("Ask your question...")

# if user_input:
#     response = get_response(user_input)

#     st.session_state.chat.append(("user", user_input))
#     st.session_state.chat.append(("bot", response))

# # -----------------------------
# # 💬 DISPLAY CHAT
# # -----------------------------
# for role, msg in st.session_state.chat:
#     if role == "user":
#         st.markdown(f'<div class="chat-user"> {msg}</div>', unsafe_allow_html=True)
#     else:
#         st.markdown(f'<div class="chat-bot"> {msg}</div>', unsafe_allow_html=True)



import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import get_close_matches

# -----------------------------
#  PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="MoneyMind", layout="wide")

# -----------------------------
#  CUSTOM CSS
# -----------------------------
st.markdown("""
    <style>
    .main {
        background-color: #0f172a;
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: #1e293b;
        color: white;
    }
    .chat-user {
        background-color: #2563eb;
        padding: 10px;
        border-radius: 10px;
        margin: 5px;
    }
    .chat-bot {
        background-color: #334155;
        padding: 10px;
        border-radius: 10px;
        margin: 5px;
    }
    .stFormSubmitButton button {
        margin-top: 28px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
""", unsafe_allow_html=True)

# -----------------------------
#  TITLE
# -----------------------------

st.markdown("""
<h1>
<i class="fa-brands fa-discourse" style="color: rgb(177, 151, 252);"></i>
MoneyMind AI Chatbot
</h1>
""", unsafe_allow_html=True)
st.caption("Your Personal Finance Assistant")

# -----------------------------
#  LOAD CSV DATA
# -----------------------------
df = pd.read_csv("P8_Chatbot_FAQ_Bank.csv")

# Clean + normalize
df["Question"] = df["Question"].str.lower()

questions = df["Question"].tolist()
answers = df["Answer"].tolist()

# -----------------------------
#  ML MODEL
# -----------------------------
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2))
X = vectorizer.fit_transform(questions)

# Common financial acronym aliases and typo corrections
ACRONYM_ALIASES = {
    'emii': 'emi',
    'sipp': 'sip',
    'npp': 'nps',
    'ppf': 'ppf',
    'elss': 'elss',
    'elis': 'elss',
    'mutual': 'mutual fund',
    'credit score': 'credit score',
}

def expand_query(user_input):
    """Expand and normalize query for better matching"""
    user_lower = user_input.lower().strip()
    
    # Check for typos using fuzzy matching
    typo_matches = get_close_matches(user_lower, questions, n=1, cutoff=0.6)
    if typo_matches:
        return typo_matches[0]
    
    # Check acronym aliases
    for typo, correct in ACRONYM_ALIASES.items():
        if typo in user_lower:
            user_lower = user_lower.replace(typo, correct)
    
    return user_lower

def get_response(user_input):
    user_input = user_input.lower()
    
    # Expand and normalize query
    expanded_input = expand_query(user_input)

    user_vec = vectorizer.transform([expanded_input])
    similarity = cosine_similarity(user_vec, X)
    idx = similarity.argmax()
    score = similarity[0][idx]

    if score < 0.30:
        return "Sorry, I didn’t understand. Please ask finance-related questions."

    return answers[idx]

# -----------------------------
#  SIDEBAR CALCULATORS
# -----------------------------
st.sidebar.markdown("""
<h3 style="display:flex; align-items:center; gap:8px;">
<i class="fa-solid fa-calculator" style="color: rgb(177, 151, 252);"></i>
<span>Financial Tools</span>
</h3>
""", unsafe_allow_html=True)

calc_type = st.sidebar.selectbox(
    "Choose Calculator",
    ["None", "EMI Calculator", "SIP Calculator", "Savings Goal"]
)

# EMI
if calc_type == "EMI Calculator":
    st.sidebar.subheader("EMI Calculator")
    P = st.sidebar.number_input("Loan Amount", min_value=0.0)
    R = st.sidebar.number_input("Interest Rate (%)", min_value=0.0)
    N = st.sidebar.number_input("Months", min_value=0)

    if st.sidebar.button("Calculate EMI"):
        try:
            if P <= 0:
                st.sidebar.error(" Loan amount must be greater than 0")
            elif R == 0:
                st.sidebar.error(" Interest rate cannot be zero")
            elif N <= 0:
                st.sidebar.error(" Months must be greater than 0")
            else:
                R_monthly = R / (12 * 100)
                emi = (P * R_monthly * (1 + R_monthly)**N) / ((1 + R_monthly)**N - 1)
                st.sidebar.success(f" EMI: ₹{round(emi, 2)}")
        except Exception as e:
            st.sidebar.error(f" Error: {str(e)}")

# SIP
elif calc_type == "SIP Calculator":
    st.sidebar.subheader("SIP Calculator")
    monthly = st.sidebar.number_input("Monthly Investment", min_value=0.0)
    rate = st.sidebar.number_input("Return Rate (%)", min_value=0.0)
    years = st.sidebar.number_input("Years", min_value=0)

    if st.sidebar.button("Calculate SIP"):
        try:
            if monthly <= 0:
                st.sidebar.error(" Monthly investment must be greater than 0")
            elif years <= 0:
                st.sidebar.error(" Years must be greater than 0")
            elif rate == 0:
                st.sidebar.error(" Return rate cannot be zero")
            else:
                rate_monthly = rate / (12 * 100)
                months = years * 12
                fv = monthly * (((1 + rate_monthly)**months - 1) / rate_monthly) * (1 + rate_monthly)
                st.sidebar.success(f" Future Value: ₹{round(fv, 2)}")
        except Exception as e:
            st.sidebar.error(f" Error: {str(e)}")

# Savings Goal
elif calc_type == "Savings Goal":
    st.sidebar.subheader("Savings Goal")
    goal = st.sidebar.number_input("Target Amount", min_value=0.0)
    rate = st.sidebar.number_input("Return (%)", min_value=0.0)
    years = st.sidebar.number_input("Years", min_value=0)

    if st.sidebar.button("Calculate"):
        try:
            if goal <= 0:
                st.sidebar.error(" Target amount must be greater than 0")
            elif years <= 0:
                st.sidebar.error(" Years must be greater than 0")
            else:
                pv = goal / ((1 + rate / 100) ** years)
                st.sidebar.success(f" Required Today: ₹{round(pv, 2)}")
        except Exception as e:
            st.sidebar.error(f" Error: {str(e)}")

# -----------------------------
#  CHAT HISTORY
# -----------------------------
if "chat" not in st.session_state:
    st.session_state.chat = []

# -----------------------------
#  INPUT
# -----------------------------
with st.form("chat_form", clear_on_submit=True):
    col1, col2 = st.columns([5, 1], gap="small")
    
    with col1:
        user_input = st.text_input("Ask your question...")
    
    with col2:
        submitted = st.form_submit_button(
        'Send',
        use_container_width=True
        )
    
    if submitted and user_input:
        response = get_response(user_input)
        
        st.session_state.chat.append(("user", user_input))
        st.session_state.chat.append(("bot", response))

# -----------------------------
#  DISPLAY CHAT
# -----------------------------
for role, msg in st.session_state.chat:
    if role == "user":
        st.markdown(f'<div class="chat-user">{msg}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-bot">{msg}</div>', unsafe_allow_html=True)
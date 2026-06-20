import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/bank/bank-full.csv', sep=';')


if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    st.title(" BankMind")
    st.subheader("Bank Marketing Intelligence Dashboard")
    st.markdown("*Analyzing what drives term deposit subscriptions — UCI Bank Marketing Dataset*")
    
    st.divider()

    st.markdown("###  Dataset at a Glance")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Records", f"{len(df):,}")
    col2.metric("Features", len(df.columns))
    col3.metric("Subscribed", f"{(df['y']=='yes').sum():,}")
    col4.metric("Subscription Rate", f"{(df['y']=='yes').mean()*100:.1f}%")

    st.divider()

    st.markdown("###  What You Can Explore")
    col1, col2 = st.columns(2)
    with col1:
        st.info(" Exploratory Data Analysis\n\nInteractive charts exploring how different features influence subscription decisions.")
    with col2:
        st.info(" Customer Prediction (Coming Soon)\n\nML-powered predictions on whether a customer will subscribe based on their profile.")

    st.divider()
    
    if st.sidebar.button("EDA Dashboard",use_container_width=True):
        st.session_state.page = "eda"
        st.rerun()
    st.sidebar.button("Customer Prediction",use_container_width=True,disabled=True)
    
if st.session_state.page == "eda":
    st.title("BankMind - Customer Subscription Insights")

    if st.sidebar.button("Home",use_container_width=True):
        st.session_state.page = "home"
        st.rerun()

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        if st.button("Job vs Subscription Rate"):
            st.session_state.page = "plot1"
            st.rerun()

    with col2:
        if st.button("Balance vs Subscription Rate"):
            st.session_state.page = "plot2"
            st.rerun()

    with col3:
        if st.button("Age vs Subscription Rate"):
            st.session_state.page = "plot3"
            st.rerun()

    with col4:
        if st.button("Housing Loan vs Subscription Rate"):
            st.session_state.page = "plot4"
            st.rerun()

if st.session_state.page == "plot1":
    st.title("BankMind - Customer Subscription Insights")
    st.header("Subscription Rate by Job")

    if st.sidebar.button("Home",use_container_width=True):
        st.session_state.page = "home"
        st.rerun()
    if st.sidebar.button("Back to EDA",use_container_width=True):
        st.session_state.page = "eda"
        st.rerun()

    selected_job = st.multiselect("Filter by job",df['job'].unique(),default = df['job'].unique())
    filtered_df = df[df['job'].isin(selected_job)]
    job_sub = filtered_df.groupby('job')['y'].apply(lambda x: (x=='yes').mean()*100).reset_index()
    job_sub.columns=["job","subscription_rate"]

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Customers", f"{len(filtered_df):,}")
    col2.metric("Subscribed", (filtered_df['y'] == 'yes').sum())
    col3.metric("Subscription Rate", f"{(filtered_df['y'] == 'yes').mean()*100:.1f}%")

    fig,ax = plt.subplots(figsize=(10,6))
    sns.barplot(x="job",y="subscription_rate",data=job_sub,ax=ax,color="pink")
    ax.set_title('Subscription Rate by Jobs')
    ax.set_xlabel('Job')
    ax.set_ylabel('Subscription Rate(%)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

elif st.session_state.page == "plot2":
    st.title("BankMind - Customer Subscription Insights")
    st.header("Subscription Rate by Balance")

    if st.sidebar.button("Home",use_container_width=True):
        st.session_state.page = "home"
        st.rerun()
    if st.sidebar.button("Back to EDA",use_container_width=True):
        st.session_state.page = "eda"
        st.rerun()
    
    min_bal, max_bal = int(df['balance'].min()),int(df["balance"].max())
    balance_range = st.slider("Filter by Balance Range",
                              min_value=min_bal,max_value=max_bal,
                              value=(0,20000))
    filtered_df = df[(df['balance']>= balance_range[0]) & (df["balance"]<= balance_range[1])]

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Customers", f"{len(filtered_df):,}")
    col2.metric("Subscribed", (filtered_df['y'] == 'yes').sum())
    col3.metric("Subscription Rate", f"{(filtered_df['y'] == 'yes').mean()*100:.1f}%")

    fig,ax = plt.subplots(figsize=(10,5))
    sns.boxplot(x="y",y="balance",data=filtered_df,ax=ax)
    ax.set_title('Subscription Rate by Account Balance')
    ax.set_xlabel('Suscribed (Y/N)')
    ax.set_ylabel('Balance')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

elif st.session_state.page == "plot3":
    st.title("BankMind - Customer Subscription Insights")
    st.header("Subscription Rate by Age")

    if st.sidebar.button("Home",use_container_width=True):
        st.session_state.page = "home"
        st.rerun()
    if st.sidebar.button("Back to EDA",use_container_width=True):
        st.session_state.page = "eda"
        st.rerun()

    min_age, max_age = int(df['age'].min()),int(df['age'].max())
    age_range = st.slider("Filter by Age",
                              min_value=min_age,max_value=max_age,
                              value=(30,40))
    selected_age = st.radio("Age Group to Highlight",options=['All', '18-30', '31-45', '46-60', '60+'])
    filtered_df = df[(df['age']>= age_range[0]) & (df['age']<= age_range[1])]

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Customers", f"{len(filtered_df):,}")
    col2.metric("Subscribed", (filtered_df['y'] == 'yes').sum())
    col3.metric("Subscription Rate", f"{(filtered_df['y'] == 'yes').mean()*100:.1f}%")

    filtered_df['age_group']=  pd.cut(filtered_df['age'],bins=[18,30,45,60,100],labels=['18-30','31-45','46-60','60+'])
    age_sub = filtered_df.groupby('age_group',observed = True)['y'].apply(lambda x: 
                                                                          (x=='yes').mean()*100).reset_index()
    age_sub.columns = ['age_group', 'subscription_rate']

    colors = []
    for group in age_sub['age_group']:
        if selected_age == 'All' or str(group) == selected_age:
            colors.append('#2ECC71')   # bright green = highlighted
        else:
            colors.append('#B9E6D3')

    fig,ax = plt.subplots(figsize=(8,5))
    sns.barplot(x="age_group",y="subscription_rate",data=age_sub,ax=ax,palette=colors)
    ax.set_title('Subscription Rate by Age')
    ax.set_xlabel('Age Range')
    ax.set_ylabel('Subscription Rate')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

elif st.session_state.page == "plot4":
    st.title("BankMind - Customer Subscription Insights")
    st.header("Subscription Rate by Housing Loan and Marital Status")

    if st.sidebar.button("Home",use_container_width=True):
        st.session_state.page = "home"
        st.rerun()
    if st.sidebar.button("Back to EDA",use_container_width=True):
        st.session_state.page = "eda"
        st.rerun()

    slected_marital = st.multiselect("Filter by marital status", df['marital'].unique(),default=df['marital'].unique())
    filtered_df = df[df['marital'].isin(slected_marital)]    

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Customers", f"{len(filtered_df):,}")
    col2.metric("Subscribed", (filtered_df['y'] == 'yes').sum())
    col3.metric("Subscription Rate", f"{(filtered_df['y'] == 'yes').mean()*100:.1f}%")

    loan_sub = filtered_df.groupby(['housing','marital'])['y'].apply(lambda x: (x=="yes").mean()*100).reset_index()
    loan_sub.columns = ['housing','marital','sub_rate']

    fig,ax = plt.subplots(figsize=(8,5))
    sns.barplot(x='housing',y="sub_rate",hue='marital',data=loan_sub,ax=ax,color="#FFEDA8")
    ax.set_title('Subscription Rate by Housing Loan')
    ax.set_xlabel('Has Housing Loan ?')
    ax.set_ylabel('Subscription Rate')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()



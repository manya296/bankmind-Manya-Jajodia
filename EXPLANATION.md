EXPLANATION.md 

Name: Manya Jajodia

Dataset: UCI Bank Marketing Dataset

Dashboard: bankmind-manya.streamlit.app


Q1. What percentage of customers in your dataset have y = yes? What does this imbalance mean for how you'd evaluate a model?

The dataset contains 45,211 records, of which 5,289 (11.7%) subscribed to a term deposit (having y = yes in dataset) and 39,922 (88.3%) did not.

This heavy imbalance matters because a model that blindly predicts "no" for every customer would still achieve 88% accuracy — making accuracy a misleading metric. This is why F1-score and recall are more meaningful evaluation criteria for this dataset. It also means the bank's marketing campaigns need to be carefully targeted, since the vast majority of contacts do not convert.


Q2. Which job category had the highest subscription rate? Does this make sense to you intuitively?

Students showed the highest subscription rate at 28.7%, followed by those who are Retired at 22.8%.

This likely reflects financial circumstances. Students may be more financially cautious and drawn to structured savings options and retired individuals tend to have stable income, lower expenses, and a greater interest in low-risk savings products like term deposits.
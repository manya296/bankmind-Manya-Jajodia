# EXPLANATION.md 

Name: Manya Jajodia

Dataset: UCI Bank Marketing Dataset

Dashboard: bankmind-manya.streamlit.app


## Q1. What percentage of customers in your dataset have y = yes? What does this imbalance mean for how you'd evaluate a model?

The dataset contains 45,211 records, of which 5,289 (11.7%) subscribed to a term deposit (having y = yes in dataset) and 39,922 (88.3%) did not.

This heavy imbalance matters because a model that blindly predicts "no" for every customer would still achieve 88% accuracy — making accuracy a misleading metric. This is why F1-score and recall are more meaningful evaluation criteria for this dataset. It also means the bank's marketing campaigns need to be carefully targeted, since the vast majority of contacts do not convert.


## Q2. Which job category had the highest subscription rate? Does this make sense to you intuitively?

Students showed the highest subscription rate at 28.7%, followed by those who are Retired at 22.8%.

This likely reflects financial circumstances. Students may be more financially cautious and drawn to structured savings options and retired individuals tend to have stable income, lower expenses, and a greater interest in low-risk savings products like term deposits.

---

## Q3. Which feature had the highest importance in your tree-based model? Why do you think that is?

In the Random Forest model, **`duration`** (the length of the last phone call in seconds) had by far the highest importance at **0.291 (29.1%)** — nearly three times more influential than the next feature.

| Feature | Importance |
|---|---|
| duration | 0.2912 |
| balance | 0.1101 |
| age | 0.1033 |
| day | 0.0903 |
| month | 0.0874 |

This makes strong intuitive sense — the longer a customer stays on a call with a bank agent, the more engaged and interested they are. A customer who hangs up in 30 seconds is clearly not interested; one who talks for 15 minutes is actively considering the product.

However, there is an important caveat: `duration` is only known **after** the call has already ended. This means it cannot be used to predict subscription *before* making the call. In a real-world pre-call targeting system, this feature would need to be removed — and the model retrained on the remaining features like `balance`, `age`, and `poutcome`.

---

## Q4. Why is F1 a better metric than accuracy for this particular dataset?

Because of the severe class imbalance (88.3% "No" vs 11.7% "Yes"), accuracy rewards a model for ignoring the minority class entirely.

**F1-Score = 2 × (Precision × Recall) / (Precision + Recall)**

It is the harmonic mean of Precision and Recall — and crucially, a model scores a high F1 only if it is doing well on **both** — not just predicting the majority class.

In our results:

| Model | Accuracy | F1 (Yes) | Macro F1 |
|---|---|---|---|
| Logistic Regression | 89% | 0.31 | 0.63 |
| Random Forest | 91% | 0.51 | 0.73 |

Logistic Regression has 89% accuracy but only 0.31 F1 on the "Yes" class — it is barely identifying subscribers at all (recall of just 0.21). The Random Forest's macro F1 of 0.73 tells a much more honest story: it is meaningfully better at the actual task of finding customers who will subscribe.

For the bank, **missing a potential subscriber (false negative) is costly** — it means a lost sale. F1 captures this cost in a way accuracy simply does not.

---

## Q5. Pick one of your 5 sample predictions. Do you actually agree with the model's call, given that customer's features? Walk through your thinking.

**I'll analyse Customer 1 — Predicted: SUBSCRIBE (61%) | Actual: No**

Customer profile:
- Age: 41
- Balance: €800
- Call duration: 899 seconds (~15 minutes)
- Housing loan: No
- Personal loan: No
- Previous outcome: Unknown (poutcome = 3)

The model predicted this customer would subscribe with 61% probability — but they did not.

**Do I agree with the model's reasoning?** Partially yes, partially no.

On the surface, this customer looks promising, no financial obligations (no housing or personal loan), a moderate balance, and a very long call duration of nearly 15 minutes. A 15-minute call strongly suggests engagement and genuine interest, so I understand why the model leaned towards "Subscribe."

However, looking more carefully, the balance of €800 is relatively modest, and the previous campaign outcome is unknown — meaning the bank had no prior successful contact to build on. The model appears to have been heavily swayed by the long call duration, which as noted in Q3, can be misleading.

**My conclusion:** The model made a reasonable but imperfect call. The long call duration created a false signal of intent. This is a good example of why `duration` being the dominant feature is a risk — it can inflate confidence in predictions without reflecting the customer's true financial readiness to commit. I would partially disagree with the model here and factor in the low balance and unknown prior outcome as stronger signals of non-conversion.

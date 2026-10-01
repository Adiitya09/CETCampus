# 🎓 CETCampus

### Navigate Your Engineering Future

**CETCampus** is a data-driven **MHT-CET engineering college recommendation platform** designed to help students explore, compare, and shortlist Maharashtra engineering colleges using historical CAP cutoff data, student percentile, preferred branches, seat categories, and location preferences.

The platform combines **data preprocessing, recommendation logic, REST APIs, PostgreSQL, and an interactive Next.js interface** to transform historical admission data into explainable college recommendations.

> ⚠️ **Disclaimer:** CETCampus provides recommendations based on historical admission data. It does **not** predict or guarantee future admission outcomes.

---

## 🚀 Project Overview

Choosing an engineering college through MHT-CET can be difficult because students need to evaluate:

- CET percentile
- Engineering branch
- College location
- Seat category
- Historical cutoff trends
- CAP round differences
- Multiple colleges simultaneously

Raw cutoff datasets are difficult to interpret manually.

**CETCampus solves this problem by converting historical admission data into an interactive recommendation system.**

The student provides their admission preferences, and the recommendation engine analyzes these inputs against historical cutoff records to generate relevant college and branch recommendations.

---

## ✨ Key Features

### 🎯 Personalized Recommendations

Students can provide:

- MHT-CET percentile
- Score type
- Seat category
- Preferred engineering branches
- Preferred locations

The system analyzes these preferences against historical CAP cutoff data.

---

### 📊 Safe / Moderate / Reach Classification

Recommendations are classified using the relationship between the student's percentile and historical cutoff.

```text
                 Student Profile
                       │
                       ▼
              Historical Cutoffs
                       │
                       ▼
                Cutoff Analysis
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
        SAFE        MODERATE       REACH
          │            │            │
     Above cutoff   Near cutoff   Below cutoff

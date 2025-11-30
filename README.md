# **AI Candidate Evaluation Engine**

**Project Architecture (`ARCHITECTURE.md`)**

---

# **AI Candidate Evaluation Engine – Project Architecture**

## **Overview**

This system evaluates candidates end-to-end using **Resume + GitHub + Job Description**, generates a **detailed authenticity & skill report**, stores results, supports **multiple candidates**, and provides **comparison** between them.

The platform is built as a **Micro-SaaS AI powered HR screening tool**.

---

# **Core Features (based on checklist)**

### **1. Resume Input**

- Upload or paste resume (PDF/text)
- Extract email, LinkedIn, GitHub, skills, work history

### **2. GitHub Profile Finder**

- Automatically detect GitHub username from resume
- If not found, infer via email/name search using GitHub API

### **3. GitHub Deep Validations (One-Line Checks)**

- **Originality Check** → Detect copied/forked/template projects
- **Commit Pattern Authenticity** → Detect one-day bulk commits / fake activity
- **Code Quality** → Structure, readability, modularity, documentation
- **Tech Stack Verification** → Compare used stack vs claimed resume skills
- **Project Depth Check** → Check if project is real or shallow
- **AI-Generated Code Check** → Identify ChatGPT-style boilerplate
- **Activity Timeline Consistency** → Ensure long-term authentic commits
- **Repo Health Score** → Issues, branches, tests, readme, maintainability
- **Skill Validation** → Derive actual skills from repositories

( Depth First Search )

### **4. Resume vs JD (ATS Parsing)**

- Extract keywords from JD
- Match resume keywords & skills to JD
- Identify missing skills / strengths / gaps

### **5. GitHub vs JD (Skill Validation)**

- Match project tech stack to job requirements
- Confirm real skills vs claimed skills

### **6. Combined AI Analysis**

- Merge resume score + GitHub authenticity score + JD fit score
- Generate:
    - Summary
    - Strengths
    - Red Flags
    - Authenticity Score (0-100)
    - Skill Match Score (0-100)
    - Overall Fit Score

### **7. Store in Database**

- MongoDB / PostgreSQL
- Store candidate data, resume text, GitHub analysis, JD analysis

### **8. Multi-Candidate Support**

- Store multiple evaluations
- Group by job position
- List candidates with ranking

### **9. Comparison Engine**

- Side-by-side candidate comparison
- Compare:
    - Fit score
    - Authenticity
    - Code quality
    - Tech match
    - Strengths / risks

---

# **High-Level Architecture**

```
+-------------------------------------------------------------+
|                       Frontend (Web App)                    |
|  - Resume upload                                            |
|  - JD upload                                                |
|  - Candidate list                                           |
|  - Reports viewer                                           |
|  - Comparison dashboard                                     |
+---------------------------|---------------------------------+
                            |
                            v
+-------------------------------------------------------------+
|                        Backend (Flask API)                  |
|                                                             |
|  /resume-upload         --> Resume Parser                    |
|  /github-fetch          --> GitHub Service                   |
|  /analyze               --> AI Engine                        |
|  /save                  --> DB Service                       |
|  /candidate/:id         --> Fetch reports                    |
|  /compare               --> Comparison module                |
|                                                             |
+---------------------------|---------------------------------+
                            |
                            v
+-------------------------------------------------------------+
|                        AI Layer (LLM)                       |
|  - Resume Parsing & ATS                                     |
|  - JD Skill Extraction                                      |
|  - GitHub Code Analysis                                     |
|  - Authenticity Detection                                   |
|  - Scoring Engine                                           |
+---------------------------|---------------------------------+
                            |
                            v
+-------------------------------------------------------------+
|                     Database (Cloud DB)                     |
|  Candidates                                                 |
|  Reports                                                    |
|  Job Descriptions                                           |
|  GitHub Project Cache                                       |
+-------------------------------------------------------------+

```

---

# **Module-Level Architecture**

### **1. Resume Parser Module**

- Extract GitHub, email, skills
- Detect missing information
- Convert PDF → text

### **2. GitHub Service Module**

- Fetch repos
- Fetch commit history
- Fetch languages
- Fetch README / project structure

### **3. AI Analysis Module**

- Resume vs JD match
- GitHub authenticity evaluation
- Generate structured report

### **4. Report Generator Module**

Outputs JSON:

```json
{
  "candidate": "",
  "github_username": "",
  "resume_score": 78,
  "authenticity_score": 85,
  "jd_fit_score": 80,
  "overall_fit_score": 82,
  "summary": "",
  "strengths": [],
  "red_flags": [],
  "projects": []
}

```

### **5. Database Module**

- Insert candidate
- Fetch reports
- Compare candidates

### **6. Comparison Module**

- Compare multiple candidate reports
- Generate ranking based on scores

---

# **Deployment Flow**

### **Backend (Render)**

- Flask + Gunicorn
- Connect to cloud DB

### **Frontend**

- React / Flutter / HTML
- API calls to backend

---

# **Future Add-ons**

- LinkedIn scraping
- Coding assignment evaluator
- Fraud detection score
- HR dashboard with role-based access

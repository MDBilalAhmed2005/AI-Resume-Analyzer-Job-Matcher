from matcher import calculate_match_score


def rank_resumes(resumes, job_description):
    results = []

    for resume_name, resume_text in resumes:

        score = calculate_match_score(
            resume_text,
            job_description
        )

        results.append({
            "Candidate": resume_name,
            "Score": score
        })

    results.sort(
        key=lambda x: x["Score"],
        reverse=True
    )

    for index, result in enumerate(results, start=1):
        result["Rank"] = index

    return results
from data.careers import CAREERS


def analyze_skills(user_skills, career):

    required_skills = CAREERS[career]["skills"]

    user_skills = [skill.strip().lower() for skill in user_skills]
    required_lower = [skill.lower() for skill in required_skills]

    matched = []
    missing = []

    for i, skill in enumerate(required_lower):
        if skill in user_skills:
            matched.append(required_skills[i])
        else:
            missing.append(required_skills[i])

    score = int((len(matched) / len(required_skills)) * 100)

    return matched, missing, score


def get_recommendations(career):

    career_data = CAREERS[career]

    projects = career_data["projects"]
    courses = career_data["courses"]
    learning_time = career_data["time"]

    return projects, courses, learning_time
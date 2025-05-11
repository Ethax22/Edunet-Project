
roadmaps = {
    "Idea": ["Validate idea", "Talk to users", "Build Lean Canvas"],
    "MVP": ["Build prototype", "Get feedback", "Iterate"],
    "Product-Market Fit": ["Growth channels", "User retention", "Metrics"],
    "Scaling": ["Hire team", "Infrastructure", "Automate operations"],
    "Fundraising": ["Prepare pitch deck", "Identify investors", "Practice pitching"]
}

def generate_roadmap(stage):
    return roadmaps.get(stage, ["General business advice"])

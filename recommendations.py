
resources = {
    "Idea": ["Lean Startup Book", "Startup School by YC"],
    "MVP": ["Figma tutorials", "No-code tools guide"],
    "Fundraising": ["Pitch Deck Template", "List of Angel Investors"]
}

def get_resources(stage):
    return resources.get(stage, ["Read generic startup blogs"])

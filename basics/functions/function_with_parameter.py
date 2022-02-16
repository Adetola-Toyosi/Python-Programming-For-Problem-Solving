def escape_by(plan):
    if plan == "jumping over":
        return "We cannot escape that way! The boulder is too big"
    elif plan == "running around":
        return "We cannot escape that way! The boulder is moving too fast"
    elif plan == "going deeper":
        return "That might not work! Let's go deeper"
    else:
        return "We cannot escape that way, the boulder is in the way"

print(escape_by("jumping over"))
print(escape_by("running around"))
print(escape_by("going deeper"))


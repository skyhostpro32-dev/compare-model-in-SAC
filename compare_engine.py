import pandas as pd

def compare_stories(story_a, story_b):

    rows = []

    widgets_a = {
        item["widget"]: item["measure"]
        for item in story_a["widgets"]
    }

    widgets_b = {
        item["widget"]: item["measure"]
        for item in story_b["widgets"]
    }

    all_widgets = set(widgets_a.keys()).union(
        widgets_b.keys()
    )

    for widget in all_widgets:

        measure_a = widgets_a.get(widget, "N/A")
        measure_b = widgets_b.get(widget, "N/A")

        status = (
            "Same"
            if measure_a == measure_b
            else "Different"
        )

        rows.append({
            "Widget": widget,
            "Story A Measure": measure_a,
            "Story B Measure": measure_b,
            "Status": status
        })

    return pd.DataFrame(rows)

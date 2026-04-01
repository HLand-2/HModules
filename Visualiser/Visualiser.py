def draw_bar_chart(data_dict):
    """Simple text-based bar chart for the console."""
    print("\n--- DATA VISUALISATION ---")
    for key, value in data_dict.items():
        bar = "█" * int(value)
        print(f"{key:10} | {bar} ({value})")

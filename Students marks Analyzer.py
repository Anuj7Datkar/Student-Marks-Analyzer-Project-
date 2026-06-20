def calculate_grade(average):
    """Assigns letter grades based on average benchmarks."""
    if average >= 90: return 'A'
    elif average >= 80: return 'B'
    elif average >= 70: return 'C'
    elif average >= 60: return 'D'
    else: return 'F'

def analyze_student_marks():
    print("--- Student Marks Analyzer ---")
    
    # Collect number of students
    try:
        num_students = int(input("Enter the number of students: "))
    except ValueError:
        print("Invalid number. Exiting.")
        return

    students_data = {}
    
    # Input data cycle
    for i in range(num_students):
        name = input(f"\nEnter name for student {i+1}: ").strip()
        while True:
            try:
                mark = float(input(f"Enter marks for {name} (0-100): "))
                if 0 <= mark <= 100:
                    students_data[name] = mark
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid numeric value.")

    if not students_data:
        return

    # Statistical Math
    all_marks = list(students_data.values())
    class_average = sum(all_marks) / len(all_marks)
    highest_mark = max(all_marks)
    lowest_mark = min(all_marks)
    
    # Identify top scorers
    toppers = [name for name, mark in students_data.items() if mark == highest_mark]

    # Generate Performance Report
    print("\n" + "="*35)
    print(f"{'Name':<15}{'Score':<10}{'Grade':<10}")
    print("="*35)
    for name, mark in students_data.items():
        grade = calculate_grade(mark)
        print(f"{name:<15}{mark:<10.2f}{grade:<10}")
    print("="*35)
    
    # Summary Dashboard
    print(f"Class Average: {class_average:.2f}")
    print(f"Highest Mark:  {highest_mark:.2f} ({', '.join(toppers)})")
    print(f"Lowest Mark:   {lowest_mark:.2f}")
    print("="*35)

if __name__ == "__main__":
    analyze_student_marks()

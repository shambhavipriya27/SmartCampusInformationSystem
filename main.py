"""
Smart Campus Information System - Fully Integrated Application
All modules work together using shared data throughout the system
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ====================== CUSTOM EXCEPTIONS ======================
class MissingFileOrFolderError(Exception):
    """Raised when a required file or folder is missing"""
    pass


# ====================== MAIN SYSTEM CLASS ======================
class SmartCampusSystem:
    """Fully integrated Smart Campus Information System"""
    
    def __init__(self):
        # Student data storage
        self.students = []           # List of student dictionaries
        self.student_ids = []        # List of student IDs
        
    # ====================== MODULE 1: Student Registration with Grade ======================
    def register_student(self):
        """Register a new student with grade evaluation"""
        print("\n" + "="*50)
        print("STUDENT REGISTRATION")
        print("="*50)
        
        # Basic student details
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        
        # Validate and collect exam score
        while True:
            try:
                score = float(input("Enter Exam Score (0-100): "))
                if 0 <= score <= 100:
                    break
                else:
                    print("Score must be between 0 and 100!")
            except ValueError:
                print("Invalid input! Please enter a number.")
        
        # Grade evaluation
        if score >= 90:
            grade = "A"
            remark = "Excellent"
        elif score >= 75:
            grade = "B"
            remark = "Very Good"
        elif score >= 60:
            grade = "C"
            remark = "Good"
        elif score >= 40:
            grade = "D"
            remark = "Average"
        else:
            grade = "F"
            remark = "Needs Improvement"
        
        # Store student data
        student = {
            "id": student_id,
            "name": name,
            "age": int(age),
            "score": score,
            "grade": grade,
            "remark": remark,
            "courses": []  # Will store enrolled courses with credits
        }
        
        self.students.append(student)
        if student_id.isdigit():
            self.student_ids.append(int(student_id))
        else:
            self.student_ids.append(student_id)
        
        # Display result
        print("\n--- Registration Successful ---")
        print(f"Student ID: {student_id}")
        print(f"Name: {name}")
        print(f"Score: {score}")
        print(f"Grade: {grade}")
        print(f"Remark: {remark}")
        
        return student
    
    # ====================== MODULE 2: Course Enrollment with Credits ======================
    def enroll_courses(self):
        """Enroll student in courses with credit validation"""
        if not self.students:
            print("\nNo student registered! Please register a student first.")
            return
        
        print("\n" + "="*50)
        print("COURSE ENROLLMENT SYSTEM")
        print("="*50)
        
        # Select student
        self.display_student_list()
        student_idx = self.select_student()
        if student_idx is None:
            return
        
        student = self.students[student_idx]
        courses = []
        max_courses = 5
        
        print(f"\nEnrolling courses for {student['name']}")
        print("Maximum courses allowed: 5\n")
        
        while True:
            if len(courses) >= max_courses:
                print("Maximum course limit reached!")
                break
            
            course_name = input("Enter course name (or 'done' to finish): ")
            if course_name.lower() == "done":
                break
            
            if not course_name.strip():
                print("Course name cannot be empty! Skipping...")
                continue
            
            credits = input("Enter credit value: ")
            
            # Validation
            if not credits.isdigit():
                print("Invalid credit value! Skipping entry...")
                continue
            
            credits = int(credits)
            if credits <= 0:
                print("Credit must be positive! Skipping entry...")
                continue
            
            # Valid entry - add to list
            courses.append((course_name, credits))
            print(f"Course '{course_name}' with {credits} credits added.\n")
        
        student["courses"] = courses
        
        # Output display
        print("\n--- Enrollment Report ---")
        total_credits = 0
        for course, credit in courses:
            print(f"Course: {course}, Credits: {credit}")
            total_credits += credit
        print(f"Total courses enrolled: {len(courses)}")
        print(f"Total credits: {total_credits}")
    
    # ====================== MODULE 3: Student Records with Event Analysis ======================
    def manage_records(self):
        """Display and manage student records with event analysis"""
        if not self.students:
            print("\nNo student records found! Please register students first.")
            return
        
        print("\n" + "="*50)
        print("STUDENT RECORDS")
        print("="*50)
        
        for student in self.students:
            print(f"\nID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Exam Score: {student['score']}")
            print(f"Grade: {student['grade']} - {student['remark']}")
            
            if student.get('courses'):
                print("Enrolled Courses:")
                for course, credit in student['courses']:
                    print(f"  - {course} (Credits: {credit})")
            print("-" * 30)
        
        # Event participation analysis using sets
        print("\n--- EVENT PARTICIPATION ANALYSIS ---")
        
        # Get event participants from user
        event_a_input = input("Enter Event A participant names (separated by commas): ")
        event_b_input = input("Enter Event B participant names (separated by commas): ")
        
        event_A = set(name.strip() for name in event_a_input.split(',') if name.strip())
        event_B = set(name.strip() for name in event_b_input.split(',') if name.strip())
        
        print(f"\nEvent A Participants: {event_A}")
        print(f"Event B Participants: {event_B}")
        print(f"Common Participants (Intersection): {event_A & event_B}")
        print(f"All Participants (Union): {event_A | event_B}")
        print(f"Only Event A (Difference A - B): {event_A - event_B}")
        print(f"Only Event B (Difference B - A): {event_B - event_A}")
    
    # ====================== MODULE 4: Sorting and Searching ======================
    def bubble_sort_ids(self):
        """Sort student IDs using Bubble Sort"""
        if not self.student_ids:
            print("\nNo student IDs available!")
            return []
        
        arr = self.student_ids.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    
    def selection_sort_ids(self):
        """Sort student IDs using Selection Sort"""
        if not self.student_ids:
            print("\nNo student IDs available!")
            return []
        
        arr = self.student_ids.copy()
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
    
    def linear_search_id(self, target):
        """Search for student ID using Linear Search"""
        for i, student_id in enumerate(self.student_ids):
            if student_id == target:
                return i
        return -1
    
    def binary_search_id(self, target):
        """Search for student ID using Binary Search"""
        sorted_ids = sorted(self.student_ids)
        low, high = 0, len(sorted_ids) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if sorted_ids[mid] == target:
                for i, original_id in enumerate(self.student_ids):
                    if original_id == target:
                        return i
                return mid
            elif sorted_ids[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    
    def sorting_searching_menu(self):
        """Handle sorting and searching operations"""
        if not self.student_ids:
            print("\nNo students registered! Please register students first.")
            return
        
        print("\n" + "="*50)
        print("SORTING & SEARCHING STUDENT IDs")
        print("="*50)
        
        print(f"\nOriginal Student IDs: {self.student_ids}")
        
        bubble_sorted = self.bubble_sort_ids()
        selection_sorted = self.selection_sort_ids()
        
        print(f"\nBubble Sort Result: {bubble_sorted}")
        print(f"Selection Sort Result: {selection_sorted}")
        
        print("\n--- SEARCH STUDENT ---")
        
        
        try:
            target = input("\nEnter Student ID to search: ")
            if target.isdigit():
                target = int(target)
            
            linear_idx = self.linear_search_id(target)
            if linear_idx != -1:
                student = self.students[linear_idx]
                print(f"\nLinear Search: Found '{student['name']}' at index {linear_idx}")
            else:
                print("\nLinear Search: Student ID not found")
            
            binary_idx = self.binary_search_id(target)
            if binary_idx != -1:
                student = self.students[binary_idx]
                print(f"Binary Search: Found '{student['name']}' at index {binary_idx}")
            else:
                print("Binary Search: Student ID not found")
                
        except Exception as e:
            print(f"Error: {e}")
    
    # ====================== MODULE 5: Fee Calculation ======================
    def calculate_fee(self, tuition_fee, hostel_fee=0, transportation_fee=0):
        """Calculate total fee"""
        total_fee = tuition_fee + hostel_fee + transportation_fee
        return total_fee
    
    def fee_calculation_menu(self):
        """Handle fee calculation for students"""
        if not self.students:
            print("\nNo students registered! Please register students first.")
            return
        
        print("\n" + "="*50)
        print("FEE CALCULATION SYSTEM")
        print("="*50)
        
        # First get fee components from user
        print("\nEnter fee structure:")
        while True:
            try:
                tuition = float(input("Enter Tuition Fee: "))
                if tuition >= 0:
                    break
                else:
                    print("Fee cannot be negative!")
            except ValueError:
                print("Invalid input!")
        
        while True:
            try:
                hostel = float(input("Enter Hostel Fee: "))
                if hostel >= 0:
                    break
                else:
                    print("Fee cannot be negative!")
            except ValueError:
                print("Invalid input!")
        
        while True:
            try:
                transport = float(input("Enter Transportation Fee: "))
                if transport >= 0:
                    break
                else:
                    print("Fee cannot be negative!")
            except ValueError:
                print("Invalid input!")
        
        # Display options
        print("\n--- Fee Calculation Options ---")
        print("1. Tuition Fee only")
        print("2. Tuition + Hostel Fee")
        print("3. Tuition + Hostel + Transportation Fee")
        
        # Calculate fee for each student
        print("\n--- Fee Calculation for Students ---")
        for student in self.students:
            print(f"\nStudent: {student['name']} (ID: {student['id']})")
            
            while True:
                try:
                    choice = int(input("Select fee option (1/2/3): "))
                    if choice in [1, 2, 3]:
                        break
                    else:
                        print("Invalid choice! Select 1, 2, or 3")
                except ValueError:
                    print("Invalid input!")
            
            if choice == 1:
                total = self.calculate_fee(tuition)
                print(f"Total Fee (Tuition only): Rs.{total}")
            elif choice == 2:
                total = self.calculate_fee(tuition, hostel_fee=hostel)
                print(f"Total Fee (Tuition + Hostel): Rs.{total}")
            else:
                total = self.calculate_fee(tuition, hostel_fee=hostel, transportation_fee=transport)
                print(f"Total Fee (Tuition + Hostel + Transport): Rs.{total}")
            
            # Store fee in student record
            student['total_fee'] = total
    
    # ====================== MODULE 6: File Handling (CSV) ======================
    def file_handling(self):
        """Save to CSV, display data, and generate report automatically"""
        if not self.students:
            print("\nNo data to save! Please register students first.")
            return
        
        filename = "student_records.csv"
        
        # Prepare data for CSV - only id, name, marks
        data = []
        for student in self.students:
            row = {
                "ID": student['id'],
                "Name": student['name'],
                "Marks": student['score']
            }
            data.append(row)
        
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f"\nRecords saved to '{filename}'")
        
        # Display the CSV data
        print("\nData stored in CSV file:")
        print("-"*40)
        print(df.to_string(index=False))
        
        # Generate report
        print("\nGenerating Report:")
        print("-"*40)
        
        total_students = len(self.students)
        total_scores = sum(s['score'] for s in self.students)
        avg_score = total_scores / total_students if total_students > 0 else 0
        
        grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
        for student in self.students:
            grade_counts[student['grade']] += 1
        
        top_student = max(self.students, key=lambda x: x['score'])
        
        print(f"Total Students: {total_students}")
        print(f"Average Exam Score: {avg_score:.2f}")
        print(f"Highest Score: {top_student['score']} scored by {top_student['name']}")
        
        
    
    # ====================== MODULE 7: Directory Scanning ======================
    def scan_directory(self):
        """Scan any directory on the device"""
        print("\n" + "="*50)
        print("DIRECTORY SCANNER")
        print("="*50)
        
        path = input("\nEnter the directory path to scan: ")
        
        try:
            if not os.path.exists(path):
                raise FileNotFoundError(f"Directory '{path}' does not exist!")
            
            if not os.path.isdir(path):
                raise NotADirectoryError(f"'{path}' is not a directory!")
            
            print(f"\nScanning directory: {path}")
            print("-"*50)
            
            files_found = False
            
            for root, dirs, files in os.walk(path):
                level = root.replace(path, "").count(os.sep)
                indent = "  " *4* level
                folder_name = os.path.basename(root)
                if folder_name:
                    print(f"{indent}{folder_name}/")
                else:
                    print(f"{indent}{path}/")
                
                sub_indent = "  " *4* (level + 1)
                for file in files:
                    print(f"{sub_indent}{file}")
                    files_found = True
            
            if not files_found:
                print("No files found in this directory!")
            else:
                print(f"\nScan completed successfully!")
            
        except FileNotFoundError as e:
            print(f"Error: {e}")
        except NotADirectoryError as e:
            print(f"Error: {e}")
        except PermissionError as e:
            print(f"Permission Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
    
    # ====================== MODULE 8: Performance Analytics using CSV ======================
    def performance_analytics(self):
        """Analyze student performance using CSV file data"""
        
        # Check if CSV file exists
        if not os.path.exists("student_records.csv"):
            print("\n" + "="*50)
            print("ERROR: CSV file not found!")
            print("="*50)
            print("\nPlease follow these steps:")
            print("1. Register students using option 1")
            print("2. Use option 6 to save records to CSV")
            print("3. Then use option 8 for Performance Analytics")
            print("\nThe CSV file 'student_records.csv' is required for analysis.")
            return
        
        print("\n" + "="*50)
        print("PERFORMANCE ANALYTICS")
        print("="*50)
        
        try:
            # Load data from CSV file
            df = pd.read_csv("student_records.csv")
            
            print("\n--- Data from student_records.csv ---")
            print(df.to_string(index=False))
            
            # Statistical summary using Pandas
            print("\n--- Statistical Summary (Pandas) ---")
            print(df['Marks'].describe())
            
            # NumPy analysis
            print("\n--- NumPy Analysis ---")
            marks_array = df['Marks'].to_numpy()
            print(f"Mean Marks: {np.mean(marks_array):.2f}")
            print(f"Median Marks: {np.median(marks_array):.2f}")
            print(f"Standard Deviation: {np.std(marks_array):.2f}")
            print(f"Min Marks: {np.min(marks_array)}")
            print(f"Max Marks: {np.max(marks_array)}")
            
            # Percentiles
            percentiles = np.percentile(marks_array, [25, 50, 75])
            print(f"\n25th Percentile: {percentiles[0]:.2f}")
            print(f"50th Percentile (Median): {percentiles[1]:.2f}")
            print(f"75th Percentile: {percentiles[2]:.2f}")
            
            
            
            # Create bar graph for all students' marks together
            self.create_performance_charts(df)
            
        except Exception as e:
            print(f"Error in analytics: {e}")
    
    def create_performance_charts(self, df):
        """Create bar graph for all student exam marks together"""
        
        plt.figure(figsize=(10, 6))
        
        # Sort by marks for better visualization
        df_sorted = df.sort_values('Marks', ascending=False)
        
        bars = plt.bar(df_sorted['Name'], df_sorted['Marks'], 
                      color='skyblue', edgecolor='black')
        
        plt.title('All Students Exam Marks', fontsize=14, fontweight='bold')
        plt.xlabel('Student Name', fontsize=12)
        plt.ylabel('Marks', fontsize=12)
        plt.ylim(0, 100)
        
        # Add marks values on top of bars
        for bar, marks in zip(bars, df_sorted['Marks']):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
                    f'{marks:.0f}', ha='center', fontsize=10, fontweight='bold')
        
        # Add average line
        avg_marks = df['Marks'].mean()
        plt.axhline(y=avg_marks, color='red', linestyle='--', 
                   label=f'Average: {avg_marks:.1f}')
        plt.legend()
        
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
        
        print("\nPerformance chart displayed for all students!")
    
    # ====================== HELPER METHODS ======================
    def display_student_list(self):
        """Display list of registered students"""
        print("\nRegistered Students:")
        print("-" * 30)
        for i, student in enumerate(self.students):
            print(f"{i+1}. {student['name']} (ID: {student['id']}) - Grade: {student['grade']}")
    
    def select_student(self):
        """Select a student from the list"""
        if not self.students:
            return None
        
        try:
            choice = int(input(f"\nSelect student (1-{len(self.students)}): ")) - 1
            if 0 <= choice < len(self.students):
                return choice
            else:
                print("Invalid selection!")
                return None
        except ValueError:
            print("Invalid input!")
            return None
    
    # ====================== MAIN DASHBOARD ======================
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*60)
        print("   SMART CAMPUS INFORMATION SYSTEM")
        print("   Dayananda Sagar College of Engineering")
        print("="*60)
        print("\nMAIN MENU")
        print("-" * 40)
        print("1.  Student Registration & Grade Evaluation")
        print("2.  Course Enrollment Management")
        print("3.  Student Records Management")
        print("4.  Sorting & Searching Student IDs")
        print("5.  Fee Calculation")
        print("6.  File Handling")
        print("7.  Directory Scanning")
        print("8.  Performance Analytics")
        print("0.  Exit")
        print("-" * 40)
        
        if self.students:
            print(f"\nSystem Status: {len(self.students)} student(s) registered")
        
    
    def run(self):
        """Main program loop"""
        print("\nWelcome to Smart Campus Information System!")
        
        while True:
            self.display_menu()
            
            choice = input("\nEnter your choice: ")
            
            if choice == "1":
                self.register_student()
            elif choice == "2":
                self.enroll_courses()
            elif choice == "3":
                self.manage_records()
            elif choice == "4":
                self.sorting_searching_menu()
            elif choice == "5":
                self.fee_calculation_menu()
            elif choice == "6":
                self.file_handling()
            elif choice == "7":
                self.scan_directory()
            elif choice == "8":
                self.performance_analytics()
            elif choice == "0":
                print("\nThank you for using Smart Campus Information System!")
                print("Have a great day!")
                break
            else:
                print("\nInvalid choice! Please try again.")
            
            input("\nPress Enter to continue...")


# ====================== PROGRAM ENTRY POINT ======================
if __name__ == "__main__":
    system = SmartCampusSystem()
    system.run()

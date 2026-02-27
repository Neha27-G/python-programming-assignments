import pandas as pd
import matplotlib.pyplot as plt


def main():


#########################################################################################################
# 1:Load the data set
#########################################################################################################
    Border="-"*100
    print(Border)
    print("1:Load the data set")
    print(Border)

    df = pd.read_csv("student_performance_ml.csv")

    print("---------------------------First 5 Records------------------------------\n")
    print(df.head())

    print("---------------------------Last 5 Records-------------------------------\n")
    print(df.tail())

    print("------------------------Total Rows and columns--------------------------\n")
    print("Rows :",df.shape[0])
    print("Columns:",df.shape[1])

    print("------------------------------Column Names------------------------------\n")
    print(df.columns.tolist)

    print("------------------------------Data Types---------------------------------\n")
    print(df.dtypes)

#########################################################################################################
# 2:Basic Counts
#########################################################################################################
    Border="-"*100
    print(Border)
    print("2: Basic Counts")
    print(Border)

    print("\n--------------------------Total Number of Student-------------------------")
    print(len(df))

    print("\n--------------------------Number of Student Passed-------------------------")
    passed = df[df["FinalResult"] == 1].shape[0]
    print(passed)

    print("\n--------------------------Number of Student Failed-------------------------")
    failed = df[df["FinalResult"] == 0].shape[0]
    print(failed)

#########################################################################################################
# 3:Calculations using pandas functions
#########################################################################################################
    Border="-"*100
    print(Border)
    print(" 3:Calculations using pandas functions")
    print(Border)

    print("\n-----------------------------Average Study Hours---------------------------")
    print(df["StudyHours"].mean())

    print("\n-----------------------------Average Attendence-----------------------------")
    print(df["Attendance"].mean())

    print("\n-----------------------------Maximum Previous score-----------------------------")
    print(df["PreviousScore"].max())

    print("\n-----------------------------Minimum Sleep Hours--------------------------------")
    print(df["SleepHours"].min())
  
#########################################################################################################
# 4. Value Counts and Percentage Distribution
#########################################################################################################
    Border="-"*100
    print(Border)
    print(" 4. Value Counts and Percentage Distribution")
    print(Border)

    print("\n------------------ FINAL RESULT DISTRIBUTION ----------------------------------------")
    result_counts = df["FinalResult"].value_counts()
    print(result_counts)

    percentage = df["FinalResult"].value_counts(normalize=True) * 100
    print("\n-------------------------- PERCENTAGE DISTRIBUTION ----------------------------------")
    print(percentage)

    if abs(percentage[1] - percentage[0]) < 10:
        print("\nDataset is approximately balanced.")
    else:
        print("\nDataset is imbalanced.")

#########################################################################################################
# 5. Analysis (Simple Observation)
#########################################################################################################
    Border="-"*100
    print(Border)
    print(" 5. Analysis (Simple Observation)")
    print(Border)

    
    avg_study_pass = df[df["FinalResult"] == 1]["StudyHours"].mean()
    avg_study_fail = df[df["FinalResult"] == 0]["StudyHours"].mean()

    avg_attendance_pass = df[df["FinalResult"] == 1]["Attendance"].mean()
    avg_attendance_fail = df[df["FinalResult"] == 0]["Attendance"].mean()

    print("Average StudyHours (Pass):", avg_study_pass)
    print("Average StudyHours (Fail):", avg_study_fail)

    print("Average Attendance (Pass):", avg_attendance_pass)
    print("Average Attendance (Fail):", avg_attendance_fail)

    if avg_study_pass > avg_study_fail:
        print("Higher StudyHours increase the chance of passing.")

    if avg_attendance_pass > avg_attendance_fail:
        print("Higher Attendance improves FinalResult.")

#########################################################################################################
# 6. Histogram of StudyHours
#########################################################################################################
    Border="-"*100
    print(Border)
    print(" 6. Histogram of StudyHours")
    print(Border)

    
    plt.figure()
    plt.hist(df["StudyHours"], bins=10)
    plt.title("Histogram of StudyHours")
    plt.xlabel("StudyHours")
    plt.ylabel("Frequency")
    plt.show()

#########################################################################################################
# 7. Scatter Plot: StudyHours vs PreviousScore
#########################################################################################################
    Border="-"*100
    print(Border)
    print(" 7. Scatter Plot: StudyHours vs PreviousScore")
    print(Border)

    plt.figure()
    plt.scatter(df["StudyHours"], df["PreviousScore"])
    plt.title("StudyHours vs PreviousScore")
    plt.xlabel("StudyHours")
    plt.ylabel("PreviousScore")
    plt.show()

#########################################################################################################
# 8: Box Plot for Attendance
#########################################################################################################

    Border="-"*100
    print(Border)
    print("8: Box Plot for Attendance")
    print(Border)

    plt.figure()
    plt.boxplot(df["Attendance"])
    plt.title("Box Plot of Attendance")
    plt.ylabel("Attendance")
    plt.show()

    print("\nObservation:")
    print("If there are points outside the whiskers, they are outliers.")
    print("If no points appear outside, then no significant outliers are present.")

#########################################################################################################
# 9: AssignmentsCompleted vs FinalResult
#########################################################################################################

    Border="-"*100
    print(Border)
    print("9: AssignmentsCompleted vs FinalResult")
    print(Border)

    plt.figure()

    # Pass students
    plt.scatter(df[df["FinalResult"]==1]["AssignmentsCompleted"],
                df[df["FinalResult"]==1]["FinalResult"],
                label="Pass",
                color="green")

    # Fail students
    plt.scatter(df[df["FinalResult"]==0]["AssignmentsCompleted"],
                df[df["FinalResult"]==0]["FinalResult"],
                label="Fail",
                color="red")

    plt.title("AssignmentsCompleted vs FinalResult")
    plt.xlabel("AssignmentsCompleted")
    plt.ylabel("FinalResult (0=Fail, 1=Pass)")
    plt.legend()
    plt.show()

    print("\nObservation:")
    print("Students who completed more assignments tend to pass.")
    print("Lower assignment completion is mostly associated with failure.")

#########################################################################################################
# 10: SleepHours vs FinalResult
#########################################################################################################

    Border="-"*100
    print(Border)
    print("10: SleepHours vs FinalResult")
    print(Border)

    plt.figure()

    # Pass students
    plt.scatter(df[df["FinalResult"]==1]["SleepHours"],
                df[df["FinalResult"]==1]["FinalResult"],
                label="Pass",
                color="blue")

    # Fail students
    plt.scatter(df[df["FinalResult"]==0]["SleepHours"],
                df[df["FinalResult"]==0]["FinalResult"],
                label="Fail",
                color="orange")

    plt.title("SleepHours vs FinalResult")
    plt.xlabel("SleepHours")
    plt.ylabel("FinalResult (0=Fail, 1=Pass)")
    plt.legend()
    plt.show()

    print("\nObservation:")
    print("Sleeping more does not guarantee success.")
    print("Both pass and fail students may have similar sleep hours.")
    print("Balanced sleep helps, but study and attendance matter more.")


if __name__=="__main__":
        main()
from sklearn.metrics import classification_report

def main():

    # Actual and Predicted values
    actual = [1,1,1,1,0,0,0,0]
    predicted = [1,1,0,1,0,1,0,0]

    # Generate classification report
    report = classification_report(actual, predicted)

    # Display report
    print("Classification Report:\n")
    print(report)


if __name__ == "__main__":
    main()
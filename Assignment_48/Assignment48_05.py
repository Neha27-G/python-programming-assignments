from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def main():

    # Actual and Predicted values
    actual = [1,1,1,1,0,0,0,0]
    predicted = [1,1,0,1,0,1,0,0]

    # Generate confusion matrix
    cm = confusion_matrix(actual, predicted)

    # Extract TN, FP, FN, TP
    tn, fp, fn, tp = cm.ravel()

    # Print confusion matrix values
    print("Confusion Matrix:")
    print(cm)

    print("\nTP:", tp)
    print("TN:", tn)
    print("FP:", fp)
    print("FN:", fn)

    # Plot confusion matrix graph
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()

    plt.title("Confusion Matrix")
    plt.show()


if __name__ == "__main__":
    main()
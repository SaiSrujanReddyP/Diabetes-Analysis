data = pd.read_csv(r'C:\Users\hellb\Projects\diaanalysis\diabetes-dataset.csv')

        X = data.drop('Outcome', axis=1)
        Y = data['Outcome']
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30)

        model = LogisticRegression()
        model.fit(X_train, Y_train)
        
        val1 = float(request.POST['n1'])  # Change request.GET to request.POST
        val2 = float(request.POST['n2'])
        val3 = float(request.POST['n3'])
        val4 = float(request.POST['n4'])
        val5 = float(request.POST['n5'])
        val6 = float(request.POST['n6'])
        val7 = float(request.POST['n7'])
        val8 = float(request.POST['n8'])

        pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])

        result1 = "5"

        if pred == [1]:
            result1 = "positive"
        else:
            result1 = "negative"

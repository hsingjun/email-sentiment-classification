
———————————————————————————Summary of Python Scripts———————————————————
——data preprocessing—— 
1. enron_preprocess.py  (train_PDF, test_PDF)
   Preprocessing enron data into Projct Data Format. The labeled data are transformed into the train_PDF file. The unlabeled testing data are transformed into the test_PDF file. Directories that contains spam files ('./enron1/spam', './enron2/spam', './enron4/spam', './enron5/spam'), ham files ('./enron1/ham', './enron2/ham', './enron4/ham', './enron5/ham') and test files ('./spam_or_ham_test') are hard coded in the script. Directories 'enron1', 'enron2', 'enron4', 'enron5' and 'spam_or_ham_test' should be placed in the same directory as the script
   
2. imdb_preprocess.py   (raw_file, formatted_file)
   Preprocessing imdb data into Project Data Format. It can deal with both training data (with label) and testing data (without label). If there is label in the raw_file, it transforms the review score into POSITIVE/NEGATIVE label based the rule that if score>=7, label POSITIVE; if score<=4, label NEGATIVE. For both labeled and unlabeled data, increment the feature index by 1.
   
3. split_data.py    (train_PDF, train, test, label, train_ratio)
   Split the whole labeled data into training set (with labels) and testing set (without labels). The actual labels of the testing set is stored in the 'label' file. The percentage of the training data among the whole set is specified by the parameter 'train_ratio)
   
4. preprocess_svm.py    (train_PDF, train_SVM, test_PDF, test_SVM)
   Transform training and testing data in PDF into SVM required format. For training data, transform POSITIVE/NEGATIVE label to +1/-1. For test data, add +1 as an arbitrary label at the beginning of each line.
   
5. preprocess_mega.py   (train_PDF, train_mega, test_PDF, test_mega)
   Transform training and testing data in PDF into MegaM required format. For training data, transform POSITIVE/NEGATIVE label to 1/0. For test data, add +1 as an arbitrary label at the beginning of each line. For both training and test data, replace the ':' between feature and value with a blank space.

6. trans_label.py   (numeric_label, alphabetic_label, dataname)
   Transform numeric label (output from SVM-Light or MegaM) to alphabetic label: if numeric label > 0 -> POSITIVE/SPAM, else -> NEGATIVE/HAM. Parameter 'dataname' takes value 'imdb' or 'email'. If dataname = 'imdb', it converts numeric label to POSITIVE/NEGATIVE. If dataname = 'email', it converts numberic label to SPAM/HAM.

——Naive Bayes model training—— 
1. nblearn.py   (trainingfile, modelfile)
   Generate modelfIne from training file
   modelfile: 1st line: dataname ('imdb' or 'email')
              2nd line: P(POSITIVE)
              3rd line: P(NEGATIVE)
              4th line: [P(feature(i)|POSITIVE)]
              5th line: [P(feature(i)|NEGATIVE)]
   
2. nbclassify.py   (modelfile, testfile)
   Do classification on test file using model file

——Result processing—
1. evaluation.py    (true_label, predict_label)
   Compares the predict_label with true_label. Output the precision, recall, f1 score and accuracy.





    
—————————————————————————————Summary of Commands———————————————————————
———Data Preprocessing——
1.Convert data into project format.
    Sentiment:        
        $ python3 imdb_preprocess.py labeledBow.feat imdb_formatted
        $ python3 imdb_preprocess.py sentiment_test sentiment_test_formatted
    Spam:
        $ python3 enron_preprocess.py enron_formatted spam_test_formatted

2.Split data into training and testing groups.
    Sentiment:
        $ python3 split_data.py imdb_formatted imdb_trainT1 imdb_testT1 imdb_labelT1 0.75
        $ python3 split_data.py imdb_formatted imdb_trainT2 imdb_testT2 imdb_labelT2 0.25
    Spam:
        $ python3 split_data.py enron_formatted enron_trainT1 enron_testT1 enron_labelT1 0.75
        $ python3 split_data.py enron_formatted enron_trainT2 enron_testT2 enron_labelT2 0.25
      
———————75% training 25% testing———————
1.Sentiment:
    a.Naive Bayes
        Command:
            $ python3 nblearn.py imdb_trainT1 imdb_nb_modelT1
            $ python3 nbclassify.py imdb_nb_modelT1 imdb_testT1 > imdb_nb_predT1
            $ python3 evaluation.py imdb_labelT1 imdb_nb_predT1 > imdb_nbT1f1
        Result:
            precision(Pos) = 0.8714581893572909
            precision(Neg) = 0.8256853396901073
            recal(Pos) = 0.8117154811715481
            recal(Neg) = 0.881641743557111
            f1(Pos) = 0.8405265789035161
            f1(Neg) = 0.8527465763963686
            Accuracy = 0.84688
            
    b.SVM-Light
        Command:
            $ python3 preprocess_svm.py imdb_trainT1 imdb_svm_trainT1 imdb_testT1 imdb_svm_testT1
            $ ./svm_learn imdb_svm_trainT1 imdb_svm_modelT1
            $ ./svm_classify imdb_svm_testT1 imdb_svm_modelT1 imdb_svm_outputT1
            $ python3 trans_label.py imdb_svm_outputT1 imdb_svm_predT1 imdb
            $ python3 evaluation.py imdb_labelT1 imdb_svm_predT1 > imdb_svmT1f1
        Result:
            precision(Pos) = 0.8601442458450925
            precision(Neg) = 0.8810846128716106
            recal(Pos) = 0.8828451882845189
            recal(Neg) = 0.858097359210945
            f1(Pos) = 0.8713468869123253
            f1(Neg) = 0.8694390715667311
            Accuracy = 0.8704
    
    c.MegaM
        Command:
            $ python3 preprocess_mega.py imdb_trainT1 imdb_mega_trainT1 imdb_testT1 imdb_mega_testT1
            $ ./megam_i686.opt -fvals binary imdb_mega_trainT1 > imdb_mega_modelT1
            $ ./megam_i686.opt -fvals -predict imdb_mega_modelT1 binary imdb_mega_testT1 > imdb_mega_outputT1
            $ python3 trans_label.py imdb_mega_outputT1 imdb_mega_predT1 imdb
            $ python3 evaluation.py imdb_labelT1 imdb_mega_predT1 > imdb_megaT1f1
        Result:
            precision(Pos) = 0.8748793824380829
            precision(Neg) = 0.8767908309455588
            recal(Pos) = 0.8754425490827165
            recal(Neg) = 0.8762328985046134
            f1(Pos) = 0.8751608751608752
            f1(Neg) = 0.8765117759388925
            Accuracy = 0.87584    
    
2.Spam:
    a.Naive Bayes
        Command:
            $ python3 nblearn.py enron_trainT1 enron_modelT1
            $ python3 nbclassify.py enron_modelT1 enron_testT1 > enron_predT1
            $ python3 evaluation.py enron_labelT1 enron_predT1 > enron_nbT1f1
        Result:
            precision(Pos) = 0.9781021897810219
            precision(Neg) = 0.9895287958115183
            recal(Pos) = 0.9901477832512315
            recal(Neg) = 0.9767441860465116
            f1(Pos) = 0.9840881272949816
            f1(Neg) = 0.9830949284785435
            Accuracy = 0.9836065573770492       
    
        b.SVM-Light
        Command:
            $ python3 preprocess_svm.py enron_trainT1 enron_svm_trainT1 enron_testT1 enron_svm_testT1 
            $ ./svm_learn enron_svm_trainT1 enron_svm_modelT1
            $ ./svm_classify enron_svm_testT1 enron_svm_modelT1 enron_svm_outputT1
            $ python3 trans_label.py enron_svm_outputT1 enron_svm_predT1 email
            $ python3 evaluation.py enron_labelT1 enron_svm_predT1 > enron_svmT1f1
        Result:
            precision(Pos) = 0.9325581395348838
            precision(Neg) = 0.9885871704053523
            recal(Pos) = 0.9897743300423131
            recal(Neg) = 0.9252302025782688
            f1(Pos) = 0.9603147451248717
            f1(Neg) = 0.9558599695585996
            Accuracy = 0.958205728697532
    
    c.MegaM
        Command:
            $ python3 preprocess_mega.py enron_trainT1 enron_mega_trainT1 enron_testT1 enron_mega_testT1
            $ ./megam_i686.opt -fvals binary enron_mega_trainT1 > enron_mega_modelT1
            $ ./megam_i686.opt -fvals -predict enron_mega_modelT1 binary enron_mega_testT1 > enron_mega_outputT1
            $ python3 trans_label.py enron_mega_outputT1 enron_mega_predT1 email
            $ python3 evaluation.py enron_labelT1 enron_mega_predT1 > enron_megaT1f1
        Result:
            precision(Pos) = 0.9679531357684356
            precision(Neg) = 0.9898074745186863
            recal(Pos) = 0.9904795486600846
            recal(Neg) = 0.9657458563535911
            f1(Pos) = 0.9790867898222376
            f1(Neg) = 0.9776286353467561
            Accuracy = 0.9783822734642407
    
———————25% training 75% testing———————
1.Sentiment:
    a.Naive Bayes
        Command:
            $ python3 nblearn.py imdb_trainT2 imdb_nb_modelT2
            $ python3 nbclassify.py imdb_nb_modelT2 imdb_testT2 > imdb_nb_predT2
            $ python3 evaluation.py imdb_labelT2 imdb_nb_predT2 > imdb_nbT2f1
        Result:
            precision(Pos) = 0.8590093160645308
            precision(Neg) = 0.8202653799758746
            recal(Pos) = 0.8087495988875816
            recal(Neg) = 0.8679927667269439
            f1(Pos) = 0.8331221420307422
            f1(Neg) = 0.8434544420900304
            Accuracy = 0.8384533333333334
            
    b.SVM-Light
        Command:
            $ python3 preprocess_svm.py imdb_trainT2 imdb_svm_trainT2 imdb_testT2 imdb_svm_testT2
            $ ./svm_learn imdb_svm_trainT2 imdb_svm_modelT2
            $ ./svm_classify imdb_svm_testT2 imdb_svm_modelT2 imdb_svm_outputT2
            $ python3 trans_label.py imdb_svm_outputT2 imdb_svm_predT2 imdb
            $ python3 evaluation.py imdb_labelT2 imdb_svm_predT2 > imdb_svmT2f1
        Result:
                precision(Pos) = 0.8304547777210015
                precision(Neg) = 0.8635805911879532
                recal(Pos) = 0.8691838699326131
                recal(Neg) = 0.8235294117647058
                f1(Pos) = 0.849378070450507
                f1(Neg) = 0.8430796036153761
                Accuracy = 0.8462933333333333
    
    c.MegaM
        Command:
            $ python3 preprocess_mega.py imdb_trainT2 imdb_mega_trainT2 imdb_testT2 imdb_mega_testT2
            $ ./megam_i686.opt -fvals binary imdb_mega_trainT2 > imdb_mega_modelT2
            $ ./megam_i686.opt -fvals -predict imdb_mega_modelT2 binary imdb_mega_testT2 > imdb_mega_outputT2
            $ python3 trans_label.py imdb_mega_outputT2 imdb_mega_predT2 imdb
            $ python3 evaluation.py imdb_labelT2 imdb_mega_predT2 > imdb_megaT2f1
        Result:
            precision(Pos) = 0.8431413178615831
            precision(Neg) = 0.8668938228182018
            recal(Pos) = 0.8704674296716226
            recal(Neg) = 0.8389533028401234
            f1(Pos) = 0.856586495447608
            f1(Neg) = 0.85269474025623
            ccuracy = 0.8546666666666667
        
2.Spam:
    a.Naive Bayes
        Command:
            $ python3 nblearn.py enron_trainT2 enron_modelT2
            $ python3 nbclassify.py enron_modelT2 enron_testT2 > enron_predT2
            $ python3 evaluation.py enron_labelT2 enron_predT2 > enron_nbT2f1
        Result:
            precision(Pos) = 0.9782016348773842
            precision(Neg) = 0.9822211397954214
            recal(Pos) = 0.9826252528858741
            recal(Neg) = 0.9776969696969697
            f1(Pos) = 0.9804084540489194
            f1(Neg) = 0.9799538330701008
            Accuracy = 0.980183750675554
        
    
        b.SVM-Light
        Command:
            $ python3 preprocess_svm.py enron_trainT2 enron_svm_trainT2 enron_testT2 enron_svm_testT2 
            $ ./svm_learn enron_svm_trainT2 enron_svm_modelT2
            $ ./svm_classify enron_svm_testT2 enron_svm_modelT2 enron_svm_outputT2
            $ python3 trans_label.py enron_svm_outputT2 enron_svm_predT2 email
            $ python3 evaluation.py enron_labelT2 enron_svm_predT2 > enron_svmT2f1
        Result:
            precision(Pos) = 0.9095983364342782
            precision(Neg) = 0.9877594465141033
            recal(Pos) = 0.9890515292157562
            recal(Neg) = 0.8998787878787878
            f1(Pos) = 0.9476624857468643
            f1(Neg) = 0.9417734365089432
            Accuracy = 0.9448747973338137
    
    c.MegaM
        Command:
            $ python3 preprocess_mega.py enron_trainT2 enron_mega_trainT2 enron_testT2 enron_mega_testT2
            $ ./megam_i686.opt -fvals binary enron_mega_trainT2 > enron_mega_modelT2
            $ ./megam_i686.opt -fvals -predict enron_mega_modelT2 binary enron_mega_testT2 > enron_mega_outputT2
            $ python3 trans_label.py enron_mega_outputT2 enron_mega_predT2 email
            $ python3 evaluation.py enron_labelT2 enron_mega_predT2 > enron_megaT2f1
        Result:
            precision(Pos) = 0.9703851106168793
            precision(Neg) = 0.9860665844636252
            recal(Pos) = 0.9865524217541354
            recal(Neg) = 0.9693333333333334
            f1(Pos) = 0.9784019827687949
            f1(Neg) = 0.9776283618581907
            Accuracy = 0.978021978021978

      
    

    

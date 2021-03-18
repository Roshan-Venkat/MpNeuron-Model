from sklearn.metrics import accuracy_score

class MPNeuron:
  
  def __inti__(self):
    self.b = none
    
  def model(self,x):
    return(sum(x) >= self.b)
  
  def predict(self,X):
    Y = []
    for x in X:
      result = self.model(x)
      Y.append(result)
    return np.array(Y)
  
  def fit(self ,X ,Y):
    safe_accu = 0
    best_b = 0
    
    for b in range(X.shape[1]+1):
      self.b = b
      y_pred = self.predict(X)
      if safe_accu < accuracy_score(y_pred,Y):
        safe_accu = accuracy_score(y_pred,Y)
        best_b = b
        
    self.b = best_b
    print(best_b,safe_accu)
    
mpmodel = MPNeuron()
mpmodel.fit(X_binary_train,Ytrain)

Y_test_prediction = mpmodel.predict(X_binary_test)
accuracy_test = accuracy_score(Y_test_prediction,Ytest)
print(accuracy_test)

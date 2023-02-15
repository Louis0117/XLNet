# XLNet
-----
## English text classifier

* Dataset
&nbsp;&nbsp;&nbsp;&nbsp; AXS_recognize_english_dataset_v10.csv
  
* Task  
&nbsp;&nbsp;&nbsp;&nbsp; Binary classification, distinguish between English text and non-English text.
  
* Implement
&nbsp;&nbsp;&nbsp;&nbsp; Fine-tuning XLNet downstream classification tasks

* Experiment

&nbsp;&nbsp;&nbsp;&nbsp; Accuracy on the test set
<table>
  <tr>
    <td>micro-F1</td>
    <td>macro-F1</td>
  </tr>
  <tr>
    <td>0.9916</td>
    <td>0.98</td>
  </tr>
</table>   

## Sentiment classifer
### Experiment 1
* task  
Sentiment analysis, classify dataset text as positive, negitive, neutral
* dataset  
AXS_data_3class_v10.csv
* model  
XLNet-Base
* hyperparameter (best)
iter = 1500   
batch size = 32    
learning rate = 1e-5 
* result  
&nbsp;&nbsp;&nbsp;&nbsp; 
F1-score on the test set
<table>
  <tr>
    <td>micro-F1</td>
    <td>macro-F1</td>
  </tr>
  <tr>
    <td> 75.5% </td>
    <td> 72.8% </td>
  </tr>
</table>   

### Experiment 2
* task  
Sentiment analysis, classify dataset text as positive, negitive, neutral
* dataset  
AXS_data_3class_v10.csv
* model  
XLNet-Base
* hyperparameter  
iter = 4000   
batch size = 32    
learning rate = 2e-5 
* result  
&nbsp;&nbsp;&nbsp;&nbsp; 
F1-score on the test set
<table>
  <tr>
    <td>micro-F1</td>
    <td>macro-F1</td>
  </tr>
  <tr>
    <td> 74.4% </td>
    <td> 71.3% </td>
  </tr>
</table>   

### Experiment 3
* task  
Sentiment analysis, classify dataset text as positive, negitive, neutral
* dataset  
AXS_data_3class_v10.csv
* model  
XLNet-Large
* hyperparameter  
iter = 400   
batch size = #    
learning rate = # 
* result  
&nbsp;&nbsp;&nbsp;&nbsp; 
F1-score on the test set
<table>
  <tr>
    <td>micro-F1</td>
    <td>macro-F1</td>
  </tr>
  <tr>
    <td> 67.5% </td>
    <td> 66.07% </td>
  </tr>
</table>   


### Experiment 4
* task  
Sentiment analysis, classify dataset text as positive, negitive, neutral
* dataset  
AXS_data_3class_v10.csv
* model  
XLNet-Large
* hyperparameter  
iter = 400   
batch size = #    
learning rate = # 
* result  
&nbsp;&nbsp;&nbsp;&nbsp; 
F1-score on the test set
<table>
  <tr>
    <td>micro-F1</td>
    <td>macro-F1</td>
  </tr>
  <tr>
    <td> 59.3% </td>
    <td> 24.8% </td>
  </tr>
</table>   

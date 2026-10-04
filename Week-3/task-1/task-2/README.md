# Week 3 - Task 2: NLP Sentiment Classification

## Overview

This project focuses on sentiment classification using real-world movie review text. Two different NLP approaches were implemented and compared:

1. TF-IDF + Logistic Regression
2. DistilBERT Transformer

The objective was to build a classical NLP baseline, fine-tune a pretrained Transformer model, evaluate both models using Accuracy and F1-score, and compare their predictions.

---

## Dataset

The IMDb Movie Reviews dataset was used for binary sentiment classification.

- **0** = Negative
- **1** = Positive

The dataset contains movie reviews labeled according to their sentiment.

For the Transformer experiment, a subset of the dataset was used to make fine-tuning practical in Google Colab.

---

## Project Workflow

The overall workflow was:

1. Load the IMDb dataset
2. Explore the text and sentiment labels
3. Clean the review text
4. Split the data into training and validation sets
5. Convert text into numerical features using TF-IDF
6. Train Logistic Regression as the classical baseline
7. Fine-tune a DistilBERT Transformer
8. Evaluate both models using Accuracy and F1-score
9. Generate example predictions with confidence scores
10. Compare the strengths and weaknesses of both approaches

---

# Model 1: TF-IDF + Logistic Regression

TF-IDF was used to convert movie reviews into numerical text features.

Logistic Regression was then trained to classify reviews as Positive or Negative.

### Results

- **Accuracy:** 89.20%
- **F1 Score:** 89.35%

The classical model provided a strong baseline and achieved better performance than the Transformer model in this experiment.

---

# Model 2: DistilBERT

DistilBERT is a smaller pretrained Transformer model from Hugging Face.

The model was fine-tuned for binary sentiment classification using the IMDb reviews.

### Results

- **Accuracy:** 85.30%
- **F1 Score:** 85.87%

Although DistilBERT is a pretrained Transformer capable of understanding contextual relationships in text, its performance in this experiment was lower than the TF-IDF baseline.

---

# Model Comparison

| Model | Accuracy | F1 Score |
|---|---:|---:|
| TF-IDF + Logistic Regression | **89.20%** | **89.35%** |
| DistilBERT | 85.30% | 85.87% |

The TF-IDF + Logistic Regression model performed approximately **3.90 percentage points better in accuracy** than DistilBERT.

This shows that a well-designed classical NLP approach can still be highly effective for sentiment classification.

---

# Example Predictions

### Example 1

**Review:**

> This movie was absolutely amazing and I loved every minute of it.

**Prediction:** Positive  
**Confidence:** 99.21%

---

### Example 2

**Review:**

> The movie was boring and a complete waste of time.

**Prediction:** Negative  
**Confidence:** 99.64%

---

### Example 3

**Review:**

> The acting was excellent and the story was very interesting.

**Prediction:** Positive  
**Confidence:** 98.97%

---

### Example 4

**Review:**

> I hated this movie. It was terrible and disappointing.

**Prediction:** Negative  
**Confidence:** 99.57%

---

# Comparing Model Predictions

One interesting example was:

> The acting was good but the movie was too long.

**TF-IDF + Logistic Regression**

- Prediction: Positive
- Confidence: 52.87%

**DistilBERT**

- Prediction: Negative
- Confidence: 99.37%

This example demonstrates that the Transformer can make a very confident contextual interpretation of a sentence, while the TF-IDF model was much less confident.

However, because this custom sentence does not have a known ground-truth label, it should be treated as an example of model behavior rather than proof that one prediction is correct.

---

# Error Analysis

The TF-IDF model achieved higher overall performance in this experiment. Its main limitation is that TF-IDF represents text mainly through word and phrase frequencies and does not fully understand the contextual meaning of a sentence.

This can make sentiment interpretation more difficult when reviews contain mixed opinions, contrasting phrases, or context-dependent language.

DistilBERT uses Transformer-based contextual representations and can consider relationships between words across a sentence. This gives it the potential to handle more complex language patterns.

However, in this experiment, the fine-tuned DistilBERT model did not outperform the TF-IDF baseline. This may be influenced by the smaller training subset and limited fine-tuning configuration used in the Colab environment.

---

# Key Findings

- TF-IDF + Logistic Regression achieved the best overall performance.
- The classical model achieved **89.20% accuracy** and **89.35% F1-score**.
- DistilBERT achieved **85.30% accuracy** and **85.87% F1-score**.
- Classical NLP can remain highly competitive for sentiment classification.
- Transformers provide stronger contextual understanding but may require more data, training time, and tuning to outperform a strong classical baseline.
- Confidence scores provide additional insight into how strongly each model supports its prediction.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Hugging Face Transformers
- DistilBERT
- PyTorch
- Google Colab

---

# Conclusion

This project demonstrates the progression from classical NLP to modern Transformer-based NLP.

The TF-IDF + Logistic Regression model achieved the strongest performance in this experiment, while DistilBERT demonstrated the ability to analyze text using contextual representations.

The comparison highlights an important practical lesson: a simpler machine learning approach can sometimes outperform a more advanced deep learning model when the dataset, preprocessing, and training configuration favor the classical approach.

---

## Repository

This notebook is part of the **EvolviX AI/ML Internship Program - Week 3**.

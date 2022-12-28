# Evaluating Deep Learning-based NIDS in Adversarial Settings
In this project we implemented our paper titled **Evaluating Deep Learning-based NIDS in Adversarial Settings**.

In this paper, we evaluate the adversarial example generation in malicious network activity classification. We use CIC-IDS2017 and CIC-DDoS2019 datasets with 76 different network features and try to find the most suitable features for generating adversarial examples in this domain. We group these features into different categories based on their nature. The result of the experiments shows that since these features are dependent and related to each other, it is impossible to make a general decision that can be supported for all different types of network attacks. After the group of All features with 38.22% success in CIC-IDS2017 and 39.76% in CIC-DDoS2019 with ε value of 0.01, the combination of Forward, Backward and Flow-based feature groups with 23.28% success in CIC-IDS2017 and 36.65% in CIC-DDoS2019 with ε value of 0.01 and the combination of Forward and Backward feature groups have the highest potential for adversarial attacks.

Our paper is available [here](https://www.researchgate.net/profile/Hesamodin-Mohammadian/publication/358631178_Evaluating_Deep_Learning-based_NIDS_in_Adversarial_Settings/links/623b8f4af559847a661479b8/Evaluating-Deep-Learning-based-NIDS-in-Adversarial-Settings.pdf)
---
## Files included in the project
* **Train.ipynb:** Training the target deep learning model
* **Attack.ipynb:** Perform the adversarial attack against the target model
* **Utils.py:** Utility functions including FGSM and MultiLayerPerceptron
* **requirements.txt:** Necessary dependencies

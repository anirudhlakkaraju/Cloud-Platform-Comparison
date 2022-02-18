1. Google Colab (Free Tier)
• Pros:
a) GPU specs: 12 GB Nvidia K80.
b) Limits to 12 hrs max per session, after which it will timeout.
c) 15 GB of disk space provided, with Google Drive as persistent storage.
d) Pre-built with many Python libraries.
e) No prior setup required.
• Cons:
a) No guarantee of session stability. Runtime can be terminated during high traffic.
b) No background execution. Session will be disconnected when tab/browser is closed.
c) Inactivity might terminate session. A captcha is shown at random intervals to check
for activity.
d) Difficult to work with large datasets as only 15 GB disk space is provided.
e) Need to install all specific libraries which are not pre-installed with Colab and this
needs to be repeated with every session.
• AI Benchmark Test
a) AI Score: 5788
b) Runtime duration: 19m 0s
2. Google Colab Pro ($9.99/month)
• Pros:
a) GPU specs: 25 GB Nvidia T4 and P100.
b) Limits to 24 hrs max per session, after which it will timeout.
c) At least 200 GB disk space provided, with Google Drive as persistent storage.
d) Pre-built with many Python libraries.
e) No prior setup required.
• Cons:
a) No guarantee of session stability. Runtime can be terminated during high traffic.
b) No background execution. Session will be disconnected when tab/browser is closed.
c) Inactivity might terminate session. A captcha pops up at random times to check for
activity.
d) Need to install all specific libraries which are not pre-installed with Colab and this
needs to be repeated with every session.
• AI Benchmark Test
a) AI Score: 23014
b) Runtime duration: 9m 45s
3. Deepnote (Free Tier)
• Pros:
a) CPU: 5 GB RAM.
b) 5 GB disk space provided.
• Cons:
a) No GPU availability for free tier.
b) Low disk space.
c) Check for activity every 15 minutes, without which session will terminated.
d) No background execution. Session will be disconnected when tab/browser is closed.
• AI Benchmark Test
a) AI Score: NA (did not complete test due to unavailability of GPU RAM)
b) Runtime duration: 19m 33s
4. Kaggle (Free Tier)
• Pros:
a) GPU: 13 GB Nvidia P100.
b) 20 GB disk space provided.
c) Limits to 9 hrs max per session, after which it will timeout.
• Cons:
a) Checks for activity every 20 minutes, without which session is terminated.
b) Low disk space makes it difficult to train models on large datasets, especially if
dataset is not available on Kaggle.
c) No background execution. Session will be disconnected when tab/browser is closed.
• AI Benchmark Test:
a) AI Score: 21090
b) Runtime duration: 10m 53s
4. Gradient (Free Tier)
• Pros:
a) GPU: up to 30 GB Nvidia V100 per instance.
b) Full version of JupyterLab.
c) Limits to 12 hours max per session, after which session will time out.
d) 5 GB disk space provided.
• Cons:
a) Low disk space makes it difficult to train models on large datasets.
b) Notebooks are public.
c) No background execution. Session will be disconnected when tab/browser is closed.
d) Allows only 1 active instance at a time.
• AI Benchmark Test:
a) AI Score: 6486
b) Runtime duration: 17m 45s
5. Google Cloud ($300 free credit)
• Pros:
a) CPU: 31 GB RAM.
b) 10 GB disk space provided (can be increased).
• Cons:
a) No GPU available in free tier.
• AI Benchmark Test
a) AI Score: 1100
b) Runtime duration: 27m 59s
6. Microsoft Azure ($200 free credit)
• Pros:
a) CPU: 16 GB RAM.
b) 100 GB disk space provided.
• Cons:
a) No GPU available in free tier.
• AI Benchmark Test
a) AI Score: NA (did not complete test due to unavailability of GPU RAM)
b) Runtime duration: 30m 9s
8. Amazon SageMaker (Free Tier)
• Pros:
a) CPU: 4 GB RAM.
b) 5 GB disk space provided.
c) Full version of JupyterLab.
• Cons:
a) No GPU available in free tier.
b) Low disk space makes it difficult to train models on large datasets.
• AI Benchmark Test
a) AI Score: NA (did not complete test due to unavailability of GPU RAM and low
CPU RAM)
b) Runtime duration: 50s
AI Benchmark Test
The benchmark consists of 46 AI and Computer Vision tests performed by neural networks running
on your smartphone. It measures over 100 different aspects of AI performance, including the speed,
accuracy, initialization time, etc. Considered neural networks comprise a comprehensive range of
architectures allowing to assess the performance and limits of various approaches used to solve
different AI tasks. A detailed description of all the tests can be found at - https://aibenchmark.com/tests.html
Performance Tracking
Weights & Biases platform was used to track the performances of all Cloud Providers.
The project for AI Benchmark can be found here - WandB Project. The runtimes can be found in
Table and the AI scores, system specifications can be found in the Logs of each run.
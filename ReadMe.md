## Comparing Cloud Platforms
### Google Colab (Free Tier)
#### Pros:
* GPU specs: 12 GB Nvidia K80.
* Limits to 12 hrs max per session, after which it will timeout.
* 15 GB of disk space provided, with Google Drive as persistent storage.
* Pre-built with many Python libraries.
* No prior setup required.
#### Cons:
* No guarantee of session stability. Runtime can be terminated during high traffic.
* No background execution. Session will be disconnected when tab/browser is closed.
* Inactivity might terminate session. A captcha is shown at random intervals to check
for activity.
* Difficult to work with large datasets as only 15 GB disk space is provided.
* Need to install all specific libraries which are not pre-installed with Colab and this needs to be repeated with every session.
#### AI Benchmark Test
* AI Score: 5788
*  Runtime duration: 19m 0s
### Google Colab Pro ($9.99/month)
#### Pros:
* GPU specs: 25 GB Nvidia T4 and P100.
* Limits to 24 hrs max per session, after which it will timeout.
* At least 200 GB disk space provided, with Google Drive as persistent storage.
* Pre-built with many Python libraries.
* No prior setup required.
#### Cons:
* No guarantee of session stability. Runtime can be terminated during high traffic.
* No background execution. Session will be disconnected when tab/browser is closed.
* Inactivity might terminate session. A captcha pops up at random times to check for activity.
* Need to install all specific libraries which are not pre-installed with Colab and this needs to be repeated with every session.
#### AI Benchmark Test
* AI Score: 23014
* Runtime duration: 9m 45s
### Deepnote (Free Tier)
#### Pros:
* CPU: 5 GB RAM.
* 5 GB disk space provided.
#### Cons:
* No GPU availability for free tier.
* Low disk space.
* Check for activity every 15 minutes, without which session will terminated.
* No background execution. Session will be disconnected when tab/browser is closed.
#### AI Benchmark Test
* AI Score: NA (did not complete test due to unavailability of GPU RAM)
* Runtime duration: 19m 33s
### Kaggle (Free Tier)
#### Pros:
* GPU: 13 GB Nvidia P100.
* 20 GB disk space provided.
* Limits to 9 hrs max per session, after which it will timeout.
### Cons:
* Checks for activity every 20 minutes, without which session is terminated.
* Low disk space makes it difficult to train models on large datasets, especially if dataset is not available on Kaggle.
* No background execution. Session will be disconnected when tab/browser is closed.
#### AI Benchmark Test:
* AI Score: 21090
* Runtime duration: 10m 53s
### Gradient (Free Tier)
#### Pros:
* GPU: up to 30 GB Nvidia V100 per instance.
* Full version of JupyterLab.
* Limits to 12 hours max per session, after which session will time out.
* 5 GB disk space provided.
#### Cons:
* Low disk space makes it difficult to train models on large datasets.
* Notebooks are public.
* No background execution. Session will be disconnected when tab/browser is closed.
* Allows only 1 active instance at a time.
#### AI Benchmark Test:
* AI Score: 6486
* Runtime duration: 17m 45s
### Google Cloud ($300 free credit)
#### Pros:
* CPU: 31 GB RAM.
* 10 GB disk space provided (can be increased).
#### Cons:
* No GPU available in free tier.
#### AI Benchmark Test
* AI Score: 1100
* Runtime duration: 27m 59s
### Microsoft Azure ($200 free credit)
#### Pros:
* CPU: 16 GB RAM.
* 100 GB disk space provided.
#### Cons:
* No GPU available in free tier.
#### AI Benchmark Test
* AI Score: NA (did not complete test due to unavailability of GPU RAM)
* Runtime duration: 30m 9s
### Amazon SageMaker (Free Tier)
#### Pros:
* CPU: 4 GB RAM.
* 5 GB disk space provided.
* Full version of JupyterLab.
#### Cons:
* No GPU available in free tier.
* Low disk space makes it difficult to train models on large datasets.
#### AI Benchmark Test
* AI Score: NA (did not complete test due to unavailability of GPU RAM and low CPU RAM)
* Runtime duration: 50s

## AI Benchmark Test
The benchmark consists of 46 AI and Computer Vision tests performed by neural networks running
on your smartphone. It measures over 100 different aspects of AI performance, including the speed,
accuracy, initialization time, etc. Considered neural networks comprise a comprehensive range of
architectures allowing to assess the performance and limits of various approaches used to solve
different AI tasks. A detailed description of all the tests can be found at - https://ai-benchmark.com/

## Performance Tracking
Weights & Biases platform was used to track the performances of all Cloud Providers.
The project for AI Benchmark can be found here - [WandB Project](https://wandb.ai/anirudhlakkaraju/ai-benchmark?workspace=user-anirudhlakkaraju). The runtimes can be found in
Table and the AI scores, system specifications can be found in the Logs of each run.
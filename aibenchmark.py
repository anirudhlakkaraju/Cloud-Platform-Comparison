from ai_benchmark import AIBenchmark
import wandb

wandb.login()
with wandb.init(project="ai-benchmark", entity="anirudhlakkaraju"):
  results = AIBenchmark().run()